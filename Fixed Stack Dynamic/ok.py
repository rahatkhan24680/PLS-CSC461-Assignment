# Python lists are inherently dynamic, but we can imitate fixed-size stack behavior

def fixed_stack_dynamic():
    # Simulating a fixed-size, stack-like array using a list
    arr = [0] * 5  # Pre-allocated with fixed size

    # Fill the list with values
    for i in range(len(arr)):
        arr[i] = i * 10

    # Display the list contents
    print("Fixed Stack-Dynamic Array (simulated in Python):")
    print(arr)

fixed_stack_dynamic()

