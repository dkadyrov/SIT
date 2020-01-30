// Daniel Kadyrov
// Stevens ID: 10455680
// CS 570 - Data Systems
// Homework Assignment #1 - Due September 16th, 2019
// Note: Using Big-Endian format 0001 is 1

package binarynumber;

public class BinaryNumber {
    // Class that represents binary numbers and includes simple operations on them

    // Initialize variables
    private int data[];
    private boolean overflow = false;

    public BinaryNumber(int length) {
        // Constructor for creating a binary number of a certain length and consisting only of zeros 

        data = new int[length];
        for (int i = 0; i < length; i++) {
            data[i] = 0;
        }
    }

    public BinaryNumber(String str) {
        // Constructor for creating a binary number given a string
        
        // Check length of Array
        if (str.length() == 0){
            throw new Error("Length must be greater than 0");
        }

        // Remove all whitespace from string
        str = str.replaceAll("\\s+", "");

        data = new int[str.length()];

        for (int i = 0; i < str.length(); i++) {
            int num;
            // Check that entered character is a 1 or 0 
            num = Character.getNumericValue(str.charAt(i));

            if (num==0 || num==1) { 
                data[i] = num;
            } else { 
                throw new Error("Binary values should be 0 or 1");
            }
        }
    }

    public int getLength() {
        // Determines the length of the binary number 

        return data.length;
    }

    public int getDigit(int index) throws ArrayIndexOutOfBoundsException {
        // Obtains digit of a binary number given index
        
        // I was not sure if you wanted us to program our own index out of bounds exception or to use the checked one. I decided to use the checked one but provided the one I programmed myself below: 

        // Check that index is not out of bounds
        // if (index > this.getLength()-1) { 
        //     throw new Error("Index is out of bounds");
        // } 

        return data[index];
    }

    public void shiftR(int amount) {
        // Shifts all digits in a binary member amount-number of places to the right.

        if (amount <= 0) {
            throw new Error("Shift amount must be greater than 0");
        }

        int newLength = this.getLength() + amount;

        int[] relocate = new int[newLength];

        for (int i=0; i < amount; i++) {
            relocate[i] = 0;
        }

        for (int i=0; i < this.getLength(); i++) {
            relocate[i+amount] = data[i];
        }

        data = relocate;
    }

    public void add(BinaryNumber aBinaryNumber) {
        // Adds two binary numbers, one is the binary number that receives the message and the other is given as a parameter 

        // Check that Arrays are the same length
        if (this.getLength() == aBinaryNumber.getLength()) {
            int[] summation = new int[this.getLength()];
            int sum = 0;
            int carry = 0;

            for (int i = this.getLength() - 1; i >= 0; i--) {
                sum = data[i] + aBinaryNumber.data[i] + carry;
                summation[i] = sum % 2;
                carry = sum / 2;
            }

            // Flag overflow if it ends in a carry
            if (carry==1) {
                overflow = true;
            } else {
                // Clear overflow if overflow was triggered before
                this.clearOverflow();
            }

            data = summation;
        } else {
            // Throws Error if Arrays are not the same length
            throw new Error("Arrays need to be the same length");
        }
    }

    public String toString() {
        // Transforms binary number to String

        String str = "";

        // If the number is the result of an overflow
        if (overflow == false) {
            for (int i = 0; i < this.getLength(); i++) {
                str += String.valueOf(data[i]);
            }
        } else {
            str = "Overflow";
        }

        return str;
    }

    public int toDecimal() {
        // Transforms the binary number to its decimal notation

        int number = 0;
        for (int i = 0; i < this.getLength(); i++) {
            number += data[i] * Math.pow(2, this.getLength() - 1 - i);
        }

        return number;
    }

    public void clearOverflow() {
        // Operation that clears the overflow flag.

        overflow = false;
    }
}