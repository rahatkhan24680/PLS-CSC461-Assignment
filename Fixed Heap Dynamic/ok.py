def fixed_heap_dynamic():
    # Demonstrating a fixed-size heap-allocated array using Python's array module
    import array
    arr = array.array('i', [0] * 5)  # Fixed length, stored on the heap
    
    # Initialize array values
    for i in range(len(arr)):
        arr[i] = i * 5

    # Display the array contents
    print("\nFixed Heap-Dynamic Array (using array module):")
    print(arr.tolist())

fixed_heap_dynamic()

