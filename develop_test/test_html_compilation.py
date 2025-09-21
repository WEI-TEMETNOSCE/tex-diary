#!/usr/bin/env python3
"""
Test script to understand HTML compilation process
This script demonstrates how the compile_to_html function works step by step
"""

import subprocess
import shutil
from pathlib import Path
import os

def create_academic_css():
    """
    Create the academic CSS styling for HTML output
    This is the same function used in the main diary script
    """
    return """
/* Academic Paper Styling for Diary HTML Output */
body {
    font-family: 'Times New Roman', Times, serif;
    line-height: 1.6;
    max-width: 8.5in;
    margin: 0 auto;
    padding: 1in;
    background-color: #ffffff;
    color: #000000;
}

/* Typography */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Times New Roman', Times, serif;
    font-weight: bold;
    margin-top: 1.5em;
    margin-bottom: 0.5em;
}

h1 { font-size: 1.5em; text-align: center; }
h2 { font-size: 1.3em; }
h3 { font-size: 1.1em; }

/* Paragraphs */
p {
    text-align: justify;
    margin-bottom: 1em;
    text-indent: 0;
}

/* Academic spacing */
.title {
    text-align: center;
    font-size: 1.8em;
    font-weight: bold;
    margin-bottom: 0.5em;
}

.author {
    text-align: center;
    font-size: 1.1em;
    margin-bottom: 2em;
}

/* Math formatting */
.math {
    font-family: 'Computer Modern', 'Times New Roman', serif;
}

/* Bibliography */
.references {
    margin-top: 2em;
    border-top: 1px solid #ccc;
    padding-top: 1em;
}

/* Citations */
.citation {
    font-style: italic;
}

/* Code blocks */
pre {
    background-color: #f5f5f5;
    border: 1px solid #ddd;
    border-radius: 4px;
    padding: 1em;
    overflow-x: auto;
    font-family: 'Courier New', monospace;
    font-size: 0.9em;
}

/* Responsive adjustments */
@media screen and (max-width: 768px) {
    body {
        padding: 0.5in;
        max-width: 100%;
    }
}
"""

def compile_to_html_test(tex_file_path):
    """
    Test version of compile_to_html function with detailed logging
    This shows exactly what happens during HTML compilation
    """
    print("🔍 HTML Compilation Test - Step by Step")
    print("=" * 50)
    
    # Convert to Path object
    tex_file = Path(tex_file_path)
    
    # Check if pandoc is available
    print(f"1️⃣ Checking pandoc availability...")
    if not shutil.which('pandoc'):
        raise RuntimeError("pandoc not found - install with: brew install pandoc")
    print("   ✅ pandoc found!")
    
    # Set up file paths
    tex_dir = tex_file.parent
    tex_name = tex_file.name
    html_file = tex_file.parent / (tex_file.stem + '.html')
    
    print(f"2️⃣ File paths:")
    print(f"   📁 Working directory: {tex_dir}")
    print(f"   📄 LaTeX file: {tex_name}")
    print(f"   🌐 HTML output: {html_file.name}")
    
    # Change to the LaTeX file directory
    original_dir = os.getcwd()
    print(f"3️⃣ Changing directory from {original_dir} to {tex_dir}")
    os.chdir(tex_dir)
    
    try:
        # Check for bibliography file (should be symlinked in output directory during real compilation)
        # For this test, we'll check the main bibliography location
        main_bib = Path(original_dir) / "latex/bibliography/reference.bib"
        local_bib = Path("reference.bib") 
        
        print(f"4️⃣ Checking for bibliography file:")
        print(f"   📍 Local: {local_bib}")
        print(f"   📍 Main: {main_bib}")
        
        bib_exists = local_bib.exists() or main_bib.exists()
        if main_bib.exists() and not local_bib.exists():
            # Create a temporary symlink for testing
            try:
                local_bib.symlink_to(main_bib.resolve())
                print(f"   🔗 Created temporary symlink to bibliography")
            except:
                # If symlink fails, copy the file
                shutil.copy(main_bib, local_bib)
                print(f"   📋 Copied bibliography file")
        
        print(f"   {'✅' if bib_exists else '❌'} Bibliography {'available' if bib_exists else 'not available'}")
        
        # Build pandoc command
        print("5️⃣ Building pandoc command...")
        cmd = ['pandoc', tex_name, '-o', html_file.name, 
               '--standalone', '--mathjax',
               '--citeproc',  # Enable citation processing
               '--css', 'https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css']
        
        # Add bibliography if it exists
        if bib_exists:
            cmd.extend(['--bibliography', 'reference.bib'])
            print("   📚 Added bibliography processing")
        
        # Create and add custom CSS
        print("6️⃣ Creating academic CSS file...")
        css_content = create_academic_css()
        css_file = Path("academic.css")  # Create in current directory (tex_dir)
        with open(css_file, 'w') as f:
            f.write(css_content)
        cmd.extend(['--css', 'academic.css'])
        print(f"   ✅ Created {css_file} in {tex_dir}")
        
        # Show the complete command
        print("7️⃣ Complete pandoc command:")
        print(f"   {' '.join(cmd)}")
        
        # Run pandoc
        print("8️⃣ Running pandoc...")
        result = subprocess.run(cmd, capture_output=True, text=True)
        
        if result.returncode == 0:
            print("   ✅ Pandoc conversion successful!")
        else:
            print("   ❌ Pandoc conversion had issues:")
            print(f"   Error: {result.stderr}")
            
        # Show output information
        if html_file.exists():
            file_size = html_file.stat().st_size
            print(f"9️⃣ HTML file generated successfully!")
            print(f"   📊 File size: {file_size:,} bytes ({file_size/1024:.1f} KB)")
            
            # Show first few lines of HTML
            print("🔍 First 10 lines of generated HTML:")
            with open(html_file, 'r') as f:
                for i, line in enumerate(f):
                    if i >= 10:
                        break
                    print(f"   {i+1:2d}: {line.rstrip()}")
        else:
            print("   ❌ HTML file was not generated")
            
        # Clean up temporary files
        print("🧹 Cleaning up temporary files...")
        if css_file.exists():
            css_file.unlink()
            print(f"   🗑️ Removed {css_file}")
        
        # Clean up temporary bibliography file if we created it
        if local_bib.exists() and main_bib.exists():
            try:
                local_bib.unlink()
                print(f"   🗑️ Removed temporary bibliography file")
            except:
                pass
            
    finally:
        # Return to original directory
        os.chdir(original_dir)
        print(f"🔄 Returned to original directory: {original_dir}")
    
    return html_file if html_file.exists() else None

def test_with_sample_file():
    """
    Test the HTML compilation with an existing LaTeX file from 2025
    """
    print("\n" + "="*60)
    print("🧪 TESTING HTML COMPILATION")
    print("="*60)
    
    # Find a LaTeX file from 2025 to test with
    posts_dir = Path("posts/2025")
    if not posts_dir.exists():
        print("❌ No posts/2025 directory found")
        return
    
    # Look for LaTeX files
    tex_files = list(posts_dir.glob("*.tex"))
    if not tex_files:
        print("❌ No .tex files found in posts/2025")
        return
    
    # Use the first available file (or the bibliography test file if it exists)
    test_file = None
    for tex_file in tex_files:
        if "bibliography-test" in tex_file.name:
            test_file = tex_file
            break
    
    if not test_file:
        test_file = tex_files[0]  # Use the first available file
    
    print(f"📄 Testing with file: {test_file}")
    
    try:
        result_html = compile_to_html_test(test_file)
        if result_html:
            print(f"\n🎉 SUCCESS! HTML file created: {result_html}")
            print(f"📂 You can open it with: open {result_html}")
        else:
            print("\n❌ FAILED! HTML file was not created")
    except Exception as e:
        print(f"\n💥 ERROR: {e}")

def explain_pandoc_options():
    """
    Explain what each pandoc option does
    """
    print("\n" + "="*60)
    print("📖 PANDOC OPTIONS EXPLAINED")
    print("="*60)
    
    options = {
        "--standalone": "Creates a complete HTML document (not just a fragment)",
        "--mathjax": "Enables MathJax for rendering LaTeX math equations",
        "--citeproc": "Processes citations and generates bibliography",
        "--css URL": "Links to external CSS for styling",
        "--bibliography file.bib": "Specifies the bibliography file to use",
        "-o output.html": "Specifies the output file name"
    }
    
    for option, description in options.items():
        print(f"🔧 {option:<25} : {description}")

if __name__ == "__main__":
    print("🐍 HTML Compilation Test Script")
    print("This script helps you understand how compile_to_html works")
    
    # Explain pandoc options first
    explain_pandoc_options()
    
    # Test with an actual file
    test_with_sample_file()
    
    print("\n" + "="*60)
    print("✅ Test completed! You now understand:")
    print("• How pandoc converts LaTeX to HTML")
    print("• How bibliography processing works")
    print("• How custom CSS is applied")
    print("• The complete workflow step-by-step")
    print("="*60)
