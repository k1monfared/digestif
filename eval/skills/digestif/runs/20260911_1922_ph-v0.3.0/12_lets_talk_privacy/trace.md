# Judge trace (scripted pipeline, opencode-go/deepseek-v4.1-flash)

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "12_lets_talk_privacy",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Encrypted chats still trust providers; only client-held keys minimize that trust.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "With Signal using recovery keys, the attack surface is much smaller",
   "reasoning": "Source ranks Signal's client-controlled keys as smaller attack surface but never asserts exclusivity of 'only client-held keys', so scope is overstated."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "E2EE means device-to-device secrecy, but users need provider exclusion, not just transit safety.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "one wants E2EE so that \"no one\" can access the data outside the sender and receivers, and in particular \"the provider\"",
   "reasoning": "Source defines device-to-device encryption and states the real goal is excluding the provider, matching the claim."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Non-expert end-user inquiry from a conversation with Omid.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This came out of a conversation with Omid. DISCLAIMER: I'm not a security expert",
   "reasoning": "Source explicitly frames the piece as an end-user attempt from an Omid conversation by a non-expert."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Metadata (network, frequency, volume, timing) still aids interpretation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they know your network, the frequency and amount of communication, times of communication etc",
   "reasoning": "Source lists exactly network, frequency, amount, and timing as interpretable metadata."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "If claims hold with no backdoors, Meta cannot read; closed source blocks certainty.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if they haven't implemented other backdoors that they have kept secret, then yes, they \"can't\" access that data. But we won't really know because the app is not open source",
   "reasoning": "Source states conditional inaccessibility plus closed-source blocking negative certainty, matching the claim."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "Business model, 2021 ad-sharing policy, and 2019 plaintext failure imply near-certain access.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can almost be certain that they can, and they do access them",
   "reasoning": "Source cites business model, 2021 policy, and plaintext failures to conclude near-certain access."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Smoking gun: history on a new device with no manual key transfer.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a smoking gun is whether the platform/app is able to \"backup\" your data",
   "reasoning": "Source names cross-device access without manual linking as the smoking gun criterion."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Locker plus receiver-only master key; server key touch equals public billboard copy.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if at any time, Facebook has access to it, it is as if you've locked your door and left a copy at the local farmers market billboard",
   "reasoning": "Source's key analogy and billboard comparison are faithfully restated."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "WhatsApp server stores encrypted history and hands keys to devices it authenticates.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server authenticates it and provides it with the keys needed to decrypt your message history",
   "reasoning": "Matches source description of server-stored history and key provisioning to authenticated devices."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Device lists and codes rely on honest reporting; a rogue device could hide.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they could simply hide a rogue device from your device list entirely",
   "reasoning": "Source states safeguards depend on honest server reporting and a rogue device could be hidden."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Proton generates the private key in-browser, wrapping it with bcrypt and AES-256.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your private key is generated in your browser, then encrypted with your password using bcrypt and AES-256",
   "reasoning": "Exact match on in-browser generation and bcrypt/AES-256 encryption."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Six-step login: type, bcrypt with server salt, authenticate, fetch key, decrypt locally, read.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Your browser hashes the password using bcrypt (with a salt provided by Proton's server)",
   "reasoning": "All six source steps are preserved in order with correct actions."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Hashing authenticates one-way; encryption protects two-way under the actual password.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Your private key is encrypted with your actual password (not the hash)",
   "reasoning": "Source's one-way hashing versus two-way encryption distinction and actual-password wrapping are preserved."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "In theory the seen hash cannot decrypt the password-wrapped key.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they can't use that hash to decrypt your encrypted private key",
   "reasoning": "Directly matches source's theoretical statement about the hash not decrypting the key."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Malicious client code could capture the typed password before hashing.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "captures your actual password when you type it - before it gets hashed",
   "reasoning": "Source states the identical residual risk of malicious client code capturing the pre-hash password."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Trust needs matching code, no compelled injection, uncompromised infrastructure.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They won't be compelled to inject malicious code in the future",
   "reasoning": "All three trust conditions mirror the source bullet list exactly."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Proton must steal the password first; WhatsApp grants keys directly.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp's architecture doesn't even require that step; the server can directly grant key access",
   "reasoning": "Source contrasts Proton's need to compromise the client with WhatsApp's direct key grant."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Signal: 30-digit passphrase file, device-to-device transfer, or unseen 64-character key.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a 64-character recovery key that Signal never sees or has access to",
   "reasoning": "All three Signal options and the exact 30-digit and 64-character figures match."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Android backup needs physical transfer; direct transfer needs both devices present.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Both devices must be physically present",
   "reasoning": "Source states physical transfer for backups and both devices present for direct transfer."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Zero-knowledge: no decryption, no recovery help after a lost key.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they cannot help you recover them if you lose your recovery key. This is genuinely zero-knowledge architecture",
   "reasoning": "Source states Signal cannot decrypt backups or help recover after key loss, calling it zero-knowledge."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Plaintext password storage cannot be ruled out with certainty.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "we don't know for certain",
   "reasoning": "Source's short answer is explicitly that certainty about plaintext storage is unavailable."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Open clients prove sending behavior, never the server's later handling.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can confirm that passwords are hashed before transmission. But you cannot verify what happens on the server",
   "reasoning": "Matches source's distinction between verifiable client behavior and unverifiable server handling."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Facebook logged hundreds of millions plaintext for years; Adobe leaked hints; MD5 persists.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "logging hundreds of millions of passwords in plaintext in internal logs for years",
   "reasoning": "All three source precedents, including unsalted MD5 at smaller services, are accurately summarized."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Proton reset destroys old mail, suggesting genuine inability, but proves nothing.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you lose access to all your old encrypted emails. This suggests they genuinely can't decrypt your data",
   "reasoning": "Source notes reset loses old mail, suggests genuine inability, and explicitly denies it is proof."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Trust rests on reputation, jurisdiction, model, behavior, not verifiable guarantees.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees",
   "reasoning": "Direct paraphrase preserving all listed trust factors and the guarantee contrast."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Escrow (WhatsApp) versus password-wrapped (Proton) versus client-controlled (Signal).",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Server-mediated key escrow",
   "reasoning": "Matches the table's three security model names for the three services."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Rogue device: YES for WhatsApp; NO for Proton and Signal (client caveat).",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "NO - but they could serve malicious client code to capture your password",
   "reasoning": "Table's YES for WhatsApp and NO for Proton/Signal, including the Proton client caveat, are preserved."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Checkable: open clients, Wireshark traffic, audits of deployed code.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Tools like Wireshark can show what's transmitted",
   "reasoning": "All three verifiable checks match source's open clients, network inspection, and audits."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Uncheckable: running code, later updates, rogue staff, breaches.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "an employee with server access could modify it, or someone who breaches their systems could inject logging",
   "reasoning": "Matches source's unverifiable items: running code, later changes, rogue employees, breaches."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Good: open servers, audits, clean breaches; bad: reset-proof data, obscurity, violations.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Can reset password and access old data",
   "reasoning": "Good and bad signs map to source lists, with 'reset-proof data' reflecting the reset-access sign."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Facebook 2019: 200-600 million passwords, 20,000+ searchers, archives from 2012.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "between 200-600 million passwords in plaintext",
   "reasoning": "The range, 20,000 employees, and 2012 archive date all match the source exactly."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Trust ends only with client-side crypto, zero-knowledge servers, verifiable builds.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "All cryptography happens client-side",
   "reasoning": "Source's three 'unless' conditions of client-side crypto, non-decryptable server, and reproducible builds are preserved."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "WhatsApp needs whole-infrastructure trust; Proton hashing honesty; Signal key custody.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Meta's entire server infrastructure",
   "reasoning": "The applied trust table entries for all three services are accurately condensed."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "Prefer client-side encryption, open source, decentralization, hardware keys like YubiKey.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "hardware security keys (like YubiKey) that never expose the secret",
   "reasoning": "All four bottom-line preferences match the source recommendation."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Sources: Meta 2021 engineering, Proton key docs, Signal September 2024 backups.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Introducing Signal Secure Backups ... (Signal Blog, September 2024)",
   "reasoning": "Source list cites Meta's July 2021 engineering post, Proton key docs, and Signal September 2024 backups."
  }
 ],
 "metrics": {
  "total_claims": 35,
  "supported": 34,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9714
 },
 "fail_list": [
  "C001"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "12_lets_talk_privacy",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: 'end-to-end encryption' means the sender's device encrypts and the receiver's device decrypts with no decryption in between, but the real question is whether the provider (not just a man-in-the-middle) can access the content, and the answer is not completely clear.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L006"
   ],
   "evidence_quote": "- 1 E2EE means device-to-device secrecy, but users need provider exclusion, not just transit safety. (¶1, ¶2)",
   "reasoning": "L003 states E2EE is device-to-device but frames the real need as provider exclusion, and L006 states certainty is blocked, capturing both halves of the thesis."
  },
  {
   "point_id": "K02",
   "point_text": "People usually want E2EE so that no one outside sender and receivers, particularly the provider, can access data. For WhatsApp this means Facebook should not access message content, but it still has metadata such as network, frequency, amount, and timing of communication.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L005"
   ],
   "evidence_quote": "- 1.2 Nuance: Metadata (network, frequency, volume, timing) still aids interpretation. (¶2)",
   "reasoning": "L003 captures provider-exclusion motive, and L005 lists the metadata dimensions closely matching network, frequency, volume/amount, timing."
  },
  {
   "point_id": "K03",
   "point_text": "For WhatsApp the answer is unclear: if implemented as claimed and with no secret backdoors they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative (that access is impossible).",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006"
   ],
   "evidence_quote": "- 1.3 If claims hold with no backdoors, Meta cannot read; closed source blocks certainty. (¶3)",
   "reasoning": "L006 preserves the conditional (claims hold, no backdoors) and the closed-source barrier to certainty, which is the core of the unclear answer."
  },
  {
   "point_id": "K04",
   "point_text": "Evidence against WhatsApp/Meta: the 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as storing hundreds of millions of passwords in plaintext, make it almost certain they can and do access message content.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007"
   ],
   "evidence_quote": "- 1.4 Business model, 2021 ad-sharing policy, and 2019 plaintext failure imply near-certain access. (¶3)",
   "reasoning": "L007 names the business model, the 2021 ad-sharing policy, and the plaintext failure, concluding near-certain access, matching the point."
  },
  {
   "point_id": "K05",
   "point_text": "Smoking gun test: whether a platform can back up or let you access history across devices without manually linking/transferring keys. If the provider ever holds the key, it is like leaving a copy of your door key on a public billboard and it can decrypt any messages at will.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009"
   ],
   "evidence_quote": "- 2 Smoking gun: history on a new device with no manual key transfer. (¶4)",
   "reasoning": "L008 states the smoking-gun test, and L009 preserves the public-billboard analogy for any server key custody."
  },
  {
   "point_id": "K06",
   "point_text": "How WhatsApp actually works: the server stores encrypted message history and device-to-account identity mappings, authenticates new devices, and provides the keys needed to decrypt history. This makes the server a trusted intermediary that could silently authenticate a rogue device and hide it from your device list, unlike Signal's manual key transfer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011"
   ],
   "evidence_quote": "- 2.2 WhatsApp server stores encrypted history and hands keys to devices it authenticates. (¶5)",
   "reasoning": "L010 captures server-stored encrypted history and key hand-off to authenticated devices, and L011 captures the rogue device hiding from device lists, matching the trusted-intermediary concern."
  },
  {
   "point_id": "K07",
   "point_text": "Proton Mail model: the private key is generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L012"
   ],
   "evidence_quote": "- 3 Proton generates the private key in-browser, wrapping it with bcrypt and AES-256. (¶6)",
   "reasoning": "L012 preserves in-browser key generation and both named algorithms (bcrypt, AES-256), capturing the encrypted-key-at-rest model."
  },
  {
   "point_id": "K08",
   "point_text": "Proton login flow: type password, browser hashes it with bcrypt plus a server-provided salt, sends the hash to authenticate, server returns the encrypted private key, and the browser decrypts it locally with the actual password.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L013"
   ],
   "evidence_quote": "- 3.1 Evidence: Six-step login: type, bcrypt with server salt, authenticate, fetch key, decrypt locally, read. (¶7)",
   "reasoning": "L013 preserves all six steps including bcrypt with server salt and local decryption with the actual password."
  },
  {
   "point_id": "K09",
   "point_text": "Distinction between hashing (one-way, used for authentication, cannot be reversed to the password) and encryption (two-way, used on the private key). Proton receives the hash for authentication while the key is encrypted with the actual password, so in theory the hash cannot decrypt the key.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L014",
    "L015"
   ],
   "evidence_quote": "- 3.2 Hashing authenticates one-way; encryption protects two-way under the actual password. (¶8)",
   "reasoning": "L014 draws the one-way hashing versus two-way encryption distinction, and L015 preserves the claim that the seen hash theoretically cannot decrypt the key."
  },
  {
   "point_id": "K10",
   "point_text": "Proton's critical residual vulnerability: Proton could serve malicious client code (web app or update) to capture the actual password before hashing and use it to decrypt the stored key. This is why open-source clients matter, yet you must still trust the served code matches the source, no future malicious injection, and no infrastructure compromise.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L016",
    "L017"
   ],
   "evidence_quote": "- 4 Counterpoint: Malicious client code could capture the typed password before hashing. (¶10)",
   "reasoning": "L016 states the malicious-client password-capture threat, and L017 preserves the three residual trust requirements (matching code, no compelled injection, uncompromised infrastructure)."
  },
  {
   "point_id": "K11",
   "point_text": "Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L019",
    "L020"
   ],
   "evidence_quote": "- 5 Signal: 30-digit passphrase file, device-to-device transfer, or unseen 64-character key. (¶12)",
   "reasoning": "L019 captures all three switching options with the 30-digit and 64-character figures, and L020 notes physical-presence constraints. However the default condition that history is stored only on the device and deleted from servers after delivery is not stated, a dropped scope qualifier for a Must have point."
  },
  {
   "point_id": "K12",
   "point_text": "Signal is genuinely zero-knowledge: servers are never positioned to grant access to message history, and even with cloud backups Signal cannot decrypt backups and cannot help recover them if the recovery key is lost.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021"
   ],
   "evidence_quote": "- 5.2 Nuance: Zero-knowledge: no decryption, no recovery help after a lost key. (¶13)",
   "reasoning": "L021 explicitly states zero-knowledge with no decryption and no recovery help after a lost key, matching the point."
  },
  {
   "point_id": "K13",
   "point_text": "Password storage limits: you can verify what an open-source client does (hashing before transmission), inspect network traffic, and read audits, but you cannot verify server-side code, whether it changed after an audit, rogue employees, or breaches. There is no cryptographic guarantee about server password handling.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022",
    "L023",
    "L029",
    "L030"
   ],
   "evidence_quote": "- 8.1 Uncheckable: running code, later updates, rogue staff, breaches. (¶22)",
   "reasoning": "L029 covers checkable items (open clients, traffic inspection, audits), L030 covers uncheckable items (running code, later updates, rogue staff, breaches), and L022 states plaintext storage cannot be ruled out with certainty, matching the no-cryptographic-guarantee claim."
  },
  {
   "point_id": "K14",
   "point_text": "Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext in internal logs for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, and many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though this is not proof.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025",
    "L032"
   ],
   "evidence_quote": "- 8.3 Evidence: Facebook 2019: 200-600 million passwords, 20,000+ searchers, archives from 2012. (¶24)",
   "reasoning": "L032 preserves the Facebook 200-600 million, 20,000+, and 2012 figures, L024 covers Adobe hints and MD5, and L025 preserves the Proton reset evidence with the not-proof caveat."
  },
  {
   "point_id": "K15",
   "point_text": "Bottom line: for most commercial services you are trusting reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious users prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys such as YubiKey that never expose the secret.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026",
    "L033",
    "L035"
   ],
   "evidence_quote": "- 8.6 Prefer client-side encryption, open source, decentralization, hardware keys like YubiKey. (¶27)",
   "reasoning": "L026 states trust rests on reputation, jurisdiction, model, behavior rather than verifiable guarantees, and L035 lists client-side encryption, open source, decentralization, and hardware keys such as YubiKey."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 11,
  "must_have_partial": 1,
  "must_have_missing": 0,
  "overall_present": 14,
  "must_recall": 0.9583,
  "overall_recall": 0.9667
 },
 "missing_list": []
}
```

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "12_lets_talk_privacy",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Encrypted chats still trust providers; only client-held keys minimize that trust.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "With Signal using recovery keys, the attack surface is much smaller",
   "reasoning": "Source ranks Signal's client-controlled keys as smaller attack surface but never asserts exclusivity of 'only client-held keys', so scope is overstated."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "E2EE means device-to-device secrecy, but users need provider exclusion, not just transit safety.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "one wants E2EE so that \"no one\" can access the data outside the sender and receivers, and in particular \"the provider\"",
   "reasoning": "Source defines device-to-device encryption and states the real goal is excluding the provider, matching the claim."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Non-expert end-user inquiry from a conversation with Omid.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This came out of a conversation with Omid. DISCLAIMER: I'm not a security expert",
   "reasoning": "Source explicitly frames the piece as an end-user attempt from an Omid conversation by a non-expert."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Metadata (network, frequency, volume, timing) still aids interpretation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they know your network, the frequency and amount of communication, times of communication etc",
   "reasoning": "Source lists exactly network, frequency, amount, and timing as interpretable metadata."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "If claims hold with no backdoors, Meta cannot read; closed source blocks certainty.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if they haven't implemented other backdoors that they have kept secret, then yes, they \"can't\" access that data. But we won't really know because the app is not open source",
   "reasoning": "Source states conditional inaccessibility plus closed-source blocking negative certainty, matching the claim."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "Business model, 2021 ad-sharing policy, and 2019 plaintext failure imply near-certain access.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can almost be certain that they can, and they do access them",
   "reasoning": "Source cites business model, 2021 policy, and plaintext failures to conclude near-certain access."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Smoking gun: history on a new device with no manual key transfer.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a smoking gun is whether the platform/app is able to \"backup\" your data",
   "reasoning": "Source names cross-device access without manual linking as the smoking gun criterion."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Locker plus receiver-only master key; server key touch equals public billboard copy.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if at any time, Facebook has access to it, it is as if you've locked your door and left a copy at the local farmers market billboard",
   "reasoning": "Source's key analogy and billboard comparison are faithfully restated."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "WhatsApp server stores encrypted history and hands keys to devices it authenticates.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server authenticates it and provides it with the keys needed to decrypt your message history",
   "reasoning": "Matches source description of server-stored history and key provisioning to authenticated devices."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Device lists and codes rely on honest reporting; a rogue device could hide.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they could simply hide a rogue device from your device list entirely",
   "reasoning": "Source states safeguards depend on honest server reporting and a rogue device could be hidden."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Proton generates the private key in-browser, wrapping it with bcrypt and AES-256.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your private key is generated in your browser, then encrypted with your password using bcrypt and AES-256",
   "reasoning": "Exact match on in-browser generation and bcrypt/AES-256 encryption."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Six-step login: type, bcrypt with server salt, authenticate, fetch key, decrypt locally, read.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Your browser hashes the password using bcrypt (with a salt provided by Proton's server)",
   "reasoning": "All six source steps are preserved in order with correct actions."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Hashing authenticates one-way; encryption protects two-way under the actual password.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Your private key is encrypted with your actual password (not the hash)",
   "reasoning": "Source's one-way hashing versus two-way encryption distinction and actual-password wrapping are preserved."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "In theory the seen hash cannot decrypt the password-wrapped key.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they can't use that hash to decrypt your encrypted private key",
   "reasoning": "Directly matches source's theoretical statement about the hash not decrypting the key."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Malicious client code could capture the typed password before hashing.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "captures your actual password when you type it - before it gets hashed",
   "reasoning": "Source states the identical residual risk of malicious client code capturing the pre-hash password."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Trust needs matching code, no compelled injection, uncompromised infrastructure.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They won't be compelled to inject malicious code in the future",
   "reasoning": "All three trust conditions mirror the source bullet list exactly."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Proton must steal the password first; WhatsApp grants keys directly.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp's architecture doesn't even require that step; the server can directly grant key access",
   "reasoning": "Source contrasts Proton's need to compromise the client with WhatsApp's direct key grant."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Signal: 30-digit passphrase file, device-to-device transfer, or unseen 64-character key.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a 64-character recovery key that Signal never sees or has access to",
   "reasoning": "All three Signal options and the exact 30-digit and 64-character figures match."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Android backup needs physical transfer; direct transfer needs both devices present.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Both devices must be physically present",
   "reasoning": "Source states physical transfer for backups and both devices present for direct transfer."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Zero-knowledge: no decryption, no recovery help after a lost key.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they cannot help you recover them if you lose your recovery key. This is genuinely zero-knowledge architecture",
   "reasoning": "Source states Signal cannot decrypt backups or help recover after key loss, calling it zero-knowledge."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Plaintext password storage cannot be ruled out with certainty.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "we don't know for certain",
   "reasoning": "Source's short answer is explicitly that certainty about plaintext storage is unavailable."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Open clients prove sending behavior, never the server's later handling.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can confirm that passwords are hashed before transmission. But you cannot verify what happens on the server",
   "reasoning": "Matches source's distinction between verifiable client behavior and unverifiable server handling."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Facebook logged hundreds of millions plaintext for years; Adobe leaked hints; MD5 persists.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "logging hundreds of millions of passwords in plaintext in internal logs for years",
   "reasoning": "All three source precedents, including unsalted MD5 at smaller services, are accurately summarized."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Proton reset destroys old mail, suggesting genuine inability, but proves nothing.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you lose access to all your old encrypted emails. This suggests they genuinely can't decrypt your data",
   "reasoning": "Source notes reset loses old mail, suggests genuine inability, and explicitly denies it is proof."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Trust rests on reputation, jurisdiction, model, behavior, not verifiable guarantees.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees",
   "reasoning": "Direct paraphrase preserving all listed trust factors and the guarantee contrast."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Escrow (WhatsApp) versus password-wrapped (Proton) versus client-controlled (Signal).",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Server-mediated key escrow",
   "reasoning": "Matches the table's three security model names for the three services."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Rogue device: YES for WhatsApp; NO for Proton and Signal (client caveat).",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "NO - but they could serve malicious client code to capture your password",
   "reasoning": "Table's YES for WhatsApp and NO for Proton/Signal, including the Proton client caveat, are preserved."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Checkable: open clients, Wireshark traffic, audits of deployed code.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Tools like Wireshark can show what's transmitted",
   "reasoning": "All three verifiable checks match source's open clients, network inspection, and audits."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Uncheckable: running code, later updates, rogue staff, breaches.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "an employee with server access could modify it, or someone who breaches their systems could inject logging",
   "reasoning": "Matches source's unverifiable items: running code, later changes, rogue employees, breaches."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Good: open servers, audits, clean breaches; bad: reset-proof data, obscurity, violations.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Can reset password and access old data",
   "reasoning": "Good and bad signs map to source lists, with 'reset-proof data' reflecting the reset-access sign."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Facebook 2019: 200-600 million passwords, 20,000+ searchers, archives from 2012.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "between 200-600 million passwords in plaintext",
   "reasoning": "The range, 20,000 employees, and 2012 archive date all match the source exactly."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Trust ends only with client-side crypto, zero-knowledge servers, verifiable builds.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "All cryptography happens client-side",
   "reasoning": "Source's three 'unless' conditions of client-side crypto, non-decryptable server, and reproducible builds are preserved."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "WhatsApp needs whole-infrastructure trust; Proton hashing honesty; Signal key custody.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Meta's entire server infrastructure",
   "reasoning": "The applied trust table entries for all three services are accurately condensed."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "Prefer client-side encryption, open source, decentralization, hardware keys like YubiKey.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "hardware security keys (like YubiKey) that never expose the secret",
   "reasoning": "All four bottom-line preferences match the source recommendation."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Sources: Meta 2021 engineering, Proton key docs, Signal September 2024 backups.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Introducing Signal Secure Backups ... (Signal Blog, September 2024)",
   "reasoning": "Source list cites Meta's July 2021 engineering post, Proton key docs, and Signal September 2024 backups."
  }
 ],
 "metrics": {
  "total_claims": 35,
  "supported": 34,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9714
 },
 "fail_list": [
  "C001"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "12_lets_talk_privacy",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: 'end-to-end encryption' means the sender's device encrypts and the receiver's device decrypts with no decryption in between, but the real question is whether the provider (not just a man-in-the-middle) can access the content, and the answer is not completely clear.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L006"
   ],
   "evidence_quote": "- 1 E2EE means device-to-device secrecy, but users need provider exclusion, not just transit safety. (¶1, ¶2)",
   "reasoning": "L003 states E2EE is device-to-device but frames the real need as provider exclusion, and L006 states certainty is blocked, capturing both halves of the thesis."
  },
  {
   "point_id": "K02",
   "point_text": "People usually want E2EE so that no one outside sender and receivers, particularly the provider, can access data. For WhatsApp this means Facebook should not access message content, but it still has metadata such as network, frequency, amount, and timing of communication.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L005"
   ],
   "evidence_quote": "- 1.2 Nuance: Metadata (network, frequency, volume, timing) still aids interpretation. (¶2)",
   "reasoning": "L003 captures provider-exclusion motive, and L005 lists the metadata dimensions closely matching network, frequency, volume/amount, timing."
  },
  {
   "point_id": "K03",
   "point_text": "For WhatsApp the answer is unclear: if implemented as claimed and with no secret backdoors they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative (that access is impossible).",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006"
   ],
   "evidence_quote": "- 1.3 If claims hold with no backdoors, Meta cannot read; closed source blocks certainty. (¶3)",
   "reasoning": "L006 preserves the conditional (claims hold, no backdoors) and the closed-source barrier to certainty, which is the core of the unclear answer."
  },
  {
   "point_id": "K04",
   "point_text": "Evidence against WhatsApp/Meta: the 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as storing hundreds of millions of passwords in plaintext, make it almost certain they can and do access message content.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007"
   ],
   "evidence_quote": "- 1.4 Business model, 2021 ad-sharing policy, and 2019 plaintext failure imply near-certain access. (¶3)",
   "reasoning": "L007 names the business model, the 2021 ad-sharing policy, and the plaintext failure, concluding near-certain access, matching the point."
  },
  {
   "point_id": "K05",
   "point_text": "Smoking gun test: whether a platform can back up or let you access history across devices without manually linking/transferring keys. If the provider ever holds the key, it is like leaving a copy of your door key on a public billboard and it can decrypt any messages at will.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009"
   ],
   "evidence_quote": "- 2 Smoking gun: history on a new device with no manual key transfer. (¶4)",
   "reasoning": "L008 states the smoking-gun test, and L009 preserves the public-billboard analogy for any server key custody."
  },
  {
   "point_id": "K06",
   "point_text": "How WhatsApp actually works: the server stores encrypted message history and device-to-account identity mappings, authenticates new devices, and provides the keys needed to decrypt history. This makes the server a trusted intermediary that could silently authenticate a rogue device and hide it from your device list, unlike Signal's manual key transfer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011"
   ],
   "evidence_quote": "- 2.2 WhatsApp server stores encrypted history and hands keys to devices it authenticates. (¶5)",
   "reasoning": "L010 captures server-stored encrypted history and key hand-off to authenticated devices, and L011 captures the rogue device hiding from device lists, matching the trusted-intermediary concern."
  },
  {
   "point_id": "K07",
   "point_text": "Proton Mail model: the private key is generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L012"
   ],
   "evidence_quote": "- 3 Proton generates the private key in-browser, wrapping it with bcrypt and AES-256. (¶6)",
   "reasoning": "L012 preserves in-browser key generation and both named algorithms (bcrypt, AES-256), capturing the encrypted-key-at-rest model."
  },
  {
   "point_id": "K08",
   "point_text": "Proton login flow: type password, browser hashes it with bcrypt plus a server-provided salt, sends the hash to authenticate, server returns the encrypted private key, and the browser decrypts it locally with the actual password.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L013"
   ],
   "evidence_quote": "- 3.1 Evidence: Six-step login: type, bcrypt with server salt, authenticate, fetch key, decrypt locally, read. (¶7)",
   "reasoning": "L013 preserves all six steps including bcrypt with server salt and local decryption with the actual password."
  },
  {
   "point_id": "K09",
   "point_text": "Distinction between hashing (one-way, used for authentication, cannot be reversed to the password) and encryption (two-way, used on the private key). Proton receives the hash for authentication while the key is encrypted with the actual password, so in theory the hash cannot decrypt the key.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L014",
    "L015"
   ],
   "evidence_quote": "- 3.2 Hashing authenticates one-way; encryption protects two-way under the actual password. (¶8)",
   "reasoning": "L014 draws the one-way hashing versus two-way encryption distinction, and L015 preserves the claim that the seen hash theoretically cannot decrypt the key."
  },
  {
   "point_id": "K10",
   "point_text": "Proton's critical residual vulnerability: Proton could serve malicious client code (web app or update) to capture the actual password before hashing and use it to decrypt the stored key. This is why open-source clients matter, yet you must still trust the served code matches the source, no future malicious injection, and no infrastructure compromise.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L016",
    "L017"
   ],
   "evidence_quote": "- 4 Counterpoint: Malicious client code could capture the typed password before hashing. (¶10)",
   "reasoning": "L016 states the malicious-client password-capture threat, and L017 preserves the three residual trust requirements (matching code, no compelled injection, uncompromised infrastructure)."
  },
  {
   "point_id": "K11",
   "point_text": "Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L019",
    "L020"
   ],
   "evidence_quote": "- 5 Signal: 30-digit passphrase file, device-to-device transfer, or unseen 64-character key. (¶12)",
   "reasoning": "L019 captures all three switching options with the 30-digit and 64-character figures, and L020 notes physical-presence constraints. However the default condition that history is stored only on the device and deleted from servers after delivery is not stated, a dropped scope qualifier for a Must have point."
  },
  {
   "point_id": "K12",
   "point_text": "Signal is genuinely zero-knowledge: servers are never positioned to grant access to message history, and even with cloud backups Signal cannot decrypt backups and cannot help recover them if the recovery key is lost.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021"
   ],
   "evidence_quote": "- 5.2 Nuance: Zero-knowledge: no decryption, no recovery help after a lost key. (¶13)",
   "reasoning": "L021 explicitly states zero-knowledge with no decryption and no recovery help after a lost key, matching the point."
  },
  {
   "point_id": "K13",
   "point_text": "Password storage limits: you can verify what an open-source client does (hashing before transmission), inspect network traffic, and read audits, but you cannot verify server-side code, whether it changed after an audit, rogue employees, or breaches. There is no cryptographic guarantee about server password handling.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022",
    "L023",
    "L029",
    "L030"
   ],
   "evidence_quote": "- 8.1 Uncheckable: running code, later updates, rogue staff, breaches. (¶22)",
   "reasoning": "L029 covers checkable items (open clients, traffic inspection, audits), L030 covers uncheckable items (running code, later updates, rogue staff, breaches), and L022 states plaintext storage cannot be ruled out with certainty, matching the no-cryptographic-guarantee claim."
  },
  {
   "point_id": "K14",
   "point_text": "Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext in internal logs for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, and many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though this is not proof.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025",
    "L032"
   ],
   "evidence_quote": "- 8.3 Evidence: Facebook 2019: 200-600 million passwords, 20,000+ searchers, archives from 2012. (¶24)",
   "reasoning": "L032 preserves the Facebook 200-600 million, 20,000+, and 2012 figures, L024 covers Adobe hints and MD5, and L025 preserves the Proton reset evidence with the not-proof caveat."
  },
  {
   "point_id": "K15",
   "point_text": "Bottom line: for most commercial services you are trusting reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious users prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys such as YubiKey that never expose the secret.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026",
    "L033",
    "L035"
   ],
   "evidence_quote": "- 8.6 Prefer client-side encryption, open source, decentralization, hardware keys like YubiKey. (¶27)",
   "reasoning": "L026 states trust rests on reputation, jurisdiction, model, behavior rather than verifiable guarantees, and L035 lists client-side encryption, open source, decentralization, and hardware keys such as YubiKey."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 11,
  "must_have_partial": 1,
  "must_have_missing": 0,
  "overall_present": 14,
  "must_recall": 0.9583,
  "overall_recall": 0.9667
 },
 "missing_list": []
}
```

## Judge Con (concision), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "concision",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "12_lets_talk_privacy",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "L002"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Summary framing but adds the client-held-keys prescription; recap of conclusion without verbatim repeat."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines E2EE versus provider exclusion; framing distinct from summary."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Setup context about Omid; maps to no must/nice point and carries low information value."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Metadata still aids interpretation; distinct fact from section 1 body."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Closed-source uncertainty specific to Meta; distinct from Proton doubt."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Business model plus 2021 policy plus 2019 failure; causal evidence appears only here."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Smoking-gun definition for no-transfer history; distinct observation."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Locker and billboard analogy; distinct illustrative content."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "WhatsApp server key handling; distinct fact."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Rogue-device hiding in WhatsApp lists; distinct from later comparison table."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton in-browser key generation and wrapping; distinct."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Six-step login sequence; distinct detail."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hash versus encryption distinction; definition unique to section 3."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Seen hash cannot decrypt wrapped key; distinct security conclusion."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Malicious client capturing typed password; distinct counterpoint."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Preconditions for trust in client code; distinct."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton must steal password versus WhatsApp direct grant; distinct comparison."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal backup methods; distinct fact."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Physical-presence constraint adds new detail beyond C018 method list."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Zero-knowledge no recovery after key loss; distinct."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Plaintext storage doubt for Proton; distinct from Meta uncertainty."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Open clients only prove sending behavior; distinct limiting caveat."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Duplicate",
   "canonical_id": "C031",
   "reasoning": "Restates 8.3 breach numbers; cross-link L043 marks 6.2 as restatement."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reset destroys old mail, suggestive not proof; distinct evidence."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Trust rests on reputation and behavior, not guarantees; distinct."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "L027"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Three trust models; canonical for the section-7 comparison later restated."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "L028"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Rogue-device outcome per model; distinct applied result."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "L029"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Checkable item list; distinct survey content."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "L030"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Uncheckable list adds rogue staff and breaches beyond C022 caveat."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "L031"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Good and bad attributes add obscurity and violations; distinct criteria."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "L032"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Facebook 2019 figures with full detail; canonical instance."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "L033"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds zero-knowledge servers and verifiable builds beyond summary prescription."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "L034"
   ],
   "label": "Duplicate",
   "canonical_id": "C026",
   "reasoning": "Restates 7.2 three-model comparison; cross-link L045 confirms restatement."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "L035"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Recommendations add decentralization and hardware keys; distinct."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "L036"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Provenance list with dated sources; contains dates, so not trivia."
  }
 ],
 "metrics": {
  "scored_claims": 35,
  "unique": 32,
  "duplicates": 2,
  "trivia": 1,
  "redundancy_rate": 0.0571,
  "trivia_rate": 0.0286,
  "structured_tokens": 592,
  "tokens_per_unique_claim": 18.5
 },
 "prune_list": [
  "C023 duplicates C031, safe to merge",
  "C033 duplicates C026, safe to merge",
  "C003 trivia, safe to drop"
 ]
}
```

## Judge F (faithfulness), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "faithfulness",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "12_lets_talk_privacy",
 "claims": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "0"
   ],
   "claim_text": "Encrypted chats still trust providers; only client-held keys minimize that trust.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "With Signal using recovery keys, the attack surface is much smaller",
   "reasoning": "Source ranks Signal's client-controlled keys as smaller attack surface but never asserts exclusivity of 'only client-held keys', so scope is overstated."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "E2EE means device-to-device secrecy, but users need provider exclusion, not just transit safety.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "one wants E2EE so that \"no one\" can access the data outside the sender and receivers, and in particular \"the provider\"",
   "reasoning": "Source defines device-to-device encryption and states the real goal is excluding the provider, matching the claim."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Non-expert end-user inquiry from a conversation with Omid.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This came out of a conversation with Omid. DISCLAIMER: I'm not a security expert",
   "reasoning": "Source explicitly frames the piece as an end-user attempt from an Omid conversation by a non-expert."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Metadata (network, frequency, volume, timing) still aids interpretation.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they know your network, the frequency and amount of communication, times of communication etc",
   "reasoning": "Source lists exactly network, frequency, amount, and timing as interpretable metadata."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "If claims hold with no backdoors, Meta cannot read; closed source blocks certainty.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if they haven't implemented other backdoors that they have kept secret, then yes, they \"can't\" access that data. But we won't really know because the app is not open source",
   "reasoning": "Source states conditional inaccessibility plus closed-source blocking negative certainty, matching the claim."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "Business model, 2021 ad-sharing policy, and 2019 plaintext failure imply near-certain access.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can almost be certain that they can, and they do access them",
   "reasoning": "Source cites business model, 2021 policy, and plaintext failures to conclude near-certain access."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Smoking gun: history on a new device with no manual key transfer.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a smoking gun is whether the platform/app is able to \"backup\" your data",
   "reasoning": "Source names cross-device access without manual linking as the smoking gun criterion."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Locker plus receiver-only master key; server key touch equals public billboard copy.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if at any time, Facebook has access to it, it is as if you've locked your door and left a copy at the local farmers market billboard",
   "reasoning": "Source's key analogy and billboard comparison are faithfully restated."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "WhatsApp server stores encrypted history and hands keys to devices it authenticates.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server authenticates it and provides it with the keys needed to decrypt your message history",
   "reasoning": "Matches source description of server-stored history and key provisioning to authenticated devices."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "Device lists and codes rely on honest reporting; a rogue device could hide.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they could simply hide a rogue device from your device list entirely",
   "reasoning": "Source states safeguards depend on honest server reporting and a rogue device could be hidden."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Proton generates the private key in-browser, wrapping it with bcrypt and AES-256.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your private key is generated in your browser, then encrypted with your password using bcrypt and AES-256",
   "reasoning": "Exact match on in-browser generation and bcrypt/AES-256 encryption."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Six-step login: type, bcrypt with server salt, authenticate, fetch key, decrypt locally, read.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Your browser hashes the password using bcrypt (with a salt provided by Proton's server)",
   "reasoning": "All six source steps are preserved in order with correct actions."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "Hashing authenticates one-way; encryption protects two-way under the actual password.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Your private key is encrypted with your actual password (not the hash)",
   "reasoning": "Source's one-way hashing versus two-way encryption distinction and actual-password wrapping are preserved."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "In theory the seen hash cannot decrypt the password-wrapped key.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they can't use that hash to decrypt your encrypted private key",
   "reasoning": "Directly matches source's theoretical statement about the hash not decrypting the key."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Malicious client code could capture the typed password before hashing.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "captures your actual password when you type it - before it gets hashed",
   "reasoning": "Source states the identical residual risk of malicious client code capturing the pre-hash password."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Trust needs matching code, no compelled injection, uncompromised infrastructure.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They won't be compelled to inject malicious code in the future",
   "reasoning": "All three trust conditions mirror the source bullet list exactly."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Proton must steal the password first; WhatsApp grants keys directly.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp's architecture doesn't even require that step; the server can directly grant key access",
   "reasoning": "Source contrasts Proton's need to compromise the client with WhatsApp's direct key grant."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Signal: 30-digit passphrase file, device-to-device transfer, or unseen 64-character key.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a 64-character recovery key that Signal never sees or has access to",
   "reasoning": "All three Signal options and the exact 30-digit and 64-character figures match."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Android backup needs physical transfer; direct transfer needs both devices present.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Both devices must be physically present",
   "reasoning": "Source states physical transfer for backups and both devices present for direct transfer."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Zero-knowledge: no decryption, no recovery help after a lost key.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they cannot help you recover them if you lose your recovery key. This is genuinely zero-knowledge architecture",
   "reasoning": "Source states Signal cannot decrypt backups or help recover after key loss, calling it zero-knowledge."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Plaintext password storage cannot be ruled out with certainty.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "we don't know for certain",
   "reasoning": "Source's short answer is explicitly that certainty about plaintext storage is unavailable."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Open clients prove sending behavior, never the server's later handling.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can confirm that passwords are hashed before transmission. But you cannot verify what happens on the server",
   "reasoning": "Matches source's distinction between verifiable client behavior and unverifiable server handling."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Facebook logged hundreds of millions plaintext for years; Adobe leaked hints; MD5 persists.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "logging hundreds of millions of passwords in plaintext in internal logs for years",
   "reasoning": "All three source precedents, including unsalted MD5 at smaller services, are accurately summarized."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Proton reset destroys old mail, suggesting genuine inability, but proves nothing.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you lose access to all your old encrypted emails. This suggests they genuinely can't decrypt your data",
   "reasoning": "Source notes reset loses old mail, suggests genuine inability, and explicitly denies it is proof."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Trust rests on reputation, jurisdiction, model, behavior, not verifiable guarantees.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees",
   "reasoning": "Direct paraphrase preserving all listed trust factors and the guarantee contrast."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "Escrow (WhatsApp) versus password-wrapped (Proton) versus client-controlled (Signal).",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Server-mediated key escrow",
   "reasoning": "Matches the table's three security model names for the three services."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Rogue device: YES for WhatsApp; NO for Proton and Signal (client caveat).",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "NO - but they could serve malicious client code to capture your password",
   "reasoning": "Table's YES for WhatsApp and NO for Proton/Signal, including the Proton client caveat, are preserved."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Checkable: open clients, Wireshark traffic, audits of deployed code.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Tools like Wireshark can show what's transmitted",
   "reasoning": "All three verifiable checks match source's open clients, network inspection, and audits."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Uncheckable: running code, later updates, rogue staff, breaches.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "an employee with server access could modify it, or someone who breaches their systems could inject logging",
   "reasoning": "Matches source's unverifiable items: running code, later changes, rogue employees, breaches."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Good: open servers, audits, clean breaches; bad: reset-proof data, obscurity, violations.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Can reset password and access old data",
   "reasoning": "Good and bad signs map to source lists, with 'reset-proof data' reflecting the reset-access sign."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Facebook 2019: 200-600 million passwords, 20,000+ searchers, archives from 2012.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "between 200-600 million passwords in plaintext",
   "reasoning": "The range, 20,000 employees, and 2012 archive date all match the source exactly."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Trust ends only with client-side crypto, zero-knowledge servers, verifiable builds.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "All cryptography happens client-side",
   "reasoning": "Source's three 'unless' conditions of client-side crypto, non-decryptable server, and reproducible builds are preserved."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "WhatsApp needs whole-infrastructure trust; Proton hashing honesty; Signal key custody.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Meta's entire server infrastructure",
   "reasoning": "The applied trust table entries for all three services are accurately condensed."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "Prefer client-side encryption, open source, decentralization, hardware keys like YubiKey.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "hardware security keys (like YubiKey) that never expose the secret",
   "reasoning": "All four bottom-line preferences match the source recommendation."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Sources: Meta 2021 engineering, Proton key docs, Signal September 2024 backups.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Introducing Signal Secure Backups ... (Signal Blog, September 2024)",
   "reasoning": "Source list cites Meta's July 2021 engineering post, Proton key docs, and Signal September 2024 backups."
  }
 ],
 "metrics": {
  "total_claims": 35,
  "supported": 34,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9714
 },
 "fail_list": [
  "C001"
 ]
}
```

## Judge Cov (coverage), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "coverage",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "12_lets_talk_privacy",
 "key_points": [
  {
   "point_id": "K01",
   "point_text": "Central thesis: 'end-to-end encryption' means the sender's device encrypts and the receiver's device decrypts with no decryption in between, but the real question is whether the provider (not just a man-in-the-middle) can access the content, and the answer is not completely clear.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L006"
   ],
   "evidence_quote": "- 1 E2EE means device-to-device secrecy, but users need provider exclusion, not just transit safety. (¶1, ¶2)",
   "reasoning": "L003 states E2EE is device-to-device but frames the real need as provider exclusion, and L006 states certainty is blocked, capturing both halves of the thesis."
  },
  {
   "point_id": "K02",
   "point_text": "People usually want E2EE so that no one outside sender and receivers, particularly the provider, can access data. For WhatsApp this means Facebook should not access message content, but it still has metadata such as network, frequency, amount, and timing of communication.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L005"
   ],
   "evidence_quote": "- 1.2 Nuance: Metadata (network, frequency, volume, timing) still aids interpretation. (¶2)",
   "reasoning": "L003 captures provider-exclusion motive, and L005 lists the metadata dimensions closely matching network, frequency, volume/amount, timing."
  },
  {
   "point_id": "K03",
   "point_text": "For WhatsApp the answer is unclear: if implemented as claimed and with no secret backdoors they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative (that access is impossible).",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006"
   ],
   "evidence_quote": "- 1.3 If claims hold with no backdoors, Meta cannot read; closed source blocks certainty. (¶3)",
   "reasoning": "L006 preserves the conditional (claims hold, no backdoors) and the closed-source barrier to certainty, which is the core of the unclear answer."
  },
  {
   "point_id": "K04",
   "point_text": "Evidence against WhatsApp/Meta: the 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as storing hundreds of millions of passwords in plaintext, make it almost certain they can and do access message content.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007"
   ],
   "evidence_quote": "- 1.4 Business model, 2021 ad-sharing policy, and 2019 plaintext failure imply near-certain access. (¶3)",
   "reasoning": "L007 names the business model, the 2021 ad-sharing policy, and the plaintext failure, concluding near-certain access, matching the point."
  },
  {
   "point_id": "K05",
   "point_text": "Smoking gun test: whether a platform can back up or let you access history across devices without manually linking/transferring keys. If the provider ever holds the key, it is like leaving a copy of your door key on a public billboard and it can decrypt any messages at will.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009"
   ],
   "evidence_quote": "- 2 Smoking gun: history on a new device with no manual key transfer. (¶4)",
   "reasoning": "L008 states the smoking-gun test, and L009 preserves the public-billboard analogy for any server key custody."
  },
  {
   "point_id": "K06",
   "point_text": "How WhatsApp actually works: the server stores encrypted message history and device-to-account identity mappings, authenticates new devices, and provides the keys needed to decrypt history. This makes the server a trusted intermediary that could silently authenticate a rogue device and hide it from your device list, unlike Signal's manual key transfer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011"
   ],
   "evidence_quote": "- 2.2 WhatsApp server stores encrypted history and hands keys to devices it authenticates. (¶5)",
   "reasoning": "L010 captures server-stored encrypted history and key hand-off to authenticated devices, and L011 captures the rogue device hiding from device lists, matching the trusted-intermediary concern."
  },
  {
   "point_id": "K07",
   "point_text": "Proton Mail model: the private key is generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L012"
   ],
   "evidence_quote": "- 3 Proton generates the private key in-browser, wrapping it with bcrypt and AES-256. (¶6)",
   "reasoning": "L012 preserves in-browser key generation and both named algorithms (bcrypt, AES-256), capturing the encrypted-key-at-rest model."
  },
  {
   "point_id": "K08",
   "point_text": "Proton login flow: type password, browser hashes it with bcrypt plus a server-provided salt, sends the hash to authenticate, server returns the encrypted private key, and the browser decrypts it locally with the actual password.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L013"
   ],
   "evidence_quote": "- 3.1 Evidence: Six-step login: type, bcrypt with server salt, authenticate, fetch key, decrypt locally, read. (¶7)",
   "reasoning": "L013 preserves all six steps including bcrypt with server salt and local decryption with the actual password."
  },
  {
   "point_id": "K09",
   "point_text": "Distinction between hashing (one-way, used for authentication, cannot be reversed to the password) and encryption (two-way, used on the private key). Proton receives the hash for authentication while the key is encrypted with the actual password, so in theory the hash cannot decrypt the key.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L014",
    "L015"
   ],
   "evidence_quote": "- 3.2 Hashing authenticates one-way; encryption protects two-way under the actual password. (¶8)",
   "reasoning": "L014 draws the one-way hashing versus two-way encryption distinction, and L015 preserves the claim that the seen hash theoretically cannot decrypt the key."
  },
  {
   "point_id": "K10",
   "point_text": "Proton's critical residual vulnerability: Proton could serve malicious client code (web app or update) to capture the actual password before hashing and use it to decrypt the stored key. This is why open-source clients matter, yet you must still trust the served code matches the source, no future malicious injection, and no infrastructure compromise.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L016",
    "L017"
   ],
   "evidence_quote": "- 4 Counterpoint: Malicious client code could capture the typed password before hashing. (¶10)",
   "reasoning": "L016 states the malicious-client password-capture threat, and L017 preserves the three residual trust requirements (matching code, no compelled injection, uncompromised infrastructure)."
  },
  {
   "point_id": "K11",
   "point_text": "Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L019",
    "L020"
   ],
   "evidence_quote": "- 5 Signal: 30-digit passphrase file, device-to-device transfer, or unseen 64-character key. (¶12)",
   "reasoning": "L019 captures all three switching options with the 30-digit and 64-character figures, and L020 notes physical-presence constraints. However the default condition that history is stored only on the device and deleted from servers after delivery is not stated, a dropped scope qualifier for a Must have point."
  },
  {
   "point_id": "K12",
   "point_text": "Signal is genuinely zero-knowledge: servers are never positioned to grant access to message history, and even with cloud backups Signal cannot decrypt backups and cannot help recover them if the recovery key is lost.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L021"
   ],
   "evidence_quote": "- 5.2 Nuance: Zero-knowledge: no decryption, no recovery help after a lost key. (¶13)",
   "reasoning": "L021 explicitly states zero-knowledge with no decryption and no recovery help after a lost key, matching the point."
  },
  {
   "point_id": "K13",
   "point_text": "Password storage limits: you can verify what an open-source client does (hashing before transmission), inspect network traffic, and read audits, but you cannot verify server-side code, whether it changed after an audit, rogue employees, or breaches. There is no cryptographic guarantee about server password handling.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022",
    "L023",
    "L029",
    "L030"
   ],
   "evidence_quote": "- 8.1 Uncheckable: running code, later updates, rogue staff, breaches. (¶22)",
   "reasoning": "L029 covers checkable items (open clients, traffic inspection, audits), L030 covers uncheckable items (running code, later updates, rogue staff, breaches), and L022 states plaintext storage cannot be ruled out with certainty, matching the no-cryptographic-guarantee claim."
  },
  {
   "point_id": "K14",
   "point_text": "Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext in internal logs for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, and many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though this is not proof.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L024",
    "L025",
    "L032"
   ],
   "evidence_quote": "- 8.3 Evidence: Facebook 2019: 200-600 million passwords, 20,000+ searchers, archives from 2012. (¶24)",
   "reasoning": "L032 preserves the Facebook 200-600 million, 20,000+, and 2012 figures, L024 covers Adobe hints and MD5, and L025 preserves the Proton reset evidence with the not-proof caveat."
  },
  {
   "point_id": "K15",
   "point_text": "Bottom line: for most commercial services you are trusting reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious users prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys such as YubiKey that never expose the secret.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L026",
    "L033",
    "L035"
   ],
   "evidence_quote": "- 8.6 Prefer client-side encryption, open source, decentralization, hardware keys like YubiKey. (¶27)",
   "reasoning": "L026 states trust rests on reputation, jurisdiction, model, behavior rather than verifiable guarantees, and L035 lists client-side encryption, open source, decentralization, and hardware keys such as YubiKey."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 11,
  "must_have_partial": 1,
  "must_have_missing": 0,
  "overall_present": 14,
  "must_recall": 0.9583,
  "overall_recall": 0.9667
 },
 "missing_list": []
}
```

## Judge Con (concision), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "concision",
 "judge_version": "1.0.0",
 "model": "opencode-go/deepseek-v4.1-flash (opencode) scripted pipeline 2026-09-15",
 "source_id": "12_lets_talk_privacy",
 "labels": [
  {
   "claim_id": "C001",
   "loglog_ids": [
    "L002"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Summary framing but adds the client-held-keys prescription; recap of conclusion without verbatim repeat."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Defines E2EE versus provider exclusion; framing distinct from summary."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Setup context about Omid; maps to no must/nice point and carries low information value."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Metadata still aids interpretation; distinct fact from section 1 body."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Closed-source uncertainty specific to Meta; distinct from Proton doubt."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Business model plus 2021 policy plus 2019 failure; causal evidence appears only here."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Smoking-gun definition for no-transfer history; distinct observation."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Locker and billboard analogy; distinct illustrative content."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "WhatsApp server key handling; distinct fact."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Rogue-device hiding in WhatsApp lists; distinct from later comparison table."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton in-browser key generation and wrapping; distinct."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Six-step login sequence; distinct detail."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hash versus encryption distinction; definition unique to section 3."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Seen hash cannot decrypt wrapped key; distinct security conclusion."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Malicious client capturing typed password; distinct counterpoint."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Preconditions for trust in client code; distinct."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton must steal password versus WhatsApp direct grant; distinct comparison."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal backup methods; distinct fact."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Physical-presence constraint adds new detail beyond C018 method list."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Zero-knowledge no recovery after key loss; distinct."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Plaintext storage doubt for Proton; distinct from Meta uncertainty."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Open clients only prove sending behavior; distinct limiting caveat."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Duplicate",
   "canonical_id": "C031",
   "reasoning": "Restates 8.3 breach numbers; cross-link L043 marks 6.2 as restatement."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reset destroys old mail, suggestive not proof; distinct evidence."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Trust rests on reputation and behavior, not guarantees; distinct."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "L027"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Three trust models; canonical for the section-7 comparison later restated."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "L028"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Rogue-device outcome per model; distinct applied result."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "L029"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Checkable item list; distinct survey content."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "L030"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Uncheckable list adds rogue staff and breaches beyond C022 caveat."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "L031"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Good and bad attributes add obscurity and violations; distinct criteria."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "L032"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Facebook 2019 figures with full detail; canonical instance."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "L033"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds zero-knowledge servers and verifiable builds beyond summary prescription."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "L034"
   ],
   "label": "Duplicate",
   "canonical_id": "C026",
   "reasoning": "Restates 7.2 three-model comparison; cross-link L045 confirms restatement."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "L035"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Recommendations add decentralization and hardware keys; distinct."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "L036"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Provenance list with dated sources; contains dates, so not trivia."
  }
 ],
 "metrics": {
  "scored_claims": 35,
  "unique": 32,
  "duplicates": 2,
  "trivia": 1,
  "redundancy_rate": 0.0571,
  "trivia_rate": 0.0286,
  "structured_tokens": 592,
  "tokens_per_unique_claim": 18.5
 },
 "prune_list": [
  "C023 duplicates C031, safe to merge",
  "C033 duplicates C026, safe to merge",
  "C003 trivia, safe to drop"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "deepseek-v4.1-flash (2026-09-15)",
 "source_id": "point-hierarchy sample (source_id not provided in inputs)",
 "inputs": {
  "faithfulness_precision": 0.9714,
  "critical_errors": 0,
  "must_recall": 0.9583,
  "overall_recall": 0.9667,
  "redundancy_rate": 0.0571,
  "trivia_rate": 0.0286
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted_score = 0.4*0.9714 + 0.4*0.9583 - 0.2*0.0571 = 0.38856 + 0.38332 - 0.01142 = 0.76046",
 "weighted_score": 0.7605,
 "verdict": "Borderline",
 "tradeoff_note": "All numeric gates pass and concision is comfortably under the redundancy max, so the 18.5 tokens per unique claim is justified by near-complete must-have coverage. However a Must-have point (K11) is only partially covered and one Partial claim (C001) sits near a Must-have trust point, so human review is advised before ship.",
 "fix_list": [
  "Restore the dropped scope qualifier in K11: state that history is stored only on your device and deleted from servers after delivery, in addition to the three device-switching options (L019/L020).",
  "Narrow C001 to match the source: Signal's client-controlled keys yield a smaller attack surface, rather than asserting that only client-held keys minimize provider trust (source quote: 'With Signal using recovery keys, the attack surface is much smaller').",
  "Merge duplicate pair C023/C031 and C033/C026 to lift the unique-claim ratio, and drop the trivia claim C003.",
  "If any slack remains after K11, spend it on the C001 nuance rather than new material, since redundancy headroom (0.0571 vs 0.15) is still ample and coverage is the binding constraint."
 ],
 "reasoning": "Gate checks in order: (1) critical_errors = 0, at the config max of 0, so no hard fail and no Critical error is present. (2) must_recall = 0.9583, computed as (11 present + 0.5 partial)/(12 must-have) from coverage metrics (must_have_total 12, present 11, partial 1, missing 0), which clears the 0.9 minimum. (3) faithfulness_precision = 0.9714 = 34 supported / 35 total claims, which clears the 0.95 minimum; there are 0 contradicted and 0 unverifiable claims. (4) redundancy_rate = 0.0571 = 2 duplicates/35 scored claims, under the 0.15 max, with trivia_rate 0.0286 from the single trivia claim C003. Because all gates pass, the weighted score applies per the config aspect_weights: 0.4 faithfulness (0.9714) gives 0.38856, 0.4 must_recall (0.9583) gives 0.38332, minus 0.2 redundancy (0.0571) = 0.01142, for 0.76046, reported as 0.7605. Verdict is Borderline rather than Pass because, although the numbers clear every gate, the one Partial faith-fulness claim C001 (Minor severity) is an overstated-scope interpretation ('only client-held keys minimize that trust') that the source does not assert, and the coverage partial K11 is a Must-have whose dropped qualifier is the default local-only storage plus server-side deletion. Under the policy's borderline rule (gates met but a Partial claim affects a Must-have point), this warrants human review, so I name C001 and K11. Concision does not affect the verdict downgrade: redundancy is low and no concision metric rescues or harms a faithfulness or coverage concern, it only serves as a tie-breaker, which is moot here."
}
```
