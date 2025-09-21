# LaTeX Resources

This directory contains all LaTeX-related files that you might want to customize for your research diary system.

## Directory Structure

```
latex/
├── styles/                     # LaTeX style files (.sty)
│   ├── diary_base.sty         # Essential diary functionality
│   ├── diary_math.sty         # Advanced math packages
│   ├── diary_commands.sty     # Custom commands and shortcuts
│   └── natbibspacing.sty      # Bibliography spacing
├── templates/                  # LaTeX templates
│   ├── collection/             # Templates for compiling full diary
│   │   └── collection_template.tex
│   └── entries/               # Templates for daily entries
│       ├── entry_template.tex # Modern template (recommended)
│       └── entry.tex          # Legacy template
├── bibliography/              # Bibliography files
│   └── reference.bib          # Your research references
└── commands/                  # Custom LaTeX commands
    └── my_newcommands.tex     # Your custom commands
```

## Customization

### Style Files (`styles/`)
- **diary_base.sty**: Core diary functionality (headers, footers, basic packages)
- **diary_math.sty**: Advanced math environments and symbols
- **diary_commands.sty**: Custom shortcuts and convenience commands
- **natbibspacing.sty**: Bibliography formatting

### Templates (`templates/`)
- **entry_template.tex**: Template for daily entries with `<VARIABLE>` placeholders
- **collection_template.tex**: Template for compiling all entries into a single document

### Bibliography (`bibliography/`)
- **reference.bib**: Add your research references here in BibTeX format

### Commands (`commands/`)
- **my_newcommands.tex**: Define your custom LaTeX commands and macros

## Editing Templates

Templates use `<VARIABLE>` syntax for placeholders:
- `<YEAR>`: Current year
- `<AUTHOR>`: Your name
- `<INSTITUTION>`: Your institution
- `<MONTH_NAME>`: Full month name (e.g., "September")
- `<DAY>`: Day of month
- `<FILENAME>`: Name of the file

## Adding References

Add references to `bibliography/reference.bib`:

```bibtex
@article{author2025,
  title={Your Paper Title},
  author={Author, Name},
  journal={Journal Name},
  year={2025}
}
```

Then cite in your entries with `\cite{author2025}`.

## Custom Commands

Add frequently used commands to `commands/my_newcommands.tex`:

```latex
\newcommand{\todo}[1]{\textcolor{red}{\textbf{TODO: #1}}}
\newcommand{\important}[1]{\textcolor{blue}{\textbf{#1}}}
```

All files in this directory are automatically linked into compilation directories, so your customizations will be available in all diary entries and compilations.
