# GitHub Setup for Diary Project

This repository contains scripts and instructions to help you set up your diary project on GitHub.

## Quick Start (Automated)

Run the automated setup script:

```bash
cd /Users/lqiang67/Downloads/diary
./setup_github.sh
```

This script will:
- ✅ Initialize a Git repository
- ✅ Configure Git with your username and email
- ✅ Create a comprehensive .gitignore file for LaTeX
- ✅ Add all files and create an initial commit
- ✅ Create a GitHub repository (requires GitHub CLI)
- ✅ Push your code to GitHub

## Prerequisites

### Required
- **Git**: Already installed ✅ (`/usr/bin/git`)

### Optional but Recommended  
- **GitHub CLI**: Not installed ❌
  ```bash
  # Install GitHub CLI
  brew install gh
  ```

## If GitHub CLI is Not Available

If you don't want to install GitHub CLI, you can:

1. **Run the script anyway** - it will do everything except create the GitHub repository
2. **Follow manual instructions** - see `manual_setup_instructions.md`
3. **Create repository manually** on GitHub.com and connect it

## What's Included

### Files Created
- `.gitignore` - Excludes LaTeX temporary files and system files
- `setup_github.sh` - Automated setup script
- `manual_setup_instructions.md` - Step-by-step manual instructions
- `GITHUB_SETUP_README.md` - This file

### LaTeX Files Excluded
The `.gitignore` file automatically excludes:
```
*.aux *.bbl *.blg *.fdb_latexmk *.fls *.log *.out *.synctex.gz
*.synctex(busy) *.toc *.lof *.lot *.acn *.acr *.alg *.glg
*.glo *.gls *.ist *.figlist *.makefile *.auxlock
```

Plus macOS, editor, and other temporary files.

## Repository Structure

Your diary project includes:
- `assets/` - Bibliography, figures, styles, and templates
- `blogs/` - HTML blog posts organized by topic
- `collections/` - Compiled diary collections
- `posts/` - Individual LaTeX diary entries
- `develop_test/` - Development and testing files
- Configuration files and documentation

## Usage Examples

### First Time Setup
```bash
# Option 1: Automated (recommended)
./setup_github.sh

# Option 2: Manual (if you prefer control)
# Follow steps in manual_setup_instructions.md
```

### Daily Workflow
```bash
# Add new diary entry
git add posts/2025/2025-09-21-new-entry.tex

# Commit changes
git commit -m "Add diary entry for 2025-09-21: Research on transformers"

# Push to GitHub
git push
```

### Working with LaTeX Files
The setup automatically handles LaTeX temporary files:
- ✅ Source files (`.tex`, `.sty`, `.bib`) are tracked
- ❌ Temporary files (`.aux`, `.log`, `.synctex.gz`) are ignored
- ✅ Final outputs (`.pdf`) are tracked (but you can exclude them if desired)

## Troubleshooting

### "Repository already exists"
If you get this error:
1. Choose a different repository name
2. Delete the existing repository on GitHub
3. Or use the existing repository (script will ask)

### Authentication Issues
```bash
# If using GitHub CLI
gh auth login

# If using HTTPS (will prompt for username/password or token)
git push
```

### Large Files
For files larger than 100MB, consider Git LFS:
```bash
brew install git-lfs
git lfs install
git lfs track "*.pdf"
```

## Support

- For Git issues: https://git-scm.com/doc
- For GitHub issues: https://docs.github.com/
- For GitHub CLI: https://cli.github.com/manual/

## Next Steps

After setup:
1. ✅ Visit your repository: https://github.com/lqiang67/diary
2. ✅ Add a description and topics on GitHub
3. ✅ Consider making it private if it contains sensitive research
4. ✅ Set up branch protection rules if collaborating
5. ✅ Configure GitHub Pages if you want to publish blogs online

---

**Created**: September 21, 2025  
**Author**: AI Assistant  
**Purpose**: Streamline GitHub setup for LaTeX diary project
