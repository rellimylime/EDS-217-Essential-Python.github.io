# EDS-217 End-of-Day Activity Alignment Action Plan

## 🎯 **Objective**
Systematically review and fix misalignments between daily course content and end-of-day (EOD) practice activities to ensure students only encounter concepts and tools they have already learned.

## 🚨 **Critical Issue Identified**

### **Day 1 EOD Practice - MAJOR MISALIGNMENT**
- **Problem:** Uses advanced concepts (pandas DataFrames, `read_csv()`, matplotlib plotting, `.head()`, `.isnull().sum()`) before teaching them
- **Day 1 actual coverage:** Only covers JupyterLab basics, variables, strings, operators, and functions
- **Impact:** High frustration potential for students on their first day
- **Status:** 🚨 **IMMEDIATE ACTION REQUIRED**

## 📋 **Four-Phase Action Plan**

### **Phase 1: Immediate Fixes (Priority 1) - Complete by Course Start**

#### 🔴 **Task 1.1: Fix Day 1 EOD Activity** ✅ **COMPLETED**
- **Current file:** `course-materials/eod-practice/eod-day1.qmd`
- **Draft file:** `course-materials/eod-practice/eod-day1-draft.qmd` ✅ **CREATED**
- **Answer key:** `course-materials/answer-keys/eod-day1-draft-key.qmd` ✅ **CREATED**
- **Action taken:** Enhanced framing approach - kept all existing code but added comprehensive "preview" framing
- **Key improvements:**
  - Clear "Coming Attractions" messaging
  - "Wonder moments" after each step explaining what happened
  - Learning timeline showing when concepts will be taught
  - Emphasis on copy/paste approach for Day 1
  - Proper expectation setting for beginners
- **Next step:** Test with stakeholders and replace original when approved

#### 🟡 **Task 1.2: Review Day 4 EOD Activity**
- **Current file:** `course-materials/eod-practice/eod-day4.qmd`
- **Issue:** Uses `parse_dates` parameter and potentially advanced visualizations
- **Action needed:** 
  1. Verify `parse_dates` is covered in Day 4 sessions
  2. Check if date handling concepts are taught before EOD
  3. If not covered, either add to curriculum or simplify EOD
- **Estimated time:** 2-3 hours

### **Phase 2: Comprehensive Content Audit (Priority 2)**

#### **Task 2.1: Create Detailed Content Matrices**
- **Deliverable:** Spreadsheet mapping concepts taught vs. concepts used in EOD
- **For each day:**
  - List all pandas methods introduced
  - Track matplotlib/seaborn concepts
  - Document Python syntax/functions taught
  - Map library imports and timing
- **Estimated time:** 8-10 hours

#### **Task 2.2: Examine All Interactive Sessions**
- **Files to review:** All files in `course-materials/interactive-sessions/`
- **Extract:** Specific concepts, methods, functions introduced each session
- **Cross-reference:** Against corresponding EOD activities
- **Estimated time:** 12-15 hours

#### **Task 2.3: Review Coding Colabs and Live Coding**
- **Directories:** `coding-colabs/` and `live-coding/`
- **Purpose:** Capture all concepts taught in hands-on sessions
- **Estimated time:** 6-8 hours

### **Phase 3: Systematic Review Process (Priority 3)**

#### **Task 3.1: Develop Content Alignment Checklist**
```markdown
## EOD Activity Pre-Flight Checklist
For each day's EOD activity, verify:

### Python Fundamentals
☐ All data types used have been introduced
☐ All Python syntax patterns are previously taught
☐ All built-in functions have been covered

### Libraries and Imports
☐ All pandas methods used have been taught
☐ All visualization libraries have been introduced  
☐ All NumPy functions are previously covered
☐ All external libraries are imported and explained

### Concept Complexity
☐ Data manipulation concepts match skill level
☐ Dataset complexity is appropriate
☐ Problem-solving approach aligns with taught methods

### Learning Progression
☐ Builds incrementally on previous days
☐ No "surprise" advanced concepts
☐ Matches expected difficulty curve
```

#### **Task 3.2: Create Review Workflow Documentation**
- **Before each course offering:** Run alignment checklist
- **After content updates:** Re-verify alignment when changing sessions
- **Student feedback integration:** Add alignment questions to evaluations
- **Estimated time:** 3-4 hours

### **Phase 4: Process Integration (Priority 4)**

#### **Task 4.1: Update Course Development Documentation**
- **File:** `tasks/2025-course-updates.md`
- **Add new section:** "End-of-Day Activity Alignment Review"
- **Include:** 
  - Alignment verification requirements
  - Checklist integration into workflow
  - Responsibility assignments

#### **Task 4.2: Create EOD Activity Template**
```markdown
## New EOD Activity Template
### Prerequisites
- List all concepts/libraries required
- Reference specific day/session where taught

### Concept Verification
- [ ] All methods used are previously taught
- [ ] Difficulty matches daily progression
- [ ] No "surprise" advanced concepts

### Skills Assessment
- Primary skills practiced:
- Secondary skills reinforced:
- New combinations introduced:
```

## 🎯 **Day-by-Day Status and Actions**

| Day | Current Status | Specific Action Required | Priority | Est. Hours |
|-----|---------------|-------------------------|----------|-----------|
| **Day 1** | 🚨 **Critical** | Complete rewrite - remove pandas/matplotlib | P1 | 4-6 |
| **Day 2** | ✅ **Good** | No changes needed | - | 0 |
| **Day 3** | ✅ **Good** | No changes needed | - | 0 |  
| **Day 4** | 🟡 **Review** | Verify parse_dates timing | P1 | 2-3 |
| **Day 5** | ✅ **Good** | No changes needed | - | 0 |
| **Day 6** | ✅ **Good** | No changes needed | - | 0 |
| **Day 7** | ✅ **Good** | No changes needed | - | 0 |

## 🔄 **Implementation Timeline**

### **Week 1: Critical Fixes**
- [x] Day 1 EOD enhanced framing (draft created with answer key)
- [ ] Test Day 1 EOD draft with stakeholders
- [ ] Day 4 EOD verification and fixes
- [ ] Initial checklist development

### **Week 2-3: Content Audit**
- [ ] Map all interactive sessions content
- [ ] Create concept progression matrices
- [ ] Review coding colabs and live sessions

### **Week 4: Process Development**
- [ ] Finalize alignment checklist
- [ ] Create review workflow documentation
- [ ] Update course development processes

### **Week 5: Integration and Testing**
- [ ] Integrate into course update documentation
- [ ] Test new Day 1 EOD with stakeholders
- [ ] Final review and validation

## 💡 **Success Metrics**

### **Immediate Indicators**
- [ ] No student complaints about "concepts not yet covered"
- [ ] Improved Day 1 confidence and engagement
- [ ] Smoother progression through early course days

### **Long-term Indicators**
- [ ] Higher course satisfaction scores
- [ ] Reduced instructor "concept review" time
- [ ] More consistent skill building progression

## 🚨 **Risk Mitigation**

### **Potential Issues:**
1. **Time constraints:** Prioritize Day 1 fix above all else
2. **Content gaps:** Better to have simpler, aligned activities than complex misaligned ones
3. **Instructor resistance:** Frame as student success improvement, not criticism

### **Contingency Plans:**
- **If Day 1 rewrite delayed:** Create simplified version removing only pandas/matplotlib
- **If comprehensive audit delayed:** Focus on Days 1-4 first as highest impact
- **If process integration delayed:** Implement manual checklist first

## 📁 **File Organization**

### **New Files Created:**
- `course-materials/eod-practice/eod-day1-draft.qmd` - ✅ **COMPLETED** Enhanced Day 1 activity with preview framing
- `course-materials/answer-keys/eod-day1-draft-key.qmd` - ✅ **COMPLETED** Corresponding answer key with teaching notes

### **New Files to Create:**
- `tasks/eod-content-matrices.xlsx` - Detailed concept mapping
- `tasks/eod-alignment-checklist.md` - Review checklist template

### **Files to Modify:**
- `tasks/2025-course-updates.md` - Add alignment review section
- `course-materials/eod-practice/eod-day1.qmd` - Replace with aligned content
- `course-materials/eod-practice/eod-day4.qmd` - Fix date parsing issues

## 🎓 **Student Impact Statement**

This action plan directly addresses student feedback about encountering unfamiliar concepts in practice activities. By ensuring proper alignment:

- **Day 1 experience** becomes confidence-building rather than overwhelming
- **Learning progression** follows logical, incremental skill building
- **Student success** increases through appropriate challenge levels
- **Course satisfaction** improves through better pedagogical alignment

---

## 🎉 **COMPLETED: Day 1 EOD Draft Solution**

**Files Created:**
- `course-materials/eod-practice/eod-day1-draft.qmd` - Enhanced student version
- `course-materials/answer-keys/eod-day1-draft-key.qmd` - Instructor version with teaching notes

**Solution Summary:**
Instead of removing the advanced concepts, the draft version reframes the entire activity as a "preview of coming attractions." Students still run the same powerful data science workflow, but with clear messaging that this is a sneak peek at their future skills.

**Key Features:**
- 🎬 "Coming Attractions" framing throughout
- 🎭 "What just happened?" explanations after each step
- 🗓️ Learning timeline showing when concepts are taught
- 🚀 Proper expectation setting and encouragement
- 💡 Maintains pedagogical value while addressing alignment concerns

**Next Steps:** 
1. Test the draft version with a few students or colleagues
2. Gather feedback on clarity and motivational impact
3. Replace original with draft version when approved
4. Proceed with Day 4 EOD review (lower priority) 