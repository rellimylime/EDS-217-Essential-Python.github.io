#!/usr/bin/env python3
"""
EDS 217 Documentation Build Script (Python version)
This script builds the Quarto website and prepares it for GitHub Pages deployment
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

def run_command(command, description):
    """Run a shell command and handle errors."""
    print(f"🔨 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        return result
    except subprocess.CalledProcessError as e:
        print(f"❌ Error: {description} failed")
        print(f"   Command: {command}")
        print(f"   Error: {e.stderr}")
        sys.exit(1)

def check_prerequisites():
    """Check if required tools are available."""
    print("🔍 Checking prerequisites...")
    
    # Check if quarto is installed
    try:
        subprocess.run(["quarto", "--version"], check=True, capture_output=True)
        print("   ✅ Quarto found")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Error: Quarto is not installed or not in PATH")
        print("Please install Quarto from https://quarto.org/docs/get-started/")
        sys.exit(1)
    
    # Check if we're in the right directory
    if not Path("_quarto.yml").exists():
        print("❌ Error: _quarto.yml not found. Are you in the project root directory?")
        sys.exit(1)
    print("   ✅ _quarto.yml found")

def clean_docs():
    """Clean the docs directory."""
    print("🧹 Cleaning previous build...")
    docs_path = Path("docs")
    if docs_path.exists():
        shutil.rmtree(docs_path)
        print("   Previous build files removed")

def build_site():
    """Build the Quarto website."""
    print("🔨 Building Quarto website...")
    run_command("quarto render", "Quarto render")

def verify_build():
    """Verify the build was successful."""
    docs_path = Path("docs")
    
    if not docs_path.exists() or not any(docs_path.iterdir()):
        print("❌ Error: docs directory is empty or doesn't exist after build")
        sys.exit(1)
    
    print("✅ Build completed successfully!")
    print("📁 Documentation built in docs/ directory")
    
    # Count files and get size
    file_count = len(list(docs_path.rglob("*")))
    size_result = subprocess.run(["du", "-sh", "docs"], capture_output=True, text=True)
    size = size_result.stdout.split()[0] if size_result.returncode == 0 else "unknown"
    
    print("📊 Build summary:")
    print(f"   - Files in docs/: {file_count}")
    print(f"   - Size: {size}")
    
    # Check critical files
    index_html = docs_path / "index.html"
    nojekyll = docs_path / ".nojekyll"
    
    if index_html.exists():
        print("   - ✅ index.html found")
    else:
        print("   - ⚠️  index.html not found")
    
    if nojekyll.exists():
        print("   - ✅ .nojekyll found (GitHub Pages compatibility)")
    else:
        print("   - ⚠️  .nojekyll not found")

def main():
    """Main build process."""
    print("🚀 Starting EDS 217 documentation build...")
    
    try:
        check_prerequisites()
        clean_docs()
        build_site()
        verify_build()
        
        print("")
        print("🎉 Your site is ready for deployment!")
        print("📝 Next steps:")
        print("   1. Review the built site in the docs/ folder")
        print("   2. Commit and push changes to your repository")
        print("   3. Your GitHub Pages site will update automatically")
        print("")
        print("🌐 To preview locally, you can run:")
        print("   quarto preview")
        
    except KeyboardInterrupt:
        print("\n❌ Build cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Unexpected error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main() 