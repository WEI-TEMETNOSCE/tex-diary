#!/bin/bash
# Publish blog to separate public repository

set -e

BLOG_REPO="diary-blog"  # Name of your public blog repo
GITHUB_USER="lqiang67"

echo "🔨 Generating blog..."
python diary blog 2025

echo "📦 Setting up separate blog repository..."

# Clone or update the separate blog repo
if [ ! -d "../$BLOG_REPO" ]; then
    echo "📥 Cloning blog repository..."
    cd ..
    git clone "https://github.com/$GITHUB_USER/$BLOG_REPO.git" || {
        echo "❌ Blog repo doesn't exist. Create it first:"
        echo "   1. Go to https://github.com/new"
        echo "   2. Create public repo: $BLOG_REPO"
        echo "   3. Run this script again"
        exit 1
    }
    cd diary
else
    echo "🔄 Updating blog repository..."
    cd "../$BLOG_REPO"
    git pull origin main
    cd ../diary
fi

# Copy blog files to separate repo
echo "📋 Copying blog files..."
cp -r blogs/2025/* "../$BLOG_REPO/"

# Publish to separate repo
cd "../$BLOG_REPO"
git add .
git commit -m "Auto-publish blog: $(date '+%Y-%m-%d %H:%M')" || echo "No changes to commit"
git push origin main

echo ""
echo "✅ Blog published successfully!"
echo "🌐 Available at: https://$GITHUB_USER.github.io/$BLOG_REPO"
echo ""
echo "📝 Next: Enable GitHub Pages on the $BLOG_REPO repository"
