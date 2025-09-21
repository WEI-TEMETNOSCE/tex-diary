# GitHub Tools

This directory contains all the scripts and documentation for setting up and managing the diary project on GitHub.

## Files

- **`setup_github.sh`** - Full automated setup script (requires GitHub CLI)
- **`setup_git_only.sh`** - Git-only setup script for manual GitHub connection
- **`manual_setup_instructions.md`** - Step-by-step manual setup instructions
- **`GITHUB_SETUP_README.md`** - Comprehensive documentation and troubleshooting guide

## Quick Start

If GitHub CLI is installed:
```bash
./setup_github.sh
```

If GitHub CLI is not installed:
```bash
./setup_git_only.sh
# Then follow the displayed instructions
```

## Usage

These tools were used to initially set up the repository at https://github.com/lqiang67/diary

For ongoing development, use standard git commands:
```bash
git add .
git commit -m "Your commit message"
git push
```

---
*Generated during initial GitHub setup on September 21, 2025*
