# 🚀 Deployment Guide - GitHub Pages

This guide explains how to deploy the PC Build Guide documentation to GitHub Pages.

## 📋 Prerequisites

1. **GitHub Account**: Ensure you have a GitHub account
2. **Repository**: Create a new repository on GitHub
3. **Local Git**: Have Git installed locally

## 🔄 Step-by-Step Deployment

### 1. Initialize Git Repository

```bash
# Navigate to project directory
cd /path/to/pc-build-guide

# Initialize git (if not already done)
git init

# Add all files
git add .

# Create initial commit
git commit -m "Initial commit: Complete PC Build Guide"
```

### 2. Connect to GitHub Repository

```bash
# Add your GitHub repository as remote
git remote add origin https://github.com/YOUR_USERNAME/pc-build-guide.git

# Push to GitHub
git branch -M main
git push -u origin main
```

### 3. Enable GitHub Pages

1. Go to your repository on GitHub
2. Click on **Settings** tab
3. Scroll down to **Pages** section
4. Under **Source**, select **GitHub Actions**
5. The workflow will automatically trigger

### 4. Configure Repository Settings

Update `mkdocs.yml` with your repository details:

```yaml
# Update these lines in mkdocs.yml
site_url: https://YOUR_USERNAME.github.io/pc-build-guide/
repo_name: YOUR_USERNAME/pc-build-guide
repo_url: https://github.com/YOUR_USERNAME/pc-build-guide
```

### 5. Wait for Deployment

- GitHub Actions will automatically build and deploy
- Check the **Actions** tab for deployment status
- Once complete, visit: `https://YOUR_USERNAME.github.io/pc-build-guide/`

## 🛠️ GitHub Actions Workflow

The `.github/workflows/deploy.yml` file handles:

- ✅ **Automatic Triggers**: Deploys on push to main branch
- 🐍 **Python Setup**: Installs Python 3.11 and dependencies
- 📦 **Dependency Caching**: Speeds up builds
- 🏗️ **MkDocs Build**: Generates static documentation
- 🚀 **GitHub Pages Deploy**: Publishes to GitHub Pages

## 🔧 Customization Options

### Custom Domain (Optional)

1. Add `CNAME` file to `docs/` directory:
```
your-domain.com
```

2. Configure DNS settings at your domain provider
3. Update `site_url` in `mkdocs.yml`

### Environment Variables

For web scraping features, add GitHub Secrets:

1. Go to **Settings** → **Secrets and variables** → **Actions**
2. Add required API keys:
   - `AMAZON_API_KEY`
   - `FLIPKART_API_KEY`
   - etc.

## 📊 Monitoring and Analytics

### GitHub Pages Analytics

- Monitor traffic in repository **Insights** → **Traffic**
- Track popular pages and referrers
- View unique visitors and page views

### Google Analytics (Optional)

Add to `mkdocs.yml`:
```yaml
extra:
  analytics:
    provider: google
    property: G-XXXXXXXXXX
```

## 🔄 Update Workflow

### For Content Updates

1. Edit documentation files locally
2. Commit and push changes:
```bash
git add .
git commit -m "Update: Component specifications"
git push origin main
```

3. GitHub Actions automatically rebuilds and deploys

### For Structure Changes

1. Update `mkdocs.yml` navigation
2. Add new files to appropriate directories
3. Test locally: `mkdocs serve`
4. Commit and push changes

## 🐛 Troubleshooting

### Common Issues

**Build Fails - Missing Dependencies**
```yaml
# Add to deploy.yml if needed
- name: Install additional dependencies
  run: pip install mkdocs-redirects mkdocs-minify-plugin
```

**404 on Custom Links**
- Check file paths in navigation
- Ensure markdown files exist
- Verify case sensitivity

**Slow Build Times**
- Check for large files in repository
- Optimize images and assets
- Use caching effectively

### Debug Locally

```bash
# Test build locally
mkdocs build --clean --strict

# Serve locally for testing
mkdocs serve --dev-addr=127.0.0.1:8000
```

## 📈 Performance Optimization

### Build Optimization

1. **Image Optimization**: Compress images before adding
2. **Caching**: Leverage GitHub Actions caching
3. **Minification**: Use `mkdocs-minify-plugin`

### Loading Speed

1. **CDN Assets**: Use Material theme's CDN
2. **Lazy Loading**: Enable for images
3. **Code Splitting**: Minimize JavaScript

## 🔐 Security Considerations

### API Keys and Secrets

- Never commit API keys to repository
- Use GitHub Secrets for sensitive data
- Rotate keys regularly

### Content Security

- Review external links regularly
- Validate user-contributed content
- Monitor for malicious changes

## 📞 Support and Resources

### GitHub Pages Documentation
- [GitHub Pages Docs](https://docs.github.com/en/pages)
- [Custom Domains](https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site)

### MkDocs Resources
- [MkDocs Documentation](https://www.mkdocs.org/)
- [Material Theme Guide](https://squidfunk.github.io/mkdocs-material/)

### Community Help
- [GitHub Discussions](https://github.com/YOUR_USERNAME/pc-build-guide/discussions)
- [MkDocs Community](https://github.com/mkdocs/mkdocs/discussions)

---

**🎉 Congratulations! Your PC Build Guide is now live on GitHub Pages!**

*Visit your site at: `https://YOUR_USERNAME.github.io/pc-build-guide/`*