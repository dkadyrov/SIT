const people = require("./data.json");

function getById(id) {
    return new Promise((resolve, reject) => {
        setTimeout(() => {
            if (id && id>0 && Number.isInteger(id) && id <= people.length) {
                for (i=0; i < people.length; i++) {
                    if (id === people[i]["id"]) {
                        resolve(people[i]);
                        break
                    }
                }
            } else {
                reject(new Error("Error: User Not Found or Incorret ID"));
            }
        }, 5000);
    });
}

module.exports = getById
