const express = require("express");
const router = express.Router();
const posts = require("../data/posts");

router.post("/", async(req, res) => {
    try{
        // console.log(req.body.id)
        await posts.remove(req.body.id)
        res.status(200).redirect("/")
    } catch (e) {
        res.status(404).redirect("/", {
            error: e.toString()
        });
        return
    };

});

module.exports = router;