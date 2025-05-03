import java.util.ArrayList;

public class Ok {
    public static void main(String[] args) {
        // Demonstrating a heap-dynamic array using Java's ArrayList
        ArrayList<Integer> arr = new ArrayList<>();

        // Dynamically add elements
        arr.add(10);
        arr.add(20);
        arr.add(30);
        arr.add(1, 15); // Insert 15 at index 1

        System.out.println("\nHeap-Dynamic Array (ArrayList):");
        for (int num : arr) {
            System.out.print(num + " ");
        }

        // Remove element at index 2
        arr.remove(2);

        System.out.println("\nAfter removal:");
        for (int num : arr) {
            System.out.print(num + " ");
        }
    }
}

