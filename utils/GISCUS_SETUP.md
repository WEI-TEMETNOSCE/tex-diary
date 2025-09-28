# Giscus Discussion Forum Setup Guide

This guide will help you set up Giscus (GitHub Discussions) for your research diary blog.

## Prerequisites

1. A GitHub repository for your diary/blog
2. GitHub Discussions enabled on your repository

## Step 1: Enable GitHub Discussions

1. Go to your GitHub repository
2. Click on the **Settings** tab
3. Scroll down to the **Features** section
4. Check the **Discussions** checkbox to enable it
5. Click **Set up discussions** if prompted

## Step 2: Get Giscus Configuration Values

1. Visit [giscus.app](https://giscus.app)
2. Fill in the configuration form:

   **Repository**: Select your repository (e.g., `username/diary`)
   
   **Discussion Category**: Choose a category (e.g., "General", "Q&A", "Comments")
   
   **Features**: 
   - ✅ Enable reactions
   - ✅ Enable discussion metadata
   - ✅ Enable strict mapping
   
   **Theme**: Choose a theme that matches your blog (e.g., "Light", "Dark", "Preferred color scheme")
   
   **Language**: Select your preferred language

3. Copy the generated configuration values

## Step 3: Update config.yaml

Edit your `config.yaml` file and update the following values:

```yaml
# Discussion Forum Settings
enable_discussion_forum: true
forum_type: "giscus"
giscus_repo: "your-username/your-repo-name"  # e.g., "qiangliu/diary"
giscus_repo_id: "R_xxxxxxxxxx"  # Get from giscus.app
giscus_category: "General"  # Your chosen category
giscus_category_id: "DIC_kwxxxxxxxxxx"  # Get from giscus.app
giscus_mapping: "pathname"  # How discussions are mapped
giscus_strict: "0"  # Strict mode
giscus_reactions_enabled: "1"  # Enable reactions
giscus_emit_metadata: "0"  # Emit metadata
giscus_input_position: "bottom"  # Input position
giscus_theme: "light"  # Theme
giscus_lang: "en"  # Language
```

## Step 4: Test the Integration

1. Convert a blog post using your latex2html script:
   ```bash
   ./latex2html posts/2025/2025-09-22.tex output_folder --template assets/html_templates/entry_template.html --css assets/html_templates/blog_post.css
   ```

2. Open the generated HTML file in a browser
3. Scroll to the bottom to see the discussion forum
4. Test posting a comment (you'll need to be logged into GitHub)

## Configuration Options

### Forum Types
- `giscus`: GitHub Discussions (recommended)
- `disqus`: Disqus comments (not yet implemented)
- `utterances`: GitHub Issues (not yet implemented)
- `none`: No forum

### Giscus Themes
- `light`: Light theme
- `dark`: Dark theme
- `dark_dimmed`: GitHub dark theme
- `transparent_dark`: Transparent dark
- `preferred_color_scheme`: Follows system preference

### Mapping Options
- `pathname`: Maps to page path
- `url`: Maps to full URL
- `title`: Maps to page title
- `og:title`: Maps to Open Graph title

## Troubleshooting

### Forum Not Appearing
1. Check that `enable_discussion_forum: true` in config.yaml
2. Verify `giscus_repo` and `giscus_repo_id` are correct
3. Ensure GitHub Discussions are enabled on your repository

### Comments Not Loading
1. Check browser console for JavaScript errors
2. Verify repository permissions (public repositories work best)
3. Ensure the category ID is correct

### Styling Issues
1. The forum should automatically match your blog's theme
2. Custom CSS can be added to `blog_post.css` under `.discussion-forum`

## Advanced Configuration

### Custom Styling
Add custom CSS to `assets/html_templates/blog_post.css`:

```css
.discussion-forum {
    /* Your custom styles */
}

.giscus {
    /* Giscus-specific styles */
}
```

### Multiple Categories
You can create different categories for different types of discussions:
- General comments
- Questions
- Suggestions
- Bug reports

## Security Notes

- Giscus uses GitHub's authentication system
- Comments are stored in GitHub Discussions
- You have full moderation control through GitHub
- No personal data is collected by Giscus

## Support

- [Giscus Documentation](https://github.com/giscus/giscus)
- [GitHub Discussions Help](https://docs.github.com/en/discussions)
- [Giscus Configuration](https://giscus.app)

---

**Note**: This setup requires a GitHub repository. If you don't have one, you can create a new repository specifically for your blog discussions.
