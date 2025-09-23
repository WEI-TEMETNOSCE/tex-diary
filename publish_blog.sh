#!/bin/bash
# Manual blog publishing script
# This script generates the blog locally and pushes to trigger GitHub Actions

set -e  # Exit on error

echo "🔨 Generating blog locally..."
python diary blog 2025

echo "📦 Committing blog files..."
git add blogs/
git commit -m "Update blog: $(date '+%Y-%m-%d %H:%M')" || echo "No changes to commit"

echo "🚀 Pushing to GitHub (will trigger auto-publish)..."
git push origin main

echo ""
echo "✅ Done! GitHub Actions will publish your blog automatically."
echo "📍 Check progress at: https://github.com/lqiang67/diary/actions"
echo "🌐 Blog will be available at: https://lqiang67.github.io/diary"
echo ""
echo "💡 Tip: You can also trigger publishing manually:"
echo "   Go to Actions tab → 'Publish Blog to GitHub Pages' → 'Run workflow'"
