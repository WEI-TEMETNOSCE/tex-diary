#!/bin/bash

# GitHub Setup Script for Diary Project
# This script initializes a git repository, creates a GitHub repo, and pushes the code
# Author: AI Assistant
# Date: $(date)

set -e  # Exit on any error

# Configuration
GITHUB_USERNAME="lqiang67"
GITHUB_EMAIL="lqiang67@gmail.com"
REPO_NAME="diary"
REPO_DESCRIPTION="Research Diary - LaTeX documents, blogs, and collections"
PROJECT_DIR="/Users/lqiang67/Downloads/diary"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Function to print colored output
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

# Function to check if command exists
command_exists() {
    command -v "$1" >/dev/null 2>&1
}

# Check prerequisites
check_prerequisites() {
    print_status "Checking prerequisites..."
    
    if ! command_exists git; then
        print_error "Git is not installed. Please install Git first."
        exit 1
    fi
    
    if ! command_exists gh; then
        print_error "GitHub CLI (gh) is not installed."
        print_status "Please install it with: brew install gh"
        print_status "Or visit: https://cli.github.com/"
        exit 1
    fi
    
    print_success "All prerequisites are installed."
}

# Check if already in a git repository
check_existing_git() {
    if [ -d "$PROJECT_DIR/.git" ]; then
        print_warning "Git repository already exists in $PROJECT_DIR"
        read -p "Do you want to continue and potentially overwrite existing git history? (y/N): " -n 1 -r
        echo
        if [[ ! $REPLY =~ ^[Yy]$ ]]; then
            print_status "Exiting..."
            exit 0
        fi
    fi
}

# Initialize git repository
init_git() {
    print_status "Initializing Git repository..."
    cd "$PROJECT_DIR"
    
    # Initialize git if not already done
    if [ ! -d ".git" ]; then
        git init
        print_success "Git repository initialized."
    fi
    
    # Configure git user
    git config user.name "$GITHUB_USERNAME"
    git config user.email "$GITHUB_EMAIL"
    print_success "Git user configuration set."
    
    # Add all files
    print_status "Adding files to git..."
    git add .
    
    # Check if there are any changes to commit
    if git diff --staged --quiet; then
        print_warning "No changes to commit."
    else
        # Create initial commit
        git commit -m "Initial commit: Research diary project with LaTeX documents, blogs, and collections

- Added LaTeX diary entries and templates
- Added blog posts in multiple categories (AI, ML, Mathematics)
- Added collections and figures
- Added comprehensive .gitignore for LaTeX temporary files
- Project structure includes assets, styles, and bibliography files"
        print_success "Initial commit created."
    fi
}

# Authenticate with GitHub
authenticate_github() {
    print_status "Checking GitHub CLI authentication..."
    
    if ! gh auth status >/dev/null 2>&1; then
        print_status "Not authenticated with GitHub. Starting authentication process..."
        gh auth login --git-protocol https --hostname github.com --web
    else
        print_success "Already authenticated with GitHub."
    fi
}

# Create GitHub repository
create_github_repo() {
    print_status "Creating GitHub repository..."
    
    # Check if repository already exists
    if gh repo view "$GITHUB_USERNAME/$REPO_NAME" >/dev/null 2>&1; then
        print_warning "Repository $GITHUB_USERNAME/$REPO_NAME already exists on GitHub."
        read -p "Do you want to use the existing repository? (Y/n): " -n 1 -r
        echo
        if [[ $REPLY =~ ^[Nn]$ ]]; then
            print_status "Please choose a different repository name or delete the existing one."
            exit 1
        fi
    else
        # Create new repository
        gh repo create "$REPO_NAME" \
            --description "$REPO_DESCRIPTION" \
            --public \
            --source=. \
            --remote=origin \
            --push
        
        print_success "GitHub repository created and code pushed!"
        return
    fi
    
    # If repository exists, just add remote and push
    setup_existing_repo
}

# Setup existing repository
setup_existing_repo() {
    print_status "Setting up connection to existing repository..."
    
    # Add remote if it doesn't exist
    if ! git remote get-url origin >/dev/null 2>&1; then
        git remote add origin "https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
        print_success "Remote origin added."
    else
        print_status "Remote origin already exists."
    fi
    
    # Push to GitHub
    print_status "Pushing to GitHub..."
    
    # Set upstream and push
    git branch -M main
    git push -u origin main --force
    
    print_success "Code pushed to GitHub!"
}

# Main execution
main() {
    print_status "Starting GitHub setup for diary project..."
    print_status "Project directory: $PROJECT_DIR"
    print_status "GitHub username: $GITHUB_USERNAME"
    print_status "Repository name: $REPO_NAME"
    echo
    
    # Check if project directory exists
    if [ ! -d "$PROJECT_DIR" ]; then
        print_error "Project directory $PROJECT_DIR does not exist!"
        exit 1
    fi
    
    # Run all steps
    check_prerequisites
    check_existing_git
    init_git
    authenticate_github
    create_github_repo
    
    echo
    print_success "🎉 Setup complete!"
    print_status "Repository URL: https://github.com/$GITHUB_USERNAME/$REPO_NAME"
    print_status "You can now:"
    print_status "  - View your repository: gh repo view --web"
    print_status "  - Clone elsewhere: git clone https://github.com/$GITHUB_USERNAME/$REPO_NAME.git"
    print_status "  - Make changes and push: git add . && git commit -m 'message' && git push"
}

# Run main function
main "$@"
