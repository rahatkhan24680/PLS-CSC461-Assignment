public class Ok {
    public static void main(String[] args) {
        // Fixed-size array allocated on the heap (Java default behavior)
        int[] arr = new int[7]; // Memory is allocated on the heap; size cannot change after creation

        // Populate the array with values
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i * 5;
        }

        // Display the array contents
        System.out.println("\nFixed Heap-Dynamic Array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}

