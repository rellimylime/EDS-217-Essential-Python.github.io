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

# Install core packages
conda install numpy pandas matplotlib seaborn jupyter jupyterlab ipykernel scipy scikit-learn plotly requests beautifulsoup4 lxml openpyxl xlrd

# Install additional packages via pip
pip install geopandas folium
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

## Package Versions Included

The new environment includes:
- Python 3.11.x
- NumPy (latest)
- Pandas (latest)
- Matplotlib (latest)
- Seaborn (latest)
- JupyterLab (latest)
- SciPy (latest)
- Scikit-learn (latest)
- And more...

All packages will be the latest compatible versions, ensuring you have the most up-to-date and secure data science stack. 