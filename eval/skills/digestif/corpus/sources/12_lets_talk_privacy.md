---
tags: privacy, computer science
---
# Let's Talk Privacy

[This came out of a conversation with Omid. DISCLAIMER: I'm not a security expert and most of how these things work are out of my ballpark. This is an attempt to understand this as an end user.]

## What Does "End-to-End Encryption" Really Mean?

When a company talks about "end-to-end encryption" (E2EE) they could mean several things in practical terms. The fact that data is encrypted "on sender's device" and then decrypted "on receiver's device" without it ever being decrypted along the way is in fact the definition of it. But we need to remember what is the purpose of this. If the purpose is that a man-in-the-middle attack will not likely compromise your data, then most implementations of this should be good enough. But usually that is not the main purpose when people need/want E2EE. In general one wants E2EE so that "no one" can access the data outside the sender and receivers, and in particular "the provider". That is if you're using WhatsApp, you don't want Facebook as a company to have access to the content of your messages. They still have a lot of information they can use to interpret things, e.g. they know your network, the frequency and amount of communication, times of communication etc. Any ways, the real question is that in theory, and in practice, can Facebook access the content of your WhatsApp messages or not. 

The answer is not completely clear. In short, if they have implemented the things in the way they "claim" they have, and if they haven't implemented other backdoors that they have kept secret, then yes, they "can't" access that data. But we won't really know because the app is not open source, and hence not really auditable. The external audits and tests will lack any certainty in the "negative" direction. That is, they can never claim it can't access those data. In reality, when you think about what the company's business is, their [2021 privacy policy changes](https://www.whatsapp.com/legal/privacy-policy) that allow sharing data with Facebook for ["showing relevant offers and ads across the Meta Company Products"](https://www.macrumors.com/2021/01/06/whatsapp-privacy-policy-data-sharing-facebook/), and [previous security failures like storing hundreds of millions of passwords in plaintext](https://about.fb.com/news/2019/03/keeping-passwords-secure/), you can almost be certain that they can, and they do access them.

### The Smoking Gun: Multi-Device Access Without Manual Key Transfer

For me, a smoking gun is whether the platform/app is able to "backup" your data. Whether you can access your history across devices without "manually" linking them somehow. I think of encryption as locking something and having a key (usually a pair of keys, the one that only locks it and everyone has that, and a master key that only the receiver of the data has it and can unlock it). Now, let's say you have master key on your phone for your WhatsApp (this is by default the case when you create an account the key is created and stored on your phone). Then you might go to another device and log-in again with the same credentials. In a simple implementation, there shouldn't be a way for that other device to have the same master key and decrypt your past messages. This is what happens in Signal. What you need to do is to somehow copy the key from your original device to your new device. Now, there are a lot of ways you could do this, but if at any time, Facebook has access to it, it is as if you've locked your door and left a copy at the local farmers market billboard. They can take the key and decrypt any/all of your messages whenever they want.

### How WhatsApp Actually Works

So what does WhatsApp do? According to their [official documentation](https://engineering.fb.com/2021/07/14/security/whatsapp-multi-device/), the server stores encrypted message history and maintains mappings between your account and all your device identities. When you add a new device, the server authenticates it and provides it with the keys needed to decrypt your message history. This is fundamentally different from Signal's approach - the server is a trusted intermediary that controls access to your encryption keys. While the keys themselves are encrypted, the server orchestrates who gets access to them. This means WhatsApp (Meta) *could* theoretically authenticate a "device" that isn't actually yours and give it access to decrypt your messages. Their claimed safeguards (device lists you can check, security codes you can verify) all depend on the server honestly reporting what devices exist - but since they control that server, they could simply hide a rogue device from your device list entirely.

### How Proton Mail Handles This

Proton Mail takes a different approach, though it still requires some trust. When you create a Proton account, your private key is generated in your browser, then encrypted with your password using bcrypt and AES-256 before being sent to their servers for storage. This is a crucial point: **your encrypted private key lives on Proton's servers**, not just on your original device.

When you log in on a new device or browser, here's what happens:

1. You type your password
2. Your browser hashes the password using bcrypt (with a salt provided by Proton's server)
3. This hashed password is sent to Proton to authenticate you (prove you know the password)
4. The server sends your **encrypted private key** back to your browser
5. Your browser uses your original password to decrypt this private key locally
6. Now you can read your emails

It's important to understand that hashing and encryption are different operations:

- **Hashing** (used for authentication): A one-way function. You can turn a password into a hash, but you theoretically cannot reverse a hash back into the password. Proton receives your hashed password to verify you are who you claim to be, but this hash alone shouldn't let them figure out your actual password.

- **Encryption** (used for your private key): A two-way function. You encrypt data with a key, and you can decrypt it back using that same key (or a paired key). Your private key is encrypted with your actual password (not the hash), so it can be decrypted when you provide the password again.

The security model here is: Proton receives your *hashed* password for authentication, but your private key is encrypted with your *actual* password. So in theory, even though they see your hashed password, they can't use that hash to decrypt your encrypted private key.

**However**, there's still a critical vulnerability: Proton could serve you malicious client code (either in the web app or through an app update) that captures your actual password when you type it - before it gets hashed. Since they already store your encrypted private key on their servers, if they capture your password, they can decrypt it. 

This is why having open-source clients matters - the community can verify that the client isn't doing anything malicious. But you still have to trust that:
- The code they're actually serving matches the open-source code
- They won't be compelled to inject malicious code in the future
- Their infrastructure hasn't been compromised by someone else who could serve malicious code

The crucial difference from WhatsApp is that Proton doesn't have direct access to your encryption keys in a form they can use - they'd need to actively compromise the client to steal your password first. WhatsApp's architecture doesn't even require that step; the server can directly grant key access to any device it authenticates.

### The Signal Difference

Signal takes the most privacy-preserving approach. By default, message history is stored only on your device and deleted from Signal's servers after delivery. When you want to switch devices, you have three options:

1. **Manual local backup (Android):** You create an encrypted backup file protected by a 30-digit passphrase, then physically transfer it to your new device
2. **Direct device-to-device transfer:** Both devices must be physically present and you transfer everything locally over your network
3. **Signal Secure Backups (newer):** Your messages are encrypted with a 64-character recovery key that Signal never sees or has access to

The critical architectural difference is that Signal's servers are never in a position to grant access to your message history. Even with the newer cloud backup feature, the recovery key stays on your device - Signal literally cannot decrypt your backups even if they wanted to, and they cannot help you recover them if you lose your recovery key. This is genuinely zero-knowledge architecture, not just marketing claims.

### The Password Storage Question

But there's another layer to this. Even if we trust the encryption architecture, how do we know companies don't store your password in plaintext on their servers? After all, if they have your password and your encrypted private key, they can decrypt everything.

The short answer: we don't know for certain. You can verify what the client does (if it's open source) - you can confirm that passwords are hashed before transmission. But you cannot verify what happens on the server after your password (or password hash) arrives. The server code is almost always closed source, and even with security audits, you're trusting that:

- The audited code is what's actually running
- They haven't changed it since the audit
- No rogue employee has modified it
- Their infrastructure hasn't been breached

Real-world examples show this isn't just paranoia. Facebook disclosed in 2019 that they'd been "accidentally" logging hundreds of millions of passwords in plaintext in internal logs for years. Adobe's 2013 breach revealed they stored password hints in plaintext. Many smaller services store passwords in plaintext or use weak hashing like MD5 without salting.

For Proton Mail specifically, there's additional evidence: if you reset your password via email/SMS recovery, you lose access to all your old encrypted emails. This suggests they genuinely can't decrypt your data without your password. But even this isn't proof - they could be deliberately not providing access to maintain their privacy-focused image, even if they technically could.

The fundamental problem remains: **you're trusting the company's reputation, jurisdiction, business model, and past behavior rather than having cryptographically verifiable guarantees.**

This is why the architecture matters so much. With WhatsApp, you're trusting Meta's entire server infrastructure. With Proton, you're trusting they won't serve malicious code. With Signal using recovery keys, the attack surface is much smaller - they'd need to compromise your device or steal your recovery key, which they never see.

---

## Detailed Comparison

| Aspect | WhatsApp | Proton Mail | Signal |
|--------|----------|-------------|--------|
| **Where encryption keys are generated** | On your device | On your device (in browser) | On your device |
| **Where private keys are stored** | Encrypted on WhatsApp's servers, encrypted with keys that the server can provide to authenticated devices | Encrypted on Proton's servers, encrypted with your password (server has encrypted version only) | Only on your device(s), OR encrypted with your recovery key that Signal never sees |
| **What happens when you add a new device** | Server authenticates your device → server provides it with keys to decrypt message history stored on server | You enter password → server sends encrypted private key → your browser decrypts it locally with your password | You either:<br>1. Physically transfer backup file + 30-digit passphrase, OR<br>2. Use 64-char recovery key that Signal never has access to, OR<br>3. Direct device-to-device transfer |
| **Can the service provider add a device without your knowledge?** | **YES** - WhatsApp controls device authentication and can silently add a device to your account and give it decryption keys | **NO** - but they could serve malicious client code to capture your password when you type it, then use that to decrypt your stored private key | **NO** - they cannot authenticate a device without either your recovery key or physical access to an existing device |
| **What the server stores** | 1. Encrypted message history<br>2. Encrypted encryption keys<br>3. Device-to-key mappings | 1. All your encrypted emails<br>2. Your encrypted private key | 1. Nothing by default (messages deleted after delivery)<br>2. With Secure Backups enabled: encrypted backup that only your recovery key can decrypt |
| **What you must trust** | 1. Meta won't abuse server control to add rogue devices<br>2. Meta's implementation is secure<br>3. Meta won't comply with government demands to add devices<br>4. Users will actually check their device list | 1. Proton won't serve malicious client code to steal your password<br>2. Open-source code matches what they actually serve<br>3. Swiss jurisdiction protects them from compelled backdoors | 1. You won't lose your recovery key/passphrase<br>2. Signal's implementation is secure<br>3. (Much less trust required overall) |
| **Security model name** | **Server-mediated key escrow** | **Password-encrypted server-side key storage** | **Client-controlled keys** (with optional encrypted cloud backup) |
| **The critical architectural difference** | Server is a trusted intermediary that controls access to your encryption keys | Server stores your encrypted key but theoretically can't decrypt it without compromising the client to steal your password | Server is minimally involved; you control keys directly |

---

## How Do We Know Companies Don't Store Plaintext Passwords?

**Short answer: We don't know for certain.**

### What We CAN Verify:

- **Open-source clients:** If client code is open-source (like Signal, Proton), you can verify the client hashes/encrypts passwords before sending. But this only proves what the client does, not what the server does.

- **Network traffic inspection:** Tools like Wireshark can show what's transmitted. If passwords are sent in plaintext over the network, that's a red flag. But even with HTTPS encryption, you can't see what the server does after decryption.

- **Security audits:** Independent auditors can review server code if given access. But you're trusting the auditor and trusting the company deployed the audited code.

### What We CANNOT Verify:

- **Server-side code:** Almost always closed-source. Even if shown to auditors, you can't verify that's what's actually running.

- **Whether they changed it later:** Even if honest during an audit, they could add password logging in a later update.

- **Rogue employees or breaches:** Even if official code doesn't log passwords, an employee with server access could modify it, or someone who breaches their systems could inject logging.

### Evidence to Look For:

#### Good Signs:

- **Open-source server code:** Rare, but some services do this
- **Independent security audits:** Third-party audits of password handling with published results
- **Breach disclosure:** If breached and passwords weren't compromised, that's evidence of proper hashing

#### Bad Signs:

- **Can reset password and access old data:** Suggests they have your encryption keys, which might mean they can store passwords too
- **Security through obscurity:** Not publishing their security model
- **History of privacy violations:** Past behavior predicting future behavior

### Real-World Examples:

- **Adobe (2013):** Breach revealed they stored password hints in plaintext, making brute-forcing easier (but at least passwords were hashed) - [Source](https://en.wikipedia.org/wiki/2013_Adobe_Systems_data_breach)

- **Facebook (2019):** Discovered they'd been logging [between 200-600 million passwords in plaintext](https://krebsonsecurity.com/2019/03/facebook-stored-hundreds-of-millions-of-user-passwords-in-plain-text-for-years/) in internal logs for years, searchable by over 20,000 Facebook employees, with some archives dating back to 2012. Facebook [claimed this was unintentional](https://about.fb.com/news/2019/03/keeping-passwords-secure/) and found no evidence of abuse.

- **Many small services:** Store passwords in plaintext or use weak hashing (MD5 without salt) - you find out when they get breached

### The Fundamental Problem:

You're always trusting the server operator to some degree unless:

1. All cryptography happens client-side (like Signal with recovery keys)
2. The server never sees anything that could decrypt your data (zero-knowledge proof systems)
3. Server code is open-source AND reproducibly built AND you can verify what's running

### Applied to Our Three Services:

| Service | What You Must Trust |
|---------|---------------------|
| **WhatsApp** | Meta's entire server infrastructure, their password handling, their response to government requests, their security against breaches |
| **Proton Mail** | They hash your password properly before checking it, they don't log it before hashing, their infrastructure isn't compromised. However, they could theoretically serve malicious client code to capture your password when you type it. |
| **Signal** | Much less trust required. With recovery keys, Signal never has access to decrypt your backups. You must trust their implementation is secure and you won't lose your recovery key. |

---

## Bottom Line

For most commercial services, you're trusting their reputation, jurisdiction, business model, and past behavior rather than cryptographically verifiable guarantees. Security-conscious people prefer client-side encryption, open-source everything, decentralized systems that minimize trust, and hardware security keys (like YubiKey) that never expose the secret.

---

## Sources

### WhatsApp
- [How WhatsApp enables multi-device capability](https://engineering.fb.com/2021/07/14/security/whatsapp-multi-device/) (Engineering at Meta, July 2021)

### Proton Mail
- [How is the private key stored?](https://proton.me/support/how-is-the-private-key-stored) (Proton Support)
- [Protect your data with zero-access encryption](https://proton.me/security/zero-access-encryption) (Proton Security)

### Signal
- [Introducing Signal Secure Backups](https://signal.org/blog/introducing-secure-backups/) (Signal Blog, September 2024)
- [Signal Secure Backups](https://support.signal.org/hc/en-us/articles/9708267671322-Signal-Secure-Backups) (Signal Support)