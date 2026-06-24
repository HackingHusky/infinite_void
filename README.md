# Domain Expansion: Infinite Void (infinite_void.py)
<img width="1376" height="768" alt="image" src="https://github.com/user-attachments/assets/cb0a22cb-8609-471f-8e89-d57761ef33b0" />

An ultra-fast, lightweight Active Directory object dumper forged with the absolute perception of Gojo Satoru. Designed specifically for the AD segments of **CPTS** and **OSCP**, this tool utilizes the `ldap3` engine to freeze a Domain Controller and strip it of all high-value targets instantly—bypassing the need for heavy, lagging third-party ingestion frameworks.



## ⚡ Sorcery Features

*   **The Six Eyes (Domain Admins)**: Instantly forces the Domain Controller to expose its absolute core leadership hierarchy (`Domain Admins`).
*   **Lapse Blue (Kerberoasting)**: Uses gravitational pull to drag hidden user accounts mapped to a Service Principal Name (`servicePrincipalName`) straight out of concealment.
*   **Reversal Red (AS-REP Roasting)**: Blasts away defensive parameters by isolating accounts configured with pre-authentication explicitly disabled (`DONT_REQ_PREAUTH`).
*   **Hollow Purple (Password Harvesting)**: Completely obliterates corporate OPSEC by parsing object "Description" fields for leaked plaintext administrative passwords.
*   **Infinite Information Flood**: Outputs everything cleanly into standardized Markdown tables so you can instantly copy-paste data blocks straight into your exam notes or final report.

## 🛠️ Prerequisites

Unleash the tool by installing the pure-Python LDAP client library:

```bash
pip install ldap3
```

## 🚀 Usage

```bash
python infinite_void.py -d <DOMAIN> -u <USER> [-p <PASSWORD> | -H <NTLM_HASH>] -dc <DC_IP>
```

### Options
*   `-d`, `--domain` : The fully qualified domain name (e.g., `jutsu.local`)
*   `-u`, `--user` : Compromised domain username acting as your foothold
*   `-p`, `--password` : Plaintext password for authentication (Mutually exclusive with `-H`)
*   `-H`, `--hash` : NTLM hash for native Pass-the-Hash authentication (Supports `LM:NT` or just `NT`)
*   `-dc`, `--dc-ip` : Target IP address of the Domain Controller

---

## 🎯 Domain Execution Examples

### The Standard Path (Plaintext Password)
```bash
python infinite_void.py -d jutsu.local -u megumi -p 'Shadows123!' -dc 10.10.11.200
```

### The Sovereign Path (Pass-the-Hash)
Provide just the NT hash side alone—the script automatically calculates and pads the backend abstraction layout:
```bash
python infinite_void.py -d jutsu.local -u satoru -H 31d6cfe0d16ae931b73c59d7e0c089c0 -dc 10.10.11.200
```

---
*Disclaimer: Created exclusively for authorized penetration testing, Active Directory security audits, and educational CTF structures. Don't worry, I'm the strongest.*
