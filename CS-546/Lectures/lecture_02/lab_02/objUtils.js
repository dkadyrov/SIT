function checkArgs(...args){ 
    // Check if at least 2 arguements
    if (args.length < 2){ 
        throw `${args || "provided arguements"} are less than 2`;
    }

    // Check if args have objects
    for (var i = 0; i < args.length; i++){
        checkObjects(arg[i]);
    }
}

function checkFunction(funct) { 
    // Check if function exists
    if (typeof funct !== "function") { 
        throw `${funct || "provided function"} is not a function`;
    }
}

function checkObject(object) { 
    // Check if object contains numbers
    if (typeof object !== "object") {
        throw `${object || "provided variable"} is not an object`;
    }
}

function extend(...args) { 
    // This method will take the properties from earlier objects in the array `args`, and compose a new object with the combined property from all the entries **without** overwriting properties from earlier entries.
    checkArgs(...args);

    let object = Object.assign({}, ...args.reverse())

    return object
}

function smush(...args) { 
    // This method will take the properties from earlier objects in the array `args`, and compose a new object with the combined property from all the entries **with** overwriting properties from earlier entries.
    checkArgs(...args);

    let object = Object.assign({}, ...args)

    return object
}

function mapValues(object, func) { 
    // Given an object and a function, evaluate the function on the values of the object and return a new object.
    checkObject(object);
    checkFunction(func);

    Object.keys(object).map(function (key, index) {
        object[key] = func(object[key])
    });

    return object
}

module.exports = {
    extend, 
    smush,
    mapValues,
}