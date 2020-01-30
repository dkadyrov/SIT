function arrayCheck(array) {
    if (!Array.isArray(array)) {
        throw `${array || "provided array"} is not an array`;
    } else if (array.length == 0) {
        throw `${array || "provided array"} is empty`;
    }
};

module.exports = {
    description: "This are array utility functions",
    head: (array) => {
        arrayCheck(array);
        // Returns the first element of an array.
        return array[0];
    },

    tail: (array) => {
        // Returns the last element of an array.
        arrayCheck(array);
        return array[array.length-1];
    },

    remove: (array, index) => {
        arrayCheck(array);
        if (index < 0 || index > array.length){
            throw `${index || "provided index"} is negative or larger than the array` 
        }
        array.splice(index, 1);
        
        return array;
    },

    range: (end, value) => {
        let array = []
        let i;
        if (end <= 0){
            throw `${end || "provided value"} is less than or equal to zero, invalid`
        }

        if (value === undefined) {
            for (i = 0; i < end; i++) {
                array.push(i);
            }
        }
        else {
            for (i = 0; i < end; i++) {
                array.push(value);
            }
        }

        return array;
    },

    countElements: (array) => {
        // Will return an object with the count of each unique element in the array. 
        // Must must check:
        // * That the array exists 
        // * The array is of the proper type
        arrayCheck(array);
        let uniques = {};
        for (i = 0; i < array.length; i++) {
                uniques[array[i]] = uniques[array[i]] ? uniques[array[i]] + 1 : 1;
        }
        return uniques;
    },

    isEqual: (arrayOne, arrayTwo) => {
        // Given two arrays, check if they are equal in terms of size and elements and return a boolean
        // Must check
        // - Arrays exist
        // - Each array is of the proper type
        arrayCheck(arrayOne);
        arrayCheck(arrayTwo);

        if (arrayOne.length == arrayTwo.length){
            for (i = 0; i < arrayOne.length; i++) {
                if (arrayOne[i] !== arrayTwo[i]){
                    return False
                };
            }
        }
        else { 
            return False
        }
    },
};