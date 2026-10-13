#!/bin/bash
set -euo pipefail

repo_dir=$(cd "$(dirname "$0")/.." && pwd)
version=1.6.3.9
package="$repo_dir/dist/DYMO-LabelWriter-4XL-Driver-$version.pkg"

python3 "$repo_dir/scripts/verify-payload.py"
mkdir -p "$repo_dir/dist"
/usr/bin/pkgbuild \
  --root "$repo_dir/driver" \
  --scripts "$repo_dir/scripts/package" \
  --identifier io.github.bleeckerj.dymo-labelwriter-4xl-driver \
  --version "$version" \
  --install-location / \
  --ownership recommended \
  "$package"
(
  cd "$repo_dir/dist"
  /usr/bin/shasum -a 256 "$(basename "$package")" > "$(basename "$package").sha256"
)
printf 'Built %s\n' "$package"
