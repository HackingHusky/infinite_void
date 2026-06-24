import argparse
import sys
from ldap3 import Server, Connection, ALL, NTLM

# --- Gojo's Aesthetic Palette (Six Eyes Azure & Limitless Purple) ---
SIX_EYES_BLUE = "\033[38;5;39m"    # Brilliant Azure Blue
LIMITLESS_PURPLE = "\033[38;5;129m" # Bright Royal Purple
VOID_BLACK = "\033[38;5;236m"       # Deep Blindfold Gray
INFINITY_WHITE = "\033[38;5;255m"   # Stark White Hair
RESET = "\033[0m"
BOLD = "\033[1m"

def print_banner():
    print(f"""{SIX_EYES_BLUE}{BOLD}
    ┌────────────────────────────────────────────────────────┐
    │  [🫸🔴🫷🔵]  DOMAIN EXPANSION: INFINITE VOID             │
    │      "Paralyze the Domain with Absolute Perception"    │
    └────────────────────────────────────────────────────────┘{RESET}""")

def parse_args():
    parser = argparse.ArgumentParser(description="Gojo's Infinite Void: AD Object Isolation Tool")
    parser.add_argument("-d", "--domain", required=True, help="Domain (e.g., corp.local)")
    parser.add_argument("-u", "--user", required=True, help="Username")
    
    # Credential inputs
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-p", "--password", help="Plaintext password for authentication")
    group.add_argument("-H", "--hash", help="NTLM hash for Pass-the-Hash authentication (LM:NT or just NT)")
    
    parser.add_argument("-dc", "--dc-ip", required=True, help="Domain Controller IP")
    return parser.parse_args()

def convert_domain_to_dn(domain):
    return ",".join([f"DC={part}" for part in domain.split(".")])

def format_nthash_for_ldap(ntlm_hash):
    """Formats the hash correctly for the ldap3 library backend."""
    if ":" in ntlm_hash:
        lm, nt = ntlm_hash.split(":")
        return f"{lm}:{nt}".lower()
    else:
        # Pad empty LM side if only NT hash is given
        return f"00000000000000000000000000000000:{ntlm_hash}".lower()

def main():
    print_banner()
    args = parse_args()
    
    base_dn = convert_domain_to_dn(args.domain)
    # Reformat domain name to short NetBIOS format for NTLM authentication mapping
    netbios_domain = args.domain.split('.')[0].upper()
    user_dn = f"{netbios_domain}\\{args.user}"
    
    print(f"{VOID_BLACK}[*] Six Eyes active. Target mapped at {args.dc_ip}...{RESET}")
    server = Server(args.dc_ip, get_info=ALL)
    
    # Handle the catalytic component (Hash vs Pass)
    if args.hash:
        auth_secret = format_nthash_for_ldap(args.hash)
        print(f"{VOID_BLACK}[*] Processing NTLM string format...{RESET}")
    else:
        auth_secret = args.password

    try:
        conn = Connection(server, user=user_dn, password=auth_secret, authentication=NTLM, auto_bind=True)
        print(f"{LIMITLESS_PURPLE}[+] Domain Expansion: Muryokusho! The target is frozen in place.{RESET}\n")
    except Exception as e:
        print(f"{SIX_EYES_BLUE}[!] Domain Expansion collapsed! Connection broke: {e}{RESET}")
        sys.exit(1)

    # --- 1. THE SIX EYES: Isolating Domain Admins ---
    print(f"{SIX_EYES_BLUE}{BOLD}=== TECHNIQUE: THE SIX EYES (Domain Administrators) ==={RESET}")
    conn.search(
        search_base=base_dn,
        search_filter="(&(objectCategory=group)(samAccountName=Domain Admins))",
        attributes=["member"]
    )
    
    print("| Elevated Member DistinguishedName | Perception Status |")
    print("| --- | --- |")
    if conn.entries:
        members = conn.entries[0].member
        if isinstance(members, str):
            members = [members]
        for member in members:
            print(f"| {member} | Directly Isolated |")
    else:
        print("| [!] No explicit 'Domain Admins' mapping found | - |")

    # --- 2. BLUE: Pulling out Kerberoastable Targets ---
    print(f"\n{SIX_EYES_BLUE}{BOLD}=== TECHNIQUE: LAPSE BLUE (Kerberoastable Accounts) ==={RESET}")
    conn.search(
        search_base=base_dn,
        search_filter="(&(objectCategory=person)(objectClass=user)(servicePrincipalName=*))",
        attributes=["samAccountName", "servicePrincipalName", "description"]
    )
    
    print("| SamAccountName | ServicePrincipalName | Description |")
    print("| --- | --- | --- |")
    for entry in conn.entries:
        print(f"| {entry.samAccountName} | {entry.servicePrincipalName} | {entry.description} |")
    
    # --- 3. RED: Blasting out AS-REP Roastable Targets ---
    print(f"\n{LIMITLESS_PURPLE}{BOLD}=== TECHNIQUE: REVERSAL RED (AS-REP Roastable Accounts) ==={RESET}")
    # 4194304 flags accounts where DONT_REQ_PREAUTH is true
    conn.search(
        search_base=base_dn,
        search_filter="(&(objectCategory=person)(objectClass=user)(userAccountControl:1.2.840.113556.1.4.803:=4194304))",
        attributes=["samAccountName", "description"]
    )
    
    print("| SamAccountName | Description | Pre-Auth Status |")
    print("| --- | --- | --- |")
    for entry in conn.entries:
        print(f"| {entry.samAccountName} | {entry.description} | Pre-Auth Stripped |")

    # --- 4. HOLLOW PURPLE: Stripping Out Plaintext Description Passwords ---
    print(f"\n{LIMITLESS_PURPLE}{BOLD}=== TECHNIQUE: HOLLOW PURPLE (Exposing Password Leaks) ==={RESET}")
    conn.search(
        search_base=base_dn,
        search_filter="(&(objectCategory=person)(objectClass=user)(description=*pass*))",
        attributes=["samAccountName", "description"]
    )
    
    print("| Target Account | Exposed Cleartext Information |")
    print("| --- | --- |")
    for entry in conn.entries:
        print(f"| {entry.samAccountName} | {entry.description} |")

    print(f"\n{INFINITY_WHITE}[*] Information flood finished. Lowering domain barrier.{RESET}")
    conn.unbind()

if __name__ == "__main__":
    main()
