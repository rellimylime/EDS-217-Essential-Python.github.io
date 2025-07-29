# Documentation Build Scripts

This repository includes scripts to build the EDS 217 course website for GitHub Pages deployment.

## Overview

The EDS 217 website is built using [Quarto](https://quarto.org/), which renders `.qmd` and `.ipynb` files into a static website deployed to the `docs/` folder for GitHub Pages.

## Available Scripts

### 1. Shell Script (Recommended for Unix/Linux/macOS)
```bash
./build_docs.sh
```

### 2. Python Script (Cross-platform)
```bash
python build_docs.py
# or
./build_docs.py
```

## What the Scripts Do

1. **Check Prerequisites**: Verify that Quarto is installed and you're in the correct directory
2. **Clean Previous Build**: Remove old files from the `docs/` directory
3. **Build Website**: Run `quarto render` to generate the static site
4. **Verify Build**: Check that the build completed successfully and required files exist
5. **Report Status**: Show build summary and next steps

## Prerequisites

- [Quarto](https://quarto.org/docs/get-started/) must be installed
- Run the script from the project root directory (where `_quarto.yml` is located)

## Typical Workflow

1. Make changes to your `.qmd` files or course materials
2. Run one of the build scripts:
   ```bash
   ./build_docs.sh
   ```
3. Review the built site in the `docs/` folder
4. Commit and push changes to GitHub:
   ```bash
   git add .
   git commit -m "Update course content and rebuild site"
   git push origin main
   ```
5. GitHub Pages will automatically deploy the updated site

## Local Preview

To preview your changes locally before building:
```bash
quarto preview
```

## Troubleshooting

- **"Quarto not found"**: Install Quarto from https://quarto.org/docs/get-started/
- **"_quarto.yml not found"**: Make sure you're running the script from the project root directory
- **Build fails**: Check the error messages and ensure all `.qmd` files have valid syntax

## Manual Build

If you prefer to build manually:
```bash
quarto render
``` 