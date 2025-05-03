def stack_dynamic(size):
    # Simulates stack-dynamic behavior: array size decided at runtime
    arr = [0] * size  # List created with runtime-determined size

    # Initialize array with values
    for i in range(size):
        arr[i] = i * 10

    # Display the array
    print(f"\nStack-Dynamic Array (size {size}):")
    print(arr)

# Call the function with different sizes to demonstrate dynamic allocation
stack_dynamic(4)
stack_dynamic(6)

