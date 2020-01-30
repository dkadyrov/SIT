const questionOne = function questionOne(arr) {
    // Implement question 1 here
    // Calculate the sum of the squares of all numbers in the array and return that result
    let totalsum = 0 
    arr.forEach((number) => { 
        totalsum += number ** 2;
    })
    return totalsum;
}

const questionTwo = function questionTwo(num) {
    // Calculate the Fibonacci (Links to an external site.)Links to an external site. that corresponds to the index given.
    function fibonacci(num) {
        if (num < 1) {
            return 0;
        } else if (num == 1) {
            return 1;
        } else {
            return fibonacci(num - 1) + fibonacci(num - 2);
        }
    }
    return fibonacci(num);
}

const questionThree = function questionThree(text) {
    // Implement question 3 here
    // This function will return the number of vowels contained in the value str. For the purposes of this exercise, we are not counting y as a vowel.
    const vowels = ["a", "e", "i", "o", "u"];
    var count = 0;
    for (letter in text) {
        if (vowels.includes(text.toString().charAt(letter))) {
            count += 1;
        }
    }
    return count
}

const questionFour = function questionFour(num) {
    // Implement question 4 here
<<<<<<< HEAD
    //This function will return the factorial of the number num provided.
=======
    // This function will return the factorial of the number num provided.
>>>>>>> dbd2ca15ff2cedb934456b3f3c5324021b0bac90
    // The factorial of a number is a simple formula:
    //     factorial(n) = n * (n - 1) * (n - 2)... * 1
    // The factorial of 0 is 1. If num is less than 0, then
    // return NaN.
    function factorial(n) {
        if (n < 0) {
            return NaN;
        } else if (n == 0) {
            return 1;
        } else {
            return n * factorial(n - 1);
        }
    }
    return factorial(num);
}

module.exports = {
    firstName: "Daniel",
    lastName: "Kadyrov",
<<<<<<< HEAD
    studentId: "YOUR STUDENT ID",
=======
    studentId: "10456178",
>>>>>>> dbd2ca15ff2cedb934456b3f3c5324021b0bac90
    questionOne,
    questionTwo,
    questionThree,
    questionFour
};