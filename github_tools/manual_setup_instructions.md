# Manual GitHub Setup Instructions

If you prefer to set up the repository manually or if the automated script doesn't work, follow these steps:

## Prerequisites

1. **Install Git** (if not already installed):
   ```bash
   # On macOS with Homebrew
   brew install git
   
   # Or download from https://git-scm.com/
   ```

2. **Install GitHub CLI** (recommended):
   ```bash
   # On macOS with Homebrew
   brew install gh
   
   # Or download from https://cli.github.com/
   ```

## Manual Setup Steps

### 1. Navigate to Project Directory
```bash
cd /Users/lqiang67/Downloads/diary
```

### 2. Initialize Git Repository
```bash
# Initialize git repository
git init

# Configure git user (replace with your details)
git config user.name "lqiang67"
git config user.email "lqiang67@gmail.com"
```

### 3. Add Files and Create Initial Commit
```bash
# Add all files (the .gitignore will exclude temporary files)
git add .

# Create initial commit
git commit -m "Initial commit: Research diary project

- Added LaTeX diary entries and templates
- Added blog posts in multiple categories (AI, ML, Mathematics)  
- Added collections and figures
- Added comprehensive .gitignore for LaTeX temporary files"
```

### 4. Create GitHub Repository

#### Option A: Using GitHub CLI (Recommended)
```bash
# Authenticate with GitHub (if not already done)
gh auth login

# Create repository and push
gh repo create diary \
  --description "Research Diary - LaTeX documents, blogs, and collections" \
  --public \
  --source=. \
  --remote=origin \
  --push
```

#### Option B: Using GitHub Web Interface
1. Go to https://github.com/new
2. Repository name: `diary`
3. Description: `Research Diary - LaTeX documents, blogs, and collections`
4. Choose Public or Private
5. **Don't** initialize with README, .gitignore, or license (we already have these)
6. Click "Create repository"

Then connect your local repository:
```bash
# Add remote origin (replace USERNAME with your GitHub username)
git remote add origin https://github.com/lqiang67/diary.git

# Set main branch and push
git branch -M main
git push -u origin main
```

### 5. Verify Setup
```bash
# Check remote connection
git remote -v

# View repository online
gh repo view --web
# Or visit: https://github.com/lqiang67/diary
```

## Future Workflow

After initial setup, use these commands for ongoing development:

```bash
# Check status
git status

# Add changes
git add .
# Or add specific files: git add filename.tex

# Commit changes
git commit -m "Add new diary entry for 2025-09-21"

# Push to GitHub
git push

# Pull latest changes (if working from multiple locations)
git pull
```

## Troubleshooting

### Authentication Issues
If you have authentication issues:
```bash
# Re-authenticate with GitHub CLI
gh auth logout
gh auth login

# Or use personal access token
# Go to GitHub Settings > Developer settings > Personal access tokens
# Create a token and use it as password when prompted
```

### Large Files
If you have large files (>100MB), you might need Git LFS:
```bash
# Install Git LFS
brew install git-lfs

# Initialize Git LFS
git lfs install

# Track large files (example for PDFs)
git lfs track "*.pdf"
git add .gitattributes
git commit -m "Add Git LFS tracking"
```

### Repository Already Exists
If the repository name already exists:
1. Choose a different name: `diary-research`, `academic-diary`, etc.
2. Or delete the existing repository from GitHub web interface
3. Update the commands above with your chosen name

## Files Excluded by .gitignore

The following LaTeX temporary files are automatically excluded:
- `*.aux`, `*.log`, `*.out` - LaTeX auxiliary files
- `*.synctex.gz` - SyncTeX files  
- `*.bbl`, `*.blg` - Bibliography files
- `*.fdb_latexmk`, `*.fls` - LaTeXmk files
- And many others...

This keeps your repository clean and focused on source files.
