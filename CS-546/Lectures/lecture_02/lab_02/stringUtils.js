const arrayUtils = require('./arrayUtils');

function checkString(str) { 
    if (typeof str!=="string") { 
        throw `${str || "provided variable"} is not a string`;
    }
}

function checkNumber(number) {
    if (typeof number!=="number") { 
        throw `${number || "provided variable"} is not a number`;
    }
    if (number<=0) { 
        throw `${number || "provided number"} is less than 0`
    }
}


function capitalize(string) { 
    // Given a string, capitalize the first letter and lowercase the remaining characters.
    checkString(string);
    return string.charAt(0).toUpperCase() + string.slice(1).toLowerCase();
}

function repeat(string, num) {
    // Given `string` and `num`, repeat the string `num` amount of times.
    checkString(string);
    checkNumber(num);
    
    return string.repeat(num)
}

function countChars(string) { 
    // Return an object that has the mapping of a character and the amount of times it appears in a string. _Hint:_ You may use a function you have written already.
    checkString(string)
    array = string.split('')
    elements = arrayUtils.countElements(array)

    return elements
}

module.exports = {
    capitalize,
    repeat, 
    countChars,
}

console.log(repeat("foo", 3))