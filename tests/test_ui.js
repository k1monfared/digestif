const path = require("path");
const fs = require("fs");

function loadPlaywright() {
  const candidates = ["playwright", "/home/k1/public/masoud/node_modules/playwright"];
  for (const c of candidates) {
    try { return require(c); } catch (e) {}
  }
  console.error("playwright module not found, skipping UI tests");
  process.exit(2);
}
const { chromium } = loadPlaywright();

const ROOT = path.join(__dirname, "..");
const TAO = "file://" + path.join(ROOT, "src/digestif/skill/runs/tao-misalignment.graph.html");
const CARBAN = "file://" + path.join(ROOT, "src/digestif/skill/examples/car-ban.graph.html");

let pass = 0, fail = 0;
const ok = (name, cond, extra) => {
  if (cond) { pass++; console.log("  PASS: " + name); }
  else { fail++; console.log("  FAIL: " + name + (extra !== undefined ? "  got " + JSON.stringify(extra) : "")); }
};

const state = page => page.evaluate(() => {
  const sel = document.querySelector("#gNodes g.selected");
  const header = sel ? sel.querySelector("text").textContent : null;
  const w = document.querySelector("#canvasWrap");
  const all = [...document.querySelectorAll("#gEdges path, #gXEdges path, #gTop path")];
  return {
    nodes: document.querySelectorAll("#gNodes g").length,
    selected: header ? header.split(" ")[0] : null,
    panelTitle: document.querySelector("#panel h2") ? document.querySelector("#panel h2").textContent : null,
    panelOpen: !!document.querySelector("#panel.open"),
    kbdFocus: document.querySelectorAll("#panel .kbd-focus").length,
    scroll: [w.scrollLeft, w.scrollTop],
    containsPaths: all.filter(p => !p.classList.contains("xedge")).length,
    xPaths: all.filter(p => p.classList.contains("xedge")).length,
    hiddenPaths: all.filter(p => p.style.display === "none").length
  };
});

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage({ viewport: { width: 1400, height: 900 } });
  const errors = [];
  page.on("pageerror", e => errors.push(String(e)));

  await page.goto(TAO);
  await page.waitForTimeout(300);
  const rectOf = ref => page.evaluate(ref => {
    const g = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith(ref));
    const r = g.getBoundingClientRect();
    return { x: r.x, y: r.y };
  }, ref);
  let s = await state(page);
  ok("initial: 10 visible nodes", s.nodes === 10, s.nodes);
  ok("initial: root selected", s.selected === "summary", s.selected);
  ok("initial: panel open on root", s.panelOpen && s.panelTitle === "Node 0", s);
  ok("initial: 9 contains edges, 2 cross edges", s.containsPaths === 9 && s.xPaths === 2, s);
  ok("initial: nothing culled in view", s.hiddenPaths === 0, s.hiddenPaths);

  const panelInfo = await page.evaluate(() => {
    const p = document.getElementById("panel");
    const pass = [...p.querySelectorAll(".passage")];
    return {
      hasTextBlock: !!p.querySelector(".text"),
      sects: [...p.querySelectorAll(".sect")].map(el => el.textContent),
      passages: pass.length,
      passagesVisible: pass.every(el => getComputedStyle(el).display !== "none" && el.textContent.length > 0)
    };
  });
  ok("sidebar: node text not repeated", panelInfo.hasTextBlock === false, panelInfo);
  ok("sidebar: no parent or children sections", !panelInfo.sects.includes("Parent") && !panelInfo.sects.includes("Children"), panelInfo.sects);
  ok("sidebar: citations expanded by default", panelInfo.passages === 2 && panelInfo.passagesVisible, panelInfo);

  await page.keyboard.press("Enter");
  s = await state(page);
  ok("enter: sidebar focus on first row", s.kbdFocus === 1, s.kbdFocus);
  await page.keyboard.press("Escape");
  s = await state(page);
  ok("escape: leaves sidebar focus", s.kbdFocus === 0, s.kbdFocus);

  await page.keyboard.press(" ");
  s = await state(page);
  ok("space: folds root", s.nodes === 1, s.nodes);
  await page.keyboard.press(" ");
  s = await state(page);
  ok("space: unfolds root", s.nodes === 10, s.nodes);

  await page.keyboard.press("ArrowDown");
  s = await state(page);
  ok("down from root: first main point", s.selected === "1", s.selected);
  await page.keyboard.press("ArrowDown");
  await page.keyboard.press("ArrowDown");
  s = await state(page);
  ok("down twice more: node 3", s.selected === "3", s.selected);
  await page.keyboard.press("ArrowUp");
  s = await state(page);
  ok("up: back to node 2", s.selected === "2", s.selected);

  const linkColors = await page.evaluate(() => [...document.querySelectorAll("#panel .linkrow .etype")].map(el => [el.textContent, getComputedStyle(el).color]));
  const colorFor = t => { const f = linkColors.find(([name]) => name === t); return f ? f[1] : null; };
  ok("sidebar: link colors match the legend palette",
    colorFor("supports") === "rgb(22, 163, 74)" && colorFor("qualifies") === "rgb(37, 99, 235)",
    linkColors);

  const srcBtn = await page.evaluate(() => {
    const b = document.getElementById("pMode");
    return b ? b.textContent : null;
  });
  ok("source: mode toggle shown on top of the sidebar", srcBtn === "Source", srcBtn);
  const rightBefore = await page.evaluate(() => document.getElementById("canvasWrap").style.right);
  await page.click("#pMode");
  await page.waitForTimeout(150);
  const srcOpen = await page.evaluate(() => ({
    inPanel: !!document.querySelector("#panel #sourceBody"),
    marks: document.querySelectorAll("#sourceBody mark").length,
    modeLabel: document.getElementById("pMode").textContent,
    right: document.getElementById("canvasWrap").style.right
  }));
  ok("source: toggle shows the full source inside the sidebar", srcOpen.inPanel && srcOpen.marks === 34, srcOpen);
  ok("source: toggling does not change the sidebar width", srcOpen.right === rightBefore, [rightBefore, srcOpen.right]);
  ok("source: toggle label flips to Excerpts", srcOpen.modeLabel === "Excerpts", srcOpen.modeLabel);
  const paint = await page.evaluate(() => {
    const g = id => {
      const m = document.getElementById(id);
      if (!m) return null;
      return { bg: getComputedStyle(m).backgroundColor };
    };
    return { own: g("src-5"), supports: g("src-20"), qualifies: g("src-30"), untouched: g("src-34") };
  });
  ok("source: selected claim sentence in claim blue", paint.own.bg === "rgb(219, 234, 254)", paint.own);
  ok("source: supports-related sentence in supports green", paint.supports.bg.startsWith("rgba(22, 163, 74"), paint.supports);
  ok("source: qualifies-related sentence in qualifies blue", paint.qualifies.bg.startsWith("rgba(37, 99, 235"), paint.qualifies);
  ok("source: unrelated sentences are not highlighted", paint.untouched.bg === "rgba(0, 0, 0, 0)", paint.untouched);
  await page.evaluate(() => document.getElementById("src-7").click());
  await page.waitForTimeout(120);
  s = await state(page);
  ok("source: clicking a cited span selects a citing node", s.selected === "3" && s.panelTitle === "Node 3", s);
  const claimPaint = await page.evaluate(() => {
    const m = document.getElementById("src-7");
    return { bg: getComputedStyle(m).backgroundColor };
  });
  ok("source: claim sentence highlighted in claim blue", claimPaint.bg === "rgb(219, 234, 254)", claimPaint);
  await page.evaluate(() => document.getElementById("src-1").click());
  await page.waitForTimeout(120);
  s = await state(page);
  const summaryPaint = await page.evaluate(() => {
    const m = document.getElementById("src-1");
    return { bg: getComputedStyle(m).backgroundColor };
  });
  ok("source: summary sentence highlighted in summary color", s.selected === "summary" && summaryPaint.bg === "rgb(229, 231, 235)", [s, summaryPaint]);
  await page.click("#pMode");
  await page.waitForTimeout(120);
  const backToExcerpts = await page.evaluate(() => ({
    excerpts: document.querySelectorAll("#panel .passage").length,
    inPanel: !!document.querySelector("#panel #sourceBody"),
    modeLabel: document.getElementById("pMode").textContent
  }));
  ok("source: toggling back restores the excerpts", !backToExcerpts.inPanel && backToExcerpts.excerpts === 2 && backToExcerpts.modeLabel === "Source", backToExcerpts);
  await page.evaluate(() => document.querySelector("#panel .passage").click());
  await page.waitForTimeout(120);
  const fromPassage = await page.evaluate(() => ({
    inPanel: !!document.querySelector("#panel #sourceBody"),
    marks: document.querySelectorAll("#sourceBody mark").length
  }));
  s = await state(page);
  ok("source: clicking an excerpt jumps into the source view", fromPassage.inPanel && fromPassage.marks === 34 && s.selected === "summary", [fromPassage, s.selected]);
  await page.keyboard.press("ArrowDown");
  await page.keyboard.press("ArrowDown");
  s = await state(page);
  ok("back to node 2 after source checks", s.selected === "2", s.selected);
  await page.click("#pMode");
  await page.waitForTimeout(100);

  const geom = () => page.evaluate(() => {
    const pane = document.getElementById("panel").getBoundingClientRect();
    const g = document.querySelector("#gNodes g.selected").getBoundingClientRect();
    const wr = document.getElementById("canvasWrap").getBoundingClientRect();
    return { w: pane.width, dx: g.x - wr.x, dy: g.y - wr.y };
  });
  const beforeResize = await geom();
  let hb = await page.locator("#panelHandle").boundingBox();
  await page.mouse.move(hb.x + hb.width / 2, hb.y + hb.height / 2);
  await page.mouse.down();
  await page.mouse.move(hb.x + hb.width / 2 - 120, hb.y + hb.height / 2, { steps: 8 });
  await page.mouse.up();
  await page.waitForTimeout(120);
  const afterResize = await geom();
  ok("sidebar: dragging the handle resizes the panel", afterResize.w > beforeResize.w + 100, [beforeResize.w, afterResize.w]);
  ok("sidebar: selected node keeps its offset from the render area corner",
    Math.abs(afterResize.dx - beforeResize.dx) <= 2 && Math.abs(afterResize.dy - beforeResize.dy) <= 2,
    [beforeResize, afterResize]);
  hb = await page.locator("#panelHandle").boundingBox();
  await page.mouse.move(hb.x + hb.width / 2, hb.y + hb.height / 2);
  await page.mouse.down();
  await page.mouse.move(hb.x + 800, hb.y + hb.height / 2, { steps: 10 });
  await page.mouse.up();
  await page.waitForTimeout(120);
  const minW = await page.evaluate(() => document.getElementById("panel").getBoundingClientRect().width);
  ok("sidebar: resize clamps at the minimum width", Math.abs(minW - 260) <= 1, minW);

  const rSpaceBefore = await rectOf("2 ");
  await page.keyboard.press(" ");
  s = await state(page);
  ok("space: one tap unfolds depth-hidden children", s.nodes === 13, s.nodes);
  const rSpaceAfter = await rectOf("2 ");
  ok("space anchoring: selected node does not move on screen",
    Math.abs(rSpaceAfter.x - rSpaceBefore.x) <= 2 && Math.abs(rSpaceAfter.y - rSpaceBefore.y) <= 2,
    [rSpaceBefore, rSpaceAfter]);
  await page.keyboard.press(" ");
  s = await state(page);
  ok("space: second tap folds again", s.nodes === 10, s.nodes);

  const rCtrlBefore = await rectOf("2 ");
  const scCtrlBefore = (await state(page)).scroll;
  await page.keyboard.press("Control+3");
  s = await state(page);
  ok("ctrl+3: all layers, selection kept", s.nodes === 38 && s.selected === "2", s);
  const rCtrlAfter = await rectOf("2 ");
  ok("ctrl+3 anchoring: selected node does not move on screen",
    Math.abs(rCtrlAfter.x - rCtrlBefore.x) <= 2 && Math.abs(rCtrlAfter.y - rCtrlBefore.y) <= 2,
    [rCtrlBefore, rCtrlAfter]);
  ok("ctrl+3 anchoring: view scrolled to compensate",
    s.scroll[0] !== scCtrlBefore[0] || s.scroll[1] !== scCtrlBefore[1], [scCtrlBefore, s.scroll]);
  const rBackBefore = await rectOf("2 ");
  await page.keyboard.press("Control+2");
  s = await state(page);
  ok("ctrl+2 back: selection kept", s.nodes === 10 && s.selected === "2", s);
  const rBackAfter = await rectOf("2 ");
  ok("ctrl+2 anchoring: selected node does not move on screen",
    Math.abs(rBackAfter.x - rBackBefore.x) <= 2 && Math.abs(rBackAfter.y - rBackBefore.y) <= 2,
    [rBackBefore, rBackAfter, s.scroll]);

  const hitPos = () => page.evaluate(() => {
    const g = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith("2 "));
    const circles = g.querySelectorAll("circle");
    const h = circles[circles.length - 1];
    const r = h.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  });
  let hit = await hitPos();
  await page.mouse.click(hit.x, hit.y);
  await page.waitForTimeout(80);
  s = await state(page);
  ok("click + button: unfolds children", s.nodes === 13 && s.selected === "2", s);
  hit = await hitPos();
  await page.mouse.click(hit.x, hit.y);
  await page.waitForTimeout(80);
  s = await state(page);
  ok("click - button: folds children", s.nodes === 10 && s.selected === "2", s);

  await page.keyboard.press("ArrowRight");
  s = await state(page);
  ok("right: unfolds and selects first child", s.selected === "2.1" && s.nodes === 13, s);
  await page.keyboard.press("ArrowLeft");
  s = await state(page);
  ok("left from leaf: goes to parent", s.selected === "2" && s.nodes === 13, s);
  await page.keyboard.press("ArrowLeft");
  s = await state(page);
  ok("left on unfolded: folds, stays", s.selected === "2" && s.nodes === 10, s);

  const hitPos4 = () => page.evaluate(() => {
    const g = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith("4 "));
    const circles = g.querySelectorAll("circle");
    const h = circles[circles.length - 1];
    const r = h.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  });
  let hit4 = await hitPos4();
  await page.mouse.click(hit4.x, hit4.y);
  await page.waitForTimeout(80);
  s = await state(page);
  ok("click +/- selects that node", s.selected === "4", s.selected);
  ok("click +/- on node 4 unfolds its children", s.nodes === 15, s.nodes);
  hit4 = await hitPos4();
  await page.mouse.click(hit4.x, hit4.y);
  await page.waitForTimeout(80);
  s = await state(page);
  ok("click +/- again folds node 4", s.nodes === 10 && s.selected === "4", s);

  await page.keyboard.press("Control+3");
  s = await state(page);
  ok("ctrl+3: all tao layers visible", s.nodes === 38, s.nodes);
  await page.keyboard.press("Control+1");
  s = await state(page);
  ok("ctrl+1: only the summary node", s.nodes === 1, s.nodes);
  await page.keyboard.press("Control+2");
  s = await state(page);
  ok("ctrl+2: summary plus main points", s.nodes === 10, s.nodes);

  const widthOf = ref => page.evaluate(ref => {
    const g = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith(ref));
    return g.getBoundingClientRect().width;
  }, ref);
  const w0 = await widthOf("1 ");
  await page.keyboard.press("Control+=");
  await page.waitForTimeout(80);
  const w1 = await widthOf("1 ");
  await page.keyboard.press("Control+-");
  await page.waitForTimeout(80);
  const w2 = await widthOf("1 ");
  ok("ctrl+= zooms in", w1 > w0 * 1.05, [w0, w1]);
  ok("ctrl+- zooms back out", w2 < w1 * 0.99 && Math.abs(w2 - w0) < w0 * 0.05, [w0, w2]);

  await page.evaluate(() => {
    const w = document.querySelector("#canvasWrap");
    w.scrollLeft = 0; w.scrollTop = 0;
    w.dispatchEvent(new Event("scroll"));
  });
  await page.waitForTimeout(80);
  s = await state(page);
  ok("scrolled to empty corner: all edges culled", s.hiddenPaths === 11, s);
  await page.evaluate(() => document.getElementById("btnFit").click());
  await page.waitForTimeout(80);
  s = await state(page);
  ok("fit: edges visible again", s.hiddenPaths === 0, s);

  const before = (await state(page)).scroll;
  const box = await page.evaluate(() => {
    const gs = [...document.querySelectorAll("#gNodes g")];
    const target = gs.find(g => g.querySelector("text").textContent.startsWith("4 "));
    const r = target.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  });
  await page.mouse.click(box.x, box.y);
  await page.waitForTimeout(80);
  s = await state(page);
  ok("click: selects node without moving view", s.selected === "4" && s.scroll[0] === before[0] && s.scroll[1] === before[1], s);

  const wrapBox = await page.locator("#canvasWrap").boundingBox();
  const beforeDrag = (await state(page)).scroll;
  await page.mouse.move(wrapBox.x + 6, wrapBox.y + 6);
  await page.mouse.down();
  await page.mouse.move(wrapBox.x + 106, wrapBox.y + 106, { steps: 5 });
  await page.mouse.up();
  await page.waitForTimeout(80);
  s = await state(page);
  ok("drag in padding pans the view", s.scroll[0] !== beforeDrag[0] || s.scroll[1] !== beforeDrag[1], [beforeDrag, s.scroll]);
  ok("drag keeps selection", s.selected === "4", s.selected);
  const selText = await page.evaluate(() => window.getSelection().toString());
  ok("drag does not select text", selText === "", selText);

  const beforeText = (await state(page)).scroll;
  const tp = await page.evaluate(() => {
    const g = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith("3 "));
    const t = g.querySelector("text");
    const r = t.getBoundingClientRect();
    return { x: r.x + 2, y: r.y + r.height / 2, x2: r.x + Math.max(20, r.width - 2), y2: r.y + r.height / 2 };
  });
  await page.mouse.move(tp.x, tp.y);
  await page.mouse.down();
  await page.mouse.move(tp.x2, tp.y2, { steps: 8 });
  await page.mouse.up();
  await page.waitForTimeout(80);
  const selText2 = await page.evaluate(() => window.getSelection().toString());
  s = await state(page);
  ok("dragging on node text selects text", selText2.length > 0, selText2);
  ok("text drag does not pan", s.scroll[0] === beforeText[0] && s.scroll[1] === beforeText[1], [beforeText, s.scroll]);
  ok("text drag keeps node selection", s.selected === "4", s.selected);

  await page.evaluate(() => {
    const w = document.querySelector("#canvasWrap");
    w.scrollLeft += 400; w.scrollTop += 400;
    w.dispatchEvent(new Event("scroll"));
  });
  await page.waitForTimeout(80);
  const rOffBefore = await rectOf("4 ");
  await page.keyboard.press("Control+3");
  await page.waitForTimeout(120);
  const rOffAfter = await rectOf("4 ");
  ok("ctrl+3 with off-screen selection still anchors",
    Math.abs(rOffAfter.x - rOffBefore.x) <= 2 && Math.abs(rOffAfter.y - rOffBefore.y) <= 2,
    [rOffBefore, rOffAfter]);
  await page.keyboard.press("Control+2");
  await page.waitForTimeout(120);
  const rOffBack = await rectOf("4 ");
  ok("ctrl+2 back with off-screen selection still anchors",
    Math.abs(rOffBack.x - rOffBefore.x) <= 2 && Math.abs(rOffBack.y - rOffBefore.y) <= 2,
    [rOffBefore, rOffBack]);

  await page.evaluate(() => document.getElementById("btnFit").click());
  await page.waitForTimeout(120);
  await page.keyboard.press("Control+3");
  await page.waitForTimeout(100);
  await page.evaluate(() => {
    const g = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith("2.1 "));
    g.scrollIntoView({ block: "center", inline: "center" });
  });
  await page.waitForTimeout(120);
  const c21 = await page.evaluate(() => {
    const g = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith("2.1 "));
    const r = g.getBoundingClientRect();
    return { x: r.x + r.width / 2, y: r.y + r.height / 2 };
  });
  await page.mouse.click(c21.x, c21.y);
  await page.waitForTimeout(100);
  s = await state(page);
  ok("zoom flow: deep node 2.1 selected", s.selected === "2.1", s.selected);
  await page.evaluate(() => {
    const w = document.querySelector("#canvasWrap");
    const parent = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith("2 "));
    const wr = w.getBoundingClientRect();
    w.scrollLeft += (parent.getBoundingClientRect().right - wr.left) + 40;
    w.dispatchEvent(new Event("scroll"));
  });
  await page.waitForTimeout(100);
  const rParentFoldBefore = await rectOf("2 ");
  await page.keyboard.press("Control+2");
  await page.waitForTimeout(160);
  s = await state(page);
  const rParentFoldAfter = await rectOf("2 ");
  ok("ctrl+2 from deep node: off-screen parent anchors, no jump",
    s.selected === "2" && Math.abs(rParentFoldAfter.x - rParentFoldBefore.x) <= 2 && Math.abs(rParentFoldAfter.y - rParentFoldBefore.y) <= 2,
    [rParentFoldBefore, rParentFoldAfter, s]);
  const rRootFoldBefore = await rectOf("summary");
  await page.keyboard.press("Control+1");
  await page.waitForTimeout(160);
  s = await state(page);
  const rRootFoldAfter = await rectOf("summary");
  ok("ctrl+1: root anchors, no jump",
    s.selected === "summary" && Math.abs(rRootFoldAfter.x - rRootFoldBefore.x) <= 2 && Math.abs(rRootFoldAfter.y - rRootFoldBefore.y) <= 2,
    [rRootFoldBefore, rRootFoldAfter, s]);

  const rSeqBefore = await rectOf("summary");
  await page.keyboard.press("Control+2");
  await page.waitForTimeout(150);
  const rSeqMid = await rectOf("summary");
  await page.keyboard.press("Control+1");
  await page.waitForTimeout(150);
  const rSeqAfter = await rectOf("summary");
  s = await state(page);
  ok("3->2->1 sequence: root anchored through both folds",
    s.selected === "summary" &&
    Math.abs(rSeqMid.y - rSeqBefore.y) <= 2 && Math.abs(rSeqMid.x - rSeqBefore.x) <= 2 &&
    Math.abs(rSeqAfter.y - rSeqMid.y) <= 2 && Math.abs(rSeqAfter.x - rSeqMid.x) <= 2,
    [rSeqBefore, rSeqMid, rSeqAfter]);

  await page.goto(CARBAN);
  await page.waitForTimeout(300);
  s = await state(page);
  ok("car-ban initial: 4 nodes, root selected", s.nodes === 4 && s.selected === "summary", s);
  await page.keyboard.press("ArrowDown");
  await page.keyboard.press("ArrowRight");
  await page.keyboard.press("ArrowRight");
  s = await state(page);
  ok("car-ban: descend to leaf 1.1.1", s.selected === "1.1.1" && s.nodes === 7, s);
  await page.keyboard.press("Control+Alt+1");
  s = await state(page);
  ok("car-ban ctrl+alt+1: selected branch stays visible", s.nodes === 4 && s.selected === "1.1.1", s);
  await page.keyboard.press("Control+2");
  s = await state(page);
  ok("ctrl+2 with deep selection: selects ancestor at that layer", s.nodes === 4 && s.selected === "1", s);
  await page.keyboard.press("Control+1");
  s = await state(page);
  ok("ctrl+1 with deep selection: selects the summary", s.nodes === 1 && s.selected === "summary", s);
  await page.keyboard.press("Control+2");
  s = await state(page);
  ok("ctrl+2 with layer-1 selection: keeps it", s.nodes === 4 && s.selected === "summary", s);

  await page.evaluate(() => document.getElementById("btnFit").click());
  await page.waitForTimeout(120);
  await page.keyboard.press("ArrowDown");
  await page.keyboard.press("ArrowRight");
  await page.keyboard.press("ArrowRight");
  s = await state(page);
  ok("car-ban: back at leaf for parent anchor test", s.selected === "1.1.1" && s.nodes === 7, s);
  const rParentBefore = await rectOf("1 ");
  await page.keyboard.press("Control+2");
  await page.waitForTimeout(140);
  s = await state(page);
  const rParentAfter = await rectOf("1 ");
  ok("fold to 2 with visible parent: parent anchors the view",
    s.selected === "1" && Math.abs(rParentAfter.x - rParentBefore.x) <= 2 && Math.abs(rParentAfter.y - rParentBefore.y) <= 2,
    [rParentBefore, rParentAfter, s]);

  await page.keyboard.press("Control+4");
  await page.waitForTimeout(100);
  await page.keyboard.press("ArrowDown");
  await page.keyboard.press("ArrowDown");
  s = await state(page);
  ok("car-ban: leaf selected again, parent on screen", s.selected === "1.1.1", s.selected);
  await page.evaluate(() => {
    const w = document.querySelector("#canvasWrap");
    const parent = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith("1 "));
    const wr = w.getBoundingClientRect();
    w.scrollLeft += (parent.getBoundingClientRect().right - wr.left) + 40;
    w.dispatchEvent(new Event("scroll"));
  });
  await page.waitForTimeout(80);
  const parentOffBefore = await page.evaluate(() => {
    const w = document.querySelector("#canvasWrap").getBoundingClientRect();
    const g = [...document.querySelectorAll("#gNodes g")].find(el => el.querySelector("text").textContent.startsWith("1 "));
    const r = g.getBoundingClientRect();
    return r.right < w.left;
  });
  const rOffParentBefore = await rectOf("1 ");
  ok("parent is off screen before the fold", parentOffBefore);
  await page.keyboard.press("Control+2");
  await page.waitForTimeout(160);
  s = await state(page);
  const rOffParentAfter = await rectOf("1 ");
  ok("fold to 2 with off-screen parent: parent anchors off screen",
    s.selected === "1" && Math.abs(rOffParentAfter.x - rOffParentBefore.x) <= 2 && Math.abs(rOffParentAfter.y - rOffParentBefore.y) <= 2,
    [rOffParentBefore, rOffParentAfter, s]);

  const { execFileSync } = require("child_process");
  const os = require("os");
  const bigGraph = path.join(ROOT, "tests/fixtures/big.graph.json");
  const bigTmp = fs.mkdtempSync(path.join(os.tmpdir(), "ph-ui-"));
  const bigHtml = path.join(bigTmp, "big.graph.html");
  execFileSync("python3", [path.join(ROOT, "src/digestif/skill/scripts/graph.py"), "to-html", bigGraph, "-o", bigHtml]);
  const big = JSON.parse(fs.readFileSync(bigGraph, "utf8"));
  const bigMains = big.nodes.filter(n => n.id !== "0" && !n.id.includes(".")).length;
  const bigLayers = Math.min(9, Math.max(...big.nodes.map(n => n.id === "0" ? 0 : n.id.split(".").length)) + 1);

  await page.goto("file://" + bigHtml);
  await page.waitForTimeout(400);
  s = await state(page);
  ok("big graph: initial shows summary and main points", s.nodes === 1 + bigMains, [s.nodes, 1 + bigMains]);
  await page.keyboard.press("Control+" + bigLayers);
  await page.waitForTimeout(250);
  s = await state(page);
  ok("big graph: all layers visible", s.nodes === big.nodes.length, [s.nodes, big.nodes.length]);
  await page.keyboard.press("Control+1");
  await page.waitForTimeout(150);
  s = await state(page);
  ok("big graph: ctrl+1 shows only the summary", s.nodes === 1 && s.selected === "summary", s);
  await page.keyboard.press(" ");
  await page.waitForTimeout(150);
  s = await state(page);
  ok("big graph: space unfolds the summary", s.nodes === 1 + bigMains, s.nodes);
  const noSrc = await page.evaluate(() => !document.getElementById("pMode"));
  ok("big graph: no source toggle without source text", noSrc);
  fs.rmSync(bigTmp, { recursive: true, force: true });

  ok("no page errors", errors.length === 0, errors);

  await browser.close();
  console.log("");
  console.log("=== Results: " + pass + " passed, " + fail + " failed ===");
  process.exit(fail === 0 ? 0 : 1);
})().catch(e => { console.error(e); process.exit(1); });
