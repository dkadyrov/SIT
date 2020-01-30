const express = require("express")
const router = express.Router()
const data = require("../data")
const people = data.people;

router.get("/:id", async (req, res) => {
    const id = req.params.id

    if (!id) {
        res.status(400)
        return
    } else {
        const person = await people.getOne(id);

        res.render('people/details', {
            person: person
        });
    }
});

module.exports = router;