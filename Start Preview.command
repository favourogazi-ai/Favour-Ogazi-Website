#!/bin/bash
# Double-click to preview Favour's website locally.
cd "$(dirname "$0")"
PORT=4321
URL="http://localhost:$PORT"
echo ""
echo "  Favour Ogazi website: local preview"
echo "  Rebuilding pages from site-src..."
if command -v python3 >/dev/null 2>&1 && python3 -c "" >/dev/null 2>&1; then
  python3 site-src/build.py
  echo "  Opening $URL  (keep this window open; press Ctrl+C to stop)"
  (sleep 1; open "$URL") &
  cd public && python3 -m http.server $PORT
elif command -v npx >/dev/null 2>&1; then
  echo "  Python not found, so pages weren't rebuilt. Serving current files."
  (sleep 3; open "$URL") &
  npx --yes serve public -l $PORT
else
  echo "  Neither Python nor Node is installed. Opening the homepage file directly."
  open public/index.html
fi
