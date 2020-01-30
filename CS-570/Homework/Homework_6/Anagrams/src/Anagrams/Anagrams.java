/**
 * An anagram is word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once. For example, “rail safety” and “fairy tales” are anagrams.
 * 
 * @author Daniel Kadyrov 
 * CWID 10455680 
 * Due Date December 2nd, 2019 
 * Homework #6
 * Anagrams
 * 
 * @version: 1.0
 * @since: 2019-12-2
 */

package Anagrams;

import java.util.Map;
import java.util.HashMap;
import java.util.ArrayList;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.BufferedReader;
import java.io.InputStreamReader;

public class Anagrams {
    final Integer[] primes;
    Map<Character, Integer> letterTable;
    Map<Long, ArrayList<String>> anagramTable;

    /**
     * The constant primes should be initialized to an array consisting of the first 26 prime numbers. It will be used to set up the letterTable, a hash table that will associate each letter in the alphabet with a prime number. More precisely, it will associate “a” with 2, “b” with 3, “c” with 5, and so on. The instance variable anagramTable will hold the main working hash table. Each entry in this hash table has the following format: 
     * • Key (of type Long): the hash code of the word. It is important that this hash be the same for all anagrams of a word. The type Long is a 64-bit two’s complement integer. More details on how to produce this key will be given below. 
     * • Value (of type ArrayList<String>): a list of the words seen up until now that have Key as hash code. Note that all the strings in this list are anagrams.
     * 
     * @return
     */
    public Anagrams() {
        this.primes = new Integer[] { 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73,
                79, 83, 89, 97, 101 };
        this.letterTable = new HashMap<Character, Integer>();
        this.anagramTable = new HashMap<Long, ArrayList<String>>();

        buildLetterTable();
    }

    /**
     * This method should be invoked by the constructor for the class Anagrams and
     * should build the hash table letterTable
     * 
     */
    private void buildLetterTable() {
        String letters = "abcdefghijklmnopqrstuvwxyz";

        for (int i = 0; i < letters.length(); ++i) {
            this.letterTable.put(letters.charAt(i), primes[i]);
        }
    }

    
    /**
     * This method should compute the hash code of the string s passed as argument,
     * and should add this word to the hash table anagramTable.
     * 
     * @param s String to add to hash
     */
    private void addWord(String s) {
        if (s == null || !(s instanceof String)) {
            throw new NullPointerException("s parameter cannot be none and has to be String");
        }

        long hash = myHashCode(s);

        ArrayList<String> list = this.anagramTable.get(hash);
        if (list == null) {
            list = new ArrayList<String>();
            list.add(s);
        } else {
            if (list.contains(s)) {
                System.out.println("String \"" + s + "\" already in ArrayList");

                return;
            } else {
                list.add(s);
            }
        }

        this.anagramTable.put(hash, list);
    }

    
    /**
     * This method, given a string s, should compute its hash code. A requirement
     * for myHashCode is that all the anagrams of a word should receive the same
     * hash code. With that aim, you should resort to the fundamental theorem of
     * arithmetic. The fundamental theorem of arithmetic, also called the unique
     * factorization theorem or the unique-prime-factorization theorem, states that
     * every integer greater than 0 either is prime itself or is the product of a
     * unique combination of prime numbers.
     * 
     * @param s String to hash
     * @return Long
     */
    private Long myHashCode(String s) {
        if (s == null || !(s instanceof String)) {
            throw new NullPointerException("s parameter cannot be none and has to be String");
        }

        Long hash = 1L;

        for (int i = 0; i < s.length(); ++i) {
            hash *= Long.valueOf(this.letterTable.get(s.charAt(i)));
        }

        return hash;
    }

    
    /**
     * The main method is processFile which receives the name of a text file
     * containing words, one per line, and builds the hash table anagramTable.
     * 
     * @param s
     * @throws IOException
     */
    public void processFile(String s) throws IOException {
        FileInputStream fstream = new FileInputStream(s);
        BufferedReader br = new BufferedReader(new InputStreamReader(fstream));
        String strLine;
        while ((strLine = br.readLine()) != null) {
            this.addWord(strLine);
        }
        br.close();
    }

    
    /**
     * This method should return the entries in the anagramTable that have the
     * largest number of anagrams. It returns a list of them since there ay be more
     * than one list of anagrams with a maximal size
     * 
     * @return ArrayList<Entry<Long, ArrayList<String>>>
     */
    private ArrayList<Map.Entry<Long, ArrayList<String>>> getMaxEntries() {
        ArrayList<Map.Entry<Long, ArrayList<String>>> list = new ArrayList<Map.Entry<Long, ArrayList<String>>>();

        int length = 0;

        for (Map.Entry<Long, ArrayList<String>> entry : anagramTable.entrySet()) {
            if (entry.getValue().size() == length) {
                list.add(entry);
            } else if (entry.getValue().size() > length) {
                list.clear();
                length = entry.getValue().size();
                list.add(entry);
            }
        }
        return list;
    }

    
    /**
     * The main method will read all the strings in a file, place them in the hash
     * table of anagrams and then iterate over the hash table to report which words
     * have the largest number of anagrams
     * 
     * @param args
     */
    public static void main(String[] args) {
        Anagrams a = new Anagrams();
        final long startTime = System.nanoTime();
        try {
            a.processFile("words_alpha.txt");
        } catch (IOException e1) {
            e1.printStackTrace();
        }
        ArrayList<Map.Entry<Long, ArrayList<String>>> maxEntries = a.getMaxEntries();
        final long estimatedTime = System.nanoTime() - startTime;
        final double seconds = ((double) estimatedTime / 1000000000);
        System.out.println("Elapsed Time: " + seconds);
        System.out.println("Key of max anagrams: " + maxEntries.get(0).getKey());
        System.out.println("List of max anagrams: " + maxEntries.get(0).getValue());
        System.out.println("Length of list of max anagrams: " + maxEntries.get(0).getValue().size());
    }
}