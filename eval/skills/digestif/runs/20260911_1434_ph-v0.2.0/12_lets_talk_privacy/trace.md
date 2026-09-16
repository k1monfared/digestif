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
   "claim_text": "Encryption excludes providers only when clients hold keys; WhatsApp escrows, Proton needs trust, Signal minimizes.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Signal's servers are never in a position to grant access to your message history ... Server-mediated key escrow ... still requires some trust",
   "reasoning": "SOURCE states WhatsApp escrow, Proton trust need, and Signal client-held key minimizing trust."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "End-to-end encryption can mean several practical things beyond device-to-device ciphertext.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they could mean several things in practical terms",
   "reasoning": "SOURCE uses nearly identical wording about E2EE meaning several practical things."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Real goal is excluding the provider, though metadata like contacts and timing still leaks.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "no one can access the data outside the sender and receivers, and in particular the provider ... they know your network, the frequency and amount of communication, times of communication",
   "reasoning": "SOURCE states provider-exclusion goal and lists metadata leaks including timing and network."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Meta likely accesses WhatsApp content given closed source, ad-data sharing, past plaintext failures.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can almost be certain that they can, and they do access them",
   "reasoning": "SOURCE cites closed source, ad-sharing policy, plaintext failures and concludes near certainty of access."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Smoking gun: history portability without manual key transfer betrays server key access.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a smoking gun is whether the platform/app is able to 'backup' your data. Whether you can access your history across devices without 'manually' linking them",
   "reasoning": "SOURCE frames cross-device history without manual linking as the smoking gun for key access."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Signal forces manual key copy; any server-touchable key is like public copies.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is what happens in Signal. What you need to do is to somehow copy the key ... left a copy at the local farmers market billboard",
   "reasoning": "SOURCE says Signal requires copying the key and compares server-accessible keys to public copies."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "WhatsApp server stores encrypted history and maps accounts to device identities.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server stores encrypted message history and maintains mappings between your account and all your device identities",
   "reasoning": "SOURCE states both storage and account-to-device mapping directly."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Server-authenticated new devices receive decryption keys; rogue devices could hide from lists.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server authenticates it and provides it with the keys needed to decrypt ... they could simply hide a rogue device from your device list entirely",
   "reasoning": "SOURCE states both claims explicitly in the WhatsApp section."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Proton generates browser-side keys, then stores them server-side encrypted under user password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your private key is generated in your browser, then encrypted with your password ... before being sent to their servers for storage",
   "reasoning": "SOURCE states browser generation and password-encrypted server storage directly."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Login: bcrypt-hash authenticates, server returns encrypted key, browser decrypts locally.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Your browser hashes the password using bcrypt ... The server sends your encrypted private key back ... decrypt this private key locally",
   "reasoning": "SOURCE's numbered login steps match the node exactly."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Hashing authenticates one-way while encryption reversibly protects the private key.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Hashing ... A one-way function ... Encryption ... A two-way function ... encrypted with your actual password",
   "reasoning": "SOURCE defines hashing as one-way for auth and encryption as two-way for the private key."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Proton could serve malicious client code capturing passwords, then decrypt stored keys.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Proton could serve you malicious client code ... that captures your actual password ... if they capture your password, they can decrypt it",
   "reasoning": "SOURCE states the malicious-client-code vulnerability and resulting decryption directly."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Open source helps only if served code matches, stays honest, infrastructure stays clean.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The code they're actually serving matches the open-source code ... They won't be compelled to inject malicious code ... infrastructure hasn't been compromised",
   "reasoning": "SOURCE lists these three trust conditions for open-source clients."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Unlike WhatsApp, Proton must first compromise the client to steal passwords.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Proton doesn't have direct access ... they'd need to actively compromise the client to steal your password first. WhatsApp's architecture doesn't even require that step",
   "reasoning": "SOURCE contrasts Proton client-compromise need against WhatsApp direct key access."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Signal stores history on-device, deleting server copies after delivery.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "message history is stored only on your device and deleted from Signal's servers after delivery",
   "reasoning": "SOURCE states on-device storage and server deletion after delivery exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Migration needs physical backup plus passphrase, device transfer, or unseen recovery key.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted backup file protected by a 30-digit passphrase ... Direct device-to-device transfer ... 64-character recovery key that Signal never sees",
   "reasoning": "SOURCE lists the same three Signal migration options."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Signal servers cannot grant history access; recovery keys stay client-side and unrecoverable.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "servers are never in a position to grant access to your message history ... recovery key stays on your device ... cannot help you recover them if you lose",
   "reasoning": "SOURCE states server inability to grant access and irrecoverability of lost keys."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Password handling adds another unverifiable layer beneath encryption architecture.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "there's another layer to this. Even if we trust the encryption architecture, how do we know companies don't store your password in plaintext",
   "reasoning": "SOURCE raises plaintext password storage as a distinct additional layer."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Client hashing is verifiable in open source; server behavior after arrival is not.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "You can verify what the client does (if it's open source) ... you cannot verify what happens on the server after your password ... arrives",
   "reasoning": "SOURCE states client verification but not server behavior verification."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Facebook logged hundreds of millions of plaintext passwords; Adobe hints leaked; small services worse.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "logging hundreds of millions of passwords in plaintext ... Adobe's 2013 breach revealed they stored password hints in plaintext. Many smaller services store passwords in plaintext",
   "reasoning": "SOURCE states each example with matching scale and party."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Proton password-reset data loss suggests honest design but proves nothing about capability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you lose access to all your old encrypted emails. This suggests they genuinely can't decrypt ... But even this isn't proof",
   "reasoning": "SOURCE draws the same suggestion while explicitly denying it is proof."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "Without client crypto guarantees, users trust reputation, jurisdiction, model, history.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees",
   "reasoning": "SOURCE lists the same four trust bases and absence of verification."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "Architecture sets trust surface: Meta infrastructure, Proton client integrity, Signal key custody.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "trusting Meta's entire server infrastructure ... trusting they won't serve malicious code ... Signal ... attack surface is much smaller",
   "reasoning": "SOURCE maps each service to the trust it demands in the same terms."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Comparison names WhatsApp escrow, Proton password-encrypted storage, Signal client control.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Server-mediated key escrow ... Password-encrypted server-side key storage ... Client-controlled keys",
   "reasoning": "SOURCE table names the same three security models."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Nobody can verify that companies avoid plaintext password storage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Short answer: We don't know for certain.",
   "reasoning": "SOURCE states plaintext storage cannot be verified with certainty."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Verifiable: open clients, traffic checks, audits with published results.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Open-source clients ... Network traffic inspection ... Independent security audits ... with published results",
   "reasoning": "SOURCE lists open clients, traffic inspection, and published audits as verifiable."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Unverifiable: closed server code, later changes, rogue staff, breaches.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Server-side code: Almost always closed-source ... changed it later ... Rogue employees or breaches",
   "reasoning": "SOURCE lists the same closed-code, later-change, rogue-employee, breach items."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Look for open servers, audits, breach behavior; beware resets, obscurity, violation history.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Open-source server code ... Independent security audits ... Breach disclosure ... Can reset password and access old data ... Security through obscurity ... History of privacy violations",
   "reasoning": "SOURCE's good and bad signs match the node's list."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Adobe 2013 hints, Facebook 2019 plaintext logging, small services with weak unsalted storage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Adobe (2013) ... password hints in plaintext ... Facebook (2019) ... plaintext ... small services ... MD5 without salt",
   "reasoning": "SOURCE records each example with matching years and details."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Trust-minimizing needs client-side crypto, zero-knowledge servers, reproducible audited builds.",
   "claim_type": "recommendation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "All cryptography happens client-side ... The server never sees anything that could decrypt your data ... open-source AND reproducibly built AND you can verify what's running",
   "reasoning": "SOURCE says reproducibly built and verifiable, not 'audited'; added qualifier slightly changes the third condition."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "Applied trust: WhatsApp everything, Proton hashing plus client, Signal implementation plus custody.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp | Meta's entire server infrastructure ... Proton Mail | They hash your password properly ... Signal | Much less trust required",
   "reasoning": "SOURCE's applied trust table matches the node's summary."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Prefer client-side encryption, open everything, decentralization, hardware security keys.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys",
   "reasoning": "SOURCE states the same four preferences verbatim in the Bottom Line."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "Sources document WhatsApp multi-device, Proton key storage, Signal secure backups.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "How WhatsApp enables multi-device capability ... How is the private key stored? ... Introducing Signal Secure Backups",
   "reasoning": "SOURCE's Sources section lists exactly these references."
  }
 ],
 "metrics": {
  "total_claims": 33,
  "supported": 32,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9697
 },
 "fail_list": [
  "C030"
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
    "L002",
    "L003",
    "L004"
   ],
   "evidence_quote": "End-to-end encryption can mean several practical things beyond device-to-device ciphertext. ... Real goal is excluding the provider",
   "reasoning": "L003 captures the definition as device-to-device ciphertext and L004 reframes the real question as excluding the provider. L002 records the mixed verdict (escrow/trust/minimize), covering the 'not completely clear' thrust."
  },
  {
   "point_id": "K02",
   "point_text": "People usually want E2EE so that no one outside sender and receivers, particularly the provider, can access data. For WhatsApp this means Facebook should not access message content, but it still has metadata such as network, frequency, amount, and timing of communication.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "Real goal is excluding the provider, though metadata like contacts and timing still leaks.",
   "reasoning": "Provider-exclusion goal and the metadata residual are both stated. The illustrative metadata list is compressed to 'contacts and timing' but the idea and its qualifier survive."
  },
  {
   "point_id": "K03",
   "point_text": "For WhatsApp the answer is unclear: if implemented as claimed and with no secret backdoors they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative (that access is impossible).",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L005",
    "L028"
   ],
   "evidence_quote": "Meta likely accesses WhatsApp content given closed source, ad-data sharing, past plaintext failures. ... Unverifiable: closed server code, later changes, rogue staff, breaches.",
   "reasoning": "Closed-source and unverifiability are captured, but the loglog hardens the original open question into a firm verdict ('likely accesses') rather than preserving 'the answer is unclear' and the cannot-prove-a-negative framing. Scope is narrowed, so Partial."
  },
  {
   "point_id": "K04",
   "point_text": "Evidence against WhatsApp/Meta: the 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as storing hundreds of millions of passwords in plaintext, make it almost certain they can and do access message content.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L005",
    "L021"
   ],
   "evidence_quote": "class closed source, ad-data sharing, past plaintext failures. ... Facebook logged hundreds of millions of plaintext passwords",
   "reasoning": "Ad-data sharing and the plaintext-failure evidence are present, and 'hundreds of millions' survives, but the 2021 date of the privacy policy change is dropped. A Must have point missing a key date is at most Partial."
  },
  {
   "point_id": "K05",
   "point_text": "Smoking gun test: whether a platform can back up or let you access history across devices without manually linking/transferring keys. If the provider ever holds the key, it is like leaving a copy of your door key on a public billboard and it can decrypt any messages at will.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L007"
   ],
   "evidence_quote": "Smoking gun: history portability without manual key transfer betrays server key access. ... Signal forces manual key copy; any server-touchable key is like public copies.",
   "reasoning": "Both the portability test and the public-key-copy analogy are captured accurately."
  },
  {
   "point_id": "K06",
   "point_text": "How WhatsApp actually works: the server stores encrypted message history and device-to-account identity mappings, authenticates new devices, and provides the keys needed to decrypt history. This makes the server a trusted intermediary that could silently authenticate a rogue device and hide it from your device list, unlike Signal's manual key transfer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009"
   ],
   "evidence_quote": "WhatsApp server stores encrypted history and maps accounts to device identities. ... Server-authenticated new devices receive decryption keys; rogue devices could hide from lists.",
   "reasoning": "All elements (encrypted history, identity mapping, device authentication, key delivery, rogue-device hiding) are present, and the Signal contrast is covered by L007."
  },
  {
   "point_id": "K07",
   "point_text": "Proton Mail model: the private key is generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L010",
    "L011"
   ],
   "evidence_quote": "Proton generates browser-side keys, then stores them server-side encrypted under user password. ... Login: bcrypt-hash authenticates",
   "reasoning": "Browser-side generation and password-encrypted server storage are captured, and bcrypt appears, but AES-256 is never named. A Must have point with a dropped technical number is at most Partial."
  },
  {
   "point_id": "K08",
   "point_text": "Proton login flow: type password, browser hashes it with bcrypt plus a server-provided salt, sends the hash to authenticate, server returns the encrypted private key, and the browser decrypts it locally with the actual password.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L011"
   ],
   "evidence_quote": "Login: bcrypt-hash authenticates, server returns encrypted key, browser decrypts locally.",
   "reasoning": "The full flow is captured: bcrypt hashing authenticates, server returns encrypted key, browser decrypts locally. The server-provided salt detail is a minor omission on a Nice to have point and does not defeat the idea."
  },
  {
   "point_id": "K09",
   "point_text": "Distinction between hashing (one-way, used for authentication, cannot be reversed to the password) and encryption (two-way, used on the private key). Proton receives the hash for authentication while the key is encrypted with the actual password, so in theory the hash cannot decrypt the key.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L012"
   ],
   "evidence_quote": "Hashing authenticates one-way while encryption reversibly protects the private key.",
   "reasoning": "The one-way versus reversible distinction is captured directly, implying the hash cannot decrypt the key. Core idea intact."
  },
  {
   "point_id": "K10",
   "point_text": "Proton's critical residual vulnerability: Proton could serve malicious client code (web app or update) to capture the actual password before hashing and use it to decrypt the stored key. This is why open-source clients matter, yet you must still trust the served code matches the source, no future malicious injection, and no infrastructure compromise.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L014"
   ],
   "evidence_quote": "Proton could serve malicious client code capturing passwords, then decrypt stored keys. ... Open source helps only if served code matches, stays honest, infrastructure stays clean.",
   "reasoning": "The malicious-code vulnerability and all three residual trust conditions (served code matches, stays honest, clean infrastructure) are captured."
  },
  {
   "point_id": "K11",
   "point_text": "Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L016",
    "L017"
   ],
   "evidence_quote": "Signal stores history on-device, deleting server copies after delivery. ... Migration needs physical backup plus passphrase, device transfer, or unseen recovery key.",
   "reasoning": "The on-device storage model and all three migration options are present with the correct qualifiers, but the 30-digit passphrase and 64-character recovery key numbers are dropped. A Must have point with dropped numbers is at most Partial."
  },
  {
   "point_id": "K12",
   "point_text": "Signal is genuinely zero-knowledge: servers are never positioned to grant access to message history, and even with cloud backups Signal cannot decrypt backups and cannot help recover them if the recovery key is lost.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018"
   ],
   "evidence_quote": "Signal servers cannot grant history access; recovery keys stay client-side and unrecoverable.",
   "reasoning": "Both the zero-knowledge server position and the unrecoverable recovery key are captured, matching the original."
  },
  {
   "point_id": "K13",
   "point_text": "Password storage limits: you can verify what an open-source client does (hashing before transmission), inspect network traffic, and read audits, but you cannot verify server-side code, whether it changed after an audit, rogue employees, or breaches. There is no cryptographic guarantee about server password handling.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L019",
    "L020",
    "L027",
    "L028"
   ],
   "evidence_quote": "Client hashing is verifiable in open source; server behavior after arrival is not. ... Verifiable: open clients, traffic checks, audits with published results. Unverifiable: closed server code, later changes, rogue staff, breaches.",
   "reasoning": "The verifiable side (open clients, traffic checks, audits) and the unverifiable side (server code, later changes, rogue staff, breaches) are both captured, preserving the no-guarantee conclusion."
  },
  {
   "point_id": "K14",
   "point_text": "Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext in internal logs for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, and many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though this is not proof.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L021",
    "L022",
    "L030"
   ],
   "evidence_quote": "Facebook logged hundreds of millions of plaintext passwords; Adobe hints leaked; small services worse. ... Adobe 2013 hints, Facebook 2019 plaintext logging, small services with weak unsalted storage. ... Proton password-reset data loss suggests honest design but proves nothing.",
   "reasoning": "The three examples and the Proton caveat are present, with years 2019/2013 and 'hundreds of millions' retained, but the 200-600 million range, 20,000 employees, 2012 archive date, and MD5 specificity are dropped. Nice to have, so this is a polish issue rather than a failure."
  },
  {
   "point_id": "K15",
   "point_text": "Bottom line: for most commercial services you are trusting reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious users prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys such as YubiKey that never expose the secret.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L031",
    "L033"
   ],
   "evidence_quote": "users trust reputation, jurisdiction, model, history. ... Trust-minimizing needs client-side crypto, zero-knowledge servers, reproducible audited builds. ... Prefer client-side encryption, open everything, decentralization, hardware security keys.",
   "reasoning": "The trust-basis conclusion and the preference list (client-side crypto, open everything, decentralization, hardware keys) are all captured. The YubiKey example and 'never expose the secret' nuance are omitted, but the actionable recommendation survives."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 8,
  "must_have_partial": 4,
  "must_have_missing": 0,
  "overall_present": 10,
  "must_recall": 0.8333,
  "overall_recall": 0.8333
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
   "claim_text": "Encryption excludes providers only when clients hold keys; WhatsApp escrows, Proton needs trust, Signal minimizes.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Signal's servers are never in a position to grant access to your message history ... Server-mediated key escrow ... still requires some trust",
   "reasoning": "SOURCE states WhatsApp escrow, Proton trust need, and Signal client-held key minimizing trust."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "End-to-end encryption can mean several practical things beyond device-to-device ciphertext.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they could mean several things in practical terms",
   "reasoning": "SOURCE uses nearly identical wording about E2EE meaning several practical things."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Real goal is excluding the provider, though metadata like contacts and timing still leaks.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "no one can access the data outside the sender and receivers, and in particular the provider ... they know your network, the frequency and amount of communication, times of communication",
   "reasoning": "SOURCE states provider-exclusion goal and lists metadata leaks including timing and network."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Meta likely accesses WhatsApp content given closed source, ad-data sharing, past plaintext failures.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can almost be certain that they can, and they do access them",
   "reasoning": "SOURCE cites closed source, ad-sharing policy, plaintext failures and concludes near certainty of access."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Smoking gun: history portability without manual key transfer betrays server key access.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a smoking gun is whether the platform/app is able to 'backup' your data. Whether you can access your history across devices without 'manually' linking them",
   "reasoning": "SOURCE frames cross-device history without manual linking as the smoking gun for key access."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Signal forces manual key copy; any server-touchable key is like public copies.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is what happens in Signal. What you need to do is to somehow copy the key ... left a copy at the local farmers market billboard",
   "reasoning": "SOURCE says Signal requires copying the key and compares server-accessible keys to public copies."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "WhatsApp server stores encrypted history and maps accounts to device identities.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server stores encrypted message history and maintains mappings between your account and all your device identities",
   "reasoning": "SOURCE states both storage and account-to-device mapping directly."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Server-authenticated new devices receive decryption keys; rogue devices could hide from lists.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server authenticates it and provides it with the keys needed to decrypt ... they could simply hide a rogue device from your device list entirely",
   "reasoning": "SOURCE states both claims explicitly in the WhatsApp section."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Proton generates browser-side keys, then stores them server-side encrypted under user password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your private key is generated in your browser, then encrypted with your password ... before being sent to their servers for storage",
   "reasoning": "SOURCE states browser generation and password-encrypted server storage directly."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Login: bcrypt-hash authenticates, server returns encrypted key, browser decrypts locally.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Your browser hashes the password using bcrypt ... The server sends your encrypted private key back ... decrypt this private key locally",
   "reasoning": "SOURCE's numbered login steps match the node exactly."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Hashing authenticates one-way while encryption reversibly protects the private key.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Hashing ... A one-way function ... Encryption ... A two-way function ... encrypted with your actual password",
   "reasoning": "SOURCE defines hashing as one-way for auth and encryption as two-way for the private key."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Proton could serve malicious client code capturing passwords, then decrypt stored keys.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Proton could serve you malicious client code ... that captures your actual password ... if they capture your password, they can decrypt it",
   "reasoning": "SOURCE states the malicious-client-code vulnerability and resulting decryption directly."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Open source helps only if served code matches, stays honest, infrastructure stays clean.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The code they're actually serving matches the open-source code ... They won't be compelled to inject malicious code ... infrastructure hasn't been compromised",
   "reasoning": "SOURCE lists these three trust conditions for open-source clients."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Unlike WhatsApp, Proton must first compromise the client to steal passwords.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Proton doesn't have direct access ... they'd need to actively compromise the client to steal your password first. WhatsApp's architecture doesn't even require that step",
   "reasoning": "SOURCE contrasts Proton client-compromise need against WhatsApp direct key access."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Signal stores history on-device, deleting server copies after delivery.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "message history is stored only on your device and deleted from Signal's servers after delivery",
   "reasoning": "SOURCE states on-device storage and server deletion after delivery exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Migration needs physical backup plus passphrase, device transfer, or unseen recovery key.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted backup file protected by a 30-digit passphrase ... Direct device-to-device transfer ... 64-character recovery key that Signal never sees",
   "reasoning": "SOURCE lists the same three Signal migration options."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Signal servers cannot grant history access; recovery keys stay client-side and unrecoverable.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "servers are never in a position to grant access to your message history ... recovery key stays on your device ... cannot help you recover them if you lose",
   "reasoning": "SOURCE states server inability to grant access and irrecoverability of lost keys."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Password handling adds another unverifiable layer beneath encryption architecture.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "there's another layer to this. Even if we trust the encryption architecture, how do we know companies don't store your password in plaintext",
   "reasoning": "SOURCE raises plaintext password storage as a distinct additional layer."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Client hashing is verifiable in open source; server behavior after arrival is not.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "You can verify what the client does (if it's open source) ... you cannot verify what happens on the server after your password ... arrives",
   "reasoning": "SOURCE states client verification but not server behavior verification."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Facebook logged hundreds of millions of plaintext passwords; Adobe hints leaked; small services worse.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "logging hundreds of millions of passwords in plaintext ... Adobe's 2013 breach revealed they stored password hints in plaintext. Many smaller services store passwords in plaintext",
   "reasoning": "SOURCE states each example with matching scale and party."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Proton password-reset data loss suggests honest design but proves nothing about capability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you lose access to all your old encrypted emails. This suggests they genuinely can't decrypt ... But even this isn't proof",
   "reasoning": "SOURCE draws the same suggestion while explicitly denying it is proof."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "Without client crypto guarantees, users trust reputation, jurisdiction, model, history.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees",
   "reasoning": "SOURCE lists the same four trust bases and absence of verification."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "Architecture sets trust surface: Meta infrastructure, Proton client integrity, Signal key custody.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "trusting Meta's entire server infrastructure ... trusting they won't serve malicious code ... Signal ... attack surface is much smaller",
   "reasoning": "SOURCE maps each service to the trust it demands in the same terms."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Comparison names WhatsApp escrow, Proton password-encrypted storage, Signal client control.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Server-mediated key escrow ... Password-encrypted server-side key storage ... Client-controlled keys",
   "reasoning": "SOURCE table names the same three security models."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Nobody can verify that companies avoid plaintext password storage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Short answer: We don't know for certain.",
   "reasoning": "SOURCE states plaintext storage cannot be verified with certainty."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Verifiable: open clients, traffic checks, audits with published results.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Open-source clients ... Network traffic inspection ... Independent security audits ... with published results",
   "reasoning": "SOURCE lists open clients, traffic inspection, and published audits as verifiable."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Unverifiable: closed server code, later changes, rogue staff, breaches.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Server-side code: Almost always closed-source ... changed it later ... Rogue employees or breaches",
   "reasoning": "SOURCE lists the same closed-code, later-change, rogue-employee, breach items."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Look for open servers, audits, breach behavior; beware resets, obscurity, violation history.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Open-source server code ... Independent security audits ... Breach disclosure ... Can reset password and access old data ... Security through obscurity ... History of privacy violations",
   "reasoning": "SOURCE's good and bad signs match the node's list."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Adobe 2013 hints, Facebook 2019 plaintext logging, small services with weak unsalted storage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Adobe (2013) ... password hints in plaintext ... Facebook (2019) ... plaintext ... small services ... MD5 without salt",
   "reasoning": "SOURCE records each example with matching years and details."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Trust-minimizing needs client-side crypto, zero-knowledge servers, reproducible audited builds.",
   "claim_type": "recommendation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "All cryptography happens client-side ... The server never sees anything that could decrypt your data ... open-source AND reproducibly built AND you can verify what's running",
   "reasoning": "SOURCE says reproducibly built and verifiable, not 'audited'; added qualifier slightly changes the third condition."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "Applied trust: WhatsApp everything, Proton hashing plus client, Signal implementation plus custody.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp | Meta's entire server infrastructure ... Proton Mail | They hash your password properly ... Signal | Much less trust required",
   "reasoning": "SOURCE's applied trust table matches the node's summary."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Prefer client-side encryption, open everything, decentralization, hardware security keys.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys",
   "reasoning": "SOURCE states the same four preferences verbatim in the Bottom Line."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "Sources document WhatsApp multi-device, Proton key storage, Signal secure backups.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "How WhatsApp enables multi-device capability ... How is the private key stored? ... Introducing Signal Secure Backups",
   "reasoning": "SOURCE's Sources section lists exactly these references."
  }
 ],
 "metrics": {
  "total_claims": 33,
  "supported": 32,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9697
 },
 "fail_list": [
  "C030"
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
    "L002",
    "L003",
    "L004"
   ],
   "evidence_quote": "End-to-end encryption can mean several practical things beyond device-to-device ciphertext. ... Real goal is excluding the provider",
   "reasoning": "L003 captures the definition as device-to-device ciphertext and L004 reframes the real question as excluding the provider. L002 records the mixed verdict (escrow/trust/minimize), covering the 'not completely clear' thrust."
  },
  {
   "point_id": "K02",
   "point_text": "People usually want E2EE so that no one outside sender and receivers, particularly the provider, can access data. For WhatsApp this means Facebook should not access message content, but it still has metadata such as network, frequency, amount, and timing of communication.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "Real goal is excluding the provider, though metadata like contacts and timing still leaks.",
   "reasoning": "Provider-exclusion goal and the metadata residual are both stated. The illustrative metadata list is compressed to 'contacts and timing' but the idea and its qualifier survive."
  },
  {
   "point_id": "K03",
   "point_text": "For WhatsApp the answer is unclear: if implemented as claimed and with no secret backdoors they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative (that access is impossible).",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L005",
    "L028"
   ],
   "evidence_quote": "Meta likely accesses WhatsApp content given closed source, ad-data sharing, past plaintext failures. ... Unverifiable: closed server code, later changes, rogue staff, breaches.",
   "reasoning": "Closed-source and unverifiability are captured, but the loglog hardens the original open question into a firm verdict ('likely accesses') rather than preserving 'the answer is unclear' and the cannot-prove-a-negative framing. Scope is narrowed, so Partial."
  },
  {
   "point_id": "K04",
   "point_text": "Evidence against WhatsApp/Meta: the 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as storing hundreds of millions of passwords in plaintext, make it almost certain they can and do access message content.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L005",
    "L021"
   ],
   "evidence_quote": "class closed source, ad-data sharing, past plaintext failures. ... Facebook logged hundreds of millions of plaintext passwords",
   "reasoning": "Ad-data sharing and the plaintext-failure evidence are present, and 'hundreds of millions' survives, but the 2021 date of the privacy policy change is dropped. A Must have point missing a key date is at most Partial."
  },
  {
   "point_id": "K05",
   "point_text": "Smoking gun test: whether a platform can back up or let you access history across devices without manually linking/transferring keys. If the provider ever holds the key, it is like leaving a copy of your door key on a public billboard and it can decrypt any messages at will.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L007"
   ],
   "evidence_quote": "Smoking gun: history portability without manual key transfer betrays server key access. ... Signal forces manual key copy; any server-touchable key is like public copies.",
   "reasoning": "Both the portability test and the public-key-copy analogy are captured accurately."
  },
  {
   "point_id": "K06",
   "point_text": "How WhatsApp actually works: the server stores encrypted message history and device-to-account identity mappings, authenticates new devices, and provides the keys needed to decrypt history. This makes the server a trusted intermediary that could silently authenticate a rogue device and hide it from your device list, unlike Signal's manual key transfer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009"
   ],
   "evidence_quote": "WhatsApp server stores encrypted history and maps accounts to device identities. ... Server-authenticated new devices receive decryption keys; rogue devices could hide from lists.",
   "reasoning": "All elements (encrypted history, identity mapping, device authentication, key delivery, rogue-device hiding) are present, and the Signal contrast is covered by L007."
  },
  {
   "point_id": "K07",
   "point_text": "Proton Mail model: the private key is generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L010",
    "L011"
   ],
   "evidence_quote": "Proton generates browser-side keys, then stores them server-side encrypted under user password. ... Login: bcrypt-hash authenticates",
   "reasoning": "Browser-side generation and password-encrypted server storage are captured, and bcrypt appears, but AES-256 is never named. A Must have point with a dropped technical number is at most Partial."
  },
  {
   "point_id": "K08",
   "point_text": "Proton login flow: type password, browser hashes it with bcrypt plus a server-provided salt, sends the hash to authenticate, server returns the encrypted private key, and the browser decrypts it locally with the actual password.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L011"
   ],
   "evidence_quote": "Login: bcrypt-hash authenticates, server returns encrypted key, browser decrypts locally.",
   "reasoning": "The full flow is captured: bcrypt hashing authenticates, server returns encrypted key, browser decrypts locally. The server-provided salt detail is a minor omission on a Nice to have point and does not defeat the idea."
  },
  {
   "point_id": "K09",
   "point_text": "Distinction between hashing (one-way, used for authentication, cannot be reversed to the password) and encryption (two-way, used on the private key). Proton receives the hash for authentication while the key is encrypted with the actual password, so in theory the hash cannot decrypt the key.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L012"
   ],
   "evidence_quote": "Hashing authenticates one-way while encryption reversibly protects the private key.",
   "reasoning": "The one-way versus reversible distinction is captured directly, implying the hash cannot decrypt the key. Core idea intact."
  },
  {
   "point_id": "K10",
   "point_text": "Proton's critical residual vulnerability: Proton could serve malicious client code (web app or update) to capture the actual password before hashing and use it to decrypt the stored key. This is why open-source clients matter, yet you must still trust the served code matches the source, no future malicious injection, and no infrastructure compromise.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L014"
   ],
   "evidence_quote": "Proton could serve malicious client code capturing passwords, then decrypt stored keys. ... Open source helps only if served code matches, stays honest, infrastructure stays clean.",
   "reasoning": "The malicious-code vulnerability and all three residual trust conditions (served code matches, stays honest, clean infrastructure) are captured."
  },
  {
   "point_id": "K11",
   "point_text": "Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L016",
    "L017"
   ],
   "evidence_quote": "Signal stores history on-device, deleting server copies after delivery. ... Migration needs physical backup plus passphrase, device transfer, or unseen recovery key.",
   "reasoning": "The on-device storage model and all three migration options are present with the correct qualifiers, but the 30-digit passphrase and 64-character recovery key numbers are dropped. A Must have point with dropped numbers is at most Partial."
  },
  {
   "point_id": "K12",
   "point_text": "Signal is genuinely zero-knowledge: servers are never positioned to grant access to message history, and even with cloud backups Signal cannot decrypt backups and cannot help recover them if the recovery key is lost.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018"
   ],
   "evidence_quote": "Signal servers cannot grant history access; recovery keys stay client-side and unrecoverable.",
   "reasoning": "Both the zero-knowledge server position and the unrecoverable recovery key are captured, matching the original."
  },
  {
   "point_id": "K13",
   "point_text": "Password storage limits: you can verify what an open-source client does (hashing before transmission), inspect network traffic, and read audits, but you cannot verify server-side code, whether it changed after an audit, rogue employees, or breaches. There is no cryptographic guarantee about server password handling.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L019",
    "L020",
    "L027",
    "L028"
   ],
   "evidence_quote": "Client hashing is verifiable in open source; server behavior after arrival is not. ... Verifiable: open clients, traffic checks, audits with published results. Unverifiable: closed server code, later changes, rogue staff, breaches.",
   "reasoning": "The verifiable side (open clients, traffic checks, audits) and the unverifiable side (server code, later changes, rogue staff, breaches) are both captured, preserving the no-guarantee conclusion."
  },
  {
   "point_id": "K14",
   "point_text": "Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext in internal logs for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, and many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though this is not proof.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L021",
    "L022",
    "L030"
   ],
   "evidence_quote": "Facebook logged hundreds of millions of plaintext passwords; Adobe hints leaked; small services worse. ... Adobe 2013 hints, Facebook 2019 plaintext logging, small services with weak unsalted storage. ... Proton password-reset data loss suggests honest design but proves nothing.",
   "reasoning": "The three examples and the Proton caveat are present, with years 2019/2013 and 'hundreds of millions' retained, but the 200-600 million range, 20,000 employees, 2012 archive date, and MD5 specificity are dropped. Nice to have, so this is a polish issue rather than a failure."
  },
  {
   "point_id": "K15",
   "point_text": "Bottom line: for most commercial services you are trusting reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious users prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys such as YubiKey that never expose the secret.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L031",
    "L033"
   ],
   "evidence_quote": "users trust reputation, jurisdiction, model, history. ... Trust-minimizing needs client-side crypto, zero-knowledge servers, reproducible audited builds. ... Prefer client-side encryption, open everything, decentralization, hardware security keys.",
   "reasoning": "The trust-basis conclusion and the preference list (client-side crypto, open everything, decentralization, hardware keys) are all captured. The YubiKey example and 'never expose the secret' nuance are omitted, but the actionable recommendation survives."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 8,
  "must_have_partial": 4,
  "must_have_missing": 0,
  "overall_present": 10,
  "must_recall": 0.8333,
  "overall_recall": 0.8333
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
   "reasoning": "Canonical summary; introduces thesis and triad, so cannot defer to earlier claim."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Frames the E2E definitional problem, distinct from later service specifics."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds provider-exclusion goal plus metadata leak caveat, new information."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specific inference about Meta access with three supporting reasons."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "The portability smoking-gun test is a distinct diagnostic argument."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contrasts Signal manual key copy; adds key-equivalence reasoning."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete WhatsApp server storage and identity-mapping facts."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Device enrollment key delivery and hidden-rogue-device counterpoint, new detail."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton key generation and password-encrypted server storage architecture."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Login flow evidence with bcrypt and local decryption, supports C009."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Definitional distinction between one-way hashing and reversible encryption, not restated."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Malicious-client-code attack path is distinct threat reasoning."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Open source caveats (code match, honesty, clean infrastructure) add new conditions."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explicit WhatsApp versus Proton compromise-order contrast, new comparison."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal on-device history and post-delivery server deletion facts."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Enumerates migration methods, concrete and not repeated elsewhere."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal recovery-key custody and unrecoverability are distinct facts."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical section-6 thesis on unverifiable password layer."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Client-versus-server verifiability split, distinct from section 8 lists."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical breach evidence (Facebook, Adobe, small services)."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton reset data-loss caveat distinguishes design honesty from capability."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Lists trust substitutes (reputation, jurisdiction, model, history), new content."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Introduces architecture-to-trust-surface causal framing, not just triad labels."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Duplicate",
   "canonical_id": "C001",
   "reasoning": "Section 7 triad restates the summary's WhatsApp/Proton/Signal comparison."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Duplicate",
   "canonical_id": "C018",
   "reasoning": "Section 8 thesis restates section 6 unverifiable password-storage claim."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "L027"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds concrete verifiable mechanisms: traffic checks, audits, published results."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "L028"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds unverifiable vectors: later changes, rogue staff, breaches."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "L029"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Actionable look-for and beware list, distinct recommendation."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "L030"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Same Adobe, Facebook, small-service breach examples already given in 6.2."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "L031"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Trust-minimizing requirements list, distinct from recommendation in 9."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "L032"
   ],
   "label": "Duplicate",
   "canonical_id": "C001",
   "reasoning": "Applied-trust triad repeats the summary/comparison service mapping."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "L033"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds decentralization and hardware keys beyond C030 recommendations."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "L034"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Meta sources line, no argumentative value, restates header-level citations."
  }
 ],
 "metrics": {
  "scored_claims": 33,
  "unique": 28,
  "duplicates": 4,
  "trivia": 1,
  "redundancy_rate": 0.1212,
  "trivia_rate": 0.0303,
  "structured_tokens": 679,
  "tokens_per_unique_claim": 24.25
 },
 "prune_list": [
  "C024 duplicates C001, safe to merge",
  "C025 duplicates C018, safe to merge",
  "C029 duplicates C020, safe to merge",
  "C031 duplicates C001, safe to merge",
  "C033 trivia meta sources line, safe to cut"
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
   "claim_text": "Encryption excludes providers only when clients hold keys; WhatsApp escrows, Proton needs trust, Signal minimizes.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Signal's servers are never in a position to grant access to your message history ... Server-mediated key escrow ... still requires some trust",
   "reasoning": "SOURCE states WhatsApp escrow, Proton trust need, and Signal client-held key minimizing trust."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "End-to-end encryption can mean several practical things beyond device-to-device ciphertext.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they could mean several things in practical terms",
   "reasoning": "SOURCE uses nearly identical wording about E2EE meaning several practical things."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "Real goal is excluding the provider, though metadata like contacts and timing still leaks.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "no one can access the data outside the sender and receivers, and in particular the provider ... they know your network, the frequency and amount of communication, times of communication",
   "reasoning": "SOURCE states provider-exclusion goal and lists metadata leaks including timing and network."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Meta likely accesses WhatsApp content given closed source, ad-data sharing, past plaintext failures.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can almost be certain that they can, and they do access them",
   "reasoning": "SOURCE cites closed source, ad-sharing policy, plaintext failures and concludes near certainty of access."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "Smoking gun: history portability without manual key transfer betrays server key access.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "a smoking gun is whether the platform/app is able to 'backup' your data. Whether you can access your history across devices without 'manually' linking them",
   "reasoning": "SOURCE frames cross-device history without manual linking as the smoking gun for key access."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "Signal forces manual key copy; any server-touchable key is like public copies.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is what happens in Signal. What you need to do is to somehow copy the key ... left a copy at the local farmers market billboard",
   "reasoning": "SOURCE says Signal requires copying the key and compares server-accessible keys to public copies."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "WhatsApp server stores encrypted history and maps accounts to device identities.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server stores encrypted message history and maintains mappings between your account and all your device identities",
   "reasoning": "SOURCE states both storage and account-to-device mapping directly."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "Server-authenticated new devices receive decryption keys; rogue devices could hide from lists.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server authenticates it and provides it with the keys needed to decrypt ... they could simply hide a rogue device from your device list entirely",
   "reasoning": "SOURCE states both claims explicitly in the WhatsApp section."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Proton generates browser-side keys, then stores them server-side encrypted under user password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your private key is generated in your browser, then encrypted with your password ... before being sent to their servers for storage",
   "reasoning": "SOURCE states browser generation and password-encrypted server storage directly."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "Login: bcrypt-hash authenticates, server returns encrypted key, browser decrypts locally.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Your browser hashes the password using bcrypt ... The server sends your encrypted private key back ... decrypt this private key locally",
   "reasoning": "SOURCE's numbered login steps match the node exactly."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Hashing authenticates one-way while encryption reversibly protects the private key.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Hashing ... A one-way function ... Encryption ... A two-way function ... encrypted with your actual password",
   "reasoning": "SOURCE defines hashing as one-way for auth and encryption as two-way for the private key."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Proton could serve malicious client code capturing passwords, then decrypt stored keys.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Proton could serve you malicious client code ... that captures your actual password ... if they capture your password, they can decrypt it",
   "reasoning": "SOURCE states the malicious-client-code vulnerability and resulting decryption directly."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Open source helps only if served code matches, stays honest, infrastructure stays clean.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The code they're actually serving matches the open-source code ... They won't be compelled to inject malicious code ... infrastructure hasn't been compromised",
   "reasoning": "SOURCE lists these three trust conditions for open-source clients."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Unlike WhatsApp, Proton must first compromise the client to steal passwords.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Proton doesn't have direct access ... they'd need to actively compromise the client to steal your password first. WhatsApp's architecture doesn't even require that step",
   "reasoning": "SOURCE contrasts Proton client-compromise need against WhatsApp direct key access."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Signal stores history on-device, deleting server copies after delivery.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "message history is stored only on your device and deleted from Signal's servers after delivery",
   "reasoning": "SOURCE states on-device storage and server deletion after delivery exactly."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "Migration needs physical backup plus passphrase, device transfer, or unseen recovery key.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted backup file protected by a 30-digit passphrase ... Direct device-to-device transfer ... 64-character recovery key that Signal never sees",
   "reasoning": "SOURCE lists the same three Signal migration options."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "Signal servers cannot grant history access; recovery keys stay client-side and unrecoverable.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "servers are never in a position to grant access to your message history ... recovery key stays on your device ... cannot help you recover them if you lose",
   "reasoning": "SOURCE states server inability to grant access and irrecoverability of lost keys."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "Password handling adds another unverifiable layer beneath encryption architecture.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "there's another layer to this. Even if we trust the encryption architecture, how do we know companies don't store your password in plaintext",
   "reasoning": "SOURCE raises plaintext password storage as a distinct additional layer."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Client hashing is verifiable in open source; server behavior after arrival is not.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "You can verify what the client does (if it's open source) ... you cannot verify what happens on the server after your password ... arrives",
   "reasoning": "SOURCE states client verification but not server behavior verification."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "Facebook logged hundreds of millions of plaintext passwords; Adobe hints leaked; small services worse.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "logging hundreds of millions of passwords in plaintext ... Adobe's 2013 breach revealed they stored password hints in plaintext. Many smaller services store passwords in plaintext",
   "reasoning": "SOURCE states each example with matching scale and party."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "Proton password-reset data loss suggests honest design but proves nothing about capability.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you lose access to all your old encrypted emails. This suggests they genuinely can't decrypt ... But even this isn't proof",
   "reasoning": "SOURCE draws the same suggestion while explicitly denying it is proof."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "6.4"
   ],
   "claim_text": "Without client crypto guarantees, users trust reputation, jurisdiction, model, history.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees",
   "reasoning": "SOURCE lists the same four trust bases and absence of verification."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "6.5"
   ],
   "claim_text": "Architecture sets trust surface: Meta infrastructure, Proton client integrity, Signal key custody.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "trusting Meta's entire server infrastructure ... trusting they won't serve malicious code ... Signal ... attack surface is much smaller",
   "reasoning": "SOURCE maps each service to the trust it demands in the same terms."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "Comparison names WhatsApp escrow, Proton password-encrypted storage, Signal client control.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Server-mediated key escrow ... Password-encrypted server-side key storage ... Client-controlled keys",
   "reasoning": "SOURCE table names the same three security models."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "Nobody can verify that companies avoid plaintext password storage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Short answer: We don't know for certain.",
   "reasoning": "SOURCE states plaintext storage cannot be verified with certainty."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "Verifiable: open clients, traffic checks, audits with published results.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Open-source clients ... Network traffic inspection ... Independent security audits ... with published results",
   "reasoning": "SOURCE lists open clients, traffic inspection, and published audits as verifiable."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Unverifiable: closed server code, later changes, rogue staff, breaches.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Server-side code: Almost always closed-source ... changed it later ... Rogue employees or breaches",
   "reasoning": "SOURCE lists the same closed-code, later-change, rogue-employee, breach items."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Look for open servers, audits, breach behavior; beware resets, obscurity, violation history.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Open-source server code ... Independent security audits ... Breach disclosure ... Can reset password and access old data ... Security through obscurity ... History of privacy violations",
   "reasoning": "SOURCE's good and bad signs match the node's list."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "Adobe 2013 hints, Facebook 2019 plaintext logging, small services with weak unsalted storage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Adobe (2013) ... password hints in plaintext ... Facebook (2019) ... plaintext ... small services ... MD5 without salt",
   "reasoning": "SOURCE records each example with matching years and details."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Trust-minimizing needs client-side crypto, zero-knowledge servers, reproducible audited builds.",
   "claim_type": "recommendation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "All cryptography happens client-side ... The server never sees anything that could decrypt your data ... open-source AND reproducibly built AND you can verify what's running",
   "reasoning": "SOURCE says reproducibly built and verifiable, not 'audited'; added qualifier slightly changes the third condition."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "Applied trust: WhatsApp everything, Proton hashing plus client, Signal implementation plus custody.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp | Meta's entire server infrastructure ... Proton Mail | They hash your password properly ... Signal | Much less trust required",
   "reasoning": "SOURCE's applied trust table matches the node's summary."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "Prefer client-side encryption, open everything, decentralization, hardware security keys.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys",
   "reasoning": "SOURCE states the same four preferences verbatim in the Bottom Line."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "Sources document WhatsApp multi-device, Proton key storage, Signal secure backups.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "How WhatsApp enables multi-device capability ... How is the private key stored? ... Introducing Signal Secure Backups",
   "reasoning": "SOURCE's Sources section lists exactly these references."
  }
 ],
 "metrics": {
  "total_claims": 33,
  "supported": 32,
  "partially_supported": 1,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9697
 },
 "fail_list": [
  "C030"
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
    "L002",
    "L003",
    "L004"
   ],
   "evidence_quote": "End-to-end encryption can mean several practical things beyond device-to-device ciphertext. ... Real goal is excluding the provider",
   "reasoning": "L003 captures the definition as device-to-device ciphertext and L004 reframes the real question as excluding the provider. L002 records the mixed verdict (escrow/trust/minimize), covering the 'not completely clear' thrust."
  },
  {
   "point_id": "K02",
   "point_text": "People usually want E2EE so that no one outside sender and receivers, particularly the provider, can access data. For WhatsApp this means Facebook should not access message content, but it still has metadata such as network, frequency, amount, and timing of communication.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L004"
   ],
   "evidence_quote": "Real goal is excluding the provider, though metadata like contacts and timing still leaks.",
   "reasoning": "Provider-exclusion goal and the metadata residual are both stated. The illustrative metadata list is compressed to 'contacts and timing' but the idea and its qualifier survive."
  },
  {
   "point_id": "K03",
   "point_text": "For WhatsApp the answer is unclear: if implemented as claimed and with no secret backdoors they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative (that access is impossible).",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L005",
    "L028"
   ],
   "evidence_quote": "Meta likely accesses WhatsApp content given closed source, ad-data sharing, past plaintext failures. ... Unverifiable: closed server code, later changes, rogue staff, breaches.",
   "reasoning": "Closed-source and unverifiability are captured, but the loglog hardens the original open question into a firm verdict ('likely accesses') rather than preserving 'the answer is unclear' and the cannot-prove-a-negative framing. Scope is narrowed, so Partial."
  },
  {
   "point_id": "K04",
   "point_text": "Evidence against WhatsApp/Meta: the 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as storing hundreds of millions of passwords in plaintext, make it almost certain they can and do access message content.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L005",
    "L021"
   ],
   "evidence_quote": "class closed source, ad-data sharing, past plaintext failures. ... Facebook logged hundreds of millions of plaintext passwords",
   "reasoning": "Ad-data sharing and the plaintext-failure evidence are present, and 'hundreds of millions' survives, but the 2021 date of the privacy policy change is dropped. A Must have point missing a key date is at most Partial."
  },
  {
   "point_id": "K05",
   "point_text": "Smoking gun test: whether a platform can back up or let you access history across devices without manually linking/transferring keys. If the provider ever holds the key, it is like leaving a copy of your door key on a public billboard and it can decrypt any messages at will.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L006",
    "L007"
   ],
   "evidence_quote": "Smoking gun: history portability without manual key transfer betrays server key access. ... Signal forces manual key copy; any server-touchable key is like public copies.",
   "reasoning": "Both the portability test and the public-key-copy analogy are captured accurately."
  },
  {
   "point_id": "K06",
   "point_text": "How WhatsApp actually works: the server stores encrypted message history and device-to-account identity mappings, authenticates new devices, and provides the keys needed to decrypt history. This makes the server a trusted intermediary that could silently authenticate a rogue device and hide it from your device list, unlike Signal's manual key transfer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L008",
    "L009"
   ],
   "evidence_quote": "WhatsApp server stores encrypted history and maps accounts to device identities. ... Server-authenticated new devices receive decryption keys; rogue devices could hide from lists.",
   "reasoning": "All elements (encrypted history, identity mapping, device authentication, key delivery, rogue-device hiding) are present, and the Signal contrast is covered by L007."
  },
  {
   "point_id": "K07",
   "point_text": "Proton Mail model: the private key is generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L010",
    "L011"
   ],
   "evidence_quote": "Proton generates browser-side keys, then stores them server-side encrypted under user password. ... Login: bcrypt-hash authenticates",
   "reasoning": "Browser-side generation and password-encrypted server storage are captured, and bcrypt appears, but AES-256 is never named. A Must have point with a dropped technical number is at most Partial."
  },
  {
   "point_id": "K08",
   "point_text": "Proton login flow: type password, browser hashes it with bcrypt plus a server-provided salt, sends the hash to authenticate, server returns the encrypted private key, and the browser decrypts it locally with the actual password.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L011"
   ],
   "evidence_quote": "Login: bcrypt-hash authenticates, server returns encrypted key, browser decrypts locally.",
   "reasoning": "The full flow is captured: bcrypt hashing authenticates, server returns encrypted key, browser decrypts locally. The server-provided salt detail is a minor omission on a Nice to have point and does not defeat the idea."
  },
  {
   "point_id": "K09",
   "point_text": "Distinction between hashing (one-way, used for authentication, cannot be reversed to the password) and encryption (two-way, used on the private key). Proton receives the hash for authentication while the key is encrypted with the actual password, so in theory the hash cannot decrypt the key.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L012"
   ],
   "evidence_quote": "Hashing authenticates one-way while encryption reversibly protects the private key.",
   "reasoning": "The one-way versus reversible distinction is captured directly, implying the hash cannot decrypt the key. Core idea intact."
  },
  {
   "point_id": "K10",
   "point_text": "Proton's critical residual vulnerability: Proton could serve malicious client code (web app or update) to capture the actual password before hashing and use it to decrypt the stored key. This is why open-source clients matter, yet you must still trust the served code matches the source, no future malicious injection, and no infrastructure compromise.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L013",
    "L014"
   ],
   "evidence_quote": "Proton could serve malicious client code capturing passwords, then decrypt stored keys. ... Open source helps only if served code matches, stays honest, infrastructure stays clean.",
   "reasoning": "The malicious-code vulnerability and all three residual trust conditions (served code matches, stays honest, clean infrastructure) are captured."
  },
  {
   "point_id": "K11",
   "point_text": "Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.",
   "weight": "Must have",
   "presence": "Partial",
   "loglog_ids": [
    "L016",
    "L017"
   ],
   "evidence_quote": "Signal stores history on-device, deleting server copies after delivery. ... Migration needs physical backup plus passphrase, device transfer, or unseen recovery key.",
   "reasoning": "The on-device storage model and all three migration options are present with the correct qualifiers, but the 30-digit passphrase and 64-character recovery key numbers are dropped. A Must have point with dropped numbers is at most Partial."
  },
  {
   "point_id": "K12",
   "point_text": "Signal is genuinely zero-knowledge: servers are never positioned to grant access to message history, and even with cloud backups Signal cannot decrypt backups and cannot help recover them if the recovery key is lost.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L018"
   ],
   "evidence_quote": "Signal servers cannot grant history access; recovery keys stay client-side and unrecoverable.",
   "reasoning": "Both the zero-knowledge server position and the unrecoverable recovery key are captured, matching the original."
  },
  {
   "point_id": "K13",
   "point_text": "Password storage limits: you can verify what an open-source client does (hashing before transmission), inspect network traffic, and read audits, but you cannot verify server-side code, whether it changed after an audit, rogue employees, or breaches. There is no cryptographic guarantee about server password handling.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L019",
    "L020",
    "L027",
    "L028"
   ],
   "evidence_quote": "Client hashing is verifiable in open source; server behavior after arrival is not. ... Verifiable: open clients, traffic checks, audits with published results. Unverifiable: closed server code, later changes, rogue staff, breaches.",
   "reasoning": "The verifiable side (open clients, traffic checks, audits) and the unverifiable side (server code, later changes, rogue staff, breaches) are both captured, preserving the no-guarantee conclusion."
  },
  {
   "point_id": "K14",
   "point_text": "Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext in internal logs for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, and many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though this is not proof.",
   "weight": "Nice to have",
   "presence": "Partial",
   "loglog_ids": [
    "L021",
    "L022",
    "L030"
   ],
   "evidence_quote": "Facebook logged hundreds of millions of plaintext passwords; Adobe hints leaked; small services worse. ... Adobe 2013 hints, Facebook 2019 plaintext logging, small services with weak unsalted storage. ... Proton password-reset data loss suggests honest design but proves nothing.",
   "reasoning": "The three examples and the Proton caveat are present, with years 2019/2013 and 'hundreds of millions' retained, but the 200-600 million range, 20,000 employees, 2012 archive date, and MD5 specificity are dropped. Nice to have, so this is a polish issue rather than a failure."
  },
  {
   "point_id": "K15",
   "point_text": "Bottom line: for most commercial services you are trusting reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious users prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys such as YubiKey that never expose the secret.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L023",
    "L031",
    "L033"
   ],
   "evidence_quote": "users trust reputation, jurisdiction, model, history. ... Trust-minimizing needs client-side crypto, zero-knowledge servers, reproducible audited builds. ... Prefer client-side encryption, open everything, decentralization, hardware security keys.",
   "reasoning": "The trust-basis conclusion and the preference list (client-side crypto, open everything, decentralization, hardware keys) are all captured. The YubiKey example and 'never expose the secret' nuance are omitted, but the actionable recommendation survives."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 8,
  "must_have_partial": 4,
  "must_have_missing": 0,
  "overall_present": 10,
  "must_recall": 0.8333,
  "overall_recall": 0.8333
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
   "reasoning": "Canonical summary; introduces thesis and triad, so cannot defer to earlier claim."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "L003"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Frames the E2E definitional problem, distinct from later service specifics."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "L004"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds provider-exclusion goal plus metadata leak caveat, new information."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "L005"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specific inference about Meta access with three supporting reasons."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "L006"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "The portability smoking-gun test is a distinct diagnostic argument."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "L007"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Contrasts Signal manual key copy; adds key-equivalence reasoning."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "L008"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete WhatsApp server storage and identity-mapping facts."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "L009"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Device enrollment key delivery and hidden-rogue-device counterpoint, new detail."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "L010"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton key generation and password-encrypted server storage architecture."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "L011"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Login flow evidence with bcrypt and local decryption, supports C009."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "L012"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Definitional distinction between one-way hashing and reversible encryption, not restated."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "L013"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Malicious-client-code attack path is distinct threat reasoning."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "L014"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Open source caveats (code match, honesty, clean infrastructure) add new conditions."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "L015"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Explicit WhatsApp versus Proton compromise-order contrast, new comparison."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "L016"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal on-device history and post-delivery server deletion facts."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "L017"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Enumerates migration methods, concrete and not repeated elsewhere."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "L018"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal recovery-key custody and unrecoverability are distinct facts."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "L019"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical section-6 thesis on unverifiable password layer."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "L020"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Client-versus-server verifiability split, distinct from section 8 lists."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "L021"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Canonical breach evidence (Facebook, Adobe, small services)."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "L022"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton reset data-loss caveat distinguishes design honesty from capability."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "L023"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Lists trust substitutes (reputation, jurisdiction, model, history), new content."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "L024"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Introduces architecture-to-trust-surface causal framing, not just triad labels."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "L025"
   ],
   "label": "Duplicate",
   "canonical_id": "C001",
   "reasoning": "Section 7 triad restates the summary's WhatsApp/Proton/Signal comparison."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "L026"
   ],
   "label": "Duplicate",
   "canonical_id": "C018",
   "reasoning": "Section 8 thesis restates section 6 unverifiable password-storage claim."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "L027"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds concrete verifiable mechanisms: traffic checks, audits, published results."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "L028"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds unverifiable vectors: later changes, rogue staff, breaches."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "L029"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Actionable look-for and beware list, distinct recommendation."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "L030"
   ],
   "label": "Duplicate",
   "canonical_id": "C020",
   "reasoning": "Same Adobe, Facebook, small-service breach examples already given in 6.2."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "L031"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Trust-minimizing requirements list, distinct from recommendation in 9."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "L032"
   ],
   "label": "Duplicate",
   "canonical_id": "C001",
   "reasoning": "Applied-trust triad repeats the summary/comparison service mapping."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "L033"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds decentralization and hardware keys beyond C030 recommendations."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "L034"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Meta sources line, no argumentative value, restates header-level citations."
  }
 ],
 "metrics": {
  "scored_claims": 33,
  "unique": 28,
  "duplicates": 4,
  "trivia": 1,
  "redundancy_rate": 0.1212,
  "trivia_rate": 0.0303,
  "structured_tokens": 679,
  "tokens_per_unique_claim": 24.25
 },
 "prune_list": [
  "C024 duplicates C001, safe to merge",
  "C025 duplicates C018, safe to merge",
  "C029 duplicates C020, safe to merge",
  "C031 duplicates C001, safe to merge",
  "C033 trivia meta sources line, safe to cut"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "deepseek-v4.1-flash (2026-09-15)",
 "source_id": "unknown",
 "inputs": {
  "faithfulness_precision": 0.9697,
  "critical_errors": 0,
  "must_recall": 0.8333,
  "overall_recall": 0.8333,
  "redundancy_rate": 0.1212,
  "trivia_rate": 0.0303
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted score equals 0.4 times faithfulness_precision plus 0.4 times must_recall minus 0.2 times redundancy_rate = 0.4*0.9697 + 0.4*0.8333 - 0.2*0.1212 = 0.38788 + 0.33332 - 0.02424 = 0.69696 (reported for audit only, non-decisive because a hard gate is missed)",
 "weighted_score": 0.697,
 "verdict": "Fail",
 "tradeoff_note": "The binding constraint is coverage, not concision: four Must have points (K03, K04, K07, K11) are only Partial because key numbers and framing were dropped, so must_recall 0.8333 falls below the 0.9 gate. Concision is healthy at 0.1212 under the 0.15 max, but concision never rescues a coverage fail.",
 "fix_list": [
  "Restore the dropped specifics in the four Partial Must have points to lift must_recall above 0.9: add AES-256 to K07 (L010/L011), add the 30-digit passphrase and 64-character recovery key to K11 (L016/L017), add the 2021 date to K04 (L005/L021), and restore K03's original unanswered framing ('the answer is unclear' and cannot prove a negative) instead of the hardened 'likely accesses' verdict (L005/L028).",
  "Merge duplicates to free length budget while keeping redundancy under 0.15: C024 into C001, C025 into C018, C029 into C020, C031 into C001, and cut trivia C033 (meta sources line).",
  "Soften C030 'reproducible audited builds' to 'reproducibly built and verifiable' to clear the sole Partially supported Minor claim and keep faithfulness_precision above the 0.95 gate."
 ],
 "reasoning": "Gate checks in policy order. (1) critical_errors = 0, so the Critical hard gate passes; no Critical contradicted claim appears in the faithfulness input, and the only non-supported claim C030 is Minor/Partially supported, not Critical. (2) must_recall = 0.8333 versus config must_recall_min = 0.9: 0.8333 < 0.9, so the Must have recall hard gate FAILS. This is driven by coverage showing must_have_present = 8 of 12 with 4 Partial and 0 Missing; the four Partial Must haves K03, K04, K07, K11 each lose recall credit for dropped content (K03 hardening of an open question, K04 missing the 2021 date, K07 missing AES-256, K11 missing the 30-digit passphrase and 64-character recovery key). (3) faithfulness_precision = 0.9697 versus min 0.95: passes, with margin from 32 supported of 33 claims and one Minor partial C030 that slightly alters the third trust-minimizing condition ('audited' vs 'reproducibly built and verifiable'). (4) redundancy_rate = 0.1212 versus redundancy_max 0.15: passes, leaving only ~0.029 of headroom, so restoring the missing Must have detail must be paid for by merging the four duplicate claims C024/C025/C029/C031 and cutting trivia C033. Because the must_recall hard gate is missed, the weighted score (0.697) is informational only and cannot change the outcome; concision at 0.1212 is a pass but is explicitly barred from rescuing a coverage fail. Borderline is not available because the numbers do not meet gates, and the failure is a genuine recall shortfall rather than a benign pass with a flagged Partial. Verdict: Fail on the must_recall gate."
}
```
