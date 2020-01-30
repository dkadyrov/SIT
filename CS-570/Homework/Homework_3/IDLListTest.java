// Daniel Kadyrov
// Stevens ID: 10455680
// CS 570 - Data Systems
// Homework Assignment #3 - Due October 14th, 2019

import static org.junit.jupiter.api.Assertions.*;

import org.junit.jupiter.api.Test;

class IDLListTest {

	@Test
	void test() {
		IDLList<Integer> list = new IDLList<Integer>();

		assertTrue(list.add(2));
		assertTrue(list.add(1));
		assertTrue(list.add(1, 3));
		assertTrue(list.append(4));
		assertTrue(list.append(5));
		assertTrue(list.append(6));
		assertEquals(list.get(1), Integer.valueOf(2));
		assertEquals(list.getHead(), Integer.valueOf(1));
		assertEquals(list.getLast(), Integer.valueOf(6));
		assertEquals(list.size(), Integer.valueOf(6));
		assertEquals(list.remove(), Integer.valueOf(1));
		assertEquals(list.removeLast(), Integer.valueOf(6));
		assertEquals(list.removeAt(1), Integer.valueOf(3));
		assertEquals(list.toString(), String.valueOf("245"));
	}
}