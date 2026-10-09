// Headless UI tests for the aligned reading view (requires playwright + chromium)
const path = require("path");
const fs = require("fs");
const os = require("os");
const { execFileSync } = require("child_process");

function loadPlaywright() {
  const candidates = ["playwright", "/home/k1/public/masoud/node_modules/playwright"];
  for (const c of candidates) {
    try { return require(c); } catch (e) {}
  }
  console.error("playwright module not found, skipping aligned view UI tests");
  process.exit(2);
}
const { chromium } = loadPlaywright();

const ROOT = path.join(__dirname, "..");
const GRAPH_PY = path.join(ROOT, "src/digestif/skill/scripts/graph.py");
const EXAMPLE = path.join(ROOT, "docs/example/graph.json");
const TMP = fs.mkdtempSync(path.join(os.tmpdir(), "digestif-aligned-"));
const OUT = path.join(TMP, "aligned.html");
execFileSync(process.env.PYTHON || "python3", [GRAPH_PY, "to-aligned", EXAMPLE, "-o", OUT]);
const GRAPH = JSON.parse(fs.readFileSync(EXAMPLE, "utf-8"));

let pass = 0, fail = 0;
const ok = (name, cond, extra) => {
  if (cond) { pass++; console.log("  PASS: " + name); }
  else { fail++; console.log("  FAIL: " + name + (extra !== undefined ? "  got " + JSON.stringify(extra) : "")); }
};

const snap = page => page.evaluate(() => ({
  visible: ALIGNED.visible(),
  rows: document.querySelectorAll(".txt").length,
  cards: [...document.querySelectorAll(".card")].map(c => c.dataset.id),
  bars: document.querySelectorAll(".bar").length,
  edges: document.querySelectorAll("#gEdges path.edge").length,
  selected: ALIGNED.state.selected,
}));

const key = async (page, k) => { await page.keyboard.press(k); await page.waitForTimeout(60); };
const selectedId = page => page.evaluate(() => ALIGNED.state.selected);
let mainPointsCount = () => 0;

const cardTop = (page, id) => page.evaluate(id => {
  const c = document.querySelector('.card[data-id="' + id + '"]');
  return c ? c.getBoundingClientRect().top : null;
}, id);

(async () => {
  const browser = await chromium.launch(process.env.PW_CHROMIUM ? { executablePath: process.env.PW_CHROMIUM } : {});
  const page = await browser.newPage({ viewport: { width: 1500, height: 950 } });
  const errors = [];
  page.on("pageerror", e => errors.push(String(e)));
  await page.goto("file://" + OUT);
  await page.waitForTimeout(250);

  const mainPoints = GRAPH.edges.filter(e => e.type === "contains" && e.from === "0").map(e => e.to)
    .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
  mainPointsCount = () => mainPoints.length;

  console.log("=== initial state ===");
  const s0 = await snap(page);
  ok("only main points visible", JSON.stringify(s0.visible) === JSON.stringify(mainPoints), s0.visible);
  ok("one card per main point", s0.cards.length === mainPoints.length, s0.cards.length);
  ok("root summary in header",
     (await page.textContent("#rootText")) === GRAPH.nodes.find(n => n.id === "0").text);

  console.log("=== text fidelity ===");
  const fid = await page.evaluate(() => {
    const strip = s => s.replace(/\s+/g, "");
    const shown = [...document.querySelectorAll(".txt")].map(t => t.textContent).join("");
    const ps = [...document.querySelectorAll(".p")].map(p => +p.dataset.p);
    return {
      same: strip(shown) === strip(G.meta.sourceText),
      unique: new Set(ps).size === ps.length,
      count: ps.length,
      total: Object.keys(G.meta.spans).length,
    };
  });
  ok("rows reproduce the source text exactly, ignoring whitespace", fid.same);
  ok("every passage rendered exactly once", fid.unique && fid.count === fid.total, fid);

  console.log("=== alignment ===");
  const align = await page.evaluate(() => [...document.querySelectorAll(".card")].map(c => {
    const id = c.dataset.id, a = ALIGNED.anchorOf(id);
    const span = document.querySelector('.p[data-p="' + a + '"]');
    const row = span.closest(".txt");
    const firstP = row.querySelector(".p");
    return {
      id, rowStartsAtAnchor: +firstP.dataset.p === a || row.classList.contains("first"),
      dy: Math.abs(c.getBoundingClientRect().top - span.getClientRects()[0].top),
    };
  }));
  const badRows = align.filter(a => !a.rowStartsAtAnchor);
  ok("each card's row starts at its anchor passage", badRows.length === 0, badRows);
  const offset = align.filter(a => a.dy > 12);
  ok("each card top is level with its first passage", offset.length === 0, offset);

  console.log("=== expand and collapse ===");
  const mp = "1";
  const kids1 = GRAPH.edges.filter(e => e.type === "contains" && e.from === mp).map(e => e.to);
  await page.evaluate(() => document.querySelector('.card[data-id="1"]').scrollIntoView({ block: "center" }));
  const before = await cardTop(page, mp);
  await page.click('.card[data-id="1"] .tog');
  await page.waitForTimeout(100);
  const s1 = await snap(page);
  ok("expand shows every child", kids1.every(k => s1.visible.includes(k)), s1.visible);
  ok("expand adds row breaks", s1.rows > s0.rows, [s0.rows, s1.rows]);
  const inCol2 = await page.evaluate(ids => ids.every(id => {
    const c = document.querySelector('.card[data-id="' + id + '"]');
    return c && c.closest(".cell").dataset.depth === "2";
  }), kids1);
  ok("children sit in the second column", inCol2);
  ok("toggle shows minus when open", (await page.textContent('.card[data-id="1"] .tog')) === "−");
  const after = await cardTop(page, mp);
  ok("expanded card keeps its place on screen", Math.abs(after - before) < 2, [before, after]);

  await page.click('.card[data-id="1.2"] .tog');
  await page.waitForTimeout(100);
  const s2 = await snap(page);
  ok("nested expand reaches the third column", s2.visible.some(id => id.startsWith("1.2.")), s2.visible);
  await page.click('.card[data-id="1"] .tog');
  await page.waitForTimeout(100);
  const s3 = await snap(page);
  ok("collapse hides the whole branch", JSON.stringify(s3.visible) === JSON.stringify(mainPoints), s3.visible);
  ok("collapse removes the extra row breaks", s3.rows === s0.rows, [s0.rows, s3.rows]);
  ok("+/- selects that point", s3.selected === "1", s3.selected);
  await page.click('.card[data-id="1"] .tog');
  await page.waitForTimeout(100);
  const s3b = await snap(page);
  ok("reopening keeps the nested branch open, like the graph view", s3b.visible.some(id => id.startsWith("1.2.")), s3b.visible);
  await page.click('.card[data-id="1"] .tog');
  await page.waitForTimeout(100);

  console.log("=== fold a column ===");
  await page.click('.card[data-id="1"] .tog');
  await page.waitForTimeout(100);
  const pre = await snap(page);
  await page.click('.ch.card-h[data-depth="2"] .fold');
  await page.waitForTimeout(100);
  const folded = await snap(page);
  const strip = await page.evaluate(() => {
    const h = document.querySelector('.ch.card-h[data-depth="2"]');
    return { cls: h.className, text: h.textContent, w: h.getBoundingClientRect().width };
  });
  ok("folded column becomes a thin L2 strip", strip.cls.includes("folded") && strip.text === "L2" && strip.w < 40, strip);
  ok("folded column hides its cards", !folded.cards.some(id => id.split(".").length === 2), folded.cards);
  ok("folding keeps the row breaks", folded.rows === pre.rows, [pre.rows, folded.rows]);
  ok("folding keeps the bars", folded.bars === pre.bars, [pre.bars, folded.bars]);
  await page.click('.ch.card-h[data-depth="2"]');
  await page.waitForTimeout(100);
  const unfolded = await snap(page);
  ok("clicking the strip reopens the column", unfolded.cards.length === pre.cards.length, unfolded.cards.length);

  console.log("=== bar cycling ===");
  const runs = await page.evaluate(() => ALIGNED.runsOf("1").length);
  ok("main point 1 has several runs", runs >= 2, runs);
  ok("one bar per run", (await page.$$('.bar[data-id="1"]')).length === runs);
  const y0 = await page.evaluate(() => window.scrollY);
  await page.click('.bar[data-id="1"][data-run="0"]');
  await page.waitForTimeout(700);
  const c1 = await page.evaluate(() => ({
    cursor: ALIGNED.state.cursor["1"], y: window.scrollY,
    flash: [...document.querySelectorAll(".p.flash")].map(p => +p.dataset.p),
    run: ALIGNED.runsOf("1")[1],
  }));
  ok("clicking a bar moves to the next run", c1.cursor === 1, c1.cursor);
  ok("the next run is tinted", c1.flash.length > 0 && c1.flash[0] === c1.run[0], c1);
  ok("the page scrolls to it", c1.y !== y0, [y0, c1.y]);
  await page.evaluate(n => {
    const b = document.querySelector('.bar[data-id="1"][data-run="' + (n - 1) + '"]');
    b.scrollIntoView({ block: "center" });
  }, runs);
  await page.click('.bar[data-id="1"][data-run="' + (runs - 1) + '"]');
  await page.waitForTimeout(200);
  ok("the last run wraps to the first", (await page.evaluate(() => ALIGNED.state.cursor["1"])) === 0);

  console.log("=== selection ===");
  await page.evaluate(() => document.querySelector('.card[data-id="2"]').scrollIntoView({ block: "center" }));
  await page.click('.card[data-id="2"]');
  await page.waitForTimeout(50);
  const sel = await page.evaluate(() => {
    const cited = new Set((G.nodes.find(n => n.id === "2").source || []));
    const tinted = [...document.querySelectorAll(".p")].filter(p => p.style.background).map(p => p.dataset.key);
    return { ok: tinted.length === cited.size && tinted.every(k => cited.has(k)), tinted: tinted.length, cited: cited.size,
             dim: document.querySelectorAll(".bar.dim").length, selBars: document.querySelectorAll('.bar.sel[data-id="2"]').length };
  });
  ok("selecting a card tints exactly its passages", sel.ok, sel);
  ok("selection emphasizes its bars and dims the rest", sel.selBars > 0 && sel.dim > 0, sel);
  await page.keyboard.press("Escape");
  const cleared = await page.evaluate(() => [...document.querySelectorAll(".p")].filter(p => p.style.background).length);
  ok("Escape clears the selection", cleared === 0, cleared);

  console.log("=== keyboard ===");
  await page.evaluate(() => window.scrollTo(0, 0));
  await key(page, "Control+1");
  await key(page, "ArrowDown");
  const order0 = await page.evaluate(() => ALIGNED.visualOrder());
  ok("down with nothing selected picks the top point", (await selectedId(page)) === order0[0], [await selectedId(page), order0[0]]);
  await key(page, "ArrowDown");
  ok("down moves in top to bottom order", (await selectedId(page)) === order0[1], [await selectedId(page), order0[1]]);
  await key(page, "ArrowUp");
  ok("up moves back", (await selectedId(page)) === order0[0]);
  const top = order0[0];
  const topKids = GRAPH.edges.filter(e => e.type === "contains" && e.from === top).map(e => e.to)
    .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }));
  await key(page, "ArrowRight");
  let sk = await snap(page);
  ok("right unfolds and selects the first child", sk.selected === topKids[0] && topKids.every(k => sk.visible.includes(k)), sk.selected);
  await key(page, "ArrowLeft");
  ok("left on a leaf-shown point goes to its parent", (await selectedId(page)) === top, await selectedId(page));
  await key(page, "ArrowLeft");
  sk = await snap(page);
  ok("left on a main point stays, it never folds", sk.selected === top && topKids.every(k => sk.visible.includes(k)), sk);
  await key(page, " ");
  sk = await snap(page);
  ok("space does nothing", sk.selected === top && topKids.every(k => sk.visible.includes(k)));
  const anchorBefore = await cardTop(page, top);
  await key(page, "Control+j");
  sk = await snap(page);
  ok("ctrl+j folds the selected point", !topKids.some(k => sk.visible.includes(k)));
  ok("folding keeps the selected card in place", Math.abs((await cardTop(page, top)) - anchorBefore) < 2);
  await key(page, "Control+j");
  sk = await snap(page);
  ok("ctrl+j unfolds it again", topKids.every(k => sk.visible.includes(k)));
  await key(page, "ArrowRight");
  const kid0 = await selectedId(page);
  await key(page, "ArrowDown");
  const sameDepth = await page.evaluate(() => ALIGNED.depthOf(ALIGNED.state.selected));
  ok("down stays at the same depth", sameDepth === 2 && (await selectedId(page)) !== kid0, [kid0, await selectedId(page)]);
  await key(page, "ArrowLeft");
  await key(page, "Control+j");

  await key(page, "Control+2");
  sk = await snap(page);
  const depth2 = GRAPH.nodes.filter(n => n.id !== "0" && n.id.split(".").length <= 2).length;
  ok("ctrl+2 shows two columns", sk.visible.length === depth2, [sk.visible.length, depth2]);
  await page.evaluate(id => ALIGNED.state.selected = id, topKids[0]);
  await key(page, "Control+1");
  sk = await snap(page);
  ok("ctrl+1 back to main points", sk.visible.length === mainPoints.length, sk.visible.length);
  ok("ctrl+1 moves a deeper selection to its main point", sk.selected === top, sk.selected);
  await key(page, "Control+0");
  sk = await snap(page);
  ok("ctrl+0 shows everything", sk.visible.length === GRAPH.nodes.length - 1, sk.visible.length);
  const deep = GRAPH.nodes.map(n => n.id).filter(id => id.split(".").length === 3)[0];
  await page.evaluate(id => ALIGNED.state.selected = id, deep);
  await key(page, "Control+Alt+1");
  sk = await snap(page);
  const chain = deep.split(".").map((_, i, a) => a.slice(0, i + 1).join("."));
  ok("ctrl+alt+1 keeps the selected branch open", chain.every(id => sk.visible.includes(id)), [deep, sk.visible.length]);
  ok("ctrl+alt+1 collapses everything else to main points",
     sk.visible.filter(id => id.split(".").length > 1).every(id => chain.includes(id)), sk.visible);
  await key(page, "Control+1");
  await key(page, "Escape");
  await page.evaluate(() => window.scrollTo(0, 0));
  const cross = await page.evaluate(() => {
    const order = [];
    (function walk(id) {
      G.edges.filter(e => e.type === "contains" && e.from === id).map(e => e.to)
        .sort((a, b) => a.localeCompare(b, undefined, { numeric: true }))
        .forEach(c => { if (c.split(".").length === 3) order.push(c); walk(c); });
    })("0");
    const first = order[0], pre = first.split(".").slice(0, 2).join(".");
    const k = order.findIndex(id => !id.startsWith(pre + "."));
    return { order, k };
  });
  await key(page, "ArrowDown");
  await key(page, "ArrowRight");
  await key(page, "ArrowRight");
  ok("arrows reach the first point at depth 3", (await selectedId(page)) === cross.order[0], [await selectedId(page), cross.order[0]]);
  for (let i = 0; i < cross.k; i++) await key(page, "ArrowDown");
  const crossed = await page.evaluate(() => ({ sel: ALIGNED.state.selected, vis: ALIGNED.visible().includes(ALIGNED.state.selected) }));
  ok("down crosses into the next branch at the same depth, opening it", crossed.sel === cross.order[cross.k] && crossed.vis, [crossed, cross.order[cross.k]]);
  await key(page, "ArrowLeft");
  const expectParent = cross.order[cross.k].split(".").slice(0, 2).join(".");
  ok("left from there goes to its own parent", (await selectedId(page)) === expectParent, [await selectedId(page), expectParent]);
  await key(page, "Control+1");
  await key(page, "Escape");

  console.log("=== edges ===");
  await key(page, "Control+0");
  const ed = await page.evaluate(() => {
    const vis = new Set(ALIGNED.visible());
    const want = ALIGNED.crossEdges().filter(e => vis.has(e.from) && vis.has(e.to)).length;
    return { want, drawn: document.querySelectorAll("#gEdges path.edge").length };
  });
  ok("every cross edge between visible points is drawn", ed.want > 0 && ed.drawn === ed.want, ed);
  const hub = await page.evaluate(() => {
    const deg = {};
    ALIGNED.crossEdges().forEach(e => { deg[e.from] = (deg[e.from] || 0) + 1; deg[e.to] = (deg[e.to] || 0) + 1; });
    return Object.keys(deg).sort((a, b) => deg[b] - deg[a])[0];
  });
  await page.evaluate(id => document.querySelector('.card[data-id="' + id + '"]').scrollIntoView({ block: "center" }), hub);
  await page.click('.card[data-id="' + hub + '"]');
  await page.waitForTimeout(80);
  const hl = await page.evaluate(id => {
    const all = [...document.querySelectorAll("#gEdges path.edge")];
    const mine = all.filter(p => p.dataset.from === id || p.dataset.to === id);
    return { mine: mine.length, bold: mine.filter(p => p.classList.contains("hl")).length,
             others: all.length - mine.length, dim: all.filter(p => p.classList.contains("dim")).length };
  }, hub);
  ok("the selected point's edges are bold", hl.mine > 0 && hl.bold === hl.mine, hl);
  ok("the other edges are dimmed", hl.dim === hl.others, hl);
  // find a spot on one of the hub's edges that is not covered by a card, and scroll it into view
  const target = await page.evaluate(id => {
    const hits = [...document.querySelectorAll("#gEdges path.edge-hit")].filter(h => h.dataset.from === id || h.dataset.to === id);
    for (const p of hits) {
      const len = p.getTotalLength();
      for (let i = 1; i < 40; i++) {
        const pt = p.getPointAtLength(len * i / 40);
        let m = p.getScreenCTM();
        window.scrollBy(0, pt.y * m.d + m.f - window.innerHeight / 2);
        m = p.getScreenCTM();
        const sx = pt.x * m.a + m.e, sy = pt.y * m.d + m.f;
        if (sy < 120 || sy > window.innerHeight - 10) continue;
        if (document.elementFromPoint(sx, sy) === p) {
          return { other: p.dataset.from === id ? p.dataset.to : p.dataset.from, type: p.dataset.type, x: sx, y: sy };
        }
      }
    }
    return null;
  }, hub);
  ok("the hub's edges are clickable somewhere", !!target);
  await page.waitForTimeout(80);
  await page.mouse.click(target.x, target.y);
  await page.waitForTimeout(150);
  const pop = await page.evaluate(() => ({
    open: document.getElementById("edgePop").classList.contains("open"),
    type: document.getElementById("edgePopType").textContent,
    sel: document.querySelectorAll("#gEdges path.edge.edge-sel").length,
  }));
  ok("clicking an edge opens its card", pop.open && pop.type.includes(target.type), pop);
  ok("the clicked edge is highlighted", pop.sel === 1, pop.sel);
  await page.click("#edgePop");
  await page.waitForTimeout(400);
  ok("follow selects the other end", (await selectedId(page)) === target.other, [await selectedId(page), target.other]);
  const onScreen = await page.evaluate(id => {
    const r = document.querySelector('.card[data-id="' + id + '"]').getBoundingClientRect();
    return r.top >= 0 && r.bottom <= window.innerHeight;
  }, target.other);
  ok("follow brings the other end on screen", onScreen);
  ok("follow closes the edge card", !(await page.evaluate(() => document.getElementById("edgePop").classList.contains("open"))));
  await key(page, "Control+1");
  const after1 = await snap(page);
  ok("edges to hidden points are not drawn", after1.edges === await page.evaluate(() => {
    const vis = new Set(ALIGNED.visible());
    return ALIGNED.crossEdges().filter(e => vis.has(e.from) && vis.has(e.to)).length;
  }));

  console.log("=== links mode and history ===");
  await key(page, "Control+2");
  const pick = await page.evaluate(() => {
    const vis = new Set(ALIGNED.visible());
    const rowsOf = id => ALIGNED.crossEdges().filter(e => e.from === id).map(e => e.to)
      .concat(ALIGNED.crossEdges().filter(e => e.to === id).map(e => e.from));
    for (const id of ALIGNED.visible()) {
      const others = rowsOf(id);
      const k = others.findIndex(o => !vis.has(o));
      if (others.length >= 2 && k >= 0) return { id, others, k };
    }
    return null;
  });
  ok("found a point with a link into a folded branch", !!pick, pick);
  await page.evaluate(id => document.querySelector('.card[data-id="' + id + '"]').scrollIntoView({ block: "center" }), pick.id);
  await page.click('.card[data-id="' + pick.id + '"]');
  const startTop = await cardTop(page, pick.id);
  await key(page, "Enter");
  await page.waitForTimeout(300);
  let lm = await page.evaluate(() => ({
    open: document.getElementById("links").classList.contains("open"),
    rows: document.querySelectorAll("#links .lrow").length,
    focus: [...document.querySelectorAll("#links .lrow")].findIndex(r => r.classList.contains("kbd-focus")),
    target: ALIGNED.state.linkTarget, sel: ALIGNED.state.selected,
    title: document.querySelector("#links h3").textContent,
  }));
  ok("enter opens the links of the selected point", lm.open && lm.rows === pick.others.length && lm.focus === 0 && lm.title.endsWith(pick.id), lm);
  ok("the first link's far end is the target", lm.target === pick.others[0] && lm.sel === pick.id, lm);
  await key(page, "ArrowDown");
  lm = await page.evaluate(() => ({ target: ALIGNED.state.linkTarget, focus: [...document.querySelectorAll("#links .lrow")].findIndex(r => r.classList.contains("kbd-focus")) }));
  ok("down picks the next link", lm.target === pick.others[1] && lm.focus === 1, lm);
  if (pick.k === 0) await key(page, "ArrowUp");
  for (let i = 1; i < pick.k; i++) await key(page, "ArrowDown");
  const foldedMark = await page.evaluate(() => document.querySelectorAll("#links .lrow.kbd-focus .folded").length);
  ok("a link into a folded branch is marked folded", foldedMark === 1);
  await key(page, "Enter");
  await page.waitForTimeout(350);
  let at = await page.evaluate(() => ({ sel: ALIGNED.state.selected, vis: ALIGNED.visible(), onScreen: (() => {
    const c = document.querySelector('.card[data-id="' + ALIGNED.state.selected + '"]');
    if (!c) return false; const r = c.getBoundingClientRect(); return r.top >= 0 && r.bottom <= window.innerHeight; })() }));
  ok("enter on a link follows it, opening the folded path", at.sel === pick.others[pick.k] && at.vis.includes(at.sel), at.sel);
  ok("the far end is scrolled into view", at.onScreen);
  await key(page, "Enter");
  await page.waitForTimeout(350);
  ok("enter again follows it back", (await selectedId(page)) === pick.id);
  await key(page, "Enter");
  await page.waitForTimeout(350);
  await key(page, "ArrowLeft");
  await key(page, " ");
  ok("left, right and space do nothing inside the links", (await selectedId(page)) === pick.others[pick.k]);
  await key(page, "Escape");
  lm = await page.evaluate(() => ({ open: document.getElementById("links").classList.contains("open"), sel: ALIGNED.state.selected,
    pill: document.getElementById("btnBack").style.display !== "none" && document.getElementById("btnBack").textContent }));
  ok("escape leaves the links on the end you are at", !lm.open && lm.sel === pick.others[pick.k], lm);
  ok("the back pill names where back goes", lm.pill === "\u2190 " + pick.id, lm.pill);
  await key(page, "Backspace");
  await page.waitForTimeout(400);
  ok("backspace goes back to where you jumped from", (await selectedId(page)) === pick.id);
  const backTop = await cardTop(page, pick.id);
  ok("back returns the point to the same spot on screen", Math.abs(backTop - startTop) <= 3, [startTop, backTop]);
  await key(page, "Alt+ArrowRight");
  await page.waitForTimeout(400);
  ok("alt+right goes forward again", (await selectedId(page)) === pick.others[pick.k]);
  await key(page, "Alt+ArrowLeft");
  await page.waitForTimeout(400);
  ok("alt+left goes back", (await selectedId(page)) === pick.id);
  const visitFrom = await selectedId(page);
  await key(page, "ArrowDown");
  const moved = await selectedId(page);
  ok("down moved to another point for the history check", moved !== visitFrom, [visitFrom, moved]);
  ok("arrow moves are visits: the pill names the point you left", await page.evaluate(() => document.getElementById("btnBack").textContent) === "\u2190 " + visitFrom);
  await key(page, "Backspace");
  await page.waitForTimeout(400);
  ok("backspace retraces an arrow move", (await selectedId(page)) === visitFrom);
  await key(page, "Enter");
  await page.waitForTimeout(250);
  await page.click('#links .lrow[data-i="1"]');
  await page.waitForTimeout(400);
  lm = await page.evaluate(() => ({ open: document.getElementById("links").classList.contains("open"), sel: ALIGNED.state.selected,
    back: ALIGNED.state.back.length && ALIGNED.state.back[ALIGNED.state.back.length - 1].id }));
  ok("clicking a link row follows it and lands there", !lm.open && lm.sel === pick.others[1] && lm.back === pick.id, lm);
  await key(page, "Enter");
  const nolinks = await page.evaluate(() => {
    const vis = ALIGNED.visible();
    const linked = new Set(ALIGNED.crossEdges().flatMap(e => [e.from, e.to]));
    return vis.find(id => !linked.has(id)) || null;
  });
  await key(page, "Escape");
  if (nolinks) {
    await page.evaluate(id => document.querySelector('.card[data-id="' + id + '"]').scrollIntoView({ block: "center" }), nolinks);
    await page.click('.card[data-id="' + nolinks + '"]');
    await key(page, "Enter");
    const h = await page.evaluate(() => ({ hint: document.getElementById("hint").classList.contains("open") && document.getElementById("hint").textContent,
      open: document.getElementById("links").classList.contains("open") }));
    ok("enter on a point without links shows a short hint", /No links/.test(h.hint || "") && !h.open, h);
  }
  await key(page, "Escape");

  console.log("=== search ===");
  await key(page, "Control+1");
  const term = await page.evaluate(() => {
    const n = G.nodes.find(n => n.id.split(".").length === 3);
    return n.text.split(/\s+/).filter(w => w.length > 6)[0].toLowerCase();
  });
  await page.fill("#searchBox", term);
  await page.waitForTimeout(150);
  const sr = await page.evaluate(term => {
    const matches = G.nodes.filter(n => n.id !== "0" && (n.text.toLowerCase().includes(term) || n.id.includes(term))).map(n => n.id);
    const want = new Set();
    matches.forEach(id => { const parts = id.split("."); for (let i = 1; i <= parts.length; i++) want.add(parts.slice(0, i).join(".")); });
    const vis = ALIGNED.visible();
    return { ok: vis.length === want.size && vis.every(id => want.has(id)), vis: vis.length, want: want.size,
      marked: document.querySelectorAll(".card.match").length, matches: matches.length,
      count: document.getElementById("searchCount").textContent };
  }, term);
  ok("search keeps only the matches and their parents", sr.ok, sr);
  ok("matches are marked", sr.marked === sr.matches, sr);
  ok("the match count is shown", sr.count === sr.matches + " matches", sr.count);
  await page.focus("#searchBox");
  await key(page, "Escape");
  const cl = await page.evaluate(() => ({ q: document.getElementById("searchBox").value, vis: ALIGNED.visible().length,
    focused: document.activeElement && document.activeElement.id }));
  ok("escape in the box clears the search", cl.q === "" && cl.vis === mainPointsCount() && cl.focused !== "searchBox", cl);

  console.log("=== help and legend ===");
  await page.click("#btnHelp");
  ok("help opens", await page.evaluate(() => document.getElementById("help").classList.contains("open")));
  await page.click("#btnLegend");
  const pops = await page.evaluate(() => ({
    help: document.getElementById("help").classList.contains("open"),
    legend: document.getElementById("legend").classList.contains("open"),
    edgeChips: document.querySelectorAll("#legendEdgeChips .chip").length,
  }));
  ok("legend replaces help", !pops.help && pops.legend, pops);
  ok("legend lists the edge types", pops.edgeChips > 0, pops.edgeChips);
  await key(page, "Escape");
  ok("escape closes the popover", !(await page.evaluate(() => document.querySelector(".pop.open"))));

  ok("no page errors", errors.length === 0, errors);
  await browser.close();
  fs.rmSync(TMP, { recursive: true, force: true });
  console.log("\n=== Results: " + pass + " passed, " + fail + " failed, " + (pass + fail) + " total ===");
  process.exit(fail ? 1 : 0);
})().catch(e => { console.error(e); process.exit(1); });
