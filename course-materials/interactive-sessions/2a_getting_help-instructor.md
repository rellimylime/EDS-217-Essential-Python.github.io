---
title: "Interactive Session 2A (Instructor)"
subtitle: "Getting `help()` in Jupyter Notebooks"
editor_options: 
  chunk_output_type: console
jupyter: eds217_2024
format:
  html:
    toc: true
    toc-depth: 3
    code-fold: show
---

# Instructor Guide: Interactive Session - Exploring Python's `help` features in Jupyter Notebooks

**Objective:** Guide students through getting help, working with variables, and exploring methods available for different Python objects in Jupyter Notebooks.


---

## 1. Getting Help in Python

### Using `help()`
- **Instructor Action:** Demonstrate using `help()` with the `len` function:
  ```python
  help(len)
  ```
  - Explain how the output provides details on how to use the function.
  
- **Student Activity:** Ask students to try `help()` on `print` or `sum` in their own notebooks.
- **Key Point:** Encourage discussion about what information was provided and how it could be useful.

### Using `?` and `??`
- **Instructor Action:** Demonstrate using `?` for quick documentation and `??` for more details:
  ```python
  len?
  len??
  ```
- **Student Activity:** Have students use `?` and `??` with other functions like `type` or `max`.
- **Additional Notes:** Explain that `?` is great for quick reference, while `??` can show source code when available.

---

## 2. Working with Variables

### Creating Variables
- **Instructor Action:** Create a few variables and demonstrate using `type()`:
  ```python
  a = 10
  b = 5.5
  c = "Hello, world!"
  ```
  - Explain the different data types (int, float, str).
  
- **Student Activity:** Students create their own variables and use `type()` to explore their types.
- **Additional Notes:** Discuss why understanding data types is crucial for avoiding errors.

### Exploring Variables
- **Instructor Action:** Encourage experimentation with changing variable values and types.
- **Student Activity:** Have students discuss the effects of changing types on variable behavior.
- **Key Point:** Highlight Python’s dynamic typing and how it influences variable usage.

---

## 3. Exploring Methods Available for Objects

### Using `dir()`
- **Instructor Action:** Demonstrate using `dir()` on variables to explore available methods:
  ```python
  dir(a)
  dir(b)
  dir(c)
  ```
  - Explain how `dir()` lists all attributes and methods tied to an object.
  
- **Student Activity:** Students use `dir()` on their own variables and explore the listed methods.
- **Additional Notes:** Emphasize that understanding these methods can greatly enhance coding efficiency.

### Using `help()` with Methods
- **Instructor Action:** Show how to use `help()` with a method:
  ```python
  help(c.upper)
  ```
  - Discuss what the output reveals about the method's usage.
  
- **Student Activity:** Students pick a method and use `help()` to learn more.
- **Key Point:** Encourage students to document what they find and how they might use these methods in practice.

### Exploring Methods
- **Instructor Action:** Demonstrate calling a method on an object:
  ```python
  c.upper()
  ```
  - Explain how methods perform operations directly on the object.
  
- **Student Activity:** Students experiment with calling different methods.
- **Additional Notes:** Ask students to share interesting methods they discovered and their potential applications.

---

## 4. Guided Practice and Q&A

### Instructor-Led Practice
- **Instructor Action:** Guide students through using methods on lists (e.g., `.append()`, `.pop()`, `.sort()`).
- **Student Activity:** Students follow along and replicate the process on their own data.
- **Additional Notes:** The TA should circulate to provide help and answer individual questions.

### Q&A Session
- **Instructor Action:** Open the floor for questions about anything covered so far.
- **Key Point:** Use this time to address any misunderstandings or explore further examples.

---

## 5. Wrap-Up and Reflection

### Summary of Key Learnings
- **Instructor Action:** Summarize the session, emphasizing the importance of help features, understanding variables, and exploring object methods.
- **Key Point:** Encourage students to use these tools regularly as they continue learning Python.

### Reflection Activity
- **Student Activity:** Students write a brief summary in a markdown cell about what they learned.
- **Instructor Action:** If time allows, ask a few students to share their reflections.

### Next Steps
- **Instructor Action:** Provide a preview of the next session and how these foundational skills will be applied.
- **Key Point:** Reinforce the idea that mastering these basics will make more advanced topics easier to learn.

---

**Instructor Tip:** Make sure to actively involve the TA throughout the session. The TA should help address individual questions, ensure that all students are following along, and provide additional explanations as needed.


