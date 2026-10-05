# 🧮 Alithm

### Text-Based Mathematical Processing System

**Alithm** is a text-based mathematical processing system that allows users to perform mathematical operations by entering them as natural text instead of selecting an operation from a predefined menu.

The system identifies the mathematical operation from the user's input, extracts the required numerical values, retrieves the corresponding operation rule, generates a mathematical expression, and evaluates it to produce the final answer.

The project is built using **Python, Streamlit, Regex, and MySQL**, without using Machine Learning, LLMs, or a large chain of operation-specific `if/elif` statements.

---

## 🚀 What is Alithm?

Traditional calculators generally require users to enter numbers and select an operation explicitly.

Alithm takes a different approach.

Instead of selecting:

```text
Operation → Square
Number → 7
```

the user can simply enter:

```text
square of 7
```

Alithm processes the text and returns:

```text
The answer is 49.
```

Similarly:

```text
cube of 9
```

produces:

```text
The answer is 729.
```

The goal is to make mathematical processing **text-driven and extensible**.

---

## ✨ Features

* 📝 Accepts mathematical operations as text
* 🔎 Identifies supported operations from user input
* 🔢 Extracts numerical values using Regex
* 🗂️ Uses operation mapping instead of operation-specific `if/elif` chains
* 🧮 Generates mathematical expressions dynamically
* ⚡ Evaluates generated expressions using Python
* 🌐 Provides a Streamlit-based interface
* ❌ Handles unsupported mathematical inputs
* 🔄 Supports both single-value and multi-value operations

---

## 💡 Example

### Input

```text
square of 7
```

### Processing

```text
User Input
    ↓
Identify "square"
    ↓
Extract 7
    ↓
Retrieve square operation
    ↓
Generate mathematical expression
    ↓
Evaluate expression
    ↓
49
```

### Output

```text
The answer is 49.
```

Another example:

```text
Input: cube of 9

Output: The answer is 729.
```

---

## 🧠 How Alithm Works

Alithm separates the processing of a mathematical request into multiple stages.

### 1. Operation Identification

The system searches the user's input for a supported mathematical operation.

For example:

```text
square of 7
```

contains the operation:

```text
square
```

For multi-word operations, longer operation names are checked first. This prevents an operation such as:

```text
square root
```

from being incorrectly identified as:

```text
square
```

---

### 2. Number Extraction

Regex is used to extract numerical values from the input.

For example:

```text
"What is 12.5 * 4?"
```

can provide:

```text
["12.5", "4"]
```

This allows the mathematical values to be processed separately from the surrounding text.

---

### 3. Operation Mapping

The identified operation is associated with its mathematical rule.

For example, an operation can be represented using information such as:

| Operation | Operator | Operand |
| --------- | -------- | ------: |
| square    | `*`      |       2 |
| cube      | `*`      |       3 |

This allows the same processing logic to work with different mathematical operations.

---

### 4. Expression Generation

The extracted values and operation information are used to generate a mathematical expression.

For example:

```text
cube of 9
```

can result in:

```text
9**3
```

The generated expression is then evaluated to obtain the result.

---

### 5. Result

The final result is presented to the user in a consistent format:

```text
The answer is 729.
```

The internal mathematical expression is not exposed in the final response.

---

## 🛠️ Technologies Used

| Technology       | Purpose                                       |
| ---------------- | --------------------------------------------- |
| **Python**       | Core application logic                        |
| **Streamlit**    | User interface                                |
| **MySQL**        | Storing mathematical operation information    |
| **Regex (re)** | Extracting numerical values from text         |
| **eval()**     | Evaluating generated mathematical expressions |

---

## 🎯 Design Approach

A major design goal of Alithm is to avoid implementing every mathematical operation using a separate conditional block.

Instead of building logic such as:

ython
if operation == "square":
    ...
elif operation == "cube":
    ...
elif operation == "sqrt":
    ...


the system uses **operation mapping and stored operation information**.

This makes the calculation mechanism more general and allows mathematical operations to be represented as data.

---

## 📌 Current Scope

Alithm currently focuses on processing supported mathematical operations provided through text input.

The project is primarily an exploration of:

* Text-based mathematical input
* Pattern matching
* Regex-based number extraction
* Operation mapping
* Dynamic expression generation
* Database-driven operation definitions
* Mathematical expression evaluation

---

## 🔐 Note on `eval()`

Alithm currently uses Python's `eval()` to evaluate expressions generated by the application.

Since `eval()` can execute arbitrary Python code if untrusted input reaches it directly, its use requires careful control over what expressions are generated.

In Alithm, the intended design is to generate expressions from recognized operations and extracted numerical values rather than directly evaluating arbitrary user-provided Python code.

---




## 👨‍💻 Author

**Mohd Ali**

B.Tech Computer Science Student

Interested in Python, databases, algorithms, and building practical software systems.

---

## 📄 License

This project is available for learning and development purposes.
