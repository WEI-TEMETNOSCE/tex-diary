# %%
#!/usr/bin/env python3
"""
Simple HTML Compilation Test - Understanding the Core Process
This script shows the essential parts of HTML compilation in a clean way
"""

import subprocess
import shutil
from pathlib import Path
import os

def simple_compile_to_html(tex_file_path):
    """
    Simplified version of compile_to_html to understand the core process
    """
    print("🔍 SIMPLE HTML COMPILATION DEMO")
    print("=" * 40)
    
    tex_file = Path(tex_file_path)
    print(f"📄 Input LaTeX file: {tex_file}")
    
    # Step 1: Check pandoc
    if not shutil.which('pandoc'):
        print("❌ pandoc not found!")
        return None
    print("✅ pandoc available")
    
    # Step 2: Set up output
    html_file = tex_file.with_suffix('.html')
    print(f"🌐 Output HTML file: {html_file}")
    
    # Step 3: Change to file directory
    original_dir = os.getcwd()
    os.chdir(tex_file.parent)
    print(f"📁 Working in: {tex_file.parent}")
    
    try:
        # Step 4: Basic pandoc command
        cmd = [
            'pandoc', 
            tex_file.name,                    # Input file
            '-o', html_file.name,             # Output file
            '--standalone',                   # Complete HTML document
            '--mathjax',                      # Math support
        ]
        
        print(f"🔧 Basic command: {' '.join(cmd)}")
        
        # Step 5: Run conversion
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Conversion successful!")
            if html_file.exists():
                size = html_file.stat().st_size
                print(f"📊 HTML file size: {size:,} bytes")
                return html_file
        else:
            print(f"❌ Conversion failed: {result.stderr}")
            
    finally:
        os.chdir(original_dir)
    
    return None

def advanced_compile_to_html(tex_file_path):
    """
    Advanced version showing all the features used in the diary system
    """
    print("\n🎓 ADVANCED HTML COMPILATION DEMO")
    print("=" * 40)
    
    tex_file = Path(tex_file_path)
    html_file = tex_file.with_suffix('.html')
    
    original_dir = os.getcwd()
    os.chdir(tex_file.parent)
    
    try:
        # Check for bibliography
        bib_file = Path("reference.bib")
        has_bib = bib_file.exists()
        print(f"📚 Bibliography: {'✅ Found' if has_bib else '❌ Not found'}")
        
        # Build advanced command
        cmd = [
            'pandoc',
            tex_file.name,
            '-o', html_file.name,
            '--standalone',                   # Complete HTML document
            '--mathjax',                      # Math rendering
            '--citeproc',                     # Citation processing
        ]
        
        # Add bibliography if available
        if has_bib:
            cmd.extend(['--bibliography', 'reference.bib'])
            print("📖 Added bibliography processing")
        
        # Add CSS styling
        cmd.extend([
            '--css', 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css'
        ])
        
        # Create custom academic CSS
        css_content = """
        body {
            font-family: 'Times New Roman', serif;
            max-width: 8.5in;
            margin: 0 auto;
            padding: 1in;
            line-height: 1.6;
        }
        h1, h2, h3 { font-weight: bold; }
        p { text-align: justify; }
        """
        
        with open('academic.css', 'w') as f:
            f.write(css_content)
        cmd.extend(['--css', 'academic.css'])
        print("🎨 Added academic styling")
        
        print(f"🔧 Full command: {' '.join(cmd)}")
        
        # Run conversion
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Advanced conversion successful!")
            if html_file.exists():
                size = html_file.stat().st_size
                print(f"📊 HTML file size: {size:,} bytes")
                
                # Show first few lines
                print("\n📖 First 5 lines of HTML:")
                with open(html_file, 'r') as f:
                    for i, line in enumerate(f):
                        if i >= 5:
                            break
                        print(f"   {line.rstrip()}")
        else:
            print(f"❌ Conversion failed: {result.stderr}")
        
        # Cleanup
        if Path('academic.css').exists():
            Path('academic.css').unlink()
        
    finally:
        os.chdir(original_dir)
    
    return html_file if html_file.exists() else None

def compare_outputs(tex_file_path):
    """
    Compare the outputs of simple vs advanced compilation
    """
    print("\n📊 COMPARISON: Simple vs Advanced")
    print("=" * 40)
    
    tex_file = Path(tex_file_path)
    
    # Simple compilation
    simple_html = simple_compile_to_html(tex_file)
    
    # Advanced compilation  
    advanced_html = advanced_compile_to_html(tex_file)
    
    if simple_html and advanced_html:
        simple_size = simple_html.stat().st_size
        advanced_size = advanced_html.stat().st_size
        
        print(f"\n📈 Size comparison:")
        print(f"   Simple:   {simple_size:,} bytes")
        print(f"   Advanced: {advanced_size:,} bytes")
        print(f"   Difference: {advanced_size - simple_size:,} bytes")
        
        print(f"\n🌐 Generated files:")
        print(f"   Simple:   {simple_html}")
        print(f"   Advanced: {advanced_html}")

def explain_key_concepts():
    """
    Explain the key concepts in HTML compilation
    """
    print("\n📖 KEY CONCEPTS EXPLAINED")
    print("=" * 40)
    
    concepts = {
        "pandoc": "Universal document converter - converts LaTeX to HTML",
        "--standalone": "Creates complete HTML with <html>, <head>, <body> tags",
        "--mathjax": "Enables mathematical equation rendering in browsers",
        "--citeproc": "Processes \\cite{} commands and generates bibliography",
        "--bibliography": "Specifies the .bib file containing references",
        "--css": "Links CSS stylesheets for visual formatting",
        "Working directory": "pandoc runs in the same directory as the LaTeX file",
        "File paths": "All paths are relative to the working directory"
    }
    
    for concept, explanation in concepts.items():
        print(f"🔧 {concept:<20}: {explanation}")

if __name__ == "__main__":
    print("🐍 SIMPLE HTML COMPILATION UNDERSTANDING")
    print("=" * 50)
    
    # Find a test file
    test_file = Path("posts/2025/2025-09-20-bibliography-test.tex")
    if not test_file.exists():
        # Find any .tex file
        tex_files = list(Path("posts/2025").glob("*.tex"))
        if tex_files:
            test_file = tex_files[0]
        else:
            print("❌ No .tex files found in posts/2025")
            exit(1)
    
    print(f"📄 Using test file: {test_file}")
    
    # Explain concepts first
    explain_key_concepts()
    
    # Run comparisons
    compare_outputs(test_file)
    
    print("\n🎯 SUMMARY")
    print("=" * 20)
    print("✅ You now understand:")
    print("• How pandoc converts LaTeX to HTML")
    print("• The difference between basic and advanced compilation")
    print("• How bibliography processing works")
    print("• How CSS styling is applied")
    print("• Why we change working directories")
