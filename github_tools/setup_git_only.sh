#!/bin/bash

# Git-Only Setup Script for Diary Project
# This script initializes git and prepares for manual GitHub setup
# Author: AI Assistant

set -e  # Exit on any error

# Configuration
GITHUB_USERNAME="lqiang67"
GITHUB_EMAIL="lqiang67@gmail.com"
REPO_NAME="diary"
PROJECT_DIR="/Users/lqiang67/Downloads/diary"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

print_status() {
    echo -e "${BLUE}[INFO]${NC} $1"
}

print_success() {
    echo -e "${GREEN}[SUCCESS]${NC} $1"
}

print_warning() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

print_error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

main() {
    print_status "Setting up Git repository for diary project..."
    
    cd "$PROJECT_DIR"
    
    # Check if git is installed
    if ! command -v git >/dev/null 2>&1; then
        print_error "Git is not installed. Please install Git first."
        exit 1
    fi
    
    # Initialize git if not already done
    if [ ! -d ".git" ]; then
        print_status "Initializing Git repository..."
        git init
        print_success "Git repository initialized."
    else
        print_warning "Git repository already exists."
    fi
    
    # Configure git user
    print_status "Configuring Git user..."
    git config user.name "$GITHUB_USERNAME"
    git config user.email "$GITHUB_EMAIL"
    print_success "Git configuration complete."
    
    # Add files
    print_status "Adding files to repository..."
    git add .
    
    # Create initial commit if needed
    if git diff --staged --quiet; then
        print_warning "No new changes to commit."
    else
        print_status "Creating initial commit..."
        git commit -m "Initial commit: Research diary project

- LaTeX diary entries and templates
- Blog posts in multiple categories (AI, ML, Mathematics)
- Collections and figures  
- Comprehensive .gitignore for LaTeX temporary files
- Project structure with assets, styles, and bibliography"
        print_success "Initial commit created."
    fi
    
    # Set main branch
    git branch -M main
    
    echo
    print_success "🎉 Git setup complete!"
    echo
    print_status "Next steps to connect to GitHub:"
    print_status "1. Go to https://github.com/new"
    print_status "2. Repository name: $REPO_NAME"
    print_status "3. Description: Research Diary - LaTeX documents, blogs, and collections"
    print_status "4. Choose Public or Private"
    print_status "5. DON'T initialize with README (we have files already)"
    print_status "6. Click 'Create repository'"
    echo
    print_status "Then run these commands:"
    echo -e "   ${GREEN}git remote add origin https://github.com/$GITHUB_USERNAME/$REPO_NAME.git${NC}"
    echo -e "   ${GREEN}git push -u origin main${NC}"
    echo
    print_status "Or install GitHub CLI for automated setup:"
    echo -e "   ${GREEN}brew install gh${NC}"
    echo -e "   ${GREEN}./setup_github.sh${NC}"
}

main "$@"
