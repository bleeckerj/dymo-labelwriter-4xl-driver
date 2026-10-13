#!/usr/bin/env python3
"""Check the exact driver payload and its recorded hashes before packaging."""
import hashlib
import json
from pathlib import Path

repo = Path(__file__).resolve().parents[1]
manifest = json.loads((repo / "provenance.json").read_text())
expected = {entry["path"]: entry for entry in manifest["files"]}
actual = {p.relative_to(repo).as_posix(): p for p in (repo / "driver").rglob("*") if p.is_file()}
if actual.keys() != expected.keys():
    raise SystemExit(f"Unexpected payload files: {sorted(actual.keys() ^ expected.keys())}")
for path, entry in expected.items():
    data = actual[path].read_bytes()
    if len(data) != entry["bytes"] or hashlib.sha256(data).hexdigest() != entry["sha256"]:
        raise SystemExit(f"Checksum mismatch: {path}")
print(f"Verified {len(actual)} vendor files, {sum(x['bytes'] for x in expected.values()):,} bytes total")
