# Research Diary System

A LaTeX-based research diary system for creating, organizing, and compiling daily latex notes into both PDF documents and HTML blogs, with a minimal tag system for easy organization. Note: The LaTeX-to-HTML blog conversion is functional but still under refinement.


## 🚀 Quick Start

```bash
# Make the script executable (first time only)
chmod +x diary

# Create today's diary entry. 
./diary today
# This would create a latex diary posts/year/year-month-day.tex. You can start typing.  

# If you create more than one diary in the same day, you can create entry with an extra name, such as 
./diary today machine-learning
# this would create posts/year/year-month-day-[optionalname].tex. 

# View system status
./diary status

# Compile all entries from current year into a single pdf with table of content. 
./diary 2025

# Compile entries with specific tags 
./diary tags AI machine-learning

# Create a blog with all files with including the union of a number of tags. 
./diary blog AI machine-learning 

or 
./diary blog 2025 # creating a blog with all posts in 2025 
```

## 📁 Directory Structure

```
diary/
├── diary                 # Main executable script
├── config.yaml           # User-friendly configuration
├── posts/                # All diary entries
│   └── 2025/             # Organized by year
│       ├── 2025-01-15-research-methods.tex
│       ├── 2025-01-16-neural-networks.tex
│       └── ...
├── collections/          # Compiled outputs (combined documents)
│   ├── year-2025/        # Yearly compilations
│   ├── ai+ml/            # Tag-based collections
│   └── ...
├── blogs/                # Individual post blogs ✨ NEW!
│   ├── ai+ml/            # Blog for AI+ML topics
│   │   ├── index.html    # Blog homepage
│   │   ├── style.css     # Blog styling
│   │   └── posts/        # Individual HTML posts
│   └── ...
└── assets/               # Templates, styles, and resources
    ├── templates/        # LaTeX templates
    ├── styles/           # LaTeX style files
    ├── html_templates/   # HTML blog templates
    ├── bib/              # Bibliography files
    └── figures/          # Research figures and images
```

## 📖 Command Line Usage

### Create Diary Entries

```bash
# Create today's entry
./diary today

# Create entry with optional name (no quotes needed!)
./diary today optimization-methods
./diary today literature-review
./diary today experiment-results
```

**What happens:**
- Creates `posts/YEAR/YYYY-MM-DD-[name].tex` 
- Automatically includes current year as tag
- Opens with template ready for editing

### View System Status

```bash
# Basic status
./diary status

# Verbose output (shows debug info)
./diary --verbose status
```

**Shows:**
- Number of entries for current year
- Available tags and their frequencies
- System configuration
- Directory locations

### Compile Collections

#### By Year (All Entries)
```bash
# Compile current year (super simple!)
./diary 2025

# Compile other years
./diary 2024
./diary 2023

# Traditional way (still works)
./diary compile --year 2025

# Compile to HTML instead of PDF
./diary compile --year 2025 --format html

# Custom output location
./diary compile --year 2025 --output my-research-2025
```

**Output:** 
- PDF: `collections/year-YYYY/YYYY-Research-Diary.pdf`
- HTML: `collections/year-YYYY/YYYY-Research-Diary.html`

#### By Tags (Filtered Entries)
```bash
# Single tag (no quotes needed!)
./diary tags machine-learning

# Multiple tags (finds entries with ANY of these tags)
./diary tags AI neural-networks deep-learning

# Tags with spaces still need quotes
./diary tags "natural language processing" "computer vision"

# Mixed - simple tags without quotes, spaced tags with quotes
./diary tags AI "machine learning" deep-learning

# Compile to HTML instead of PDF
./diary tags AI deep-learning --format html

# Custom output location
./diary tags AI ML --output my-ai-collection
```

**Output:** 
- PDF: `collections/tag1+tag2+tag3/tag1+tag2+tag3.pdf`
- HTML: `collections/tag1+tag2+tag3/tag1+tag2+tag3.html`

#### Create Blog (Individual HTML Posts) ✨ ENHANCED!
```bash
# Create a blog with individual HTML posts
./diary blog AI machine-learning

# Create blog for specific research topics
./diary blog "deep learning" transformers

# Multiple topics with full LaTeX support
./diary blog research-methods statistics analysis

# Compact table-of-contents style (default)
./diary blog 2025

# Full card layout with excerpts
./diary blog 2025 --full
```

**What happens:**
- Creates `blogs/tag1+tag2/` directory with minimalist grey design
- Generates individual HTML files with full LaTeX command support
- All 100+ custom LaTeX commands work perfectly (\argmax, \KL, \E, etc.)
- Creates beautiful responsive `index.html` with post previews
- Includes professional CSS styling optimized for academic content
- Automatic MathJax integration for mathematical notation

**Output Structure:**
```
blogs/tag1+tag2/
├── index.html          # Main blog page with post list
├── style.css           # Blog styling
└── posts/              # Individual post HTML files
    ├── 2025-01-15-entry1.html
    ├── 2025-01-16-entry2.html
    ├── post.css         # Post styling
    └── ...
```

## 🏷️ Tagging System

### Adding Tags to Entries

Edit the tag line in your `.tex` files:

```latex
% <TAGs>: 2025, machine learning, neural networks, research methods
```

**Tag Rules:**
- **Comma-separated**: Use commas to separate multiple tags
- **Spaces allowed**: "neural networks", "machine learning", "research methods"
- **Case insensitive**: "AI" matches "ai" matches "Ai"
- **Auto year**: Current year automatically added
- **Custom tags**: Add any topics relevant to your research

### Tag Examples

```latex
% <TAGs>: 2025, deep learning, transformers, attention mechanisms
% <TAGs>: 2025, experiment results, statistical analysis
% <TAGs>: 2025, literature review, survey paper, related work
% <TAGs>: 2025, meeting notes, advisor discussion
% <TAGs>: 2025, conference paper, submission deadline
```

## ⚙️ Configuration

Edit `config.yaml` to customize your setup:

```yaml
author: "Your Name"
institution: "Your University"
current_year: "auto"
default_editor: "code"
```

**Key Settings:**
- `auto` for year = automatically use current year
- Editor options: `code` (VS Code), `open` (macOS default), `vim`, etc.

## 📝 Writing Diary Entries

Each entry supports full LaTeX formatting:

```latex
\section{Research Progress}

Today I worked on \textbf{attention mechanisms} in transformers.

\subsection{Key Findings}
\begin{itemize}
    \item Multi-head attention improves performance
    \item Positional encoding is crucial: $PE_{pos,2i} = \sin(pos/10000^{2i/d})$
    \item Self-attention complexity is $O(n^2)$
\end{itemize}

\subsection{Next Steps}
\begin{enumerate}
    \item Implement efficient attention
    \item Run experiments on dataset
    \item Compare with baseline models
\end{enumerate}
```

## 🔧 Advanced Usage

### Workflow Examples

```bash
# Daily research workflow (no quotes needed!)
./diary today monday-research
./diary today tuesday-experiments  
./diary today wednesday-analysis

# Project-based entries
./diary today project-alpha-week3
./diary today paper-submission-final

# Meeting notes
./diary today advisor-meeting
./diary today group-discussion

# Compile monthly progress
./diary tags project-alpha --output monthly-alpha-progress

# Compile all meetings
./diary tags meeting discussion --output all-meetings

# Year-end compilation (super simple!)
./diary 2024
```

### Multiple Tag Searches

```bash
# Find entries about any ML topic (mix of simple and spaced tags)
./diary tags "machine learning" "deep learning" neural-networks AI

# Research methodology entries
./diary tags experiment analysis methodology statistics

# Paper writing entries  
./diary tags writing paper submission review
```

## 📋 Requirements

### Essential
- **Python 3.6+** (usually pre-installed)

### For PDF Compilation
- **LaTeX** (for PDF compilation):
  - macOS: `brew install --cask mactex`
  - Ubuntu: `sudo apt-get install texlive-full`
  - Windows: Install MiKTeX or TeX Live

### For HTML Compilation ✨ NEW!
- **Pandoc** (for HTML compilation):
  - macOS: `brew install pandoc`
  - Ubuntu: `sudo apt install pandoc`
  - Windows: Download from [pandoc.org](https://pandoc.org/installing.html)
- **Internet connection** (for MathJax CDN)

### HTML Features ✨ ENHANCED!
- 📚 **Bibliography Support** - Automatic citation processing with `--citeproc`
- 🎨 **Minimalist Design** - Clean grey aesthetic optimized for academic content
- 🧮 **Advanced Math Support** - 100+ LaTeX commands work seamlessly in HTML
- ⚡ **Perfect LaTeX Integration** - \argmax, \KL, \E, \dd, \blue{}, \vv{} all supported
- 📱 **Responsive Design** - Works beautifully on mobile and desktop
- 🔍 **Searchable** - Full-text search with Ctrl+F
- 🎯 **Chronological Sorting** - Entries sorted by creation time, not filename
- 📐 **Professional Typography** - Times New Roman, proper margins, justified text

## 🛠️ Troubleshooting

### Common Issues

**"pdflatex not found"**
```bash
# Install LaTeX distribution
brew install --cask mactex  # macOS
sudo apt install texlive-full  # Ubuntu
```

**"pandoc not found"** (for HTML compilation)
```bash
# Install pandoc
brew install pandoc  # macOS
sudo apt install pandoc  # Ubuntu
```

**"No diary entries found"**
- Check you're in the right directory
- Ensure entries have proper `<TAGs>:` format
- Use `./diary status` to see available entries

**HTML compilation issues**
- Ensure internet connection for MathJax and Bootstrap CSS
- Try running pandoc manually: `pandoc file.tex -o file.html --standalone --mathjax`

**Template not found**
- Ensure `latex/templates/` directory exists
- Check file permissions

### Getting Help

```bash
# Show all available commands
./diary --help

# Show help for specific command
./diary today --help
./diary compile --help
./diary tags --help
```

## 🎯 Tips & Best Practices

### Daily Habits
1. **Consistent naming**: Use descriptive entry names
2. **Tag everything**: Add relevant tags to all entries
3. **Regular compilation**: Weekly/monthly progress reviews
4. **Backup**: Keep your `posts/` directory backed up

### Tag Organization
- **Broad categories**: "research", "meetings", "writing"
- **Specific topics**: "transformer", "CNN", "optimization"
- **Project names**: "project-alpha", "paper-submission"
- **Time periods**: "week1", "month3", "semester1"

### Compilation Strategies
- **Daily**: Individual entry review
- **Weekly**: `./diary tags "week1" "week2"`
- **Monthly**: `./diary compile --year 2025`
- **Project**: `./diary tags "project-name"`
- **Topic**: `./diary tags "specific-research-area"`

---

**Happy researching! 📚✨**

For questions or issues, check the troubleshooting section or examine the simple `diary` script source code.