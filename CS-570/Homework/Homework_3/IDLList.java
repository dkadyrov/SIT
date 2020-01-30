// Daniel Kadyrov
// Stevens ID: 10455680
// CS 570 - Data Systems
// Homework Assignment #3 - Due October 14th, 2019

import java.util.ArrayList;

public class IDLList<E> {
    // Creates an empty double-linked list

    private class Node<E> {
        private E data;
        private Node<E> next;
        private Node<E> prev;

        public Node(E elem) {
            this.data = elem;
            this.prev = null;
            this.next = null;
        }

        public Node(E elem, Node<E> prev, Node<E> next) {
            this.data = elem;
            this.prev = prev;
            this.next = next;
        }
    }

    private Node<E> head;
    private Node<E> tail;
    private int size;
    private ArrayList<Node<E>> indices;

    public IDLList() {
        head = null;
        tail = null;
        size = 0;
        indices = new ArrayList<Node<E>>();
    }

    public boolean add(int index, E elem) {
        // Adds elem at position index (counting from wherever head is). It uses the
        // index for fast access.

        if (index < 0 || index > size + 1) {
            throw new IllegalArgumentException();
        }

        if (index == 0) {
            add(elem);
        } else if (index == size - 1) {
            append(elem);
        } else {
            Node<E> prev_node = indices.get(index - 1);
            Node<E> next_node = indices.get(index);
            Node<E> node = new Node<E>(elem, prev_node, next_node);
            prev_node.next = node;
            next_node.prev = node;
            indices.add(index, node);
            size++;
        }
        return true;
    }

    public boolean add(E elem) {
        // Adds elem at the head (i.e. it becomes the first element of the list)

        if (head == null) {
            Node<E> node = new Node<E>(elem);
            head = node;
            tail = node;
            indices.add(0, node);
        } else {
            Node<E> node = new Node<E>(elem, null, head);
            indices.add(0, node);
            head.prev = node;
            head = node;
        }
        size++;

        return true;
    }

    public boolean append(E elem) {
        // Adds elem as the new last element of the list (i.e. at the tail)

        Node<E> node = new Node<E>(elem, tail, null);
        indices.add(node);
        tail.next = node;
        tail = node;
        size++;

        return true;
    }

    public E get(int index) {
        // Returns the object at position index from the head. It uses the index for
        // fast access. Indexing starts from 0, thus get(0) returns the head element of
        // the list.

        return indices.get(index).data;
    }

    public E getHead() {
        // Returns the object at the head.

        return head.data;
    }

    public E getLast() {
        // Returns the object at the tail.

        return tail.data;
    }

    public int size() {
        // Returns the list size.

        return size;
    }

    public E remove() {
        // Removes and returns the element at the head.

        E result = head.data;
        indices.get(1).prev = null;
        indices.remove(0);
        head = indices.get(0);
        size--;

        return result;
    }

    public E removeLast() {
        // Removes and returns the element at the tail

        E result = tail.data;
        tail = tail.prev;
        tail.next = null;
        indices.remove(size - 1);
        size--;

        return result;
    }

    public E removeAt(int index) {
        // Removes and returns the element at the index index. Use the index for fast
        // access

        E result = indices.get(index).data;

        if (index == 0) {
            remove();
        } else if (index == size - 1) {
            removeLast();
        } else if (index < size - 1) {
            indices.get(index - 1).next = indices.get(index + 1);
            indices.get(index + 1).prev = indices.get(index - 1);
            indices.remove(index);
            size--;
        } else {
            return null;
        }

        return result;
    }

    public boolean remove(E elem) {
        // Removes the first occurrence of elem in the list and returns true. Return
        // false if elem was not in the list.

        for (int i = 0; i < size; i++) {
            if (indices.get(i).data == elem) {
                E result = indices.get(i).data;
                remove(result);
            } else {
                return false;
            }
        }

        return true;
    }

    public String toString() {
        // Presents a string representation of the list.

        String result = new String();

        for (int i = 0; i < size; i++) {
            result += indices.get(i).data;
        }

        return result;
    }
}
