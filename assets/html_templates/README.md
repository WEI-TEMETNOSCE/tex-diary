# HTML Templates and CSS Customization

This directory contains CSS templates for customizing the appearance of your blog.

## Available CSS Templates

### Blog Post Styles

1. **`blog_post.css`** - Enhanced LaTeX-style blog post with theorem environments
   - Professional academic appearance
   - Styled theorem, proof, definition, lemma environments
   - LaTeX-like typography
   - Responsive design

2. **`blog_post_simple.css`** - Clean, minimal blog post style
   - Simple and readable
   - Good for general blog posts
   - Lightweight and fast

### Blog Index Styles

1. **`blog_index.css`** - Modern grid-based blog index
   - Card-based layout
   - Gradient background
   - Hover effects and animations
   - Responsive grid

## Customization

### Easy Customization Options

You can easily customize the appearance by:

1. **Editing existing CSS files** - Modify colors, fonts, spacing, etc.
2. **Creating new themes** - Copy an existing CSS file and modify it
3. **Switching themes** - Update the diary script to use different templates

### Common Customizations

#### Colors
- **Primary color**: Change `#3498db` to your preferred color
- **Text color**: Modify `#2c3e50` for headings
- **Background**: Update `background-color` or `background` properties

#### Fonts
- **Main font**: Change `font-family` in the `body` selector
- **Math font**: LaTeX fonts work well with `'Computer Modern'`

#### Layout
- **Width**: Adjust `max-width` in the `body` selector
- **Spacing**: Modify `margin` and `padding` values
- **Responsive breakpoints**: Update `@media` queries

### Example: Creating a Dark Theme

```css
body {
    background-color: #1a1a1a;
    color: #e0e0e0;
}

h1, h2, h3 {
    color: #ffffff;
}

.post-card {
    background: #2d2d2d;
    border-left: 4px solid #e74c3c;
}
```

## File Structure

```
assets/html_templates/
├── blog_post.css          # Enhanced LaTeX-style post
├── blog_post_simple.css   # Simple clean post
├── blog_index.css         # Modern index page
└── README.md              # This file
```

## Integration

The diary script automatically loads CSS templates from this directory. You can:

1. **Edit existing files** - Changes take effect immediately
2. **Add new themes** - Create new CSS files and reference them in the script
3. **Override styles** - Add custom CSS rules to override defaults

## Tips

- **Test changes**: Use the blog generation command to see your changes
- **Backup originals**: Keep copies of working CSS before major changes  
- **Use browser dev tools**: Inspect elements to understand the CSS structure
- **Mobile-first**: Always test on different screen sizes
