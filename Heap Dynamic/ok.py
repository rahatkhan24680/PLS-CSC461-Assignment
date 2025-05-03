def heap_dynamic():
    # Python's list is a built-in heap-dynamic data structure
    arr = []  # Start with an empty list

    # Dynamically add elements
    arr.append(10)
    arr.append(20)
    arr.append(30)
    arr.insert(1, 15)  # Insert 15 at index 1

    print("\nHeap-Dynamic Array (Python list):")
    print(arr)

    # Remove the element at index 2
    arr.pop(2)

    print("After removal:")
    print(arr)

heap_dynamic()

