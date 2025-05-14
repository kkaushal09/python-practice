import string

def is_valid_ipv4(ip):
    parts = ip.split('.')
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit():
            return False
        if part.startswith('0') and len(part) > 1:
            return False
        num = int(part)
        if num < 0 or num > 255:
            return False
    return True

def is_valid_ipv6(ip):
    parts = ip.split(':')
    if len(parts) != 8:
        return False
    # hex_digits = set(string.hexdigits)  # 0-9, a-f, A-F
    hex_digits = set("0123456789abcdefABCDEF")
    for part in parts:
        if len(part) == 0 or len(part) > 4:
            return False
        if not all(char in hex_digits for char in part):
            return False
    return True

def validate_ip_address(ip):
    if is_valid_ipv4(ip):
        return "Valid IPv4 address"
    elif is_valid_ipv6(ip):
        return "Valid IPv6 address"
    else:
        return "Invalid IP address"

# Input size and IP addresses
size = int(input("Enter the number of IP addresses: "))
ips = []

# Collect IP addresses
for i in range(size):
    ip = input(f"Enter IP address {i+1}: ")
    ips.append(ip)

# Validate each IP address
for ip in ips:
    print(f"{ip}: {validate_ip_address(ip)}")
