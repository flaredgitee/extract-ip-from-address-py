# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Extract IP from an address string."""

import re
import sys
import argparse


def extract_ip_from_address(address: str) -> str:
    """
    Extract the IP part from an address which may include a port.

    Supported forms:
    - IPv4 with optional port: "192.168.1.1:8080" or "192.168.1.1"
    - IPv6 with brackets and optional port: "[2001:db8::1]:8080" or "[2001:db8::1]"
    - Plain IPv6 without brackets: "2001:db8::1"

    If the input doesn't match known patterns, the original string is returned.
    """
    address = address.strip()

    # Match bracketed IPv6, with optional port: [ipv6] or [ipv6]:port
    m = re.match(r"^\[(?P<ip>[^\]]+)\](?::\d+)?$", address)
    if m:
        return m.group("ip")

    # Match IPv4 with optional port: 1.2.3.4 or 1.2.3.4:8080
    m = re.match(r"^(?P<ip>(?:\d{1,3}\.){3}\d{1,3})(?::\d+)?$", address)
    if m:
        return m.group("ip")

    # Match plain IPv6 without brackets (no port support without brackets)
    m = re.match(r"^(?P<ip>[0-9A-Fa-f:]+)$", address)
    if m:
        return m.group("ip")

    # Fallback to returning the original string unchanged
    return address


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Extract IP from an 'ip:port' like address string."
    )

    try:
        address = sys.stdin.readline().strip()
        result = extract_ip_from_address(address)
        print(result)
    except Exception as e:
        # Print a helpful error to stderr and show usage
        print(
            f"Error processing '{address}' - {type(e).__name__} - {e}", file=sys.stderr
        )
        print()
        parser.print_help()
        return 1
    else:
        return 0


if __name__ == "__main__":
    sys.exit(main())
