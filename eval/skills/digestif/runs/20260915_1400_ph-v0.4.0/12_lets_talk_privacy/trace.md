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
   "claim_text": "E2EE trust varies by architecture: WhatsApp mediates keys, Proton stores password-encrypted keys, Signal never holds them, and plaintext password storage stays unverifiable.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server can directly grant key access to any device it authenticates ... Signal literally cannot decrypt your backups ... we don't know for certain",
   "reasoning": "Each component matches the source: WhatsApp server-mediated keys, Proton server-stored encrypted key, Signal never sees key, plaintext storage uncertain."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "End-to-end encryption can mean several things in practice, and the real question is whether the provider can access your data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they could mean several things in practical terms ... can Facebook access the content of your WhatsApp messages or not",
   "reasoning": "Source states multiple meanings and frames the core question as provider access, matching the node."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "The author is not a security expert and writes this as an attempt to understand privacy as an end user.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I'm not a security expert ... This is an attempt to understand this as an end user",
   "reasoning": "Direct restatement of the disclaimer paragraph."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Encrypting on the sender's device and decrypting on the receiver's device without decryption along the way is the definition of E2EE.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted \"on sender's device\" and then decrypted \"on receiver's device\" without it ever being decrypted along the way is in fact the definition of it",
   "reasoning": "Node reproduces the source definition verbatim in meaning."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "If the purpose is only to defeat a man-in-the-middle attack, most implementations should be good enough.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "If the purpose is that a man-in-the-middle attack will not likely compromise your data, then most implementations of this should be good enough",
   "reasoning": "Source hedges with \"not likely compromise\"; node strengthens to \"defeat\" and adds \"only\", dropping the probabilistic qualifier."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "Usually the purpose is that no one, and in particular the provider, can access the data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In general one wants E2EE so that \"no one\" can access the data outside the sender and receivers, and in particular \"the provider\"",
   "reasoning": "\"Usually\" matches \"In general\"; the no-one/provider purpose is stated directly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "claim_text": "With WhatsApp, you do not want Facebook to access message content, though it still knows your network, communication frequency, amount, and times.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you don't want Facebook as a company to have access to the content of your messages ... they know your network, the frequency and amount of communication, times of communication",
   "reasoning": "All listed metadata matches the source's example."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "1.6"
   ],
   "claim_text": "The real question is whether Facebook can access the content of your WhatsApp messages in theory and in practice.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "in theory, and in practice, can Facebook access the content of your WhatsApp messages or not",
   "reasoning": "Direct restatement of the source's framing question."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "WhatsApp's answer is not completely clear: it depends on unverifiable implementation claims.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The answer is not completely clear ... we won't really know because the app is not open source, and hence not really auditable",
   "reasoning": "Node captures the source's uncertainty and lack of auditability."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "If they implemented things as claimed and added no secret backdoors, then yes, they cannot access the data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if they have implemented the things in the way they \"claim\" they have, and if they haven't implemented other backdoors ... then yes, they \"can't\" access that data",
   "reasoning": "Both conditions and the negative conclusion match the source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "We will not really know, because the app is not open source and hence not really auditable.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "we won't really know because the app is not open source, and hence not really auditable",
   "reasoning": "Near-verbatim restatement including the causal because clause."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "External audits and tests lack certainty in the negative direction: they can never claim it cannot access the data.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "external audits and tests will lack any certainty in the \"negative\" direction. That is, they can never claim it can't access those data",
   "reasoning": "Reproduces the source's point about unprovable negatives."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "The 2021 privacy policy changes allow sharing data with Facebook for relevant offers and ads across Meta company products.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "their 2021 privacy policy changes that allow sharing data with Facebook for \"showing relevant offers and ads across the Meta Company Products\"",
   "reasoning": "Year 2021 and the sharing purpose match the source exactly."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Previous security failures include storing hundreds of millions of passwords in plaintext.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "previous security failures like storing hundreds of millions of passwords in plaintext",
   "reasoning": "Quantity and plaintext detail preserved from source."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.6"
   ],
   "claim_text": "Given the company's business, you can almost be certain that they can, and do, access the messages.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "when you think about what the company's business is ... you can almost be certain that they can, and they do access them",
   "reasoning": "The hedge \"almost be certain\" and the claim of access match source."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "2.7"
   ],
   "claim_text": "A smoking gun is whether the platform or app can back up your data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For me, a smoking gun is whether the platform/app is able to \"backup\" your data",
   "reasoning": "Direct restatement of the author's smoking gun."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "2.7.1"
   ],
   "claim_text": "It is whether you can access history across devices without manually linking them somehow.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Whether you can access your history across devices without \"manually\" linking them somehow",
   "reasoning": "Verbatim in meaning, including the manual-linking condition."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "2.8"
   ],
   "claim_text": "Encryption is locking something with a key: one that only locks and that everyone has, and a master key only the receiver holds.",
   "claim_type": "definition",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "I think of encryption as locking something and having a key (usually a pair of keys, the one that only locks it and everyone has that, and a master key that only the receiver of the data has it",
   "reasoning": "Source frames this as the author's model and hedges \"usually a pair of keys\"; node states it as a flat definition."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "2.9"
   ],
   "claim_text": "Your master key is created and stored on your phone by default when you create an account.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "this is by default the case when you create an account the key is created and stored on your phone",
   "reasoning": "Matches the source's default-storage statement."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "2.10"
   ],
   "claim_text": "In a simple implementation, another device should not have the same master key to decrypt past messages.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In a simple implementation, there shouldn't be a way for that other device to have the same master key and decrypt your past messages",
   "reasoning": "Preserves the negation and the simple-implementation qualifier."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "2.10.1"
   ],
   "claim_text": "This is what happens in Signal, where you somehow copy the key from your original device to the new one.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is what happens in Signal. What you need to do is to somehow copy the key from your original device to your new device",
   "reasoning": "Direct restatement of the Signal key-copy behavior."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "2.11"
   ],
   "claim_text": "If at any time Facebook has access to the key, the situation is compromised.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if at any time, Facebook has access to it ... They can take the key and decrypt any/all of your messages whenever they want",
   "reasoning": "Node paraphrases the source's consequence of Facebook holding the key."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "2.11.1"
   ],
   "claim_text": "It is as if you locked your door and left a copy at the local farmers market billboard.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "it is as if you've locked your door and left a copy at the local farmers market billboard",
   "reasoning": "Reproduces the author's analogy exactly."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "2.12"
   ],
   "claim_text": "WhatsApp's official documentation says the server stores encrypted message history and maintains mappings between your account and your device identities.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "According to their official documentation, the server stores encrypted message history and maintains mappings between your account and all your device identities",
   "reasoning": "Attribution and both server functions match the source."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "2.13"
   ],
   "claim_text": "When you add a new device, the server authenticates it and provides the keys needed to decrypt your message history.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "When you add a new device, the server authenticates it and provides it with the keys needed to decrypt your message history",
   "reasoning": "Verbatim restatement."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "2.14"
   ],
   "claim_text": "This is fundamentally different from Signal: the server is a trusted intermediary that controls access to your encryption keys.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is fundamentally different from Signal's approach - the server is a trusted intermediary that controls access to your encryption keys",
   "reasoning": "Direct restatement including the Signal contrast."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "2.15"
   ],
   "claim_text": "Meta could theoretically authenticate a device that is not yours and give it access to decrypt your messages.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp (Meta) *could* theoretically authenticate a \"device\" that isn't actually yours and give it access to decrypt your messages",
   "reasoning": "Preserves the theoretical possibility and the device-not-yours condition."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "2.15.1"
   ],
   "claim_text": "The claimed safeguards, device lists you can check and security codes you can verify, depend on the server accurately reporting what devices exist.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Their claimed safeguards (device lists you can check, security codes you can verify) all depend on the server honestly reporting what devices exist",
   "reasoning": "Both safeguards and the dependency on honest server reporting are preserved."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "2.15.2"
   ],
   "claim_text": "Since they control that server, they could simply hide a rogue device from your device list entirely.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "since they control that server, they could simply hide a rogue device from your device list entirely",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "2.16"
   ],
   "claim_text": "The multi-device description comes from Meta's engineering post on how WhatsApp enables multi-device capability, from July 2021.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "How WhatsApp enables multi-device capability ... (Engineering at Meta, July 2021)",
   "reasoning": "Attribution, title, and July 2021 date match the source's reference list."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Proton stores your encrypted private key on its servers, so the trust shifts to the client.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your encrypted private key lives on Proton's servers ... This is why having open-source clients matters",
   "reasoning": "Source states key storage on servers and that the client becomes the trust concern."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "When you create a Proton account, your private key is generated in your browser and encrypted with your password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your private key is generated in your browser, then encrypted with your password",
   "reasoning": "Direct restatement of the source's account-creation description."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "3.1.1"
   ],
   "claim_text": "The encryption uses bcrypt and AES-256 before the key is sent to Proton's servers for storage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted with your password using bcrypt and AES-256 before being sent to their servers",
   "reasoning": "Source names bcrypt and AES-256 and the send-for-storage step."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "The crucial point: your encrypted private key lives on Proton's servers, not just on your original device.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your encrypted private key lives on Proton's servers, not just on your original device",
   "reasoning": "Near-verbatim restatement including the 'not just' qualifier."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "On a new device or browser, the login sequence runs as follows.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "When you log in on a new device or browser, here's what happens",
   "reasoning": "Faithful lead-in to the enumerated login steps."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "3.3.1"
   ],
   "claim_text": "You type your password, and your browser hashes it with bcrypt using a salt provided by Proton's server.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "hashes the password using bcrypt (with a salt provided by Proton's server)",
   "reasoning": "Matches source step 2 exactly, including the server-provided salt."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "3.3.2"
   ],
   "claim_text": "The hashed password is sent to Proton to prove you know the password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "sent to Proton to authenticate you (prove you know the password)",
   "reasoning": "Matches source step 3 without altering meaning."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "3.3.3"
   ],
   "claim_text": "The server sends your encrypted private key back to your browser.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The server sends your encrypted private key back to your browser",
   "reasoning": "Matches source step 4 verbatim."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "3.3.4"
   ],
   "claim_text": "Your browser uses your original password to decrypt the private key locally, and now you can read your emails.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "uses your original password to decrypt this private key locally ... Now you can read your emails",
   "reasoning": "Combines source steps 5 and 6 with identical meaning."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "Hashing is one-way: you can turn a password into a hash, but you theoretically cannot reverse a hash back into the password.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "A one-way function ... you theoretically cannot reverse a hash back into the password",
   "reasoning": "Preserves the 'theoretically' hedge and the one-way definition."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "3.5"
   ],
   "claim_text": "Proton receives your hashed password to verify you are who you claim to be, but this hash alone should not reveal your password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "this hash alone shouldn't let them figure out your actual password",
   "reasoning": "Keeps the source's 'shouldn't' hedge; meaning unchanged."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "3.6"
   ],
   "claim_text": "Encryption is two-way: you encrypt data with a key and decrypt it with that same key or a paired one.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can decrypt it back using that same key (or a paired key)",
   "reasoning": "Matches the source's two-way definition including the paired-key parenthetical."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "3.7"
   ],
   "claim_text": "Your private key is encrypted with your actual password, not the hash, so it can be decrypted when you provide the password again.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted with your actual password (not the hash), so it can be decrypted when you provide the password again",
   "reasoning": "Preserves the 'not the hash' negation and the decryption condition."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "3.8"
   ],
   "claim_text": "The security model: Proton receives your hashed password, but the private key is encrypted with your actual password, so the hash cannot decrypt it.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "even though they see your hashed password, they can't use that hash to decrypt your encrypted private key",
   "reasoning": "Retains the in-theory hedge and the hash-cannot-decrypt conclusion."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "3.9"
   ],
   "claim_text": "There is a critical vulnerability: Proton could serve malicious client code, in the web app or through an app update.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "there's still a critical vulnerability: Proton could serve you malicious client code (either in the web app or through an app update)",
   "reasoning": "Matches the vulnerability and both cited delivery channels."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "3.9.1"
   ],
   "claim_text": "That code could capture your actual password when you type it, before it gets hashed.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "captures your actual password when you type it - before it gets hashed",
   "reasoning": "Restates the capture-before-hashing point faithfully."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "3.10"
   ],
   "claim_text": "Since they already store your encrypted private key on their servers, if they capture your password they can decrypt it.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Since they already store your encrypted private key on their servers, if they capture your password, they can decrypt it",
   "reasoning": "Causal claim matches source nearly verbatim."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "3.11"
   ],
   "claim_text": "This is why having open-source clients matters: the community can verify that the client is not doing anything malicious.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "having open-source clients matters - the community can verify that the client isn't doing anything malicious",
   "reasoning": "Preserves the open-source rationale and its negation."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "3.12"
   ],
   "claim_text": "But you still have to trust several things.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "But you still have to trust that:",
   "reasoning": "Faithful lead-in to the three trust bullets; 'several' matches the three items."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "3.12.1"
   ],
   "claim_text": "That the code they are actually serving matches the open-source code.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The code they're actually serving matches the open-source code",
   "reasoning": "First trust bullet restated without change."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "3.12.2"
   ],
   "claim_text": "That they will not be compelled to inject malicious code in the future.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They won't be compelled to inject malicious code in the future",
   "reasoning": "Second trust bullet's negation preserved."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "3.12.3"
   ],
   "claim_text": "That their infrastructure has not been compromised by someone else who could serve malicious code.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Their infrastructure hasn't been compromised by someone else who could serve malicious code",
   "reasoning": "Third trust bullet's negation preserved."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "3.13"
   ],
   "claim_text": "The crucial difference from WhatsApp is that Proton does not have direct access to your keys in a usable form.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Proton doesn't have direct access to your encryption keys in a form they can use",
   "reasoning": "Matches the source's contrast and negation."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "3.14"
   ],
   "claim_text": "They would need to actively compromise the client to steal your password first, while WhatsApp's server can directly grant key access.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they'd need to actively compromise the client to steal your password first. WhatsApp's architecture doesn't even require that step; the server can directly grant key access",
   "reasoning": "Both halves of the contrast preserved with the same conditions."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "3.15"
   ],
   "claim_text": "Proton documents key storage and zero-access encryption in its support and security pages.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "How is the private key stored? (Proton Support) ... Protect your data with zero-access encryption (Proton Security)",
   "reasoning": "Accurately summarizes the two cited Proton sources."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Signal never holds your keys: its servers are never in a position to grant access to your message history.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Signal's servers are never in a position to grant access to your message history",
   "reasoning": "Matches the 'never' framing and the server-access claim."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "By default, message history is stored only on your device and deleted from Signal's servers after delivery.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "By default, message history is stored only on your device and deleted from Signal's servers after delivery",
   "reasoning": "Verbatim restatement of the default storage behavior."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Switching devices leaves you three options.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "When you want to switch devices, you have three options",
   "reasoning": "The count of three matches the source exactly."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Manual local backup on Android: create an encrypted backup file protected by a 30-digit passphrase, then physically transfer it to your new device.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted backup file protected by a 30-digit passphrase, then physically transfer it to your new device",
   "reasoning": "The 30-digit number and Android scope match the source."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Direct device-to-device transfer: both devices must be physically present and you transfer everything locally over your network.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Both devices must be physically present and you transfer everything locally over your network",
   "reasoning": "Restates option two with no altered conditions."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Signal Secure Backups: messages are encrypted with a 64-character recovery key that Signal never sees or has access to.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted with a 64-character recovery key that Signal never sees or has access to",
   "reasoning": "The 64-character figure and the 'never sees' negation are intact."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "4.6"
   ],
   "claim_text": "Even with the newer cloud backup feature, the recovery key stays on your device.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Even with the newer cloud backup feature, the recovery key stays on your device",
   "reasoning": "Matches the source's concession and key-location claim."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "4.6.1"
   ],
   "claim_text": "Signal literally cannot decrypt your backups even if they wanted to, and cannot help you recover them if you lose the key.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Signal literally cannot decrypt your backups even if they wanted to, and they cannot help you recover them if you lose your recovery key",
   "reasoning": "Both incapacity claims restated without change."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "4.7"
   ],
   "claim_text": "This is genuinely zero-knowledge architecture, not just marketing claims.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is genuinely zero-knowledge architecture, not just marketing claims.",
   "reasoning": "Verbatim restatement of the source's assessment."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "4.8"
   ],
   "claim_text": "Signal documents Secure Backups in a September 2024 blog post and support article.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Introducing Signal Secure Backups (Signal Blog, September 2024) ... Signal Secure Backups (Signal Support)",
   "reasoning": "The September 2024 date and both source types match the citation list."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Even trusting the encryption architecture, plaintext password storage on servers cannot be ruled out.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Even if we trust the encryption architecture, how do we know companies don't store your password in plaintext on their servers?",
   "reasoning": "Source poses exactly this open question, matching the loglog claim."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "If they have your password and your encrypted private key, they can decrypt everything.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if they have your password and your encrypted private key, they can decrypt everything",
   "reasoning": "Verbatim restatement of the source sentence."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "The short answer is that we do not know for certain.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The short answer: we don't know for certain.",
   "reasoning": "Identical meaning, only contraction expanded."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "You can verify what the client does if it is open source: that passwords are hashed before transmission.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "You can verify what the client does (if it's open source) - you can confirm that passwords are hashed before transmission.",
   "reasoning": "Source states precisely this verifiable client behavior."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "But you cannot verify what happens on the server after your password or password hash arrives; the server code is almost always closed source.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you cannot verify what happens on the server after your password (or password hash) arrives. The server code is almost always closed source",
   "reasoning": "Both the negation and the 'almost always' qualifier are preserved."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "Even with security audits, you are trusting the server operator.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "even with security audits, you're trusting that:",
   "reasoning": "Source introduces a list of things trusted after audits; paraphrase holds."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "5.5.1"
   ],
   "claim_text": "That the audited code is what is actually running.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The audited code is what's actually running",
   "reasoning": "Direct verbatim restatement of the bullet."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "5.5.2"
   ],
   "claim_text": "That they have not changed it since the audit.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They haven't changed it since the audit",
   "reasoning": "Negation and meaning preserved exactly."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "5.5.3"
   ],
   "claim_text": "That no rogue employee has modified it.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "No rogue employee has modified it",
   "reasoning": "Direct restatement of the bullet."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "5.5.4"
   ],
   "claim_text": "That their infrastructure has not been breached.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Their infrastructure hasn't been breached",
   "reasoning": "Negation and content preserved."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "5.6"
   ],
   "claim_text": "Real-world examples show this is not just paranoia.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Real-world examples show this isn't just paranoia.",
   "reasoning": "Verbatim restatement, contraction expanded only."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "5.6.1"
   ],
   "claim_text": "Facebook disclosed in 2019 that they had been accidentally logging hundreds of millions of passwords in plaintext in internal logs for years.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Facebook disclosed in 2019 that they'd been \"accidentally\" logging hundreds of millions of passwords in plaintext in internal logs for years.",
   "reasoning": "Year 2019 and quantity 'hundreds of millions' preserved; only scare quotes dropped."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "5.6.2"
   ],
   "claim_text": "Adobe's 2013 breach revealed they stored password hints in plaintext.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Adobe's 2013 breach revealed they stored password hints in plaintext.",
   "reasoning": "Entity, year 2013, and detail match source exactly."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "5.6.3"
   ],
   "claim_text": "Many smaller services store passwords in plaintext or use weak hashing like MD5 without salting.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Many smaller services store passwords in plaintext or use weak hashing like MD5 without salting.",
   "reasoning": "Verbatim restatement including the 'without salting' negation."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "5.7"
   ],
   "claim_text": "For Proton specifically: resetting your password via email or SMS recovery loses access to all your old encrypted emails.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if you reset your password via email/SMS recovery, you lose access to all your old encrypted emails",
   "reasoning": "Service, method, and consequence all match source."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "5.7.1"
   ],
   "claim_text": "That suggests they genuinely cannot decrypt your data without your password.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This suggests they genuinely can't decrypt your data without your password.",
   "reasoning": "Hedged 'suggests' retained; meaning identical."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "5.8"
   ],
   "claim_text": "But even this is not proof: they could deliberately withhold access to maintain their privacy-focused image, even if they technically could decrypt.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "But even this isn't proof - they could be deliberately not providing access to maintain their privacy-focused image, even if they technically could.",
   "reasoning": "Negation and both hedging clauses ('could') preserved."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "The fundamental problem: you are trusting reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you're trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees.",
   "reasoning": "All four trust factors and the contrast are retained."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Architecture matters: with WhatsApp, you are trusting Meta's entire server infrastructure.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is why the architecture matters so much. With WhatsApp, you're trusting Meta's entire server infrastructure.",
   "reasoning": "Entity and claim match source directly."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "With Proton, you are trusting that they will not serve malicious code.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "With Proton, you're trusting they won't serve malicious code.",
   "reasoning": "Negation and content preserved."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "With Signal and recovery keys, the attack surface is much smaller: they would need to compromise your device or steal your recovery key.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "With Signal using recovery keys, the attack surface is much smaller - they'd need to compromise your device or steal your recovery key",
   "reasoning": "Mechanism and both required attack paths match source."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "The comparison tables contrast key generation, key storage, new-device behavior, provider device injection, server storage, required trust, and security model.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Where encryption keys are generated ... Where private keys are stored ... What happens when you add a new device ... What you must trust ... Security model name",
   "reasoning": "Enumerated table aspects correspond to source rows; meta summary is accurate."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Can the provider add a device without your knowledge? WhatsApp yes; Proton no, but could serve malicious client code; Signal no.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "YES - WhatsApp controls device authentication ... NO - but they could serve malicious client code ... NO - they cannot authenticate a device",
   "reasoning": "All three per-service verdicts match the source table."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "What the server stores: WhatsApp keeps encrypted history, keys, and device-to-key mappings; Proton keeps emails and the encrypted private key; Signal keeps nothing by default.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp: 1. Encrypted message history 2. Encrypted encryption keys 3. Device-to-key mappings ... Signal: 1. Nothing by default",
   "reasoning": "Storage items for each service match the source table."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Security model names: server-mediated key escrow for WhatsApp, password-encrypted server-side key storage for Proton, client-controlled keys for Signal.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Security model name | Server-mediated key escrow | Password-encrypted server-side key storage | Client-controlled keys",
   "reasoning": "All three labels reproduce the source table exactly."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "The verification question gets its own treatment: what can and cannot be checked.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "## How Do We Know Companies Don't Store Plaintext Passwords?",
   "reasoning": "Source devotes a section to verifying plaintext storage, then enumerates what can and cannot be verified."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "What you can verify: open-source clients hash or encrypt passwords before sending, though this proves only what the client does.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "you can verify the client hashes/encrypts passwords before sending. But this only proves what the client does",
   "reasoning": "Source states the same scope limitation verbatim."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Network traffic inspection with tools like Wireshark shows what is transmitted; plaintext over the network is a red flag.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Tools like Wireshark can show what's transmitted. If passwords are sent in plaintext over the network, that's a red flag.",
   "reasoning": "Matches source exactly."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "8.2.1"
   ],
   "claim_text": "Even with HTTPS encryption, you cannot see what the server does after decryption.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "even with HTTPS encryption, you can't see what the server does after decryption",
   "reasoning": "Identical meaning, negation preserved."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Security audits: independent auditors can review server code if given access, but you trust the auditor and that the audited code was deployed.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Independent auditors can review server code if given access. But you're trusting the auditor and trusting the company deployed the audited code.",
   "reasoning": "Both trust conditions retained."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "What you cannot verify: server-side code is almost always closed source, and even if shown to auditors you cannot verify it is what runs.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Server-side code: Almost always closed-source. Even if shown to auditors, you can't verify that's what's actually running.",
   "reasoning": "Qualifier 'almost always' and negation preserved."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Even if truthful during an audit, they could add password logging in a later update.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Even if honest during an audit, they could add password logging in a later update.",
   "reasoning": "'truthful' is an equivalent restatement of 'honest'."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "An employee with server access could modify the code, or someone who breaches their systems could inject logging.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "an employee with server access could modify it, or someone who breaches their systems could inject logging",
   "reasoning": "Matches source; omitted lead-in condition does not alter the claim's meaning."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "8.7"
   ],
   "claim_text": "Good signs: open-source server code, independent audits with published results, and breach disclosure where passwords were not compromised.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Open-source server code ... Independent security audits ... with published results ... If breached and passwords weren't compromised",
   "reasoning": "All three good signs accurately listed with negation intact."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "8.8"
   ],
   "claim_text": "Bad signs: being able to reset a password and access old data, security through obscurity, and a history of privacy violations.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Can reset password and access old data ... Security through obscurity ... History of privacy violations",
   "reasoning": "All three bad signs match source items."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "8.9"
   ],
   "claim_text": "Facebook 2019: between 200-600 million passwords were logged in plaintext and searchable by over 20,000 Facebook employees.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "between 200-600 million passwords in plaintext ... searchable by over 20,000 Facebook employees",
   "reasoning": "Numbers, range, and entity preserved exactly."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "8.9.1"
   ],
   "claim_text": "Some archives dated back to 2012, and Facebook claimed the logging was unintentional.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "with some archives dating back to 2012. Facebook claimed this was unintentional",
   "reasoning": "Date and attribution to Facebook's claim match source."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "8.10"
   ],
   "claim_text": "Adobe 2013: the breach revealed stored password hints in plaintext, making brute-forcing easier, though at least passwords were hashed.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Adobe (2013): Breach revealed they stored password hints in plaintext, making brute-forcing easier (but at least passwords were hashed)",
   "reasoning": "Year, name, and the hashed-password caveat all preserved."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "8.11"
   ],
   "claim_text": "Many small services store passwords in plaintext or use MD5 without salt, and you find out when they get breached.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Many small services: Store passwords in plaintext or use weak hashing (MD5 without salt)",
   "reasoning": "Matches source, including MD5-without-salt detail."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "8.12"
   ],
   "claim_text": "You are always trusting the server operator to some degree unless one of three conditions holds.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "You're always trusting the server operator to some degree unless:",
   "reasoning": "Source lists exactly three numbered conditions."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "8.12.1"
   ],
   "claim_text": "All cryptography happens client-side, like Signal with recovery keys.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "All cryptography happens client-side (like Signal with recovery keys)",
   "reasoning": "Verbatim match of condition one."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "8.12.2"
   ],
   "claim_text": "The server never sees anything that could decrypt your data, as with zero-knowledge proof systems.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "The server never sees anything that could decrypt your data (zero-knowledge proof systems)",
   "reasoning": "Verbatim match of condition two, 'never' preserved."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "8.12.3"
   ],
   "claim_text": "Server code is open-source and reproducibly built, and you can verify what is running.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Server code is open-source AND reproducibly built AND you can verify what's running",
   "reasoning": "Conjunctive conditions preserved."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "The bottom line: for most commercial services you trust reputation, jurisdiction, business model, and past behavior rather than cryptographic guarantees.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "you're trusting their reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees",
   "reasoning": "Scope 'most commercial services' and contrast retained."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware keys like YubiKey that never expose the secret.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys (like YubiKey) that never expose the secret",
   "reasoning": "Verbatim match including YubiKey example and 'never' negation."
  }
 ],
 "metrics": {
  "total_claims": 110,
  "supported": 108,
  "partially_supported": 2,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9818
 },
 "fail_list": [
  "C005",
  "C018"
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
   "point_text": "Central thesis: E2EE means sender-device encryption and receiver-device decryption with nothing decrypting in between, but the real question is whether the provider (not merely a man-in-the-middle) can access content, and the answer is not completely clear.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L005",
    "L006",
    "L009"
   ],
   "evidence_quote": "Encrypting on the sender's device and decrypting on the receiver's device without decryption along the way is the definition of E2EE. ... The real question is whether Facebook can access the content of your WhatsApp messages in theory and in practice.",
   "reasoning": "L005 gives the definition, L006 notes MITM is a lesser concern, L009 states the real provider-access question, and L003 frames E2EE meaning several things. Thesis fully captured."
  },
  {
   "point_id": "K02",
   "point_text": "People usually want E2EE so no one outside sender and receivers, especially the provider, can access data. For WhatsApp this means Facebook should not read message content, though it still holds metadata: network, frequency, amount, and timing of communication.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L008"
   ],
   "evidence_quote": "Usually the purpose is that no one, and in particular the provider, can access the data. ... With WhatsApp, you do not want Facebook to access message content, though it still knows your network, communication frequency, amount, and times.",
   "reasoning": "L007 gives the purpose and provider focus, L008 gives the WhatsApp example with all four metadata categories intact."
  },
  {
   "point_id": "K03",
   "point_text": "WhatsApp's answer is unclear: if implemented as claimed with no secret backdoors, they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011",
    "L012",
    "L013"
   ],
   "evidence_quote": "If they implemented things as claimed and added no secret backdoors, then yes, they cannot access the data. ... External audits and tests lack certainty in the negative direction: they can never claim it cannot access the data.",
   "reasoning": "L010-L013 capture the conditional claim, the closed-source non-auditability, and the inability to prove the negative. Condition and negation preserved."
  },
  {
   "point_id": "K04",
   "point_text": "Evidence against WhatsApp/Meta: 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as plaintext storage of hundreds of millions of passwords, making it almost certain they can and do access message content.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L014",
    "L015",
    "L016"
   ],
   "evidence_quote": "The 2021 privacy policy changes allow sharing data with Facebook for relevant offers and ads across Meta company products. ... Given the company's business, you can almost be certain that they can, and do, access the messages.",
   "reasoning": "All three elements present: 2021 policy change, plaintext password failures, and the almost-certain conclusion with the qualifier preserved."
  },
  {
   "point_id": "K05",
   "point_text": "Smoking-gun test: whether a platform can back up or let you access history across devices without manually linking/transferring keys. If the provider ever holds the key it is like leaving a copy of your door key on a public billboard, letting it decrypt at will.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L017",
    "L018",
    "L023",
    "L024"
   ],
   "evidence_quote": "A smoking gun is whether the platform or app can back up your data. ... It is as if you locked your door and left a copy at the local farmers market billboard.",
   "reasoning": "L017-L018 state the test, L023-L024 preserve the billboard analogy and the at-will compromise implication."
  },
  {
   "point_id": "K06",
   "point_text": "How WhatsApp works: server stores encrypted message history and device-to-account identity mappings, authenticates new devices, and provides keys to decrypt history. This makes the server a trusted intermediary that could silently authenticate a rogue device and hide it from your device list, unlike Signal's manual key transfer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022",
    "L025",
    "L026",
    "L027",
    "L028",
    "L029",
    "L030"
   ],
   "evidence_quote": "the server stores encrypted message history and maintains mappings between your account and your device identities. ... they could simply hide a rogue device from your device list entirely.",
   "reasoning": "L025-L030 fully capture server storage, mappings, new-device authentication and key provision, trusted-intermediary framing, rogue-device injection and hiding, and L022 gives the Signal contrast."
  },
  {
   "point_id": "K07",
   "point_text": "Proton Mail model: private key generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L033",
    "L034",
    "L035"
   ],
   "evidence_quote": "your private key is generated in your browser and encrypted with your password. ... The encryption uses bcrypt and AES-256 before the key is sent to Proton's servers for storage.",
   "reasoning": "L033-L035 capture browser key generation, bcrypt + AES-256, and encrypted server-side storage. Numbers and algorithm names intact."
  },
  {
   "point_id": "K08",
   "point_text": "Proton login flow: type password, browser hashes it with bcrypt plus a server-provided salt, sends hash to authenticate, server returns the encrypted private key, and browser decrypts it locally with the actual password.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L036",
    "L037",
    "L038",
    "L039",
    "L040"
   ],
   "evidence_quote": "You type your password, and your browser hashes it with bcrypt using a salt provided by Proton's server. ... Your browser uses your original password to decrypt the private key locally.",
   "reasoning": "L036-L040 give the complete four-step flow including the server-provided salt and local decryption with the original password."
  },
  {
   "point_id": "K09",
   "point_text": "Distinction between hashing (one-way, used for authentication, cannot be reversed to the password) and encryption (two-way, used on the private key). Proton receives the hash for authentication while the key is encrypted with the actual password, so in theory the hash cannot decrypt the key.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L041",
    "L042",
    "L043",
    "L044",
    "L045"
   ],
   "evidence_quote": "Hashing is one-way ... Encryption is two-way ... the private key is encrypted with your actual password, so the hash cannot decrypt it.",
   "reasoning": "L041-L045 capture both definitions and the concluding separation that the hash cannot decrypt the key."
  },
  {
   "point_id": "K10",
   "point_text": "Proton's critical residual vulnerability: Proton could serve malicious client code (web app or update) to capture the actual password before hashing and use it to decrypt the stored key. This is why open-source clients matter, yet you must still trust the served code matches source, no future malicious injection, and no infrastructure compromise.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L046",
    "L047",
    "L048",
    "L049",
    "L050",
    "L051",
    "L052",
    "L053"
   ],
   "evidence_quote": "Proton could serve malicious client code, in the web app or through an app update. ... That they will not be compelled to inject malicious code in the future. ... That their infrastructure has not been compromised.",
   "reasoning": "All elements present: malicious code vector, password capture before hashing, decryption of stored key, value of open source, and the three residual trust assumptions."
  },
  {
   "point_id": "K11",
   "point_text": "Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L058",
    "L059",
    "L060",
    "L061",
    "L062"
   ],
   "evidence_quote": "message history is stored only on your device and deleted from Signal's servers after delivery. ... a 30-digit passphrase ... a 64-character recovery key that Signal never sees",
   "reasoning": "L058 gives device-only storage and server deletion, L059-L062 give all three device-switch options with both numbers intact."
  },
  {
   "point_id": "K12",
   "point_text": "Signal is genuinely zero-knowledge: servers are never positioned to grant access to message history, and even with cloud backups Signal cannot decrypt backups and cannot help recover them if the recovery key is lost.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L057",
    "L063",
    "L064",
    "L065"
   ],
   "evidence_quote": "Signal literally cannot decrypt your backups even if they wanted to, and cannot help you recover them if you lose the key. ... This is genuinely zero-knowledge architecture, not just marketing claims.",
   "reasoning": "L057 states servers never positioned to grant access, L063-L064 give cloud backup non-decryptability and non-recoverability, L065 names it genuine zero-knowledge."
  },
  {
   "point_id": "K13",
   "point_text": "Password storage limits: you can verify what an open-source client does (hashing before transmission), inspect network traffic, and read audits, but you cannot verify server-side code, whether it changed after an audit, rogue employees, or breaches. There is no cryptographic guarantee about server password handling.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L069",
    "L070",
    "L071",
    "L072",
    "L073",
    "L074",
    "L075",
    "L076",
    "L094",
    "L095",
    "L096",
    "L097"
   ],
   "evidence_quote": "you can verify what the client does if it is open source ... But you cannot verify what happens on the server ... No cryptographic guarantee about server password handling.",
   "reasoning": "L070-L076 and L094-L097 cover both the verifiable client side and the four unverifiable server-side risks, matching the point's scope."
  },
  {
   "point_id": "K14",
   "point_text": "Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though not proof.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L078",
    "L079",
    "L080",
    "L081",
    "L082",
    "L102",
    "L103",
    "L104",
    "L105"
   ],
   "evidence_quote": "between 200-600 million passwords were logged in plaintext and searchable by over 20,000 Facebook employees. ... Some archives dated back to 2012 ... Adobe's 2013 breach ... resetting your password via email or SMS recovery loses access to all your old encrypted emails.",
   "reasoning": "All examples present with full numbers: Facebook 200-600M, 20,000 employees, 2012 archives, Adobe 2013, MD5, and the Proton reset example with the not-proof caveat in L083."
  },
  {
   "point_id": "K15",
   "point_text": "Bottom line: for most commercial services you trust reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious users prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys such as YubiKey that never expose the secret.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L110",
    "L111"
   ],
   "evidence_quote": "for most commercial services you trust reputation, jurisdiction, business model, and past behavior rather than cryptographic guarantees. ... hardware keys like YubiKey that never expose the secret.",
   "reasoning": "L110 and L111 together preserve the closing thesis and the full list of preferred practices including decentralized systems and YubiKey."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 12,
  "must_have_partial": 0,
  "must_have_missing": 0,
  "overall_present": 15,
  "must_recall": 1.0,
  "overall_recall": 1.0
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
   "claim_text": "E2EE trust varies by architecture: WhatsApp mediates keys, Proton stores password-encrypted keys, Signal never holds them, and plaintext password storage stays unverifiable.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server can directly grant key access to any device it authenticates ... Signal literally cannot decrypt your backups ... we don't know for certain",
   "reasoning": "Each component matches the source: WhatsApp server-mediated keys, Proton server-stored encrypted key, Signal never sees key, plaintext storage uncertain."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "End-to-end encryption can mean several things in practice, and the real question is whether the provider can access your data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they could mean several things in practical terms ... can Facebook access the content of your WhatsApp messages or not",
   "reasoning": "Source states multiple meanings and frames the core question as provider access, matching the node."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "The author is not a security expert and writes this as an attempt to understand privacy as an end user.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I'm not a security expert ... This is an attempt to understand this as an end user",
   "reasoning": "Direct restatement of the disclaimer paragraph."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Encrypting on the sender's device and decrypting on the receiver's device without decryption along the way is the definition of E2EE.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted \"on sender's device\" and then decrypted \"on receiver's device\" without it ever being decrypted along the way is in fact the definition of it",
   "reasoning": "Node reproduces the source definition verbatim in meaning."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "If the purpose is only to defeat a man-in-the-middle attack, most implementations should be good enough.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "If the purpose is that a man-in-the-middle attack will not likely compromise your data, then most implementations of this should be good enough",
   "reasoning": "Source hedges with \"not likely compromise\"; node strengthens to \"defeat\" and adds \"only\", dropping the probabilistic qualifier."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "Usually the purpose is that no one, and in particular the provider, can access the data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In general one wants E2EE so that \"no one\" can access the data outside the sender and receivers, and in particular \"the provider\"",
   "reasoning": "\"Usually\" matches \"In general\"; the no-one/provider purpose is stated directly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "claim_text": "With WhatsApp, you do not want Facebook to access message content, though it still knows your network, communication frequency, amount, and times.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you don't want Facebook as a company to have access to the content of your messages ... they know your network, the frequency and amount of communication, times of communication",
   "reasoning": "All listed metadata matches the source's example."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "1.6"
   ],
   "claim_text": "The real question is whether Facebook can access the content of your WhatsApp messages in theory and in practice.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "in theory, and in practice, can Facebook access the content of your WhatsApp messages or not",
   "reasoning": "Direct restatement of the source's framing question."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "WhatsApp's answer is not completely clear: it depends on unverifiable implementation claims.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The answer is not completely clear ... we won't really know because the app is not open source, and hence not really auditable",
   "reasoning": "Node captures the source's uncertainty and lack of auditability."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "If they implemented things as claimed and added no secret backdoors, then yes, they cannot access the data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if they have implemented the things in the way they \"claim\" they have, and if they haven't implemented other backdoors ... then yes, they \"can't\" access that data",
   "reasoning": "Both conditions and the negative conclusion match the source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "We will not really know, because the app is not open source and hence not really auditable.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "we won't really know because the app is not open source, and hence not really auditable",
   "reasoning": "Near-verbatim restatement including the causal because clause."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "External audits and tests lack certainty in the negative direction: they can never claim it cannot access the data.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "external audits and tests will lack any certainty in the \"negative\" direction. That is, they can never claim it can't access those data",
   "reasoning": "Reproduces the source's point about unprovable negatives."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "The 2021 privacy policy changes allow sharing data with Facebook for relevant offers and ads across Meta company products.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "their 2021 privacy policy changes that allow sharing data with Facebook for \"showing relevant offers and ads across the Meta Company Products\"",
   "reasoning": "Year 2021 and the sharing purpose match the source exactly."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Previous security failures include storing hundreds of millions of passwords in plaintext.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "previous security failures like storing hundreds of millions of passwords in plaintext",
   "reasoning": "Quantity and plaintext detail preserved from source."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.6"
   ],
   "claim_text": "Given the company's business, you can almost be certain that they can, and do, access the messages.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "when you think about what the company's business is ... you can almost be certain that they can, and they do access them",
   "reasoning": "The hedge \"almost be certain\" and the claim of access match source."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "2.7"
   ],
   "claim_text": "A smoking gun is whether the platform or app can back up your data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For me, a smoking gun is whether the platform/app is able to \"backup\" your data",
   "reasoning": "Direct restatement of the author's smoking gun."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "2.7.1"
   ],
   "claim_text": "It is whether you can access history across devices without manually linking them somehow.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Whether you can access your history across devices without \"manually\" linking them somehow",
   "reasoning": "Verbatim in meaning, including the manual-linking condition."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "2.8"
   ],
   "claim_text": "Encryption is locking something with a key: one that only locks and that everyone has, and a master key only the receiver holds.",
   "claim_type": "definition",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "I think of encryption as locking something and having a key (usually a pair of keys, the one that only locks it and everyone has that, and a master key that only the receiver of the data has it",
   "reasoning": "Source frames this as the author's model and hedges \"usually a pair of keys\"; node states it as a flat definition."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "2.9"
   ],
   "claim_text": "Your master key is created and stored on your phone by default when you create an account.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "this is by default the case when you create an account the key is created and stored on your phone",
   "reasoning": "Matches the source's default-storage statement."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "2.10"
   ],
   "claim_text": "In a simple implementation, another device should not have the same master key to decrypt past messages.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In a simple implementation, there shouldn't be a way for that other device to have the same master key and decrypt your past messages",
   "reasoning": "Preserves the negation and the simple-implementation qualifier."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "2.10.1"
   ],
   "claim_text": "This is what happens in Signal, where you somehow copy the key from your original device to the new one.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is what happens in Signal. What you need to do is to somehow copy the key from your original device to your new device",
   "reasoning": "Direct restatement of the Signal key-copy behavior."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "2.11"
   ],
   "claim_text": "If at any time Facebook has access to the key, the situation is compromised.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if at any time, Facebook has access to it ... They can take the key and decrypt any/all of your messages whenever they want",
   "reasoning": "Node paraphrases the source's consequence of Facebook holding the key."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "2.11.1"
   ],
   "claim_text": "It is as if you locked your door and left a copy at the local farmers market billboard.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "it is as if you've locked your door and left a copy at the local farmers market billboard",
   "reasoning": "Reproduces the author's analogy exactly."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "2.12"
   ],
   "claim_text": "WhatsApp's official documentation says the server stores encrypted message history and maintains mappings between your account and your device identities.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "According to their official documentation, the server stores encrypted message history and maintains mappings between your account and all your device identities",
   "reasoning": "Attribution and both server functions match the source."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "2.13"
   ],
   "claim_text": "When you add a new device, the server authenticates it and provides the keys needed to decrypt your message history.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "When you add a new device, the server authenticates it and provides it with the keys needed to decrypt your message history",
   "reasoning": "Verbatim restatement."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "2.14"
   ],
   "claim_text": "This is fundamentally different from Signal: the server is a trusted intermediary that controls access to your encryption keys.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is fundamentally different from Signal's approach - the server is a trusted intermediary that controls access to your encryption keys",
   "reasoning": "Direct restatement including the Signal contrast."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "2.15"
   ],
   "claim_text": "Meta could theoretically authenticate a device that is not yours and give it access to decrypt your messages.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp (Meta) *could* theoretically authenticate a \"device\" that isn't actually yours and give it access to decrypt your messages",
   "reasoning": "Preserves the theoretical possibility and the device-not-yours condition."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "2.15.1"
   ],
   "claim_text": "The claimed safeguards, device lists you can check and security codes you can verify, depend on the server accurately reporting what devices exist.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Their claimed safeguards (device lists you can check, security codes you can verify) all depend on the server honestly reporting what devices exist",
   "reasoning": "Both safeguards and the dependency on honest server reporting are preserved."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "2.15.2"
   ],
   "claim_text": "Since they control that server, they could simply hide a rogue device from your device list entirely.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "since they control that server, they could simply hide a rogue device from your device list entirely",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "2.16"
   ],
   "claim_text": "The multi-device description comes from Meta's engineering post on how WhatsApp enables multi-device capability, from July 2021.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "How WhatsApp enables multi-device capability ... (Engineering at Meta, July 2021)",
   "reasoning": "Attribution, title, and July 2021 date match the source's reference list."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Proton stores your encrypted private key on its servers, so the trust shifts to the client.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your encrypted private key lives on Proton's servers ... This is why having open-source clients matters",
   "reasoning": "Source states key storage on servers and that the client becomes the trust concern."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "When you create a Proton account, your private key is generated in your browser and encrypted with your password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your private key is generated in your browser, then encrypted with your password",
   "reasoning": "Direct restatement of the source's account-creation description."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "3.1.1"
   ],
   "claim_text": "The encryption uses bcrypt and AES-256 before the key is sent to Proton's servers for storage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted with your password using bcrypt and AES-256 before being sent to their servers",
   "reasoning": "Source names bcrypt and AES-256 and the send-for-storage step."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "The crucial point: your encrypted private key lives on Proton's servers, not just on your original device.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your encrypted private key lives on Proton's servers, not just on your original device",
   "reasoning": "Near-verbatim restatement including the 'not just' qualifier."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "On a new device or browser, the login sequence runs as follows.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "When you log in on a new device or browser, here's what happens",
   "reasoning": "Faithful lead-in to the enumerated login steps."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "3.3.1"
   ],
   "claim_text": "You type your password, and your browser hashes it with bcrypt using a salt provided by Proton's server.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "hashes the password using bcrypt (with a salt provided by Proton's server)",
   "reasoning": "Matches source step 2 exactly, including the server-provided salt."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "3.3.2"
   ],
   "claim_text": "The hashed password is sent to Proton to prove you know the password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "sent to Proton to authenticate you (prove you know the password)",
   "reasoning": "Matches source step 3 without altering meaning."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "3.3.3"
   ],
   "claim_text": "The server sends your encrypted private key back to your browser.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The server sends your encrypted private key back to your browser",
   "reasoning": "Matches source step 4 verbatim."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "3.3.4"
   ],
   "claim_text": "Your browser uses your original password to decrypt the private key locally, and now you can read your emails.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "uses your original password to decrypt this private key locally ... Now you can read your emails",
   "reasoning": "Combines source steps 5 and 6 with identical meaning."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "Hashing is one-way: you can turn a password into a hash, but you theoretically cannot reverse a hash back into the password.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "A one-way function ... you theoretically cannot reverse a hash back into the password",
   "reasoning": "Preserves the 'theoretically' hedge and the one-way definition."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "3.5"
   ],
   "claim_text": "Proton receives your hashed password to verify you are who you claim to be, but this hash alone should not reveal your password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "this hash alone shouldn't let them figure out your actual password",
   "reasoning": "Keeps the source's 'shouldn't' hedge; meaning unchanged."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "3.6"
   ],
   "claim_text": "Encryption is two-way: you encrypt data with a key and decrypt it with that same key or a paired one.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can decrypt it back using that same key (or a paired key)",
   "reasoning": "Matches the source's two-way definition including the paired-key parenthetical."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "3.7"
   ],
   "claim_text": "Your private key is encrypted with your actual password, not the hash, so it can be decrypted when you provide the password again.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted with your actual password (not the hash), so it can be decrypted when you provide the password again",
   "reasoning": "Preserves the 'not the hash' negation and the decryption condition."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "3.8"
   ],
   "claim_text": "The security model: Proton receives your hashed password, but the private key is encrypted with your actual password, so the hash cannot decrypt it.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "even though they see your hashed password, they can't use that hash to decrypt your encrypted private key",
   "reasoning": "Retains the in-theory hedge and the hash-cannot-decrypt conclusion."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "3.9"
   ],
   "claim_text": "There is a critical vulnerability: Proton could serve malicious client code, in the web app or through an app update.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "there's still a critical vulnerability: Proton could serve you malicious client code (either in the web app or through an app update)",
   "reasoning": "Matches the vulnerability and both cited delivery channels."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "3.9.1"
   ],
   "claim_text": "That code could capture your actual password when you type it, before it gets hashed.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "captures your actual password when you type it - before it gets hashed",
   "reasoning": "Restates the capture-before-hashing point faithfully."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "3.10"
   ],
   "claim_text": "Since they already store your encrypted private key on their servers, if they capture your password they can decrypt it.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Since they already store your encrypted private key on their servers, if they capture your password, they can decrypt it",
   "reasoning": "Causal claim matches source nearly verbatim."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "3.11"
   ],
   "claim_text": "This is why having open-source clients matters: the community can verify that the client is not doing anything malicious.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "having open-source clients matters - the community can verify that the client isn't doing anything malicious",
   "reasoning": "Preserves the open-source rationale and its negation."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "3.12"
   ],
   "claim_text": "But you still have to trust several things.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "But you still have to trust that:",
   "reasoning": "Faithful lead-in to the three trust bullets; 'several' matches the three items."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "3.12.1"
   ],
   "claim_text": "That the code they are actually serving matches the open-source code.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The code they're actually serving matches the open-source code",
   "reasoning": "First trust bullet restated without change."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "3.12.2"
   ],
   "claim_text": "That they will not be compelled to inject malicious code in the future.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They won't be compelled to inject malicious code in the future",
   "reasoning": "Second trust bullet's negation preserved."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "3.12.3"
   ],
   "claim_text": "That their infrastructure has not been compromised by someone else who could serve malicious code.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Their infrastructure hasn't been compromised by someone else who could serve malicious code",
   "reasoning": "Third trust bullet's negation preserved."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "3.13"
   ],
   "claim_text": "The crucial difference from WhatsApp is that Proton does not have direct access to your keys in a usable form.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Proton doesn't have direct access to your encryption keys in a form they can use",
   "reasoning": "Matches the source's contrast and negation."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "3.14"
   ],
   "claim_text": "They would need to actively compromise the client to steal your password first, while WhatsApp's server can directly grant key access.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they'd need to actively compromise the client to steal your password first. WhatsApp's architecture doesn't even require that step; the server can directly grant key access",
   "reasoning": "Both halves of the contrast preserved with the same conditions."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "3.15"
   ],
   "claim_text": "Proton documents key storage and zero-access encryption in its support and security pages.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "How is the private key stored? (Proton Support) ... Protect your data with zero-access encryption (Proton Security)",
   "reasoning": "Accurately summarizes the two cited Proton sources."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Signal never holds your keys: its servers are never in a position to grant access to your message history.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Signal's servers are never in a position to grant access to your message history",
   "reasoning": "Matches the 'never' framing and the server-access claim."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "By default, message history is stored only on your device and deleted from Signal's servers after delivery.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "By default, message history is stored only on your device and deleted from Signal's servers after delivery",
   "reasoning": "Verbatim restatement of the default storage behavior."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Switching devices leaves you three options.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "When you want to switch devices, you have three options",
   "reasoning": "The count of three matches the source exactly."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Manual local backup on Android: create an encrypted backup file protected by a 30-digit passphrase, then physically transfer it to your new device.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted backup file protected by a 30-digit passphrase, then physically transfer it to your new device",
   "reasoning": "The 30-digit number and Android scope match the source."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Direct device-to-device transfer: both devices must be physically present and you transfer everything locally over your network.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Both devices must be physically present and you transfer everything locally over your network",
   "reasoning": "Restates option two with no altered conditions."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Signal Secure Backups: messages are encrypted with a 64-character recovery key that Signal never sees or has access to.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted with a 64-character recovery key that Signal never sees or has access to",
   "reasoning": "The 64-character figure and the 'never sees' negation are intact."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "4.6"
   ],
   "claim_text": "Even with the newer cloud backup feature, the recovery key stays on your device.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Even with the newer cloud backup feature, the recovery key stays on your device",
   "reasoning": "Matches the source's concession and key-location claim."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "4.6.1"
   ],
   "claim_text": "Signal literally cannot decrypt your backups even if they wanted to, and cannot help you recover them if you lose the key.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Signal literally cannot decrypt your backups even if they wanted to, and they cannot help you recover them if you lose your recovery key",
   "reasoning": "Both incapacity claims restated without change."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "4.7"
   ],
   "claim_text": "This is genuinely zero-knowledge architecture, not just marketing claims.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is genuinely zero-knowledge architecture, not just marketing claims.",
   "reasoning": "Verbatim restatement of the source's assessment."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "4.8"
   ],
   "claim_text": "Signal documents Secure Backups in a September 2024 blog post and support article.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Introducing Signal Secure Backups (Signal Blog, September 2024) ... Signal Secure Backups (Signal Support)",
   "reasoning": "The September 2024 date and both source types match the citation list."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Even trusting the encryption architecture, plaintext password storage on servers cannot be ruled out.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Even if we trust the encryption architecture, how do we know companies don't store your password in plaintext on their servers?",
   "reasoning": "Source poses exactly this open question, matching the loglog claim."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "If they have your password and your encrypted private key, they can decrypt everything.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if they have your password and your encrypted private key, they can decrypt everything",
   "reasoning": "Verbatim restatement of the source sentence."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "The short answer is that we do not know for certain.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The short answer: we don't know for certain.",
   "reasoning": "Identical meaning, only contraction expanded."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "You can verify what the client does if it is open source: that passwords are hashed before transmission.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "You can verify what the client does (if it's open source) - you can confirm that passwords are hashed before transmission.",
   "reasoning": "Source states precisely this verifiable client behavior."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "But you cannot verify what happens on the server after your password or password hash arrives; the server code is almost always closed source.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you cannot verify what happens on the server after your password (or password hash) arrives. The server code is almost always closed source",
   "reasoning": "Both the negation and the 'almost always' qualifier are preserved."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "Even with security audits, you are trusting the server operator.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "even with security audits, you're trusting that:",
   "reasoning": "Source introduces a list of things trusted after audits; paraphrase holds."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "5.5.1"
   ],
   "claim_text": "That the audited code is what is actually running.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The audited code is what's actually running",
   "reasoning": "Direct verbatim restatement of the bullet."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "5.5.2"
   ],
   "claim_text": "That they have not changed it since the audit.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They haven't changed it since the audit",
   "reasoning": "Negation and meaning preserved exactly."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "5.5.3"
   ],
   "claim_text": "That no rogue employee has modified it.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "No rogue employee has modified it",
   "reasoning": "Direct restatement of the bullet."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "5.5.4"
   ],
   "claim_text": "That their infrastructure has not been breached.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Their infrastructure hasn't been breached",
   "reasoning": "Negation and content preserved."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "5.6"
   ],
   "claim_text": "Real-world examples show this is not just paranoia.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Real-world examples show this isn't just paranoia.",
   "reasoning": "Verbatim restatement, contraction expanded only."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "5.6.1"
   ],
   "claim_text": "Facebook disclosed in 2019 that they had been accidentally logging hundreds of millions of passwords in plaintext in internal logs for years.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Facebook disclosed in 2019 that they'd been \"accidentally\" logging hundreds of millions of passwords in plaintext in internal logs for years.",
   "reasoning": "Year 2019 and quantity 'hundreds of millions' preserved; only scare quotes dropped."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "5.6.2"
   ],
   "claim_text": "Adobe's 2013 breach revealed they stored password hints in plaintext.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Adobe's 2013 breach revealed they stored password hints in plaintext.",
   "reasoning": "Entity, year 2013, and detail match source exactly."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "5.6.3"
   ],
   "claim_text": "Many smaller services store passwords in plaintext or use weak hashing like MD5 without salting.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Many smaller services store passwords in plaintext or use weak hashing like MD5 without salting.",
   "reasoning": "Verbatim restatement including the 'without salting' negation."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "5.7"
   ],
   "claim_text": "For Proton specifically: resetting your password via email or SMS recovery loses access to all your old encrypted emails.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if you reset your password via email/SMS recovery, you lose access to all your old encrypted emails",
   "reasoning": "Service, method, and consequence all match source."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "5.7.1"
   ],
   "claim_text": "That suggests they genuinely cannot decrypt your data without your password.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This suggests they genuinely can't decrypt your data without your password.",
   "reasoning": "Hedged 'suggests' retained; meaning identical."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "5.8"
   ],
   "claim_text": "But even this is not proof: they could deliberately withhold access to maintain their privacy-focused image, even if they technically could decrypt.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "But even this isn't proof - they could be deliberately not providing access to maintain their privacy-focused image, even if they technically could.",
   "reasoning": "Negation and both hedging clauses ('could') preserved."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "The fundamental problem: you are trusting reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you're trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees.",
   "reasoning": "All four trust factors and the contrast are retained."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Architecture matters: with WhatsApp, you are trusting Meta's entire server infrastructure.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is why the architecture matters so much. With WhatsApp, you're trusting Meta's entire server infrastructure.",
   "reasoning": "Entity and claim match source directly."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "With Proton, you are trusting that they will not serve malicious code.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "With Proton, you're trusting they won't serve malicious code.",
   "reasoning": "Negation and content preserved."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "With Signal and recovery keys, the attack surface is much smaller: they would need to compromise your device or steal your recovery key.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "With Signal using recovery keys, the attack surface is much smaller - they'd need to compromise your device or steal your recovery key",
   "reasoning": "Mechanism and both required attack paths match source."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "The comparison tables contrast key generation, key storage, new-device behavior, provider device injection, server storage, required trust, and security model.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Where encryption keys are generated ... Where private keys are stored ... What happens when you add a new device ... What you must trust ... Security model name",
   "reasoning": "Enumerated table aspects correspond to source rows; meta summary is accurate."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Can the provider add a device without your knowledge? WhatsApp yes; Proton no, but could serve malicious client code; Signal no.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "YES - WhatsApp controls device authentication ... NO - but they could serve malicious client code ... NO - they cannot authenticate a device",
   "reasoning": "All three per-service verdicts match the source table."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "What the server stores: WhatsApp keeps encrypted history, keys, and device-to-key mappings; Proton keeps emails and the encrypted private key; Signal keeps nothing by default.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp: 1. Encrypted message history 2. Encrypted encryption keys 3. Device-to-key mappings ... Signal: 1. Nothing by default",
   "reasoning": "Storage items for each service match the source table."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Security model names: server-mediated key escrow for WhatsApp, password-encrypted server-side key storage for Proton, client-controlled keys for Signal.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Security model name | Server-mediated key escrow | Password-encrypted server-side key storage | Client-controlled keys",
   "reasoning": "All three labels reproduce the source table exactly."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "The verification question gets its own treatment: what can and cannot be checked.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "## How Do We Know Companies Don't Store Plaintext Passwords?",
   "reasoning": "Source devotes a section to verifying plaintext storage, then enumerates what can and cannot be verified."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "What you can verify: open-source clients hash or encrypt passwords before sending, though this proves only what the client does.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "you can verify the client hashes/encrypts passwords before sending. But this only proves what the client does",
   "reasoning": "Source states the same scope limitation verbatim."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Network traffic inspection with tools like Wireshark shows what is transmitted; plaintext over the network is a red flag.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Tools like Wireshark can show what's transmitted. If passwords are sent in plaintext over the network, that's a red flag.",
   "reasoning": "Matches source exactly."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "8.2.1"
   ],
   "claim_text": "Even with HTTPS encryption, you cannot see what the server does after decryption.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "even with HTTPS encryption, you can't see what the server does after decryption",
   "reasoning": "Identical meaning, negation preserved."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Security audits: independent auditors can review server code if given access, but you trust the auditor and that the audited code was deployed.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Independent auditors can review server code if given access. But you're trusting the auditor and trusting the company deployed the audited code.",
   "reasoning": "Both trust conditions retained."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "What you cannot verify: server-side code is almost always closed source, and even if shown to auditors you cannot verify it is what runs.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Server-side code: Almost always closed-source. Even if shown to auditors, you can't verify that's what's actually running.",
   "reasoning": "Qualifier 'almost always' and negation preserved."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Even if truthful during an audit, they could add password logging in a later update.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Even if honest during an audit, they could add password logging in a later update.",
   "reasoning": "'truthful' is an equivalent restatement of 'honest'."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "An employee with server access could modify the code, or someone who breaches their systems could inject logging.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "an employee with server access could modify it, or someone who breaches their systems could inject logging",
   "reasoning": "Matches source; omitted lead-in condition does not alter the claim's meaning."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "8.7"
   ],
   "claim_text": "Good signs: open-source server code, independent audits with published results, and breach disclosure where passwords were not compromised.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Open-source server code ... Independent security audits ... with published results ... If breached and passwords weren't compromised",
   "reasoning": "All three good signs accurately listed with negation intact."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "8.8"
   ],
   "claim_text": "Bad signs: being able to reset a password and access old data, security through obscurity, and a history of privacy violations.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Can reset password and access old data ... Security through obscurity ... History of privacy violations",
   "reasoning": "All three bad signs match source items."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "8.9"
   ],
   "claim_text": "Facebook 2019: between 200-600 million passwords were logged in plaintext and searchable by over 20,000 Facebook employees.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "between 200-600 million passwords in plaintext ... searchable by over 20,000 Facebook employees",
   "reasoning": "Numbers, range, and entity preserved exactly."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "8.9.1"
   ],
   "claim_text": "Some archives dated back to 2012, and Facebook claimed the logging was unintentional.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "with some archives dating back to 2012. Facebook claimed this was unintentional",
   "reasoning": "Date and attribution to Facebook's claim match source."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "8.10"
   ],
   "claim_text": "Adobe 2013: the breach revealed stored password hints in plaintext, making brute-forcing easier, though at least passwords were hashed.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Adobe (2013): Breach revealed they stored password hints in plaintext, making brute-forcing easier (but at least passwords were hashed)",
   "reasoning": "Year, name, and the hashed-password caveat all preserved."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "8.11"
   ],
   "claim_text": "Many small services store passwords in plaintext or use MD5 without salt, and you find out when they get breached.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Many small services: Store passwords in plaintext or use weak hashing (MD5 without salt)",
   "reasoning": "Matches source, including MD5-without-salt detail."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "8.12"
   ],
   "claim_text": "You are always trusting the server operator to some degree unless one of three conditions holds.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "You're always trusting the server operator to some degree unless:",
   "reasoning": "Source lists exactly three numbered conditions."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "8.12.1"
   ],
   "claim_text": "All cryptography happens client-side, like Signal with recovery keys.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "All cryptography happens client-side (like Signal with recovery keys)",
   "reasoning": "Verbatim match of condition one."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "8.12.2"
   ],
   "claim_text": "The server never sees anything that could decrypt your data, as with zero-knowledge proof systems.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "The server never sees anything that could decrypt your data (zero-knowledge proof systems)",
   "reasoning": "Verbatim match of condition two, 'never' preserved."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "8.12.3"
   ],
   "claim_text": "Server code is open-source and reproducibly built, and you can verify what is running.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Server code is open-source AND reproducibly built AND you can verify what's running",
   "reasoning": "Conjunctive conditions preserved."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "The bottom line: for most commercial services you trust reputation, jurisdiction, business model, and past behavior rather than cryptographic guarantees.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "you're trusting their reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees",
   "reasoning": "Scope 'most commercial services' and contrast retained."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware keys like YubiKey that never expose the secret.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys (like YubiKey) that never expose the secret",
   "reasoning": "Verbatim match including YubiKey example and 'never' negation."
  }
 ],
 "metrics": {
  "total_claims": 110,
  "supported": 108,
  "partially_supported": 2,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9818
 },
 "fail_list": [
  "C005",
  "C018"
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
   "point_text": "Central thesis: E2EE means sender-device encryption and receiver-device decryption with nothing decrypting in between, but the real question is whether the provider (not merely a man-in-the-middle) can access content, and the answer is not completely clear.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L005",
    "L006",
    "L009"
   ],
   "evidence_quote": "Encrypting on the sender's device and decrypting on the receiver's device without decryption along the way is the definition of E2EE. ... The real question is whether Facebook can access the content of your WhatsApp messages in theory and in practice.",
   "reasoning": "L005 gives the definition, L006 notes MITM is a lesser concern, L009 states the real provider-access question, and L003 frames E2EE meaning several things. Thesis fully captured."
  },
  {
   "point_id": "K02",
   "point_text": "People usually want E2EE so no one outside sender and receivers, especially the provider, can access data. For WhatsApp this means Facebook should not read message content, though it still holds metadata: network, frequency, amount, and timing of communication.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L008"
   ],
   "evidence_quote": "Usually the purpose is that no one, and in particular the provider, can access the data. ... With WhatsApp, you do not want Facebook to access message content, though it still knows your network, communication frequency, amount, and times.",
   "reasoning": "L007 gives the purpose and provider focus, L008 gives the WhatsApp example with all four metadata categories intact."
  },
  {
   "point_id": "K03",
   "point_text": "WhatsApp's answer is unclear: if implemented as claimed with no secret backdoors, they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011",
    "L012",
    "L013"
   ],
   "evidence_quote": "If they implemented things as claimed and added no secret backdoors, then yes, they cannot access the data. ... External audits and tests lack certainty in the negative direction: they can never claim it cannot access the data.",
   "reasoning": "L010-L013 capture the conditional claim, the closed-source non-auditability, and the inability to prove the negative. Condition and negation preserved."
  },
  {
   "point_id": "K04",
   "point_text": "Evidence against WhatsApp/Meta: 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as plaintext storage of hundreds of millions of passwords, making it almost certain they can and do access message content.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L014",
    "L015",
    "L016"
   ],
   "evidence_quote": "The 2021 privacy policy changes allow sharing data with Facebook for relevant offers and ads across Meta company products. ... Given the company's business, you can almost be certain that they can, and do, access the messages.",
   "reasoning": "All three elements present: 2021 policy change, plaintext password failures, and the almost-certain conclusion with the qualifier preserved."
  },
  {
   "point_id": "K05",
   "point_text": "Smoking-gun test: whether a platform can back up or let you access history across devices without manually linking/transferring keys. If the provider ever holds the key it is like leaving a copy of your door key on a public billboard, letting it decrypt at will.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L017",
    "L018",
    "L023",
    "L024"
   ],
   "evidence_quote": "A smoking gun is whether the platform or app can back up your data. ... It is as if you locked your door and left a copy at the local farmers market billboard.",
   "reasoning": "L017-L018 state the test, L023-L024 preserve the billboard analogy and the at-will compromise implication."
  },
  {
   "point_id": "K06",
   "point_text": "How WhatsApp works: server stores encrypted message history and device-to-account identity mappings, authenticates new devices, and provides keys to decrypt history. This makes the server a trusted intermediary that could silently authenticate a rogue device and hide it from your device list, unlike Signal's manual key transfer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022",
    "L025",
    "L026",
    "L027",
    "L028",
    "L029",
    "L030"
   ],
   "evidence_quote": "the server stores encrypted message history and maintains mappings between your account and your device identities. ... they could simply hide a rogue device from your device list entirely.",
   "reasoning": "L025-L030 fully capture server storage, mappings, new-device authentication and key provision, trusted-intermediary framing, rogue-device injection and hiding, and L022 gives the Signal contrast."
  },
  {
   "point_id": "K07",
   "point_text": "Proton Mail model: private key generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L033",
    "L034",
    "L035"
   ],
   "evidence_quote": "your private key is generated in your browser and encrypted with your password. ... The encryption uses bcrypt and AES-256 before the key is sent to Proton's servers for storage.",
   "reasoning": "L033-L035 capture browser key generation, bcrypt + AES-256, and encrypted server-side storage. Numbers and algorithm names intact."
  },
  {
   "point_id": "K08",
   "point_text": "Proton login flow: type password, browser hashes it with bcrypt plus a server-provided salt, sends hash to authenticate, server returns the encrypted private key, and browser decrypts it locally with the actual password.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L036",
    "L037",
    "L038",
    "L039",
    "L040"
   ],
   "evidence_quote": "You type your password, and your browser hashes it with bcrypt using a salt provided by Proton's server. ... Your browser uses your original password to decrypt the private key locally.",
   "reasoning": "L036-L040 give the complete four-step flow including the server-provided salt and local decryption with the original password."
  },
  {
   "point_id": "K09",
   "point_text": "Distinction between hashing (one-way, used for authentication, cannot be reversed to the password) and encryption (two-way, used on the private key). Proton receives the hash for authentication while the key is encrypted with the actual password, so in theory the hash cannot decrypt the key.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L041",
    "L042",
    "L043",
    "L044",
    "L045"
   ],
   "evidence_quote": "Hashing is one-way ... Encryption is two-way ... the private key is encrypted with your actual password, so the hash cannot decrypt it.",
   "reasoning": "L041-L045 capture both definitions and the concluding separation that the hash cannot decrypt the key."
  },
  {
   "point_id": "K10",
   "point_text": "Proton's critical residual vulnerability: Proton could serve malicious client code (web app or update) to capture the actual password before hashing and use it to decrypt the stored key. This is why open-source clients matter, yet you must still trust the served code matches source, no future malicious injection, and no infrastructure compromise.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L046",
    "L047",
    "L048",
    "L049",
    "L050",
    "L051",
    "L052",
    "L053"
   ],
   "evidence_quote": "Proton could serve malicious client code, in the web app or through an app update. ... That they will not be compelled to inject malicious code in the future. ... That their infrastructure has not been compromised.",
   "reasoning": "All elements present: malicious code vector, password capture before hashing, decryption of stored key, value of open source, and the three residual trust assumptions."
  },
  {
   "point_id": "K11",
   "point_text": "Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L058",
    "L059",
    "L060",
    "L061",
    "L062"
   ],
   "evidence_quote": "message history is stored only on your device and deleted from Signal's servers after delivery. ... a 30-digit passphrase ... a 64-character recovery key that Signal never sees",
   "reasoning": "L058 gives device-only storage and server deletion, L059-L062 give all three device-switch options with both numbers intact."
  },
  {
   "point_id": "K12",
   "point_text": "Signal is genuinely zero-knowledge: servers are never positioned to grant access to message history, and even with cloud backups Signal cannot decrypt backups and cannot help recover them if the recovery key is lost.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L057",
    "L063",
    "L064",
    "L065"
   ],
   "evidence_quote": "Signal literally cannot decrypt your backups even if they wanted to, and cannot help you recover them if you lose the key. ... This is genuinely zero-knowledge architecture, not just marketing claims.",
   "reasoning": "L057 states servers never positioned to grant access, L063-L064 give cloud backup non-decryptability and non-recoverability, L065 names it genuine zero-knowledge."
  },
  {
   "point_id": "K13",
   "point_text": "Password storage limits: you can verify what an open-source client does (hashing before transmission), inspect network traffic, and read audits, but you cannot verify server-side code, whether it changed after an audit, rogue employees, or breaches. There is no cryptographic guarantee about server password handling.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L069",
    "L070",
    "L071",
    "L072",
    "L073",
    "L074",
    "L075",
    "L076",
    "L094",
    "L095",
    "L096",
    "L097"
   ],
   "evidence_quote": "you can verify what the client does if it is open source ... But you cannot verify what happens on the server ... No cryptographic guarantee about server password handling.",
   "reasoning": "L070-L076 and L094-L097 cover both the verifiable client side and the four unverifiable server-side risks, matching the point's scope."
  },
  {
   "point_id": "K14",
   "point_text": "Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though not proof.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L078",
    "L079",
    "L080",
    "L081",
    "L082",
    "L102",
    "L103",
    "L104",
    "L105"
   ],
   "evidence_quote": "between 200-600 million passwords were logged in plaintext and searchable by over 20,000 Facebook employees. ... Some archives dated back to 2012 ... Adobe's 2013 breach ... resetting your password via email or SMS recovery loses access to all your old encrypted emails.",
   "reasoning": "All examples present with full numbers: Facebook 200-600M, 20,000 employees, 2012 archives, Adobe 2013, MD5, and the Proton reset example with the not-proof caveat in L083."
  },
  {
   "point_id": "K15",
   "point_text": "Bottom line: for most commercial services you trust reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious users prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys such as YubiKey that never expose the secret.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L110",
    "L111"
   ],
   "evidence_quote": "for most commercial services you trust reputation, jurisdiction, business model, and past behavior rather than cryptographic guarantees. ... hardware keys like YubiKey that never expose the secret.",
   "reasoning": "L110 and L111 together preserve the closing thesis and the full list of preferred practices including decentralized systems and YubiKey."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 12,
  "must_have_partial": 0,
  "must_have_missing": 0,
  "overall_present": 15,
  "must_recall": 1.0,
  "overall_recall": 1.0
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
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Top-level summary carries the whole document thesis, not repeated elsewhere as one claim."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section 1 thesis on provider access; not restated by a later single claim."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Author disclaimer; informational context, not a filler transition or restated header."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Core E2EE definition, stated once."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Caveated MITM point; contradiction-adjacent, kept visible and distinct."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specifies usual purpose; adds beyond C002."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete WhatsApp/Facebook metadata example, not repeated."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "1.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Narrows the question to practice and theory; distinct from C002."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "WhatsApp section conclusion, distinct from its supporting points."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Conditional claim about implementation, not duplicated."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Closed-source auditability causal point, unique."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audit certainty-in-negative claim; distinct from section 8 audit points."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Dated 2021 policy fact, single mention."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First preview of plaintext password failures; distinct framing from later examples."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Business-model inference, unique."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "2.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Backup capability as smoking gun, unique."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "2.7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cross-device history access detail, distinct from C016."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "2.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Lock-and-key definition; partially supported, kept visible."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "2.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Key creation/storage fact, unique."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "2.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Simple-implementation key isolation claim, unique."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "2.10.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal key-copy example, distinct from C020."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "2.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Causal key-access claim; canonical for its analogy."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "2.11.1"
   ],
   "label": "Duplicate",
   "canonical_id": "C022",
   "reasoning": "Billboard analogy restates C022 with no new proposition."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "2.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "WhatsApp server-storage documentation fact, unique."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "2.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New-device key provisioning fact, distinct from C024."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "2.14"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal contrast and trusted-intermediary framing, unique."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "2.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Rogue-device possibility, canonical for the table row C088."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "2.15.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Safeguard dependence on server reporting, unique."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "2.15.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hidden rogue device consequence, distinct from C028."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "2.16"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sourced multi-device engineering post, unique."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton section lead and trust-shift conclusion, unique."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Key generation/encryption fact, unique."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "3.1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "bcrypt/AES-256 detail, distinct from C032."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds not-just-original-device insight beyond the section lead C031."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Pure signpost introducing the login sequence; no independent content."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "3.3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bcrypt salt login step, unique."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "3.3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hashed password transmission step, unique."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "3.3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Server returns encrypted key step, unique."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "3.3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Local decryption step, unique."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "One-way hashing definition, unique."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "3.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hash-verification claim, distinct from C039."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "3.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two-way encryption definition, unique."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "3.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Key encrypted with actual password, unique."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "3.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Security-model synthesis, distinct from C041/C043."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "3.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Malicious client-code vulnerability, unique."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "3.9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Password capture mechanism, distinct from C045."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "3.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Capture-plus-stored-key causal chain, unique."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "3.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Open-source client rationale, unique."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "3.12"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Signpost to the trust list; supplies no facts itself."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "3.12.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Served-code matches open source, unique."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "3.12.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No future compelled injection, distinct from later trust items."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "3.12.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Infrastructure not compromised; canonical for C075."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "3.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No usable-key access contrast, unique."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "3.14"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Mechanism behind the Proton/WhatsApp difference, unique."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "3.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sourced zero-access documentation, unique."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal section lead on key non-custody, unique."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Default storage/deletion fact, distinct from C056."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "States three options; numeric content, not trivia."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Android backup option with 30-digit passphrase, unique."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Device-to-device transfer option, unique."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Secure Backup 64-character key fact, unique."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "4.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Recovery key stays on device, distinct from C061."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "4.6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No-decrypt/no-recovery consequence, unique."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "4.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Zero-knowledge conclusion beyond marketing, unique."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "4.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Dated Secure Backup source, unique."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section 5 lead on plaintext storage risk, unique."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Password-plus-key decrypt chain, unique."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Uncertainty conclusion, unique."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Client verifiability claim; related to C092 but not restated verbatim."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Server unverifiability claim; distinct from C096's audit caveat."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "5.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audit-era trust claim, introduces its own four-item list."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "5.5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audited code is running, distinct from C096."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "5.5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No change since audit, distinct from C097."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "5.5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No rogue employee, distinct from C098's combined claim."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "5.5.4"
   ],
   "label": "Duplicate",
   "canonical_id": "C052",
   "reasoning": "Infrastructure not breached restates item 3.12.3 with no new content."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "5.6"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Lead-in to the examples; filler framing with no fact."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "5.6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Facebook plaintext logging; canonical for the section 8 restatement."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "5.6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adobe 2013 hint example; canonical for C103."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "5.6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Small-services weak hashing; canonical for C104."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "5.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton reset-loses-data fact, unique."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "5.7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Inference from reset behavior, unique."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "5.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Counter-caveat that withholding is possible, unique."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section 6 trust basis; canonical for the section 9 restatement."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "WhatsApp infrastructure trust, unique."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton malicious-code trust, unique."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal smaller attack surface, unique."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated header describing the comparison tables; no new claim."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.1"
   ],
   "label": "Duplicate",
   "canonical_id": "C027",
   "reasoning": "Table row recaps the provider rogue-device point from 2.15."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Server-storage comparison across services, unique summary content."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Security-model naming, unique."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "8"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated header for the verification theme; no independent claim."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "8.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds client-only-proof caveat beyond C069."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "8.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Wireshark traffic inspection method, unique."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "8.2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "HTTPS post-decryption blind spot, unique."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "8.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audit trust caveats, unique."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "8.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Unverifiable server code with auditor caveat, distinct."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "8.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Later-update logging risk, unique."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "8.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Employee or breach injection, combines distinct actors."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "8.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Good-sign indicators, unique."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "8.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bad-sign indicators, unique."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "8.9"
   ],
   "label": "Duplicate",
   "canonical_id": "C077",
   "reasoning": "Facebook plaintext logging recap; only adds figures to the same fact."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "8.9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "2012 archive and unintentional claim, new detail beyond C101."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "8.10"
   ],
   "label": "Duplicate",
   "canonical_id": "C078",
   "reasoning": "Adobe 2013 plaintext hints restated with brute-force note."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "8.11"
   ],
   "label": "Duplicate",
   "canonical_id": "C079",
   "reasoning": "Small-services plaintext/MD5 restated with breach discovery."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "8.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Frames the three-condition escape; content differs from C071."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "8.12.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Client-side crypto condition, unique."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "8.12.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Server-never-sees condition, unique."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "8.12.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reproducible open-source build condition, unique."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "9"
   ],
   "label": "Duplicate",
   "canonical_id": "C083",
   "reasoning": "Bottom line restates the section 6 trust-basis claim nearly verbatim."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Recommendation list for security-conscious users, unique."
  }
 ],
 "metrics": {
  "scored_claims": 110,
  "unique": 98,
  "duplicates": 7,
  "trivia": 5,
  "redundancy_rate": 0.0636,
  "trivia_rate": 0.0455,
  "structured_tokens": 1900,
  "tokens_per_unique_claim": 19.4
 },
 "prune_list": [
  "C023 duplicates C022 (billboard analogy adds no proposition), safe to merge",
  "C075 duplicates C052 (infrastructure-not-breached item repeated), safe to merge",
  "C088 duplicates C027 (table row recaps rogue-device point), safe to merge",
  "C101 duplicates C077 (Facebook plaintext logging restated), safe to merge",
  "C103 duplicates C078 (Adobe 2013 hints restated), safe to merge",
  "C104 duplicates C079 (small-services MD5 restated), safe to merge",
  "C109 duplicates C083 (bottom line restates fundamental problem), safe to merge",
  "C035 trivia (login-sequence signpost), cut",
  "C049 trivia (you-must-trust signpost), cut",
  "C076 trivia (lead-in to real-world examples), cut",
  "C087 trivia (restated header for comparison tables), cut",
  "C091 trivia (restated header for verification section), cut"
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
   "claim_text": "E2EE trust varies by architecture: WhatsApp mediates keys, Proton stores password-encrypted keys, Signal never holds them, and plaintext password storage stays unverifiable.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "the server can directly grant key access to any device it authenticates ... Signal literally cannot decrypt your backups ... we don't know for certain",
   "reasoning": "Each component matches the source: WhatsApp server-mediated keys, Proton server-stored encrypted key, Signal never sees key, plaintext storage uncertain."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "claim_text": "End-to-end encryption can mean several things in practice, and the real question is whether the provider can access your data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they could mean several things in practical terms ... can Facebook access the content of your WhatsApp messages or not",
   "reasoning": "Source states multiple meanings and frames the core question as provider access, matching the node."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "claim_text": "The author is not a security expert and writes this as an attempt to understand privacy as an end user.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "I'm not a security expert ... This is an attempt to understand this as an end user",
   "reasoning": "Direct restatement of the disclaimer paragraph."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "claim_text": "Encrypting on the sender's device and decrypting on the receiver's device without decryption along the way is the definition of E2EE.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted \"on sender's device\" and then decrypted \"on receiver's device\" without it ever being decrypted along the way is in fact the definition of it",
   "reasoning": "Node reproduces the source definition verbatim in meaning."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "claim_text": "If the purpose is only to defeat a man-in-the-middle attack, most implementations should be good enough.",
   "claim_type": "interpretation",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "If the purpose is that a man-in-the-middle attack will not likely compromise your data, then most implementations of this should be good enough",
   "reasoning": "Source hedges with \"not likely compromise\"; node strengthens to \"defeat\" and adds \"only\", dropping the probabilistic qualifier."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "claim_text": "Usually the purpose is that no one, and in particular the provider, can access the data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In general one wants E2EE so that \"no one\" can access the data outside the sender and receivers, and in particular \"the provider\"",
   "reasoning": "\"Usually\" matches \"In general\"; the no-one/provider purpose is stated directly."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "claim_text": "With WhatsApp, you do not want Facebook to access message content, though it still knows your network, communication frequency, amount, and times.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you don't want Facebook as a company to have access to the content of your messages ... they know your network, the frequency and amount of communication, times of communication",
   "reasoning": "All listed metadata matches the source's example."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "1.6"
   ],
   "claim_text": "The real question is whether Facebook can access the content of your WhatsApp messages in theory and in practice.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "in theory, and in practice, can Facebook access the content of your WhatsApp messages or not",
   "reasoning": "Direct restatement of the source's framing question."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2"
   ],
   "claim_text": "WhatsApp's answer is not completely clear: it depends on unverifiable implementation claims.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The answer is not completely clear ... we won't really know because the app is not open source, and hence not really auditable",
   "reasoning": "Node captures the source's uncertainty and lack of auditability."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.1"
   ],
   "claim_text": "If they implemented things as claimed and added no secret backdoors, then yes, they cannot access the data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if they have implemented the things in the way they \"claim\" they have, and if they haven't implemented other backdoors ... then yes, they \"can't\" access that data",
   "reasoning": "Both conditions and the negative conclusion match the source."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.2"
   ],
   "claim_text": "We will not really know, because the app is not open source and hence not really auditable.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "we won't really know because the app is not open source, and hence not really auditable",
   "reasoning": "Near-verbatim restatement including the causal because clause."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.3"
   ],
   "claim_text": "External audits and tests lack certainty in the negative direction: they can never claim it cannot access the data.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "external audits and tests will lack any certainty in the \"negative\" direction. That is, they can never claim it can't access those data",
   "reasoning": "Reproduces the source's point about unprovable negatives."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.4"
   ],
   "claim_text": "The 2021 privacy policy changes allow sharing data with Facebook for relevant offers and ads across Meta company products.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "their 2021 privacy policy changes that allow sharing data with Facebook for \"showing relevant offers and ads across the Meta Company Products\"",
   "reasoning": "Year 2021 and the sharing purpose match the source exactly."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.5"
   ],
   "claim_text": "Previous security failures include storing hundreds of millions of passwords in plaintext.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "previous security failures like storing hundreds of millions of passwords in plaintext",
   "reasoning": "Quantity and plaintext detail preserved from source."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.6"
   ],
   "claim_text": "Given the company's business, you can almost be certain that they can, and do, access the messages.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "when you think about what the company's business is ... you can almost be certain that they can, and they do access them",
   "reasoning": "The hedge \"almost be certain\" and the claim of access match source."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "2.7"
   ],
   "claim_text": "A smoking gun is whether the platform or app can back up your data.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "For me, a smoking gun is whether the platform/app is able to \"backup\" your data",
   "reasoning": "Direct restatement of the author's smoking gun."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "2.7.1"
   ],
   "claim_text": "It is whether you can access history across devices without manually linking them somehow.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Whether you can access your history across devices without \"manually\" linking them somehow",
   "reasoning": "Verbatim in meaning, including the manual-linking condition."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "2.8"
   ],
   "claim_text": "Encryption is locking something with a key: one that only locks and that everyone has, and a master key only the receiver holds.",
   "claim_type": "definition",
   "verdict": "Partially supported",
   "severity": "Minor",
   "evidence_quote": "I think of encryption as locking something and having a key (usually a pair of keys, the one that only locks it and everyone has that, and a master key that only the receiver of the data has it",
   "reasoning": "Source frames this as the author's model and hedges \"usually a pair of keys\"; node states it as a flat definition."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "2.9"
   ],
   "claim_text": "Your master key is created and stored on your phone by default when you create an account.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "this is by default the case when you create an account the key is created and stored on your phone",
   "reasoning": "Matches the source's default-storage statement."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "2.10"
   ],
   "claim_text": "In a simple implementation, another device should not have the same master key to decrypt past messages.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "In a simple implementation, there shouldn't be a way for that other device to have the same master key and decrypt your past messages",
   "reasoning": "Preserves the negation and the simple-implementation qualifier."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "2.10.1"
   ],
   "claim_text": "This is what happens in Signal, where you somehow copy the key from your original device to the new one.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is what happens in Signal. What you need to do is to somehow copy the key from your original device to your new device",
   "reasoning": "Direct restatement of the Signal key-copy behavior."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "2.11"
   ],
   "claim_text": "If at any time Facebook has access to the key, the situation is compromised.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if at any time, Facebook has access to it ... They can take the key and decrypt any/all of your messages whenever they want",
   "reasoning": "Node paraphrases the source's consequence of Facebook holding the key."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "2.11.1"
   ],
   "claim_text": "It is as if you locked your door and left a copy at the local farmers market billboard.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "it is as if you've locked your door and left a copy at the local farmers market billboard",
   "reasoning": "Reproduces the author's analogy exactly."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "2.12"
   ],
   "claim_text": "WhatsApp's official documentation says the server stores encrypted message history and maintains mappings between your account and your device identities.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "According to their official documentation, the server stores encrypted message history and maintains mappings between your account and all your device identities",
   "reasoning": "Attribution and both server functions match the source."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "2.13"
   ],
   "claim_text": "When you add a new device, the server authenticates it and provides the keys needed to decrypt your message history.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "When you add a new device, the server authenticates it and provides it with the keys needed to decrypt your message history",
   "reasoning": "Verbatim restatement."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "2.14"
   ],
   "claim_text": "This is fundamentally different from Signal: the server is a trusted intermediary that controls access to your encryption keys.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is fundamentally different from Signal's approach - the server is a trusted intermediary that controls access to your encryption keys",
   "reasoning": "Direct restatement including the Signal contrast."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "2.15"
   ],
   "claim_text": "Meta could theoretically authenticate a device that is not yours and give it access to decrypt your messages.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp (Meta) *could* theoretically authenticate a \"device\" that isn't actually yours and give it access to decrypt your messages",
   "reasoning": "Preserves the theoretical possibility and the device-not-yours condition."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "2.15.1"
   ],
   "claim_text": "The claimed safeguards, device lists you can check and security codes you can verify, depend on the server accurately reporting what devices exist.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Their claimed safeguards (device lists you can check, security codes you can verify) all depend on the server honestly reporting what devices exist",
   "reasoning": "Both safeguards and the dependency on honest server reporting are preserved."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "2.15.2"
   ],
   "claim_text": "Since they control that server, they could simply hide a rogue device from your device list entirely.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "since they control that server, they could simply hide a rogue device from your device list entirely",
   "reasoning": "Direct restatement."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "2.16"
   ],
   "claim_text": "The multi-device description comes from Meta's engineering post on how WhatsApp enables multi-device capability, from July 2021.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "How WhatsApp enables multi-device capability ... (Engineering at Meta, July 2021)",
   "reasoning": "Attribution, title, and July 2021 date match the source's reference list."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "3"
   ],
   "claim_text": "Proton stores your encrypted private key on its servers, so the trust shifts to the client.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your encrypted private key lives on Proton's servers ... This is why having open-source clients matters",
   "reasoning": "Source states key storage on servers and that the client becomes the trust concern."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "3.1"
   ],
   "claim_text": "When you create a Proton account, your private key is generated in your browser and encrypted with your password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your private key is generated in your browser, then encrypted with your password",
   "reasoning": "Direct restatement of the source's account-creation description."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "3.1.1"
   ],
   "claim_text": "The encryption uses bcrypt and AES-256 before the key is sent to Proton's servers for storage.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted with your password using bcrypt and AES-256 before being sent to their servers",
   "reasoning": "Source names bcrypt and AES-256 and the send-for-storage step."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "3.2"
   ],
   "claim_text": "The crucial point: your encrypted private key lives on Proton's servers, not just on your original device.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "your encrypted private key lives on Proton's servers, not just on your original device",
   "reasoning": "Near-verbatim restatement including the 'not just' qualifier."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "3.3"
   ],
   "claim_text": "On a new device or browser, the login sequence runs as follows.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "When you log in on a new device or browser, here's what happens",
   "reasoning": "Faithful lead-in to the enumerated login steps."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "3.3.1"
   ],
   "claim_text": "You type your password, and your browser hashes it with bcrypt using a salt provided by Proton's server.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "hashes the password using bcrypt (with a salt provided by Proton's server)",
   "reasoning": "Matches source step 2 exactly, including the server-provided salt."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "3.3.2"
   ],
   "claim_text": "The hashed password is sent to Proton to prove you know the password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "sent to Proton to authenticate you (prove you know the password)",
   "reasoning": "Matches source step 3 without altering meaning."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "3.3.3"
   ],
   "claim_text": "The server sends your encrypted private key back to your browser.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The server sends your encrypted private key back to your browser",
   "reasoning": "Matches source step 4 verbatim."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "3.3.4"
   ],
   "claim_text": "Your browser uses your original password to decrypt the private key locally, and now you can read your emails.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "uses your original password to decrypt this private key locally ... Now you can read your emails",
   "reasoning": "Combines source steps 5 and 6 with identical meaning."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "3.4"
   ],
   "claim_text": "Hashing is one-way: you can turn a password into a hash, but you theoretically cannot reverse a hash back into the password.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "A one-way function ... you theoretically cannot reverse a hash back into the password",
   "reasoning": "Preserves the 'theoretically' hedge and the one-way definition."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "3.5"
   ],
   "claim_text": "Proton receives your hashed password to verify you are who you claim to be, but this hash alone should not reveal your password.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "this hash alone shouldn't let them figure out your actual password",
   "reasoning": "Keeps the source's 'shouldn't' hedge; meaning unchanged."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "3.6"
   ],
   "claim_text": "Encryption is two-way: you encrypt data with a key and decrypt it with that same key or a paired one.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you can decrypt it back using that same key (or a paired key)",
   "reasoning": "Matches the source's two-way definition including the paired-key parenthetical."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "3.7"
   ],
   "claim_text": "Your private key is encrypted with your actual password, not the hash, so it can be decrypted when you provide the password again.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted with your actual password (not the hash), so it can be decrypted when you provide the password again",
   "reasoning": "Preserves the 'not the hash' negation and the decryption condition."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "3.8"
   ],
   "claim_text": "The security model: Proton receives your hashed password, but the private key is encrypted with your actual password, so the hash cannot decrypt it.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "even though they see your hashed password, they can't use that hash to decrypt your encrypted private key",
   "reasoning": "Retains the in-theory hedge and the hash-cannot-decrypt conclusion."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "3.9"
   ],
   "claim_text": "There is a critical vulnerability: Proton could serve malicious client code, in the web app or through an app update.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "there's still a critical vulnerability: Proton could serve you malicious client code (either in the web app or through an app update)",
   "reasoning": "Matches the vulnerability and both cited delivery channels."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "3.9.1"
   ],
   "claim_text": "That code could capture your actual password when you type it, before it gets hashed.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "captures your actual password when you type it - before it gets hashed",
   "reasoning": "Restates the capture-before-hashing point faithfully."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "3.10"
   ],
   "claim_text": "Since they already store your encrypted private key on their servers, if they capture your password they can decrypt it.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Since they already store your encrypted private key on their servers, if they capture your password, they can decrypt it",
   "reasoning": "Causal claim matches source nearly verbatim."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "3.11"
   ],
   "claim_text": "This is why having open-source clients matters: the community can verify that the client is not doing anything malicious.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "having open-source clients matters - the community can verify that the client isn't doing anything malicious",
   "reasoning": "Preserves the open-source rationale and its negation."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "3.12"
   ],
   "claim_text": "But you still have to trust several things.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "But you still have to trust that:",
   "reasoning": "Faithful lead-in to the three trust bullets; 'several' matches the three items."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "3.12.1"
   ],
   "claim_text": "That the code they are actually serving matches the open-source code.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The code they're actually serving matches the open-source code",
   "reasoning": "First trust bullet restated without change."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "3.12.2"
   ],
   "claim_text": "That they will not be compelled to inject malicious code in the future.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They won't be compelled to inject malicious code in the future",
   "reasoning": "Second trust bullet's negation preserved."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "3.12.3"
   ],
   "claim_text": "That their infrastructure has not been compromised by someone else who could serve malicious code.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Their infrastructure hasn't been compromised by someone else who could serve malicious code",
   "reasoning": "Third trust bullet's negation preserved."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "3.13"
   ],
   "claim_text": "The crucial difference from WhatsApp is that Proton does not have direct access to your keys in a usable form.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Proton doesn't have direct access to your encryption keys in a form they can use",
   "reasoning": "Matches the source's contrast and negation."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "3.14"
   ],
   "claim_text": "They would need to actively compromise the client to steal your password first, while WhatsApp's server can directly grant key access.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "they'd need to actively compromise the client to steal your password first. WhatsApp's architecture doesn't even require that step; the server can directly grant key access",
   "reasoning": "Both halves of the contrast preserved with the same conditions."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "3.15"
   ],
   "claim_text": "Proton documents key storage and zero-access encryption in its support and security pages.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "How is the private key stored? (Proton Support) ... Protect your data with zero-access encryption (Proton Security)",
   "reasoning": "Accurately summarizes the two cited Proton sources."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "4"
   ],
   "claim_text": "Signal never holds your keys: its servers are never in a position to grant access to your message history.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Signal's servers are never in a position to grant access to your message history",
   "reasoning": "Matches the 'never' framing and the server-access claim."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "4.1"
   ],
   "claim_text": "By default, message history is stored only on your device and deleted from Signal's servers after delivery.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "By default, message history is stored only on your device and deleted from Signal's servers after delivery",
   "reasoning": "Verbatim restatement of the default storage behavior."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "4.2"
   ],
   "claim_text": "Switching devices leaves you three options.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "When you want to switch devices, you have three options",
   "reasoning": "The count of three matches the source exactly."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "4.3"
   ],
   "claim_text": "Manual local backup on Android: create an encrypted backup file protected by a 30-digit passphrase, then physically transfer it to your new device.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted backup file protected by a 30-digit passphrase, then physically transfer it to your new device",
   "reasoning": "The 30-digit number and Android scope match the source."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "4.4"
   ],
   "claim_text": "Direct device-to-device transfer: both devices must be physically present and you transfer everything locally over your network.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Both devices must be physically present and you transfer everything locally over your network",
   "reasoning": "Restates option two with no altered conditions."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "4.5"
   ],
   "claim_text": "Signal Secure Backups: messages are encrypted with a 64-character recovery key that Signal never sees or has access to.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "encrypted with a 64-character recovery key that Signal never sees or has access to",
   "reasoning": "The 64-character figure and the 'never sees' negation are intact."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "4.6"
   ],
   "claim_text": "Even with the newer cloud backup feature, the recovery key stays on your device.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Even with the newer cloud backup feature, the recovery key stays on your device",
   "reasoning": "Matches the source's concession and key-location claim."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "4.6.1"
   ],
   "claim_text": "Signal literally cannot decrypt your backups even if they wanted to, and cannot help you recover them if you lose the key.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Signal literally cannot decrypt your backups even if they wanted to, and they cannot help you recover them if you lose your recovery key",
   "reasoning": "Both incapacity claims restated without change."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "4.7"
   ],
   "claim_text": "This is genuinely zero-knowledge architecture, not just marketing claims.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is genuinely zero-knowledge architecture, not just marketing claims.",
   "reasoning": "Verbatim restatement of the source's assessment."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "4.8"
   ],
   "claim_text": "Signal documents Secure Backups in a September 2024 blog post and support article.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Introducing Signal Secure Backups (Signal Blog, September 2024) ... Signal Secure Backups (Signal Support)",
   "reasoning": "The September 2024 date and both source types match the citation list."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "5"
   ],
   "claim_text": "Even trusting the encryption architecture, plaintext password storage on servers cannot be ruled out.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Even if we trust the encryption architecture, how do we know companies don't store your password in plaintext on their servers?",
   "reasoning": "Source poses exactly this open question, matching the loglog claim."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "5.1"
   ],
   "claim_text": "If they have your password and your encrypted private key, they can decrypt everything.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if they have your password and your encrypted private key, they can decrypt everything",
   "reasoning": "Verbatim restatement of the source sentence."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "5.2"
   ],
   "claim_text": "The short answer is that we do not know for certain.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The short answer: we don't know for certain.",
   "reasoning": "Identical meaning, only contraction expanded."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "5.3"
   ],
   "claim_text": "You can verify what the client does if it is open source: that passwords are hashed before transmission.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "You can verify what the client does (if it's open source) - you can confirm that passwords are hashed before transmission.",
   "reasoning": "Source states precisely this verifiable client behavior."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "5.4"
   ],
   "claim_text": "But you cannot verify what happens on the server after your password or password hash arrives; the server code is almost always closed source.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you cannot verify what happens on the server after your password (or password hash) arrives. The server code is almost always closed source",
   "reasoning": "Both the negation and the 'almost always' qualifier are preserved."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "5.5"
   ],
   "claim_text": "Even with security audits, you are trusting the server operator.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "even with security audits, you're trusting that:",
   "reasoning": "Source introduces a list of things trusted after audits; paraphrase holds."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "5.5.1"
   ],
   "claim_text": "That the audited code is what is actually running.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "The audited code is what's actually running",
   "reasoning": "Direct verbatim restatement of the bullet."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "5.5.2"
   ],
   "claim_text": "That they have not changed it since the audit.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "They haven't changed it since the audit",
   "reasoning": "Negation and meaning preserved exactly."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "5.5.3"
   ],
   "claim_text": "That no rogue employee has modified it.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "No rogue employee has modified it",
   "reasoning": "Direct restatement of the bullet."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "5.5.4"
   ],
   "claim_text": "That their infrastructure has not been breached.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Their infrastructure hasn't been breached",
   "reasoning": "Negation and content preserved."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "5.6"
   ],
   "claim_text": "Real-world examples show this is not just paranoia.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Real-world examples show this isn't just paranoia.",
   "reasoning": "Verbatim restatement, contraction expanded only."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "5.6.1"
   ],
   "claim_text": "Facebook disclosed in 2019 that they had been accidentally logging hundreds of millions of passwords in plaintext in internal logs for years.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Facebook disclosed in 2019 that they'd been \"accidentally\" logging hundreds of millions of passwords in plaintext in internal logs for years.",
   "reasoning": "Year 2019 and quantity 'hundreds of millions' preserved; only scare quotes dropped."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "5.6.2"
   ],
   "claim_text": "Adobe's 2013 breach revealed they stored password hints in plaintext.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Adobe's 2013 breach revealed they stored password hints in plaintext.",
   "reasoning": "Entity, year 2013, and detail match source exactly."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "5.6.3"
   ],
   "claim_text": "Many smaller services store passwords in plaintext or use weak hashing like MD5 without salting.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Many smaller services store passwords in plaintext or use weak hashing like MD5 without salting.",
   "reasoning": "Verbatim restatement including the 'without salting' negation."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "5.7"
   ],
   "claim_text": "For Proton specifically: resetting your password via email or SMS recovery loses access to all your old encrypted emails.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "if you reset your password via email/SMS recovery, you lose access to all your old encrypted emails",
   "reasoning": "Service, method, and consequence all match source."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "5.7.1"
   ],
   "claim_text": "That suggests they genuinely cannot decrypt your data without your password.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This suggests they genuinely can't decrypt your data without your password.",
   "reasoning": "Hedged 'suggests' retained; meaning identical."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "5.8"
   ],
   "claim_text": "But even this is not proof: they could deliberately withhold access to maintain their privacy-focused image, even if they technically could decrypt.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "But even this isn't proof - they could be deliberately not providing access to maintain their privacy-focused image, even if they technically could.",
   "reasoning": "Negation and both hedging clauses ('could') preserved."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "6"
   ],
   "claim_text": "The fundamental problem: you are trusting reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "you're trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees.",
   "reasoning": "All four trust factors and the contrast are retained."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "6.1"
   ],
   "claim_text": "Architecture matters: with WhatsApp, you are trusting Meta's entire server infrastructure.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "This is why the architecture matters so much. With WhatsApp, you're trusting Meta's entire server infrastructure.",
   "reasoning": "Entity and claim match source directly."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "6.2"
   ],
   "claim_text": "With Proton, you are trusting that they will not serve malicious code.",
   "claim_type": "interpretation",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "With Proton, you're trusting they won't serve malicious code.",
   "reasoning": "Negation and content preserved."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "6.3"
   ],
   "claim_text": "With Signal and recovery keys, the attack surface is much smaller: they would need to compromise your device or steal your recovery key.",
   "claim_type": "causal_link",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "With Signal using recovery keys, the attack surface is much smaller - they'd need to compromise your device or steal your recovery key",
   "reasoning": "Mechanism and both required attack paths match source."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7"
   ],
   "claim_text": "The comparison tables contrast key generation, key storage, new-device behavior, provider device injection, server storage, required trust, and security model.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Where encryption keys are generated ... Where private keys are stored ... What happens when you add a new device ... What you must trust ... Security model name",
   "reasoning": "Enumerated table aspects correspond to source rows; meta summary is accurate."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.1"
   ],
   "claim_text": "Can the provider add a device without your knowledge? WhatsApp yes; Proton no, but could serve malicious client code; Signal no.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "YES - WhatsApp controls device authentication ... NO - but they could serve malicious client code ... NO - they cannot authenticate a device",
   "reasoning": "All three per-service verdicts match the source table."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2"
   ],
   "claim_text": "What the server stores: WhatsApp keeps encrypted history, keys, and device-to-key mappings; Proton keeps emails and the encrypted private key; Signal keeps nothing by default.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "WhatsApp: 1. Encrypted message history 2. Encrypted encryption keys 3. Device-to-key mappings ... Signal: 1. Nothing by default",
   "reasoning": "Storage items for each service match the source table."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.3"
   ],
   "claim_text": "Security model names: server-mediated key escrow for WhatsApp, password-encrypted server-side key storage for Proton, client-controlled keys for Signal.",
   "claim_type": "definition",
   "verdict": "Supported",
   "severity": "Harmless",
   "evidence_quote": "Security model name | Server-mediated key escrow | Password-encrypted server-side key storage | Client-controlled keys",
   "reasoning": "All three labels reproduce the source table exactly."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "8"
   ],
   "claim_text": "The verification question gets its own treatment: what can and cannot be checked.",
   "claim_type": "meta",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "## How Do We Know Companies Don't Store Plaintext Passwords?",
   "reasoning": "Source devotes a section to verifying plaintext storage, then enumerates what can and cannot be verified."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "8.1"
   ],
   "claim_text": "What you can verify: open-source clients hash or encrypt passwords before sending, though this proves only what the client does.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "you can verify the client hashes/encrypts passwords before sending. But this only proves what the client does",
   "reasoning": "Source states the same scope limitation verbatim."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "8.2"
   ],
   "claim_text": "Network traffic inspection with tools like Wireshark shows what is transmitted; plaintext over the network is a red flag.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Tools like Wireshark can show what's transmitted. If passwords are sent in plaintext over the network, that's a red flag.",
   "reasoning": "Matches source exactly."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "8.2.1"
   ],
   "claim_text": "Even with HTTPS encryption, you cannot see what the server does after decryption.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "even with HTTPS encryption, you can't see what the server does after decryption",
   "reasoning": "Identical meaning, negation preserved."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "8.3"
   ],
   "claim_text": "Security audits: independent auditors can review server code if given access, but you trust the auditor and that the audited code was deployed.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Independent auditors can review server code if given access. But you're trusting the auditor and trusting the company deployed the audited code.",
   "reasoning": "Both trust conditions retained."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "8.4"
   ],
   "claim_text": "What you cannot verify: server-side code is almost always closed source, and even if shown to auditors you cannot verify it is what runs.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Server-side code: Almost always closed-source. Even if shown to auditors, you can't verify that's what's actually running.",
   "reasoning": "Qualifier 'almost always' and negation preserved."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "8.5"
   ],
   "claim_text": "Even if truthful during an audit, they could add password logging in a later update.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Even if honest during an audit, they could add password logging in a later update.",
   "reasoning": "'truthful' is an equivalent restatement of 'honest'."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "8.6"
   ],
   "claim_text": "An employee with server access could modify the code, or someone who breaches their systems could inject logging.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "an employee with server access could modify it, or someone who breaches their systems could inject logging",
   "reasoning": "Matches source; omitted lead-in condition does not alter the claim's meaning."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "8.7"
   ],
   "claim_text": "Good signs: open-source server code, independent audits with published results, and breach disclosure where passwords were not compromised.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Open-source server code ... Independent security audits ... with published results ... If breached and passwords weren't compromised",
   "reasoning": "All three good signs accurately listed with negation intact."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "8.8"
   ],
   "claim_text": "Bad signs: being able to reset a password and access old data, security through obscurity, and a history of privacy violations.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Can reset password and access old data ... Security through obscurity ... History of privacy violations",
   "reasoning": "All three bad signs match source items."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "8.9"
   ],
   "claim_text": "Facebook 2019: between 200-600 million passwords were logged in plaintext and searchable by over 20,000 Facebook employees.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "between 200-600 million passwords in plaintext ... searchable by over 20,000 Facebook employees",
   "reasoning": "Numbers, range, and entity preserved exactly."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "8.9.1"
   ],
   "claim_text": "Some archives dated back to 2012, and Facebook claimed the logging was unintentional.",
   "claim_type": "number_or_date",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "with some archives dating back to 2012. Facebook claimed this was unintentional",
   "reasoning": "Date and attribution to Facebook's claim match source."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "8.10"
   ],
   "claim_text": "Adobe 2013: the breach revealed stored password hints in plaintext, making brute-forcing easier, though at least passwords were hashed.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Adobe (2013): Breach revealed they stored password hints in plaintext, making brute-forcing easier (but at least passwords were hashed)",
   "reasoning": "Year, name, and the hashed-password caveat all preserved."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "8.11"
   ],
   "claim_text": "Many small services store passwords in plaintext or use MD5 without salt, and you find out when they get breached.",
   "claim_type": "fact",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Many small services: Store passwords in plaintext or use weak hashing (MD5 without salt)",
   "reasoning": "Matches source, including MD5-without-salt detail."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "8.12"
   ],
   "claim_text": "You are always trusting the server operator to some degree unless one of three conditions holds.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "You're always trusting the server operator to some degree unless:",
   "reasoning": "Source lists exactly three numbered conditions."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "8.12.1"
   ],
   "claim_text": "All cryptography happens client-side, like Signal with recovery keys.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "All cryptography happens client-side (like Signal with recovery keys)",
   "reasoning": "Verbatim match of condition one."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "8.12.2"
   ],
   "claim_text": "The server never sees anything that could decrypt your data, as with zero-knowledge proof systems.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "The server never sees anything that could decrypt your data (zero-knowledge proof systems)",
   "reasoning": "Verbatim match of condition two, 'never' preserved."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "8.12.3"
   ],
   "claim_text": "Server code is open-source and reproducibly built, and you can verify what is running.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Server code is open-source AND reproducibly built AND you can verify what's running",
   "reasoning": "Conjunctive conditions preserved."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "9"
   ],
   "claim_text": "The bottom line: for most commercial services you trust reputation, jurisdiction, business model, and past behavior rather than cryptographic guarantees.",
   "claim_type": "claim",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "you're trusting their reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees",
   "reasoning": "Scope 'most commercial services' and contrast retained."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "9.1"
   ],
   "claim_text": "Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware keys like YubiKey that never expose the secret.",
   "claim_type": "recommendation",
   "verdict": "Supported",
   "severity": "none",
   "evidence_quote": "Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys (like YubiKey) that never expose the secret",
   "reasoning": "Verbatim match including YubiKey example and 'never' negation."
  }
 ],
 "metrics": {
  "total_claims": 110,
  "supported": 108,
  "partially_supported": 2,
  "unverifiable": 0,
  "contradicted": 0,
  "critical_errors": 0,
  "faithfulness_precision": 0.9818
 },
 "fail_list": [
  "C005",
  "C018"
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
   "point_text": "Central thesis: E2EE means sender-device encryption and receiver-device decryption with nothing decrypting in between, but the real question is whether the provider (not merely a man-in-the-middle) can access content, and the answer is not completely clear.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L003",
    "L005",
    "L006",
    "L009"
   ],
   "evidence_quote": "Encrypting on the sender's device and decrypting on the receiver's device without decryption along the way is the definition of E2EE. ... The real question is whether Facebook can access the content of your WhatsApp messages in theory and in practice.",
   "reasoning": "L005 gives the definition, L006 notes MITM is a lesser concern, L009 states the real provider-access question, and L003 frames E2EE meaning several things. Thesis fully captured."
  },
  {
   "point_id": "K02",
   "point_text": "People usually want E2EE so no one outside sender and receivers, especially the provider, can access data. For WhatsApp this means Facebook should not read message content, though it still holds metadata: network, frequency, amount, and timing of communication.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L007",
    "L008"
   ],
   "evidence_quote": "Usually the purpose is that no one, and in particular the provider, can access the data. ... With WhatsApp, you do not want Facebook to access message content, though it still knows your network, communication frequency, amount, and times.",
   "reasoning": "L007 gives the purpose and provider focus, L008 gives the WhatsApp example with all four metadata categories intact."
  },
  {
   "point_id": "K03",
   "point_text": "WhatsApp's answer is unclear: if implemented as claimed with no secret backdoors, they cannot access data, but the app is not open source and not truly auditable, so external audits can never prove the negative.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L010",
    "L011",
    "L012",
    "L013"
   ],
   "evidence_quote": "If they implemented things as claimed and added no secret backdoors, then yes, they cannot access the data. ... External audits and tests lack certainty in the negative direction: they can never claim it cannot access the data.",
   "reasoning": "L010-L013 capture the conditional claim, the closed-source non-auditability, and the inability to prove the negative. Condition and negation preserved."
  },
  {
   "point_id": "K04",
   "point_text": "Evidence against WhatsApp/Meta: 2021 privacy policy changes allowing data sharing with Facebook for relevant offers and ads across Meta products, plus prior security failures such as plaintext storage of hundreds of millions of passwords, making it almost certain they can and do access message content.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L014",
    "L015",
    "L016"
   ],
   "evidence_quote": "The 2021 privacy policy changes allow sharing data with Facebook for relevant offers and ads across Meta company products. ... Given the company's business, you can almost be certain that they can, and do, access the messages.",
   "reasoning": "All three elements present: 2021 policy change, plaintext password failures, and the almost-certain conclusion with the qualifier preserved."
  },
  {
   "point_id": "K05",
   "point_text": "Smoking-gun test: whether a platform can back up or let you access history across devices without manually linking/transferring keys. If the provider ever holds the key it is like leaving a copy of your door key on a public billboard, letting it decrypt at will.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L017",
    "L018",
    "L023",
    "L024"
   ],
   "evidence_quote": "A smoking gun is whether the platform or app can back up your data. ... It is as if you locked your door and left a copy at the local farmers market billboard.",
   "reasoning": "L017-L018 state the test, L023-L024 preserve the billboard analogy and the at-will compromise implication."
  },
  {
   "point_id": "K06",
   "point_text": "How WhatsApp works: server stores encrypted message history and device-to-account identity mappings, authenticates new devices, and provides keys to decrypt history. This makes the server a trusted intermediary that could silently authenticate a rogue device and hide it from your device list, unlike Signal's manual key transfer.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L022",
    "L025",
    "L026",
    "L027",
    "L028",
    "L029",
    "L030"
   ],
   "evidence_quote": "the server stores encrypted message history and maintains mappings between your account and your device identities. ... they could simply hide a rogue device from your device list entirely.",
   "reasoning": "L025-L030 fully capture server storage, mappings, new-device authentication and key provision, trusted-intermediary framing, rogue-device injection and hiding, and L022 gives the Signal contrast."
  },
  {
   "point_id": "K07",
   "point_text": "Proton Mail model: private key generated in the browser and encrypted with your password using bcrypt and AES-256, then stored encrypted on Proton's servers, so the server holds only an encrypted private key.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L033",
    "L034",
    "L035"
   ],
   "evidence_quote": "your private key is generated in your browser and encrypted with your password. ... The encryption uses bcrypt and AES-256 before the key is sent to Proton's servers for storage.",
   "reasoning": "L033-L035 capture browser key generation, bcrypt + AES-256, and encrypted server-side storage. Numbers and algorithm names intact."
  },
  {
   "point_id": "K08",
   "point_text": "Proton login flow: type password, browser hashes it with bcrypt plus a server-provided salt, sends hash to authenticate, server returns the encrypted private key, and browser decrypts it locally with the actual password.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L036",
    "L037",
    "L038",
    "L039",
    "L040"
   ],
   "evidence_quote": "You type your password, and your browser hashes it with bcrypt using a salt provided by Proton's server. ... Your browser uses your original password to decrypt the private key locally.",
   "reasoning": "L036-L040 give the complete four-step flow including the server-provided salt and local decryption with the original password."
  },
  {
   "point_id": "K09",
   "point_text": "Distinction between hashing (one-way, used for authentication, cannot be reversed to the password) and encryption (two-way, used on the private key). Proton receives the hash for authentication while the key is encrypted with the actual password, so in theory the hash cannot decrypt the key.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L041",
    "L042",
    "L043",
    "L044",
    "L045"
   ],
   "evidence_quote": "Hashing is one-way ... Encryption is two-way ... the private key is encrypted with your actual password, so the hash cannot decrypt it.",
   "reasoning": "L041-L045 capture both definitions and the concluding separation that the hash cannot decrypt the key."
  },
  {
   "point_id": "K10",
   "point_text": "Proton's critical residual vulnerability: Proton could serve malicious client code (web app or update) to capture the actual password before hashing and use it to decrypt the stored key. This is why open-source clients matter, yet you must still trust the served code matches source, no future malicious injection, and no infrastructure compromise.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L046",
    "L047",
    "L048",
    "L049",
    "L050",
    "L051",
    "L052",
    "L053"
   ],
   "evidence_quote": "Proton could serve malicious client code, in the web app or through an app update. ... That they will not be compelled to inject malicious code in the future. ... That their infrastructure has not been compromised.",
   "reasoning": "All elements present: malicious code vector, password capture before hashing, decryption of stored key, value of open source, and the three residual trust assumptions."
  },
  {
   "point_id": "K11",
   "point_text": "Signal's approach: by default history is stored only on your device and deleted from servers after delivery. Device switching offers three options: manual local backup protected by a 30-digit passphrase, direct device-to-device local transfer, or Secure Backups encrypted with a 64-character recovery key Signal never sees.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L058",
    "L059",
    "L060",
    "L061",
    "L062"
   ],
   "evidence_quote": "message history is stored only on your device and deleted from Signal's servers after delivery. ... a 30-digit passphrase ... a 64-character recovery key that Signal never sees",
   "reasoning": "L058 gives device-only storage and server deletion, L059-L062 give all three device-switch options with both numbers intact."
  },
  {
   "point_id": "K12",
   "point_text": "Signal is genuinely zero-knowledge: servers are never positioned to grant access to message history, and even with cloud backups Signal cannot decrypt backups and cannot help recover them if the recovery key is lost.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L057",
    "L063",
    "L064",
    "L065"
   ],
   "evidence_quote": "Signal literally cannot decrypt your backups even if they wanted to, and cannot help you recover them if you lose the key. ... This is genuinely zero-knowledge architecture, not just marketing claims.",
   "reasoning": "L057 states servers never positioned to grant access, L063-L064 give cloud backup non-decryptability and non-recoverability, L065 names it genuine zero-knowledge."
  },
  {
   "point_id": "K13",
   "point_text": "Password storage limits: you can verify what an open-source client does (hashing before transmission), inspect network traffic, and read audits, but you cannot verify server-side code, whether it changed after an audit, rogue employees, or breaches. There is no cryptographic guarantee about server password handling.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L069",
    "L070",
    "L071",
    "L072",
    "L073",
    "L074",
    "L075",
    "L076",
    "L094",
    "L095",
    "L096",
    "L097"
   ],
   "evidence_quote": "you can verify what the client does if it is open source ... But you cannot verify what happens on the server ... No cryptographic guarantee about server password handling.",
   "reasoning": "L070-L076 and L094-L097 cover both the verifiable client side and the four unverifiable server-side risks, matching the point's scope."
  },
  {
   "point_id": "K14",
   "point_text": "Real-world examples: Facebook in 2019 logged roughly 200-600 million passwords in plaintext for years, searchable by over 20,000 employees with archives dating to 2012, claiming it was unintentional. Adobe's 2013 breach exposed plaintext password hints, many small services use plaintext or unsalted MD5. Proton's loss of old emails after an email/SMS password reset suggests genuine inability to decrypt, though not proof.",
   "weight": "Nice to have",
   "presence": "Present",
   "loglog_ids": [
    "L078",
    "L079",
    "L080",
    "L081",
    "L082",
    "L102",
    "L103",
    "L104",
    "L105"
   ],
   "evidence_quote": "between 200-600 million passwords were logged in plaintext and searchable by over 20,000 Facebook employees. ... Some archives dated back to 2012 ... Adobe's 2013 breach ... resetting your password via email or SMS recovery loses access to all your old encrypted emails.",
   "reasoning": "All examples present with full numbers: Facebook 200-600M, 20,000 employees, 2012 archives, Adobe 2013, MD5, and the Proton reset example with the not-proof caveat in L083."
  },
  {
   "point_id": "K15",
   "point_text": "Bottom line: for most commercial services you trust reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious users prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys such as YubiKey that never expose the secret.",
   "weight": "Must have",
   "presence": "Present",
   "loglog_ids": [
    "L110",
    "L111"
   ],
   "evidence_quote": "for most commercial services you trust reputation, jurisdiction, business model, and past behavior rather than cryptographic guarantees. ... hardware keys like YubiKey that never expose the secret.",
   "reasoning": "L110 and L111 together preserve the closing thesis and the full list of preferred practices including decentralized systems and YubiKey."
  }
 ],
 "metrics": {
  "total_points": 15,
  "must_have_total": 12,
  "must_have_present": 12,
  "must_have_partial": 0,
  "must_have_missing": 0,
  "overall_present": 15,
  "must_recall": 1.0,
  "overall_recall": 1.0
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
    "0"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Top-level summary carries the whole document thesis, not repeated elsewhere as one claim."
  },
  {
   "claim_id": "C002",
   "loglog_ids": [
    "1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section 1 thesis on provider access; not restated by a later single claim."
  },
  {
   "claim_id": "C003",
   "loglog_ids": [
    "1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Author disclaimer; informational context, not a filler transition or restated header."
  },
  {
   "claim_id": "C004",
   "loglog_ids": [
    "1.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Core E2EE definition, stated once."
  },
  {
   "claim_id": "C005",
   "loglog_ids": [
    "1.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Caveated MITM point; contradiction-adjacent, kept visible and distinct."
  },
  {
   "claim_id": "C006",
   "loglog_ids": [
    "1.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Specifies usual purpose; adds beyond C002."
  },
  {
   "claim_id": "C007",
   "loglog_ids": [
    "1.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Concrete WhatsApp/Facebook metadata example, not repeated."
  },
  {
   "claim_id": "C008",
   "loglog_ids": [
    "1.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Narrows the question to practice and theory; distinct from C002."
  },
  {
   "claim_id": "C009",
   "loglog_ids": [
    "2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "WhatsApp section conclusion, distinct from its supporting points."
  },
  {
   "claim_id": "C010",
   "loglog_ids": [
    "2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Conditional claim about implementation, not duplicated."
  },
  {
   "claim_id": "C011",
   "loglog_ids": [
    "2.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Closed-source auditability causal point, unique."
  },
  {
   "claim_id": "C012",
   "loglog_ids": [
    "2.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audit certainty-in-negative claim; distinct from section 8 audit points."
  },
  {
   "claim_id": "C013",
   "loglog_ids": [
    "2.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Dated 2021 policy fact, single mention."
  },
  {
   "claim_id": "C014",
   "loglog_ids": [
    "2.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "First preview of plaintext password failures; distinct framing from later examples."
  },
  {
   "claim_id": "C015",
   "loglog_ids": [
    "2.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Business-model inference, unique."
  },
  {
   "claim_id": "C016",
   "loglog_ids": [
    "2.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Backup capability as smoking gun, unique."
  },
  {
   "claim_id": "C017",
   "loglog_ids": [
    "2.7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Cross-device history access detail, distinct from C016."
  },
  {
   "claim_id": "C018",
   "loglog_ids": [
    "2.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Lock-and-key definition; partially supported, kept visible."
  },
  {
   "claim_id": "C019",
   "loglog_ids": [
    "2.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Key creation/storage fact, unique."
  },
  {
   "claim_id": "C020",
   "loglog_ids": [
    "2.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Simple-implementation key isolation claim, unique."
  },
  {
   "claim_id": "C021",
   "loglog_ids": [
    "2.10.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal key-copy example, distinct from C020."
  },
  {
   "claim_id": "C022",
   "loglog_ids": [
    "2.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Causal key-access claim; canonical for its analogy."
  },
  {
   "claim_id": "C023",
   "loglog_ids": [
    "2.11.1"
   ],
   "label": "Duplicate",
   "canonical_id": "C022",
   "reasoning": "Billboard analogy restates C022 with no new proposition."
  },
  {
   "claim_id": "C024",
   "loglog_ids": [
    "2.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "WhatsApp server-storage documentation fact, unique."
  },
  {
   "claim_id": "C025",
   "loglog_ids": [
    "2.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "New-device key provisioning fact, distinct from C024."
  },
  {
   "claim_id": "C026",
   "loglog_ids": [
    "2.14"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal contrast and trusted-intermediary framing, unique."
  },
  {
   "claim_id": "C027",
   "loglog_ids": [
    "2.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Rogue-device possibility, canonical for the table row C088."
  },
  {
   "claim_id": "C028",
   "loglog_ids": [
    "2.15.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Safeguard dependence on server reporting, unique."
  },
  {
   "claim_id": "C029",
   "loglog_ids": [
    "2.15.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hidden rogue device consequence, distinct from C028."
  },
  {
   "claim_id": "C030",
   "loglog_ids": [
    "2.16"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sourced multi-device engineering post, unique."
  },
  {
   "claim_id": "C031",
   "loglog_ids": [
    "3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton section lead and trust-shift conclusion, unique."
  },
  {
   "claim_id": "C032",
   "loglog_ids": [
    "3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Key generation/encryption fact, unique."
  },
  {
   "claim_id": "C033",
   "loglog_ids": [
    "3.1.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "bcrypt/AES-256 detail, distinct from C032."
  },
  {
   "claim_id": "C034",
   "loglog_ids": [
    "3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds not-just-original-device insight beyond the section lead C031."
  },
  {
   "claim_id": "C035",
   "loglog_ids": [
    "3.3"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Pure signpost introducing the login sequence; no independent content."
  },
  {
   "claim_id": "C036",
   "loglog_ids": [
    "3.3.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bcrypt salt login step, unique."
  },
  {
   "claim_id": "C037",
   "loglog_ids": [
    "3.3.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hashed password transmission step, unique."
  },
  {
   "claim_id": "C038",
   "loglog_ids": [
    "3.3.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Server returns encrypted key step, unique."
  },
  {
   "claim_id": "C039",
   "loglog_ids": [
    "3.3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Local decryption step, unique."
  },
  {
   "claim_id": "C040",
   "loglog_ids": [
    "3.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "One-way hashing definition, unique."
  },
  {
   "claim_id": "C041",
   "loglog_ids": [
    "3.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Hash-verification claim, distinct from C039."
  },
  {
   "claim_id": "C042",
   "loglog_ids": [
    "3.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Two-way encryption definition, unique."
  },
  {
   "claim_id": "C043",
   "loglog_ids": [
    "3.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Key encrypted with actual password, unique."
  },
  {
   "claim_id": "C044",
   "loglog_ids": [
    "3.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Security-model synthesis, distinct from C041/C043."
  },
  {
   "claim_id": "C045",
   "loglog_ids": [
    "3.9"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Malicious client-code vulnerability, unique."
  },
  {
   "claim_id": "C046",
   "loglog_ids": [
    "3.9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Password capture mechanism, distinct from C045."
  },
  {
   "claim_id": "C047",
   "loglog_ids": [
    "3.10"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Capture-plus-stored-key causal chain, unique."
  },
  {
   "claim_id": "C048",
   "loglog_ids": [
    "3.11"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Open-source client rationale, unique."
  },
  {
   "claim_id": "C049",
   "loglog_ids": [
    "3.12"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Signpost to the trust list; supplies no facts itself."
  },
  {
   "claim_id": "C050",
   "loglog_ids": [
    "3.12.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Served-code matches open source, unique."
  },
  {
   "claim_id": "C051",
   "loglog_ids": [
    "3.12.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No future compelled injection, distinct from later trust items."
  },
  {
   "claim_id": "C052",
   "loglog_ids": [
    "3.12.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Infrastructure not compromised; canonical for C075."
  },
  {
   "claim_id": "C053",
   "loglog_ids": [
    "3.13"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No usable-key access contrast, unique."
  },
  {
   "claim_id": "C054",
   "loglog_ids": [
    "3.14"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Mechanism behind the Proton/WhatsApp difference, unique."
  },
  {
   "claim_id": "C055",
   "loglog_ids": [
    "3.15"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Sourced zero-access documentation, unique."
  },
  {
   "claim_id": "C056",
   "loglog_ids": [
    "4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal section lead on key non-custody, unique."
  },
  {
   "claim_id": "C057",
   "loglog_ids": [
    "4.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Default storage/deletion fact, distinct from C056."
  },
  {
   "claim_id": "C058",
   "loglog_ids": [
    "4.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "States three options; numeric content, not trivia."
  },
  {
   "claim_id": "C059",
   "loglog_ids": [
    "4.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Android backup option with 30-digit passphrase, unique."
  },
  {
   "claim_id": "C060",
   "loglog_ids": [
    "4.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Device-to-device transfer option, unique."
  },
  {
   "claim_id": "C061",
   "loglog_ids": [
    "4.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Secure Backup 64-character key fact, unique."
  },
  {
   "claim_id": "C062",
   "loglog_ids": [
    "4.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Recovery key stays on device, distinct from C061."
  },
  {
   "claim_id": "C063",
   "loglog_ids": [
    "4.6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No-decrypt/no-recovery consequence, unique."
  },
  {
   "claim_id": "C064",
   "loglog_ids": [
    "4.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Zero-knowledge conclusion beyond marketing, unique."
  },
  {
   "claim_id": "C065",
   "loglog_ids": [
    "4.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Dated Secure Backup source, unique."
  },
  {
   "claim_id": "C066",
   "loglog_ids": [
    "5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section 5 lead on plaintext storage risk, unique."
  },
  {
   "claim_id": "C067",
   "loglog_ids": [
    "5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Password-plus-key decrypt chain, unique."
  },
  {
   "claim_id": "C068",
   "loglog_ids": [
    "5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Uncertainty conclusion, unique."
  },
  {
   "claim_id": "C069",
   "loglog_ids": [
    "5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Client verifiability claim; related to C092 but not restated verbatim."
  },
  {
   "claim_id": "C070",
   "loglog_ids": [
    "5.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Server unverifiability claim; distinct from C096's audit caveat."
  },
  {
   "claim_id": "C071",
   "loglog_ids": [
    "5.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audit-era trust claim, introduces its own four-item list."
  },
  {
   "claim_id": "C072",
   "loglog_ids": [
    "5.5.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audited code is running, distinct from C096."
  },
  {
   "claim_id": "C073",
   "loglog_ids": [
    "5.5.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No change since audit, distinct from C097."
  },
  {
   "claim_id": "C074",
   "loglog_ids": [
    "5.5.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "No rogue employee, distinct from C098's combined claim."
  },
  {
   "claim_id": "C075",
   "loglog_ids": [
    "5.5.4"
   ],
   "label": "Duplicate",
   "canonical_id": "C052",
   "reasoning": "Infrastructure not breached restates item 3.12.3 with no new content."
  },
  {
   "claim_id": "C076",
   "loglog_ids": [
    "5.6"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Lead-in to the examples; filler framing with no fact."
  },
  {
   "claim_id": "C077",
   "loglog_ids": [
    "5.6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Facebook plaintext logging; canonical for the section 8 restatement."
  },
  {
   "claim_id": "C078",
   "loglog_ids": [
    "5.6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adobe 2013 hint example; canonical for C103."
  },
  {
   "claim_id": "C079",
   "loglog_ids": [
    "5.6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Small-services weak hashing; canonical for C104."
  },
  {
   "claim_id": "C080",
   "loglog_ids": [
    "5.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton reset-loses-data fact, unique."
  },
  {
   "claim_id": "C081",
   "loglog_ids": [
    "5.7.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Inference from reset behavior, unique."
  },
  {
   "claim_id": "C082",
   "loglog_ids": [
    "5.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Counter-caveat that withholding is possible, unique."
  },
  {
   "claim_id": "C083",
   "loglog_ids": [
    "6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Section 6 trust basis; canonical for the section 9 restatement."
  },
  {
   "claim_id": "C084",
   "loglog_ids": [
    "6.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "WhatsApp infrastructure trust, unique."
  },
  {
   "claim_id": "C085",
   "loglog_ids": [
    "6.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Proton malicious-code trust, unique."
  },
  {
   "claim_id": "C086",
   "loglog_ids": [
    "6.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Signal smaller attack surface, unique."
  },
  {
   "claim_id": "C087",
   "loglog_ids": [
    "7"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated header describing the comparison tables; no new claim."
  },
  {
   "claim_id": "C088",
   "loglog_ids": [
    "7.1"
   ],
   "label": "Duplicate",
   "canonical_id": "C027",
   "reasoning": "Table row recaps the provider rogue-device point from 2.15."
  },
  {
   "claim_id": "C089",
   "loglog_ids": [
    "7.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Server-storage comparison across services, unique summary content."
  },
  {
   "claim_id": "C090",
   "loglog_ids": [
    "7.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Security-model naming, unique."
  },
  {
   "claim_id": "C091",
   "loglog_ids": [
    "8"
   ],
   "label": "Trivia",
   "canonical_id": null,
   "reasoning": "Restated header for the verification theme; no independent claim."
  },
  {
   "claim_id": "C092",
   "loglog_ids": [
    "8.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Adds client-only-proof caveat beyond C069."
  },
  {
   "claim_id": "C093",
   "loglog_ids": [
    "8.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Wireshark traffic inspection method, unique."
  },
  {
   "claim_id": "C094",
   "loglog_ids": [
    "8.2.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "HTTPS post-decryption blind spot, unique."
  },
  {
   "claim_id": "C095",
   "loglog_ids": [
    "8.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Audit trust caveats, unique."
  },
  {
   "claim_id": "C096",
   "loglog_ids": [
    "8.4"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Unverifiable server code with auditor caveat, distinct."
  },
  {
   "claim_id": "C097",
   "loglog_ids": [
    "8.5"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Later-update logging risk, unique."
  },
  {
   "claim_id": "C098",
   "loglog_ids": [
    "8.6"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Employee or breach injection, combines distinct actors."
  },
  {
   "claim_id": "C099",
   "loglog_ids": [
    "8.7"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Good-sign indicators, unique."
  },
  {
   "claim_id": "C100",
   "loglog_ids": [
    "8.8"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Bad-sign indicators, unique."
  },
  {
   "claim_id": "C101",
   "loglog_ids": [
    "8.9"
   ],
   "label": "Duplicate",
   "canonical_id": "C077",
   "reasoning": "Facebook plaintext logging recap; only adds figures to the same fact."
  },
  {
   "claim_id": "C102",
   "loglog_ids": [
    "8.9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "2012 archive and unintentional claim, new detail beyond C101."
  },
  {
   "claim_id": "C103",
   "loglog_ids": [
    "8.10"
   ],
   "label": "Duplicate",
   "canonical_id": "C078",
   "reasoning": "Adobe 2013 plaintext hints restated with brute-force note."
  },
  {
   "claim_id": "C104",
   "loglog_ids": [
    "8.11"
   ],
   "label": "Duplicate",
   "canonical_id": "C079",
   "reasoning": "Small-services plaintext/MD5 restated with breach discovery."
  },
  {
   "claim_id": "C105",
   "loglog_ids": [
    "8.12"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Frames the three-condition escape; content differs from C071."
  },
  {
   "claim_id": "C106",
   "loglog_ids": [
    "8.12.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Client-side crypto condition, unique."
  },
  {
   "claim_id": "C107",
   "loglog_ids": [
    "8.12.2"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Server-never-sees condition, unique."
  },
  {
   "claim_id": "C108",
   "loglog_ids": [
    "8.12.3"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Reproducible open-source build condition, unique."
  },
  {
   "claim_id": "C109",
   "loglog_ids": [
    "9"
   ],
   "label": "Duplicate",
   "canonical_id": "C083",
   "reasoning": "Bottom line restates the section 6 trust-basis claim nearly verbatim."
  },
  {
   "claim_id": "C110",
   "loglog_ids": [
    "9.1"
   ],
   "label": "Unique",
   "canonical_id": null,
   "reasoning": "Recommendation list for security-conscious users, unique."
  }
 ],
 "metrics": {
  "scored_claims": 110,
  "unique": 98,
  "duplicates": 7,
  "trivia": 5,
  "redundancy_rate": 0.0636,
  "trivia_rate": 0.0455,
  "structured_tokens": 1900,
  "tokens_per_unique_claim": 19.4
 },
 "prune_list": [
  "C023 duplicates C022 (billboard analogy adds no proposition), safe to merge",
  "C075 duplicates C052 (infrastructure-not-breached item repeated), safe to merge",
  "C088 duplicates C027 (table row recaps rogue-device point), safe to merge",
  "C101 duplicates C077 (Facebook plaintext logging restated), safe to merge",
  "C103 duplicates C078 (Adobe 2013 hints restated), safe to merge",
  "C104 duplicates C079 (small-services MD5 restated), safe to merge",
  "C109 duplicates C083 (bottom line restates fundamental problem), safe to merge",
  "C035 trivia (login-sequence signpost), cut",
  "C049 trivia (you-must-trust signpost), cut",
  "C076 trivia (lead-in to real-world examples), cut",
  "C087 trivia (restated header for comparison tables), cut",
  "C091 trivia (restated header for verification section), cut"
 ]
}
```

## Judge Top (overall), opencode-go/deepseek-v4.1-flash

```json
{
 "judge": "overall",
 "judge_version": "1.0.0",
 "model": "deepseek-v4.1-flash 2026-09-15",
 "source_id": "unspecified",
 "inputs": {
  "faithfulness_precision": 0.9818,
  "critical_errors": 0,
  "must_recall": 1.0,
  "overall_recall": 1.0,
  "redundancy_rate": 0.0636,
  "trivia_rate": 0.0455
 },
 "weights_used": {
  "faithfulness_precision": 0.4,
  "coverage_must_recall": 0.4,
  "redundancy_penalty": 0.2
 },
 "computation": "weighted score = 0.4 * faithfulness_precision + 0.4 * must_recall - 0.2 * redundancy_rate = 0.4 * 0.9818 + 0.4 * 1.0 - 0.2 * 0.0636 = 0.39272 + 0.4 - 0.01272 = 0.78",
 "weighted_score": 0.78,
 "verdict": "Borderline",
 "tradeoff_note": "Coverage is maximal (must_recall 1.0, overall_recall 1.0) and redundancy (0.0636) sits well below the 0.15 max, so the extra length is justified by coverage with no concision penalty. The numbers pass every gate, but two Partial claims sit on core definitional/interpretive points, so human review is advised.",
 "fix_list": [
  "Fix C005 (loglog 1.3): restore the source hedge, change 'defeat a man-in-the-middle attack' back to 'will not likely compromise your data' and drop 'only', so the probabilistic qualifier survives.",
  "Fix C018 (loglog 2.8): frame the encryption statement as the author's model with the source hedge 'usually a pair of keys' instead of asserting it as a flat definition.",
  "Prune the seven duplication pairs (C023/C022, C075/C052, C088/C027, C101/C077, C103/C078, C104/C079, C109/C083) and the five trivia signposts/headers (C035, C049, C076, C087, C091) to push redundancy (0.0636) and trivia (0.0455) further down."
 ],
 "reasoning": "Gate checks per config pass_gates. Hard fail 1: critical_contradicted_max is 0 and faithfulness reports contradicted = 0 and critical_errors = 0, so no Critical error and no hard fail. Hard fail 2: must_recall_min is 0.9 and coverage reports must_recall = 1.0 (12 of 12 must-have points present, must_have_missing = 0), so this gate passes. Hard fail 3: faithfulness_precision_min is 0.95 and faithfulness_precision = 0.9818 (108 fully supported of 110 claims, 2 partially supported, 0 contradicted, 0 unverifiable), so this gate passes. Concision gate: redundancy_max is 0.15 and redundancy_rate = 0.0636, well under the cap, so length is not penalized beyond the weighted term. All three hard gates pass, so the sample is not a Fail. Weighted score: 0.4 * 0.9818 = 0.39272 for faithfulness, 0.4 * 1.0 = 0.4 for coverage, minus 0.2 * 0.0636 = 0.01272 for redundancy, giving 0.39272 + 0.4 - 0.01272 = 0.78. Applying the Borderline rule: gates are met on numbers, but two Partial claims, C005 (loglog 1.3, MITM threat model strengthened from 'not likely compromise' to 'defeat' with an added 'only') and C018 (loglog 2.8, encryption key model asserted as a flat definition instead of the author's hedged model with 'usually a pair of keys'), both concern core conceptual points that plausibly belong to the must-have set. Because a Partial claim touches must-have substance, I mark Borderline and name C005 and C018 rather than a clean Pass. On tradeoff, concision neither rescues nor undermines anything here: coverage is saturated (1.0/1.0) and redundancy is below max, so the length cost is justified purely by coverage gain. Highest-leverage fixes are the two Partial rewrites, since they are the only obstacles between this sample and an unambiguous Pass."
}
```
