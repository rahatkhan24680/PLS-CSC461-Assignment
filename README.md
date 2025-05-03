# 🔍 Java vs. Python: Array Types & Structural Differences

This educational project explores how **Java** and **Python** manage array-like data structures. It examines how different types of arrays are implemented and stored in memory, with attention to stack vs. heap allocation, resizability, and language-level support.

---

## 📦 Array Types and Their Behaviors

We classify arrays into four main types based on size mutability and memory allocation:

---

### 1. ✅ **Fixed Stack-Dynamic Arrays**

* **Definition**: Size is known at compile time. Allocated in stack memory (Java) and does not change at runtime.
* **Example Use Case**: Temporary buffers, counters, loop-state arrays.

| Feature           | Java (`int[]`)              | Python (`list` concept)             |
| ----------------- | --------------------------- | ----------------------------------- |
| Memory Location   | Stack (for primitives)      | Heap                                |
| Resize Capability | ❌ Not resizable             | ✅ List can grow/shrink              |
| Lifetime          | Tied to method execution    | Tied to object references           |
| Type Constraint   | Homogeneous (e.g., `int[]`) | Heterogeneous (mixed types allowed) |

🔸 *Note*: In Python, even fixed-looking lists are heap-allocated. Memory is managed via reference counting + garbage collection.

---

### 2. ⚙️ **Stack-Dynamic Arrays**

* **Definition**: Size determined at runtime. Still allocated on the stack in Java (when primitive arrays are used).
* **Example Use Case**: Arrays created inside recursive or runtime-determined loops.

| Feature           | Java (`new int[size]`)  | Python (`[0] * size`)           |
| ----------------- | ----------------------- | ------------------------------- |
| Memory Location   | Stack (Java), temporary | Heap (Python lists always heap) |
| Resize Capability | ❌ Not resizable         | ✅ Yes                           |
| Type Constraint   | Homogeneous             | Heterogeneous                   |
| Efficiency        | Very fast memory access | Slower but flexible             |

⚠️ Python lacks stack-allocated array equivalents; even variables created inside functions live on the heap.

---

### 3. 🧱 **Fixed Heap-Dynamic Arrays**

* **Definition**: Fixed-size arrays allocated on the heap; can’t change size but live beyond a function's execution.

| Feature           | Java (`Integer[]`)           | Python (`array.array`)            |
| ----------------- | ---------------------------- | --------------------------------- |
| Memory Location   | Heap                         | Heap                              |
| Resize Capability | ❌ Not resizable              | ❌ Not resizable                   |
| Type Enforced?    | ✅ Yes (Object wrapper class) | ✅ Yes (via array type code)       |
| Lifetime          | Controlled via reference     | Controlled via garbage collection |

💡 *Use when*: You need fixed, type-safe data with longer lifetime (Java) or minimal memory footprint (Python arrays).

---

### 4. 🌱 **Heap-Dynamic Arrays**

* **Definition**: Fully resizable arrays that grow and shrink dynamically during runtime. Memory is allocated on the heap.

| Feature           | Java (`ArrayList`)        | Python (`list`)                |
| ----------------- | ------------------------- | ------------------------------ |
| Memory Location   | Heap                      | Heap                           |
| Resize Capability | ✅ Yes                     | ✅ Yes                          |
| Backing Structure | Backed by array (resized) | Backed by over-allocated array |
| Type Enforcement  | Optional via Generics     | Not enforced                   |

⚙️ *Behavior*: Both use **doubling strategies** internally (e.g., 2x reallocation when full) for amortized O(1) `append()` or `add()`.

---

## 🧠 Under-the-Hood: Memory Management

### 🔹 Java

* **Stack**: Stores method-local variables (primitive types, references).
* **Heap**: Used for `new` objects (`ArrayList`, `Integer[]`, etc.)
* **GC**: Garbage Collector cleans up unused heap memory.
* **Type Safety**: Strong static typing (must declare array type).

### 🔸 Python

* **Everything is an object**, even integers and lists.
* **All memory** is heap-allocated.
* **Reference Counting + Garbage Collection** handles cleanup.
* **Dynamic typing**: You can mix integers, strings, and objects in a list.

---

## 📊 Full Feature Comparison Table

| Type                | Java Example             | Python Example            | Fixed Size | Memory Location | Resizable | Type-Safe   |
| ------------------- | ------------------------ | ------------------------- | ---------- | --------------- | --------- | ----------- |
| Fixed Stack Dynamic | `int[] arr = new int[5]` | `arr = [0]*5` (simulated) | ✅ Yes      | Stack / Heap    | ❌ No      | ✅ Java      |
| Stack Dynamic       | `new int[size]`          | `[0]*size`                | ✅ Yes      | Stack / Heap    | ❌ No      | ✅ Java      |
| Fixed Heap Dynamic  | `new Integer[5]`         | `array.array('i', [...])` | ✅ Yes      | Heap            | ❌ No      | ✅ Both      |
| Heap Dynamic        | `new ArrayList<>()`      | `[]`                      | ❌ No       | Heap            | ✅ Yes     | ⚠️ Optional |

---

## 📘 Language-Specific Notes

### Java

* Arrays are **strongly typed** and can't be resized.
* `ArrayList` offers flexibility, but has performance overhead.
* Stack-allocated arrays improve speed but have scope-limited lifespan.

### Python

* Lists are inherently dynamic and flexible.
* Ideal for scripting and rapid prototyping.
* Arrays from `array` or `numpy` offer memory-efficient alternatives.

---

## 🧪 Performance Insight

| Operation       | Java Array  | Python List |
| --------------- | ----------- | ----------- |
| Access (Index)  | O(1)        | O(1)        |
| Append          | O(1) amort. | O(1) amort. |
| Insert (middle) | O(n)        | O(n)        |
| Remove (middle) | O(n)        | O(n)        |
| Memory Overhead | Low         | Medium-High |

---

## ▶️ How to Run

* **Java**:

  ```bash
  javac YourFile.java  
  java YourFile
  ```

* **Python**:

  ```bash
  python3 your_script.py
  ```

---

## 🎓 Purpose of This Project

This repository was developed as an assignment under the guidance of **Md. Nazir Ahmed Sir**, designed to help students:

* Understand memory models in programming languages.
* Compare runtime behaviors across languages.
* Grasp the differences between stack and heap memory.
* Explore how resizable arrays are implemented behind the scenes.

---

## 🔚 Conclusion

Understanding the **array behavior and memory model** of your programming language is critical for writing **efficient, reliable**, and **scalable software**. Java gives you **control and performance**, while Python offers **flexibility and ease of use**.


