const express = require("express");
const router = express.Router();

router.get("/", async (req, res) => {
    try {
        const about = await require('../data/education.json');
        res.json(about);
    } catch (e) {
        res.status(500).send();
    }
});

module.exports = router;
