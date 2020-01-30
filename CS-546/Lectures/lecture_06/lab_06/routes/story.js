const express = require("express");
const router = express.Router();
// const data = require("../data");
// const aboutData = data.about;

router.get("/", async (req, res) => {
    try {
        const about = await require('../data/story.json');
        res.json(about);
    } catch (e) {
        res.status(500).send();
    }
});

module.exports = router;
