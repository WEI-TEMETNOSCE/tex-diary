# LaTeX2HTML Converter

A standalone, modular tool for converting LaTeX files to HTML with comprehensive support for custom commands, figures, bibliography, and templates.

## Features

✅ **Custom LaTeX Commands**: Automatically parses and converts custom commands from `.sty` and `.tex` files  
✅ **MathJax Integration**: Generates MathJax configuration with custom macros  
✅ **Figure Handling**: Copies referenced figures with proper relative paths  
✅ **Bibliography Support**: Processes `.bib` files and citations  
✅ **Include/Input Processing**: Handles `\include{}` and `\input{}` directives  
✅ **Template System**: Supports custom HTML templates and CSS  
✅ **Modular Design**: Clean, extensible architecture with separate components  

## Installation

The tool is a standalone Python script with no external dependencies beyond what's already in your diary system:

```bash
# Make executable
chmod +x latex2html

# Test installation
./latex2html --help
```

## Usage

### Basic Conversion

```bash
./latex2html input.tex output_folder
```

### With Template and CSS

```bash
./latex2html input.tex output_folder --template template.html --css style.css
```

### Verbose Output

```bash
./latex2html input.tex output_folder --verbose
```

### Skip Asset Copying

```bash
./latex2html input.tex output_folder --no-assets
```

## Examples

### Convert Test Document

```bash
./latex2html test_document.tex test_output/basic --verbose
```

### Convert with Template

```bash
./latex2html test_document.tex test_output/templated \
  --template test_template.html --css test_style.css --verbose
```

### Convert Real Diary Entry

```bash
./latex2html posts/2025/2025-09-20-newmethod.tex test_output/real_entry --verbose
```

## Architecture

The converter is built with a modular architecture:

### Core Components

- **`LaTeX2HTMLConverter`**: Main orchestrator class
- **`LaTeXCommandParser`**: Parses custom commands from `.sty` and `.tex` files
- **`FigureHandler`**: Handles figure copying and path management
- **`BibliographyHandler`**: Processes bibliography files and citations
- **`IncludeHandler`**: Handles `\include{}` and `\input{}` directives
- **`TemplateEngine`**: Applies HTML templates and CSS
- **`MathJaxProcessor`**: Enhances HTML with MathJax configuration

### Processing Pipeline

1. **Parse Commands**: Scan all `.sty` and `.tex` files for custom command definitions
2. **Process Includes**: Handle `\include{}` and `\input{}` directives
3. **Copy Figures**: Copy referenced figures with proper relative paths
4. **Handle Bibliography**: Copy and process `.bib` files
5. **Convert to HTML**: Use pandoc for LaTeX to HTML conversion
6. **Enhance MathJax**: Add custom MathJax configuration
7. **Apply Template**: Apply HTML template if provided

## Custom Commands Support

The tool automatically detects and converts custom LaTeX commands:

### Simple Commands
```latex
\newcommand{\RR}{\mathbb{R}}
\newcommand{\CC}{\mathbb{C}}
```

### One-Argument Commands
```latex
\newcommand{\vv}[1]{\boldsymbol{#1}}
\newcommand{\set}[1]{\mathcal{#1}}
```

### Two-Argument Commands
```latex
\newcommand{\f}[2]{\frac{#1}{#2}}
```

### Math Operators
```latex
\DeclareMathOperator*{\argmax}{arg\,max}
\DeclareMathOperator{\trace}{trace}
```

## Figure Handling

The tool automatically:
- Finds figure references in LaTeX files
- Copies figures to output directory
- Maintains proper relative paths
- Supports multiple figure formats (PNG, JPG, PDF, EPS, SVG)

## Bibliography Support

- Automatically detects `\bibliography{}` commands
- Copies `.bib` files to output directory
- Configures pandoc for citation processing
- Supports multiple bibliography files

## Template System

### HTML Template Variables

- `{{TITLE}}`: Document title
- `{{CONTENT}}`: Main document content
- `{{CSS_FILE}}`: CSS file name
- `{{DATE}}`: Generation date

### Example Template

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{{TITLE}}</title>
    <link rel="stylesheet" href="{{CSS_FILE}}">
</head>
<body>
    <div class="container">
        <h1>{{TITLE}}</h1>
        <main>{{CONTENT}}</main>
    </div>
</body>
</html>
```

## Testing

Run the comprehensive test suite:

```bash
python3 test_runner.py
```

The test suite validates:
- Basic LaTeX to HTML conversion
- Template application
- Asset copying
- Real diary entry conversion
- Command parsing

## Integration with Diary System

The `latex2html` tool is designed to work seamlessly with the existing diary system:

- Uses the same command definitions from `assets/styles/`
- Supports the same figure and bibliography structure
- Compatible with existing templates
- Can be integrated into the main diary script

## Error Handling

The tool includes comprehensive error handling:

- Graceful fallbacks for missing files
- Detailed error messages with verbose mode
- Continues processing even if some components fail
- Logs all operations for debugging

## Performance

- Efficient command parsing with regex optimization
- Minimal file copying (only referenced assets)
- Parallel processing where possible
- Memory-efficient for large documents

## Future Enhancements

Potential improvements:
- Support for more LaTeX packages
- Advanced template features (loops, conditionals)
- Batch processing capabilities
- Integration with build systems
- Custom output formats

## Troubleshooting

### Common Issues

1. **Pandoc not found**: Install pandoc with `brew install pandoc` (macOS) or `apt install pandoc` (Linux)
2. **Permission denied**: Make sure the script is executable with `chmod +x latex2html`
3. **Missing figures**: Check that figure paths are correct relative to the LaTeX file
4. **Bibliography errors**: Ensure `.bib` files are in the expected locations

### Debug Mode

Use `--verbose` flag for detailed logging:

```bash
./latex2html input.tex output_folder --verbose
```

## License

This tool is part of the Research Diary System and follows the same license terms.
