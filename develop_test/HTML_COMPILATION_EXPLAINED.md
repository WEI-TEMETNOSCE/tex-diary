# HTML Compilation in Diary System - Code Explanation

## 🎯 Overview

The `compile_to_html` function in the diary system converts LaTeX files to HTML using pandoc. This document explains how it works step by step.

## 📋 Function Breakdown

### 1. Prerequisites Check
```python
if not shutil.which('pandoc'): 
    raise RuntimeError("pandoc not found - install with: brew install pandoc")
```
**What it does**: Checks if pandoc is installed and available in the system PATH.

### 2. File Path Setup
```python
tex_dir, tex_name, html_file = tex_file.parent, tex_file.name, tex_file.parent / (tex_file.stem + '.html')
```
**What it does**: 
- `tex_dir`: Directory containing the LaTeX file
- `tex_name`: Just the filename (e.g., "2025-09-20-research.tex")
- `html_file`: Output HTML file path (same name, .html extension)

### 3. Working Directory Change
```python
original_dir = os.getcwd()
os.chdir(tex_dir)
```
**Why this is needed**: pandoc needs to run in the same directory as the LaTeX file so it can find:
- Referenced images
- Bibliography files
- Style files
- Other included files

### 4. Bibliography Detection
```python
bib_file = tex_dir / "reference.bib"
if bib_file.exists():
    cmd.extend(['--bibliography', 'reference.bib'])
```
**What it does**: Checks if a bibliography file exists and adds it to the pandoc command if found.

### 5. Pandoc Command Construction
```python
cmd = ['pandoc', tex_name, '-o', html_file.name, 
       '--standalone', '--mathjax',
       '--citeproc',
       '--css', 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css']
```

**Each option explained**:
- `pandoc`: The program to run
- `tex_name`: Input LaTeX file
- `-o html_file.name`: Output HTML file
- `--standalone`: Creates complete HTML document (not fragment)
- `--mathjax`: Enables math equation rendering
- `--citeproc`: Processes citations and generates bibliography
- `--css URL`: Links external CSS for styling

### 6. Custom CSS Creation
```python
css_content = create_academic_css()
css_file = tex_dir / "academic.css"
with open(css_file, 'w') as f:
    f.write(css_content)
cmd.extend(['--css', 'academic.css'])
```
**What it does**: Creates a temporary CSS file with academic formatting (Times New Roman, proper margins, etc.)

### 7. Pandoc Execution
```python
result = subprocess.run(cmd, capture_output=True, text=True)
if result.returncode != 0:
    print(f"Warning: pandoc conversion had issues: {result.stderr}")
```
**What it does**: Runs the pandoc command and captures any error output.

### 8. Cleanup
```python
if css_file.exists():
    css_file.unlink()
```
**What it does**: Removes the temporary CSS file after conversion.

### 9. Directory Restoration
```python
finally:
    os.chdir(original_dir)
```
**What it does**: Always returns to the original directory, even if an error occurs.

## 🔧 Key Technical Concepts

### Why Change Working Directory?
LaTeX files often reference other files with relative paths:
```latex
\bibliography{reference}          % Looks for reference.bib in current directory
\usepackage{diary_base}           % Looks for diary_base.sty in current directory
\includegraphics{image.png}       % Looks for image.png in current directory
```

By changing to the LaTeX file's directory, pandoc can find all these referenced files.

### Citation Processing Flow
1. **LaTeX input**: `\cite{example2025}` in the .tex file
2. **Bibliography file**: `reference.bib` contains the reference details
3. **Pandoc processing**: `--citeproc` converts citations to formatted text
4. **HTML output**: `(Author 2025)` with a generated bibliography section

### CSS Styling Strategy
The function applies **two CSS files**:
1. **Bootstrap CSS** (from CDN): Provides basic responsive layout
2. **Academic CSS** (custom): Overrides with academic formatting (Times New Roman, margins, etc.)

## 📊 Comparison: PDF vs HTML Compilation

| Aspect | PDF (pdflatex) | HTML (pandoc) |
|--------|----------------|---------------|
| **Engine** | pdflatex + bibtex | pandoc --citeproc |
| **Math** | Native LaTeX | MathJax |
| **Citations** | bibtex | pandoc citeproc |
| **Styling** | .sty files | CSS |
| **Output** | Fixed layout | Responsive |

## 🧪 Testing the Code

Use the provided test files:
- `test_html_compilation.py`: Detailed step-by-step execution
- `simple_html_test.py`: Clean comparison of simple vs advanced compilation

Both files demonstrate:
- How each step works
- What files are created
- How errors are handled
- The difference between basic and advanced compilation

## 🎯 Integration with Diary System

The `compile_to_html` function is called from:
- `cmd_compile()`: For year-based compilations
- `cmd_tags()`: For tag-based compilations

Both functions:
1. Generate the LaTeX file (combining multiple entries)
2. Set up the output directory (with symlinks to style files and bibliography)
3. Call `compile_to_html()` if `--format html` is specified
4. Return the path to the generated HTML file

## 🔍 Debugging Tips

If HTML compilation fails:
1. Check if pandoc is installed: `which pandoc`
2. Check if the LaTeX file is valid
3. Look at the pandoc error message in `result.stderr`
4. Verify bibliography file exists if citations are used
5. Test with a minimal LaTeX file first

## 📚 Further Reading

- [Pandoc Manual](https://pandoc.org/MANUAL.html)
- [MathJax Documentation](https://docs.mathjax.org/)
- [Citation Style Language](https://citationstyles.org/)
