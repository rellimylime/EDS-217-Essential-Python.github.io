# EDS 217 Environment Migration Guide: Python 3.11

This guide will help you migrate from the `eds217_2024` environment (Python 3.10) to the new `eds217_2025` environment (Python 3.11).

## Step 1: Export Current Environment (Optional Backup)

If you want to keep a backup of your current environment packages:

```bash
# Activate your current environment
conda activate eds217_2024

# Export the environment to a backup file
conda env export > eds217_2024_backup.yml
```

## Step 2: Create New Python 3.11 Environment

### Option A: Using the provided environment.yml file

```bash
# Create the new environment from the environment.yml file
conda env create -f environment.yml

# Activate the new environment
conda activate eds217_2025
```

### Option B: Manual creation

```bash
# Create new environment with Python 3.11
conda create -n eds217_2025 python=3.11

# Activate the new environment
conda activate eds217_2025

# Install core packages with version constraints
conda install \
  "numpy>=2.3,<3.0" \
  "pandas>=2.3,<3.0" \
  "matplotlib>=3.9,<4.0" \
  "seaborn>=0.13,<1.0" \
  jupyter \
  "jupyterlab>=4.4,<5.0" \
  "ipykernel>=6.30" \
  "scipy>=1.11" \
  "scikit-learn>=1.3" \
  "plotly>=5.17" \
  "requests>=2.31" \
  "beautifulsoup4>=4.12" \
  "lxml>=4.9" \
  "openpyxl>=3.1" \
  "xlrd>=2.0" \
  "statsmodels>=0.14"
```

## Step 3: Register the New Environment with Jupyter

```bash
# Make sure you're in the new environment
conda activate eds217_2025

# Register the environment as a Jupyter kernel
python -m ipykernel install --user --name eds217_2025 --display-name "Python 3.11 (EDS 217 2025)"
```

## Step 4: Verify Installation

```bash
# Check Python version
python --version
# Should show: Python 3.11.x

# Check installed packages
conda list

# Launch JupyterLab to test
jupyter lab
```

In JupyterLab, you should now see "Python 3.11 (EDS 217 2025)" as an available kernel option.

## Step 5: Update Your Workflow

- When creating new notebooks, select "Python 3.11 (EDS 217 2025)" as your kernel
- For existing notebooks, you can change the kernel via Kernel → Change Kernel in JupyterLab

## Step 6: Remove Old Environment (Optional)

Once you've verified everything works with the new environment:

```bash
# Remove the old environment
conda env remove -n eds217_2024

# Remove the old Jupyter kernel
jupyter kernelspec remove eds217_2024
```

## Troubleshooting

### If packages are missing:
```bash
conda activate eds217_2025
conda install [package-name]
```

### If you need to add the environment to a specific Jupyter installation:
```bash
conda activate eds217_2025
python -m ipykernel install --user --name eds217_2025
```

### Check available environments:
```bash
conda env list
```

### Check available Jupyter kernels:
```bash
jupyter kernelspec list
```

## Key Benefits of Python 3.11

- **Performance**: 10-60% faster than Python 3.10
- **Better error messages**: More helpful debugging information
- **Enhanced features**: Latest Python language improvements
- **Improved compatibility**: Better support for modern data science libraries

## Package Versions and Rationale

The new environment includes carefully selected packages with version constraints for educational stability:

### Core Data Science Stack
- **Python 3.11.x** - Latest stable Python with 10-60% performance improvements
- **NumPy ≥2.3** - Enhanced array operations and Python 3.11 optimizations
- **Pandas ≥2.3** - Modern DataFrame operations with copy-on-write improvements
- **Matplotlib ≥3.9** - Latest plotting capabilities with better defaults
- **Seaborn ≥0.13** - Statistical visualizations optimized for modern matplotlib
- **JupyterLab ≥4.4** - Enhanced interface with better debugging tools

### Scientific Computing
- **SciPy ≥1.11** - Statistical functions and scientific algorithms
- **Statsmodels ≥0.14** - Advanced statistical modeling capabilities

### Data Access and Processing
- **Requests ≥2.31** - HTTP library for API calls and web data access
- **BeautifulSoup4 ≥4.12** - HTML/XML parsing for web scraping
- **lxml ≥4.9** - Fast XML/HTML parsing backend
- **OpenPyXL ≥3.1** - Modern Excel (.xlsx) file support
- **xlrd ≥2.0** - Legacy Excel (.xls) file support

### Visualization and Analysis
- **Plotly ≥5.17** - Interactive visualizations for enhanced data exploration
- **Scikit-learn ≥1.3** - Machine learning algorithms for introductory ML concepts

### Version Pinning Strategy
All packages include **minimum version constraints** to ensure:
- ✅ Educational stability across student environments
- ✅ Access to modern features and performance improvements
- ✅ Compatibility with Python 3.11 optimizations
- ✅ Security updates and bug fixes

Upper bounds prevent breaking changes while allowing patch updates. 