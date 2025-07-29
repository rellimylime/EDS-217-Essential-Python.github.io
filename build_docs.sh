#!/bin/bash

# EDS 217 Documentation Build Script
# This script builds the Quarto website and prepares it for GitHub Pages deployment

set -e  # Exit on any error

echo "🚀 Starting EDS 217 documentation build..."

# Check if quarto is installed
if ! command -v quarto &> /dev/null; then
    echo "❌ Error: Quarto is not installed or not in PATH"
    echo "Please install Quarto from https://quarto.org/docs/get-started/"
    exit 1
fi

# Check if we're in the right directory (look for _quarto.yml)
if [ ! -f "_quarto.yml" ]; then
    echo "❌ Error: _quarto.yml not found. Are you in the project root directory?"
    exit 1
fi

# Clean the docs directory first (optional - comment out if you want incremental builds)
echo "🧹 Cleaning previous build..."
if [ -d "docs" ]; then
    rm -rf docs/*
    echo "   Previous build files removed"
fi

# Build the documentation
echo "🔨 Building Quarto website..."
quarto render

# Check if build was successful
if [ $? -eq 0 ]; then
    echo "✅ Build completed successfully!"
    
    # Check if docs directory exists and has content
    if [ -d "docs" ] && [ "$(ls -A docs)" ]; then
        echo "📁 Documentation built in docs/ directory"
        echo "📊 Build summary:"
        echo "   - Files in docs/: $(find docs -type f | wc -l)"
        echo "   - Size: $(du -sh docs | cut -f1)"
        
        # Verify critical files exist
        if [ -f "docs/index.html" ]; then
            echo "   - ✅ index.html found"
        else
            echo "   - ⚠️  index.html not found"
        fi
        
        if [ -f "docs/.nojekyll" ]; then
            echo "   - ✅ .nojekyll found (GitHub Pages compatibility)"
        else
            echo "   - ⚠️  .nojekyll not found"
        fi
        
        echo ""
        echo "🎉 Your site is ready for deployment!"
        echo "📝 Next steps:"
        echo "   1. Review the built site in the docs/ folder"
        echo "   2. Commit and push changes to your repository"
        echo "   3. Your GitHub Pages site will update automatically"
        echo ""
        echo "🌐 To preview locally, you can run:"
        echo "   quarto preview"
        
    else
        echo "❌ Error: docs directory is empty or doesn't exist after build"
        exit 1
    fi
else
    echo "❌ Build failed! Check the error messages above."
    exit 1
fi 