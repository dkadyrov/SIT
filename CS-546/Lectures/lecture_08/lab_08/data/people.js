const axios = require('axios');

async function getAll() {
    const {data} = await axios.get("https://gist.githubusercontent.com/robherley/5112d73f5c69a632ef3ae9b7b3073f78/raw/24a7e1453e65a26a8aa12cd0fb266ed9679816aa/people.json");

    return data
}

async function getOne(id) {
    if (!id) throw "ID must be provided";

    const people = await getAll();

    const person = people.find(i => i.id == id);

    if (person === undefined) {
        throw `${person || "person"} cannot be found`;
    };

    return person;
}

async function search(name) {
    if (!name || typeof (name) !== "string") throw "Name must be provided";

    const query = name.toLowerCase();

    const people = await getAll();

    let results = [];

    for (let i = 0; i < people.length; i++) {
        // Search for the string in the persons first name and last name
        if (people[i].firstName.toLowerCase().includes(name) || people[i].lastName.toLowerCase().includes(query)) {
            // List must be no more than 20 people
            if (results.length < 20) {
                results.push(people[i])
            } else {
                break
            }
        }
    };

    return results;
}


module.exports = {
    getOne,
    getAll,
    search,
}