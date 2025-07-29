# EDS 217 Conda Environment Setup - Quick Reference

## For Students (Simple Setup)

### Option 1: Quick Setup (Base Environment)
```bash
conda install python=3.11
conda install jupyter jupyterlab numpy pandas matplotlib seaborn
```

### Option 2: Dedicated Environment (Recommended)
```bash
# Create the EDS 217 environment
conda env create -f environment.yml

# Activate it
conda activate eds217_2025

# Register with Jupyter
python -m ipykernel install --user --name eds217_2025 --display-name "Python 3.11 (EDS 217 2025)"
```

## For Instructors (Migration from 2024)

### If you have an existing eds217_2024 environment:

1. **Export current environment (backup):**
   ```bash
   conda activate eds217_2024
   conda env export > eds217_2024_backup.yml
   ```

2. **Create new environment:**
   ```bash
   conda env create -f environment.yml
   conda activate eds217_2025
   python -m ipykernel install --user --name eds217_2025 --display-name "Python 3.11 (EDS 217 2025)"
   ```

3. **Test the environment:**
   ```bash
   python --version  # Should show 3.11.x
   jupyter lab       # Should show new kernel option
   ```

4. **Remove old environment (optional):**
   ```bash
   conda env remove -n eds217_2024
   jupyter kernelspec remove eds217_2024
   ```

## Verification

In JupyterLab, you should see "Python 3.11 (EDS 217 2025)" as a kernel option when creating new notebooks.

## Package List

The environment includes:
- Python 3.11
- NumPy, Pandas, Matplotlib, Seaborn
- JupyterLab, IPython
- SciPy, Scikit-learn
- Plotly, Requests
- GeoPandas, Folium
- And more... 