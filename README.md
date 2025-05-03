# Array Types and Structural Comparison: Java vs. Python

This repository demonstrates how four different array types are implemented in Java and Python, focusing on how their internal structures differ between the two languages.

---

## Array Types Covered

###  1. Fixed Stack Dynamic Arrays

**Description:** Arrays with a fixed size known at compile time and stored on the stack.

| Feature               | Java                    | Python                                      |
| --------------------- | ----------------------- | ------------------------------------------- |
| Memory Allocation     | Stack (primitive types) | Heap (lists are objects)                    |
| Can Resize?           | ❌ No                    | ✅ Technically yes, though not the intention |
| True Stack Structure? | ✅ Yes                   | ❌ No (lists are heap-allocated)             |

**Note:** Python does not use stack-allocated arrays; all objects are allocated on the heap.

---

###  2. Stack Dynamic Arrays

**Description:** Size is determined during runtime, but the array is created on the stack.

| Feature               | Java                     | Python                   |
| --------------------- | ------------------------ | ------------------------ |
| Memory Allocation     | Stack (primitive arrays) | Heap (lists are objects) |
| Can Resize?           | ❌ No                     | ✅ Yes                    |
| True Stack Structure? | ✅ Yes                    | ❌ No                     |

**Observation:** Java supports real stack-based arrays, while Python's lists are always heap-allocated.

---

###  3. Fixed Heap Dynamic Arrays

**Description:** Arrays with a fixed size allocated on the heap.

| Feature             | Java                      | Python                                           |
| ------------------- | ------------------------- | ------------------------------------------------ |
| Wrapper Class Usage | ✅ Yes (e.g., `Integer[]`) | ✅ Yes (`array` module mimics fixed-size storage) |
| Can Resize?         | ❌ No                      | ❌ No                                             |

**Note:** Both languages can simulate fixed-size heap arrays, but this is less common in Python.

---

###  4. Heap Dynamic Arrays

**Description:** Arrays that can dynamically grow or shrink during runtime and are stored on the heap.

| Feature           | Java              | Python          |
| ----------------- | ----------------- | --------------- |
| Memory Allocation | Heap              | Heap            |
| Can Resize?       | ✅ Yes             | ✅ Yes           |
| Dynamic Support   | ✅ Via `ArrayList` | ✅ Built-in list |

**Observation:** Both Java's `ArrayList` and Python's built-in `list` support dynamic array behavior on the heap.

---

##  Summary Comparison Table

| Category            | Java Example             | Python Example                      | Fixed Size | Memory Location     | Resizable |
| ------------------- | ------------------------ | ----------------------------------- | ---------- | ------------------- | --------- |
| Fixed Stack Dynamic | `int[] arr = new int[5]` | `arr = [0]*5` *(conceptually only)* | Yes        | Stack (Java) / Heap | No        |
| Stack Dynamic       | `new int[size]`          | `[0]*size`                          | Yes        | Stack / Heap        | No        |
| Fixed Heap Dynamic  | `new Integer[5]`         | `array.array('i', [...])`           | Yes        | Heap                | No        |
| Heap Dynamic        | `new ArrayList<>()`      | `[]`                                | No         | Heap                | Yes       |

---

## Key Takeaways

* **Default Behavior:**
  Java arrays are fixed-size by default, while Python lists are dynamic.

* **Memory Control:**
  Java allows explicit control over stack and heap allocation. Python hides memory management details.

* **Data Types:**
  Java arrays are homogeneous; Python lists can mix types.

* **Performance:**
  Java arrays perform well for fixed-size data. Python lists are optimized for dynamic usage.

* **Syntax Differences:**
  Java requires type declarations and `new`; Python uses simple bracket notation.

---

##  How to Execute

* **Java:** Use a Java Development Kit (JDK) to compile and run `.java` files.
* **Python:** Use Python 3 to run `.py` scripts.

---

##  Educational Purpose

This project was created as an assignment from **Md. Nazir Ahmed Sir** to help students explore different memory models and understand dynamic array behavior in Java and Python.
