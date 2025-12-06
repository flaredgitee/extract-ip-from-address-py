# Copyright 2025 flaredgitee

# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at

#     http://www.apache.org/licenses/LICENSE-2.0

# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Unit tests for extract_ip_from_address function."""

import unittest
import importlib.util
import pathlib


class TestExtractIP(unittest.TestCase):

    def setUp(self) -> None:
        # Load the module directly from its file because the package
        # directory contains a hyphen and cannot be imported normally.
        module_path = (
            pathlib.Path(__file__).resolve().parent.parent
            / "extract-ip-from-address"
            / "app.py"
        )
        spec = importlib.util.spec_from_file_location("ex_app", str(module_path))
        if spec is None:
            raise ImportError(f"Could not load module from {module_path}")
        mod = importlib.util.module_from_spec(spec)
        loader = spec.loader
        if loader is None:
            raise ImportError(f"No loader for module from {module_path}")
        loader.exec_module(mod)
        self.extract_ip = mod.extract_ip_from_address

    def test_examples(self) -> None:
        cases = {
            "192.168.1.1:8080": "192.168.1.1",
            "192.168.1.1": "192.168.1.1",
            "[2001:db8::1]:8080": "2001:db8::1",
            "[2001:db8::1]": "2001:db8::1",
            "2001:db8::1": "2001:db8::1",
            # Non-numeric port should be left unchanged (behavior preserved)
            "192.168.1.1:http": "192.168.1.1:http",
            # Ambiguous IPv6 with trailing :8080 (no brackets) should remain unchanged
            "2001:db8::1:8080": "2001:db8::1:8080",
            # Leading/trailing whitespace should be trimmed
            "  192.168.1.1:8080  ": "192.168.1.1",
        }

        for addr, expected in cases.items():
            with self.subTest(addr=addr):
                self.assertEqual(self.extract_ip(addr), expected)


if __name__ == "__main__":
    unittest.main()
