# Diary System Configuration

This file contains the configuration for your research diary system. Edit the values below to customize your diary setup.

## Personal Information

**Author Name**: Research Student
> Your full name as it will appear on diary covers and headers

**Institution**: University  
> Your university or organization name

**Current Year**: auto
> The year for which you're keeping diary entries (use 'auto' for current year)

## Directory Settings

**Output Directory**: collections
> Legacy directory setting. All compilations now go to 'collections' folder by default (year-based: collections/year-YYYY/, tag-based: collections/tag1+tag2/)

**Template Directory**: latex/templates
> Directory containing LaTeX templates (relative to diary root)

## LaTeX Files (relative paths from diary root)

**Style Files Directory**: latex/styles
> Directory containing .sty files

**Bibliography File**: latex/bibliography/reference.bib
> Path to your bibliography file

**Entry Template**: latex/templates/entries/entry_template.tex
> Template for individual diary entries

**Collection Template**: latex/templates/collection/collection_template.tex
> Template for compiled collections

## Editor Settings

**Default Editor**: open
> Command to open files (macOS: 'open', Linux: 'xdg-open', or specific editor like 'code', 'vim')

## Advanced Settings

**LaTeX Engine**: pdflatex
> LaTeX compiler to use

**LaTeX Options**: -interaction=nonstopmode -file-line-error
> Command line options for LaTeX compilation

**Cleanup Extensions**: .aux .log .out .toc .lof .lot .bbl .blg .fls .fdb_latexmk .synctex.gz .nav .snm .vrb .tmp .tmp~
> File extensions to clean up after LaTeX compilation
