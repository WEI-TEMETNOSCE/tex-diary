# HTML Templates and CSS Customization

This directory contains both HTML templates and CSS templates for complete customization of your research diary blog.

## Template System Overview

The diary system now uses a **template-based approach** similar to the LaTeX template system, allowing you to customize both the structure (HTML) and appearance (CSS) of your blog without modifying Python code.

## Available Templates

### HTML Templates
- **`index_template.html`** - Blog index page structure with Mustache-style templating
- **`entry_template.html`** - Individual blog post page structure

### CSS Templates
- **`blog_post.css`** - Enhanced LaTeX-style blog post with theorem environments
- **`blog_post_simple.css`** - Clean, minimal blog post style
- **`blog_index.css`** - Modern grid-based blog index (full mode)
- **`blog_index_compact.css`** - Minimal table-of-contents style index

## HTML Template Syntax

Templates use **Mustache-style syntax** for dynamic content:

### Variables
```html
<title>{{PAGE_TITLE}}</title>
<h1>{{BLOG_TITLE}}</h1>
<p>{{AUTHOR}} • {{INSTITUTION}}</p>
```

### Conditional Sections
```html
{{#COMPACT_MODE}}
<!-- Content shown only in compact mode -->
<ul class="posts-list">...</ul>
{{/COMPACT_MODE}}

{{^COMPACT_MODE}}
<!-- Content shown only in non-compact mode -->
<div class="post-list">...</div>
{{/COMPACT_MODE}}
```

### Loops
```html
{{#POSTS}}
<article class="post-item">
    <h2><a href="posts/{{HTML_FILE}}">{{TITLE}}</a></h2>
    <div class="post-date">{{FORMATTED_DATE}}</div>
    <div class="post-excerpt">{{EXCERPT}}</div>
    <div class="post-tags">
        {{#TAGS}}<span class="tag">{{.}}</span>{{/TAGS}}
    </div>
</article>
{{/POSTS}}
```

## Template Variables Reference

### Index Template (`index_template.html`)

**Basic Information:**
- `PAGE_TITLE` - Browser title
- `BLOG_TITLE` - Main blog heading
- `AUTHOR` - Author name from config
- `INSTITUTION` - Institution from config
- `POST_COUNT` - Number of posts
- `TOPICS` - Comma-separated topic list
- `GENERATION_DATE` - When the blog was generated

**Conditionals:**
- `#COMPACT_MODE` / `^COMPACT_MODE` - Layout mode
- `#TOPICS` - If topics exist
- `#POSTS` - Posts array exists

**Post Loop Variables (within `{{#POSTS}}`):**
- `TITLE` - Post title
- `HTML_FILE` - Post filename
- `SHORT_DATE` - Short date format (MM/DD)
- `FORMATTED_DATE` - Full date format (Month DD, YYYY)
- `EXCERPT` - Post excerpt
- `TAGS` - Array of post tags

### Entry Template (`entry_template.html`)

- `TITLE` - Entry title
- `CONTENT` - Main entry content (from pandoc)
- `MATHJAX_MACROS` - Auto-generated LaTeX macro definitions

## Customization Examples

### 1. Custom Index Layout

```html
<!-- Add navigation -->
<nav class="navbar">
    <a href="#recent">Recent</a>
    <a href="#topics">Topics</a>
    <a href="#archive">Archive</a>
</nav>

<!-- Custom post cards -->
{{#POSTS}}
<div class="custom-post-card">
    <div class="post-meta">
        <span class="date">{{SHORT_DATE}}</span>
        <div class="tags">{{#TAGS}}#{{.}} {{/TAGS}}</div>
    </div>
    <h3><a href="posts/{{HTML_FILE}}">{{TITLE}}</a></h3>
    <p class="snippet">{{EXCERPT}}</p>
</div>
{{/POSTS}}
```

### 2. Custom Entry Template

```html
<!-- Custom header with metadata -->
<header class="entry-header">
    <h1 class="entry-title">{{TITLE}}</h1>
    <div class="entry-meta">
        <time>{{FORMATTED_DATE}}</time>
        <span class="reading-time">5 min read</span>
    </div>
</header>

<!-- Main content -->
<main class="entry-content">
    {{CONTENT}}
</main>

<!-- Custom footer -->
<footer class="entry-footer">
    <p>📚 Part of my research diary series</p>
    <a href="../index.html">← Back to all entries</a>
</footer>
```

### 3. CSS Customization

```css
/* Custom color scheme */
:root {
    --primary-color: #8b0000;    /* Dark red */
    --secondary-color: #ff6b6b;  /* Light red */
    --background-color: #fafafa; /* Light gray */
}

/* Custom fonts */
body {
    font-family: 'Helvetica Neue', Arial, sans-serif;
}

/* Custom post styling */
.post-item {
    border-left: 4px solid var(--primary-color);
    background: linear-gradient(135deg, #fff, #f9f9f9);
}
```

## Advanced Features

### Automatic LaTeX Integration

The template system automatically integrates with the LaTeX command system:

1. **MathJax Macros**: LaTeX commands are converted to MathJax macros
2. **199+ Commands**: All your custom LaTeX commands work in HTML
3. **Automatic Discovery**: New commands in `.sty` files are automatically included

### Responsive Design

Templates include responsive design features:

```html
<!-- Mobile-friendly meta tag -->
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<!-- Responsive layout -->
{{#COMPACT_MODE}}
<!-- Mobile-optimized compact layout -->
{{/COMPACT_MODE}}
```

### Fallback System

Robust fallback system ensures your blog always works:

1. **Template Loading**: Custom template → Legacy hardcoded HTML
2. **CSS Loading**: Custom CSS → Basic fallback CSS
3. **Error Handling**: Graceful degradation on template errors

## File Structure

```
assets/html_templates/
├── index_template.html      # Blog index structure
├── entry_template.html      # Blog post structure
├── blog_post.css           # Enhanced post styling
├── blog_post_simple.css    # Simple post styling
├── blog_index.css          # Full index styling
├── blog_index_compact.css  # Compact index styling
└── README.md               # This documentation
```

## Benefits

1. **🎨 Complete Control** - Customize both structure and appearance
2. **🔧 Easy Maintenance** - No Python code changes needed
3. **📱 Responsive** - Mobile-friendly by default
4. **🧮 LaTeX Integration** - Seamless math rendering
5. **🚀 Extensible** - Easy to add new features
6. **🔄 Consistent** - Same approach as LaTeX templates

## Getting Started

1. **Basic Customization**: Edit existing CSS files for colors/fonts
2. **Layout Changes**: Modify HTML templates for structure
3. **New Features**: Add template variables and CSS classes
4. **Testing**: Use `./diary blog <tag>` to see changes

## Tips

- **Backup**: Keep copies of working templates before major changes
- **Test**: Always test on different screen sizes
- **Iterate**: Make small changes and test frequently
- **Inspect**: Use browser dev tools to understand the structure
- **Learn**: Study existing templates to understand the system

---

*Generated by Research Diary System - Template System v2.0*