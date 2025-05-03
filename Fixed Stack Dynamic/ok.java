public class Ok {
    public static void main(String[] args) {
        // Fixed Stack-Dynamic Array
        int[] arr = new int[5]; // Array size is set at compile-time and stored on the stack for primitive types

        // Populate the array with values
        for (int i = 0; i < arr.length; i++) {
            arr[i] = i * 10;
        }

        // Output the array elements
        System.out.println("Fixed Stack-Dynamic Array:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}

