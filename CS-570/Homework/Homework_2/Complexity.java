// Daniel Kadyrov
// Stevens ID: 10455680
// CS 570 - Data Systems
// Homework Assignment #2 - Due September 30th, 2019

package complexity;

public class Complexity {
    // Method to implement various methods of time complexity O(n) and prints out values from 1 to n (or close to) through a value of accumulator that counts number of "operations" performed 

    public static void method0(int n) {
        // Time Complexity O(n)

        int counter = 0;
        
        for (int i = 0; i < n; i++) {
            System.out.println("Operation " + counter);
            counter++;
        }
    }

    public static void method1(int n) {
        // Time Complexity O(n^2)

        int counter = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                System.out.println("Operation " + counter);
                counter++;
            }
        }
    }

    public static void method2(int n) {
        // Time Complexity O(n^3)

        int counter = 0;

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < n; j++) {
                for (int k = 0; k < n; k++) {
                    System.out.println("Operation " + counter);
                    counter++;
                }
            }
        }
    }

    public static void method3(int n) {
        // Time Complexity O(log n)

        int counter = 0;

        for (int i = 1; i < n; i *= 2) {
            System.out.println("Operation " + counter);
            counter++;
        }

    }

    public static void method4(int n) {
        // Time Complexity O(n log n)

        int counter = 0;

        for (int j = 1; j < n; j *= 2) {
            for (int i = 0; i < n; i++) {
                System.out.println("Operation " + counter);
                counter++;
            }
        }

    }

    public static void method5(int n) {
        // Time Complexity O(log log n)

        int counter = 0;

        for (int i = 1; i < n; i *= 2) {
            for (int j = 1; j < n; j *= 2) {
                System.out.println("Operation " + counter);
                counter++;
            }
        }
    }

    public static void method6(int n) {
        // Time Complexity O(2^n)

        int counter = 0;

        for (int i = 1; i <= Math.pow(2, n); i++) {
            System.out.println("Operation " + counter);
            counter++;
        }
    }
}
