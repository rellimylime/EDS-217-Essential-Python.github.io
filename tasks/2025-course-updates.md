# EDS-217 Course Updates for 2025

## Critical Updates (Must Do First)

### Dates and Schedule
- [ ] Update all course dates from September 2024 to 2025 schedule in `_quarto.yml` navigation (lines 21-38)
- [ ] Update dates in individual day files (`day1.qmd`, `day7.qmd`, etc.) to match 2025 schedule  
- [ ] Change `index.qmd` subtitle from "Summer 2024" to "Summer 2025"

### External Links and Data Sources
- [ ] Check and update external links: syllabus Google Doc, NASA GISS data URLs, documentation links
- [ ] Test all data URLs in `data/data_urls.py` and update environmental datasets for currency
- [ ] Verify GitHub repository link in navigation points to correct location

## Important Content & Technology Updates

### Python Environment
- [ ] Evaluate updating from Python 3.10 to Python 3.11 or 3.12 for 2025
- [ ] Review and update core library versions (pandas, numpy, matplotlib, seaborn, jupyter)
- [ ] Review and update Python/Miniconda installation instructions for current best practices

### Course Content  
- [ ] Decide on commented-out sessions in `_quarto.yml` (lines 49, 53, 57, 77) - include or remove
- [ ] Update examples to use modern Python features (f-strings, type hints, current pandas syntax)
- [ ] Consider adding content on modern data science practices (type hints, conda-lock/poetry, etc.)

## Quality & Enhancement Tasks

### Course Structure
- [ ] Evaluate day-by-day content distribution and interactive vs lecture balance
- [ ] Review end-of-day practice distribution across all days
- [ ] Update data science workflow template to reflect current best practices

### Accessibility & Usability
- [ ] Review materials for accessibility (screen sizes, color schemes, interactive elements)
- [ ] Ensure all interactive elements work properly
- [ ] Update any references to software versions or capabilities

### Modern Examples
- [ ] Update examples to reflect current environmental challenges
- [ ] Consider incorporating more recent data science techniques
- [ ] Add more recent climate/environmental data examples

## Nice to Have Improvements

- [ ] Consider adding modern visualization libraries (plotly, altair) content
- [ ] Evaluate JupyterLab 4.x features and VS Code integration recommendations
- [ ] Review conda vs. mamba recommendations for faster package installation
- [ ] Add content on collaborative coding practices (GitHub workflows, etc.)

---

**Notes:**
- Priority should be given to Critical Updates first
- Test all changes in a development environment before deploying
- Consider student feedback from previous years when making content changes
- Verify all external dependencies are stable for the duration of the 2025 course 