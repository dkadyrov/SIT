const axios = require('axios');

function checkIndex(object, index){
    if (typeof index !== "number") { 
        throw `${index || "index"} is not a number`;
    }
    if (index < 0) {
        throw `${index || "index"} is less than 0`;
    }
    if (index > Object.keys(object).length){
        throw `${index || "index"} is greater than the length`;
    }
}

function checkString(string){
    if (string === undefined){
        throw "Undefined variable(s)"
    }
    if (typeof string !== "string") {
        throw `${string || "string"} is not a string`;
    }
}

function checkIP(ip) {
    checkString(ip)
    const ipformat = /^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$/;

    if (!ip.match(ipformat)) {
        throw `${ip || "ip"} is not a valid IP`;
    }
}

async function getPeople(){
    const { data } = await axios.get("https://gist.githubusercontent.com/robherley/5112d73f5c69a632ef3ae9b7b3073f78/raw/24a7e1453e65a26a8aa12cd0fb266ed9679816aa/people.json");

    return data
}

async function getWork() {
    const { data } = await axios.get("https://gist.githubusercontent.com/robherley/61d560338443ba2a01cde3ad0cac6492/raw/8ea1be9d6adebd4bfd6cf4cc6b02ad8c5b1ca751/work.json");

    return data 
}

async function getWeather() { 
    const { data } = await axios.get("https://gist.githubusercontent.com/robherley/1b950dc4fbe9d5209de4a0be7d503801/raw/eee79bf85970b8b2b80771a66182aa488f1d7f29/weather.json")

    return data
}

async function getPersonById(index){
    const data = await getPeople()
    checkIndex(data, index); 

    return data[index];
}

async function lexIndex(index){
    const data = await getPeople()
    checkIndex(data, index)
    const sortedData = data.sort(
        function(a,b){
            return a.lastName.localeCompare(b.lastName);
        }
    );

    return sortedData[index].firstName + ' ' + sortedData[index].lastName;
}

async function firstNameMetrics(){
    const data = await getPeople();
    const vowels = ["a", "e", "i", "o" , "u"];
    const consonants = ["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "y", "z"];
    let totalLetters = 0;
    let totalVowels = 0;
    let totalConsonants = 0;
    let longestName = data[0].firstName
    let shortestName = data[0].firstName
    data.forEach(function (arrayItem) {
        totalLetters += arrayItem.firstName.length;
        for (let letter of arrayItem.firstName.toLowerCase()){
            if (vowels.includes(letter)){
                totalVowels ++ 
            }
            if (consonants.includes(letter)){
                totalConsonants ++ 
            }
        }
        if (arrayItem.firstName.length > longestName.length){
            longestName = arrayItem.firstName
        } 
        if (arrayItem.firstName.length < shortestName.length){
            shortestName = arrayItem.firstName
        }
    });
    const metrics = {
        "totalLetters" : totalLetters,
        "totalVowels" : totalVowels,
        "totalConsonants" : totalConsonants,
        "longestName" : longestName, 
        "shortestName" : shortestName
    }

    return metrics
}

async function shouldTheyGoOutside(firstName, lastName){
    checkString(firstName)
    checkString(lastName)
    const people = await getPeople();

    const person = people.find(i => i.firstName == firstName && i.lastName == lastName);

    if (person === undefined) {
        throw `${person || "person"} cannot be found`;
    }

    const weather = await getWeather();

    const temp = weather.find(i => i.zip == person.zip).temp;

    let status = "Yes"
    let status1 = "should"
    if (temp < 34){
        status = "No"
        status1 = "should not"
    }

    return `${status}, ${person.firstName} ${status1} go outside.`
}

async function whereDoTheyWork(firstName, lastName){
    checkString(firstName)
    checkString(lastName)
    const people = await getPeople();

    const person = people.find(i => i.firstName == firstName && i.lastName == lastName);

    if (person === undefined) {
        throw `${person || "person"} cannot be found`;
    }

    const work = await getWork();

    const job = work.find(i => i.ssn == person.ssn);

    let fired = "will not"
    if (job.willBeFired === "true"){
        fired = "will"
    }

    const line = `${person.firstName} ${person.lastName} - ${job.jobTitle} at ${job.company}. They ${fired} be fired.`

    return line
}



async function findTheHacker(ip){
    checkIP(ip)
    const work = await getWork();

    const person_ip = work.find(i => i.ip == ip);

    if (person_ip === undefined) {
        throw `${ip || "ip"} cannot be found in database`;
    }
    
    const people = await getPeople();

    const person = people.find(i => i.ssn == person_ip.ssn);

    return `${person.firstName} ${person.lastName} is the hacker!`
}

module.export = {
    getPersonById, 
    lexIndex,
    firstNameMetrics,
    shouldTheyGoOutside,
    whereDoTheyWork,
    findTheHacker
}