// Daniel Kadyrov
// Student ID: 10455680
// Due Date: November 4th, 2019
// Homework 4

package Maze;

public class PairInt {

    // data field
    private int x;
    private int y;

    // constructor
    public PairInt(int x, int y) {
        this.x = x;
        this.y = y;

    }

    // getter for x
    public int getX() {
        return x;
    }

    // getter for y
    public int getY() {
        return y;
    }

    //setter for x
    public void setX(int x) {
        this.x = x;
    }

    // setter for y
    public void setY(int y) {
        this.y = y;
    }


    @Override
    public boolean equals(Object p) {
        if ( p == null) {
            return false;
        }

        PairInt pairInt = (PairInt) p;
        return (this.x == pairInt.x && this.y == pairInt.y);

    }

    @Override
    public String toString() {

        return "(" + x + ", " + y + ")";
    }

    public PairInt copy() {
        return new PairInt(x, y);

    }
}