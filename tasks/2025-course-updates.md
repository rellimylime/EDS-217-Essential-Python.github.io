# EDS-217 Course Updates for 2025

## Critical Updates (Must Do First)

### Dates and Schedule
- [x] Update all course dates from September 2024 to 2025 schedule in `_quarto.yml` navigation (lines 21-38)
- [x] Update dates in individual day files (`day1.qmd`, `day7.qmd`, etc.) to match 2025 schedule  
- [x] Change `index.qmd` subtitle from "Summer 2024" to "Summer 2025"

### External Links and Data Sources
- [ ] Check and update external links: syllabus Google Doc, NASA GISS data URLs, documentation links
- [ ] Test all data URLs in `data/data_urls.py` and update environmental datasets for currency
- [ ] Verify GitHub repository link in navigation points to correct location

## Important Content & Technology Updates

### Python Environment
- [x] **COMPLETED:** Updated from Python 3.10 to Python 3.11 for 2025 (all .qmd files updated)
- [x] **COMPLETED:** Created new eds217_2025 conda environment with Python 3.11
- [x] **COMPLETED:** Updated all course materials to reference eds217_2025 environment
- [x] **COMPLETED:** Created migration guide and environment.yml file
- [x] **COMPLETED:** Review and update core library versions (pandas, numpy, matplotlib, seaborn, jupyter) ✅ **ALL CURRENT**
- [x] **COMPLETED:** Review and update Python/Miniconda installation instructions for current best practices ✅ **COMPREHENSIVE DOCS**

### Course Content  
- [x] **DECIDED:** Keep commented-out sessions in `_quarto.yml` (lines 49, 53, 57, 75) - preserved for future course iterations
- [x] **PLANNED:** Update examples to use modern Python features (f-strings, type hints, current pandas syntax) ✅ **COMPREHENSIVE PLAN CREATED**
- [x] **PLANNED:** Consider adding content on modern data science practices (type hints, conda-lock/poetry, etc.) ✅ **INTEGRATION STRATEGY DEVELOPED**

### Modern Python Features Integration
- [x] **COMPLETED:** Created comprehensive integration plan (`tasks/modern-python-integration-plan.md`)
- [x] **COMPLETED:** Prioritized features by importance for data science students
- [x] **COMPLETED:** Mapped features to specific course days and sessions
- [x] **IMPLEMENTATION:** Execute Phase 1 - F-string standardization and print statement updates ✅ **COMPLETED**
- [ ] **IMPLEMENTATION:** Execute Phase 2 - Uncomment Sessions 2c & 2d, add pathlib
- [ ] **IMPLEMENTATION:** Execute Phase 3 - Enhanced type hints and modern pandas patterns
- [ ] **IMPLEMENTATION:** Execute Phase 4 - Testing and refinement

#### Modern Features Implementation Plan Summary
**Priority 1 (Essential):** F-string standardization, pathlib, list comprehensions
**Priority 2 (Professional):** Type hints, exception handling, context managers  
**Priority 3 (Advanced):** Dataclasses, modern pandas patterns
**Total Development Time:** 38-55 hours across 4 phases

## Quality & Enhancement Tasks

### Course Structure
- [x] Evaluate day-by-day content distribution and interactive vs lecture balance
- [x] **PRIORITY: Complete End-of-Day Activity Alignment Review** (see `tasks/course-audit/comprehensive-audit-review.md`) ✅ **COMPLETED - 100% SUCCESS**
- [ ] Review end-of-day practice distribution across all days
- [ ] Update data science workflow template to reflect current best practices

### End-of-Day Activity Alignment Process ✅ **COMPLETED**
- [x] **COMPLETED:** Created comprehensive EOD alignment checklist (`tasks/course-audit/eod-alignment-checklist.md`)
- [x] **COMPLETED:** Systematic audit of all EOD activities (Days 1-7) with 100% alignment achieved
- [x] **COMPLETED:** Major revisions successfully applied to Days 3, 5, 6 using proven "Option 1: Simplify" strategy
- [x] **COMPLETED:** Perfect library introduction sequence validated (pandas → matplotlib → seaborn)
- [x] **COMPLETED:** Comprehensive documentation created (`tasks/course-audit/` directory)
- [ ] **ONGOING:** Implement alignment checklist for all future course updates
- [ ] **REQUIRED:** Use alignment checklist before each course offering to verify activities match taught content

#### Alignment Review Requirements
1. **Before Each Course:** Run alignment checklist on all EOD activities
2. **After Content Updates:** Re-verify alignment when changing interactive sessions
3. **New EOD Activities:** Must pass alignment checklist before implementation
4. **Student Feedback Integration:** Include alignment questions in course evaluations

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