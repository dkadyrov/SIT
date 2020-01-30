const ObjectID = require('mongodb').ObjectID


function sanitizeID(id) {
    if (typeof id === "string") {
        return ObjectID(id);
    }
    return id;
}

module.exports = {
    sanitizeID
}