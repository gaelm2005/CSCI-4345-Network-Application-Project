import socket
from colorama import init, Fore
from scapy.all import ARP, Ether, srp
from threading import Thread

# Initialize colors
init()
GREEN = Fore.GREEN
RESET = Fore.RESET
GRAY = Fore.LIGHTBLACK_EX

def discover_hosts(ip_range):
    """
    Uses Scapy to perform an ARP ping to discover active IPs on the network.
    """
    print(f"[*] Discovering active hosts on {ip_range}...")
    active_ips = []
    
    # Create ARP packet
    arp = ARP(pdst=ip_range)
    # Create the Ether broadcast packet
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    # Stack them
    packet = ether/arp

    # Send the packet and receive responses
    result = srp(packet, timeout=3, verbose=0)[0]

    # Parse the responses to grab the IP addresses
    for sent, received in result:
        active_ips.append(received.psrc)
        
    return active_ips

def is_port_open(host, port):
    """
    Determine whether `host` has the `port` open.
    """
    s = socket.socket()
    s.settimeout(0.5) # Added timeout to speed up the scan significantly
    try:
        s.connect((host, port))
    except:
        return False
    else:
        s.close() # Always close the socket after opening it
        return True

def scan_ports(target_ip, max_port=1024):
    """
    Scans a given IP address for open ports.
    """
    print(f"\n[*] Commencing port scan on {target_ip}")
    for port in range(1, max_port + 1):
        if is_port_open(target_ip, port):
            print(f"{GREEN}[+] {target_ip}:{port} is open      {RESET}")
        else:
            # Using \r overwrites the line so the console doesn't get flooded
            print(f"{GRAY}[!] {target_ip}:{port} is closed    {RESET}", end="\r")
    
    # Clear the lingering closed port message
    print(" " * 50, end="\r")

if __name__ == "__main__":
    # 1. Define your local subnet (e.g., 192.168.1.0/24)
    # Be sure to change this to match your actual local network!
    subnet = input("Enter the subnet to scan (e.g., 192.168.1.0/24): ")
    
    # 2. Run the discovery phase
    found_hosts = discover_hosts(subnet)
    
    if not found_hosts:
        print("[-] No hosts discovered. Exiting.")
    else:
        print(f"[+] Discovered {len(found_hosts)} hosts: {found_hosts}")
        
        # 3. Iterate through discovered hosts and run the port scanner
        for host in found_hosts:
            scan_ports(host, max_port=100) # Kept to 100 for testing speed
            
        print("\n[*] Automated scanning complete.")