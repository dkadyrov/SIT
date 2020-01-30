const express = require("express")
const router = express.Router()
const data = require("../data")
const people = data.people;

router.post("/", async (req, res) => {
    const personName = req.body.personName

    if (!personName) {
        res.status(400).render('people/error')
        return
    }
    else {
        const results = await people.search(personName);

        const results_json = {
            name: personName, 
            results: results
        };

        res.render('people/search', {people: results_json});
    }
});


module.exports = router;
