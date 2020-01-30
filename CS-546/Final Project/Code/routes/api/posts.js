const express = require("express");
const router = express.Router();
const data = require("../../data");
const posts = data.posts;
const users = data.users;

router.get("/", async (req, res) => {
    try {
        let allPosts = await posts.getAll();
        res.status(200).json(allPosts);
    } catch (e) {
        res.status(500).json({
            error: e.toString()
        });
        return
    }
})

router.get("/:id", async(req, res) => {
    try { 
        const post = await posts.get(req.params.id)

        res.status(200).json(post)
    } catch(e) { 
        res.status(404).json({
            error: e.toString()
        });
        return
    }
})

router.post("/", async (req, res) => {
    try {
        try {
            await users.get(req.body.author)
        } catch (e) {
            res.status(404).json({
                error: "User not found"
            });
            return
        }

        const author = await users.get(req.body.author)

        const post = await posts.create(req.body, author);

        res.status(200).json(post);
    } catch (e) {
        res.status(500).json({
            error: e.toString()
        });
        return
    }
});

router.put("/:id", async (req, res) => {
    try {
        try {
            await posts.get(req.params.id)
        } catch (e) {
            res.status(404).json({
                error: "Post not found"
            });
            return
        }

        const post = await posts.update(req.params.id, req.body)

        res.status(200).json(post)
    } catch (e) {
        res.status(404).json({
            error: e.toString()
        })
        return
    }

});

router.delete("/:id", async (req, res) => {
    try {
        try {
            await posts.get(req.params.id)
        } catch (e) {
            res.status(404).json({
                error: "Post not found"
            });
            return
        }

        const post = await posts.remove(req.params.id)

        res.status(200).json(post)
    } catch (e) {
        res.status(404).json({
            error: e.toString()
        })
        return
    }

});

module.exports = router;