# Extract IP From Address

A really simple Python CLI utility to extract the IP portion from address strings that may include ports. Supports IPv4 and IPv6 (bracketed) formats.

## Quick Start

### **Run from stdin**: echo an address and pipe to the script

```shell
echo "192.168.1.1:8080" | uv run src/extract_ip_from_address/app.py
```

### Build & Install with *astral-uv*

```shell
uv tool install -e .
```

## Function

- `extract_ip_from_address(address: str) -> str`: returns the extracted IP portion for inputs like `192.168.1.1:8080`, `[2001:db8::1]:8080`, `[2001:db8::1]`, or `2001:db8::1`. If the input does not match known patterns, the input is returned unchanged.

### Notes & Edge Cases

- Bracketed IPv6 with port (`[ipv6]:port`) is supported and returns the IPv6 without brackets.
- Plain IPv6 without brackets is supported only when there is no trailing port (e.g. `2001:db8::1`).
- IPv4 with numeric port (`x.x.x.x:port`) is supported. Non-numeric ports are left unchanged.

### License

Apache-2.0
