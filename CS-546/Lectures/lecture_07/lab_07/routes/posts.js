const express = require("express");
const router = express.Router();
const data = require("../data");
const posts = data.posts;
const likes = data.likes;
const animals = data.animals;

router.get("/", async (req, res) => {
    try {
        const postList = await posts.getAll();
        res.json(postList);
    } catch (e) {
        res.status(500).json({
            error: "Error displaying posts"
        });
    }
});

router.post("/", async (req, res) => {
    const postData = req.body;

    try {
        await animals.getOne(postData.author);
    } catch (e) {
        res.status(404).json({
            error: "Animal not found"
        });
        return;
    }
    try {
        const {
            title,
            author,
            content
        } = postData;
        const newPost = await posts.createOne(title, author, content);

        res.status(200).json(newPost);
    } catch (e) {
        res.status(500).json({
            error: e.toString()
        });
    }
});

router.get("/:id", async (req, res) => {
    try {
        const post = await posts.getOne(req.params.id);
        res.status(200).json(post);
    } catch (e) {
        res.status(404).json({
            error: "Post not found"
        });
    }
});

router.put("/:id", async (req, res) => {
    const updatedData = req.body;
    try {
        await posts.getOne(req.params.id);
    } catch (e) {
        res.status(404).json({
            error: "Post not found"
        });
    }

    try {
        const updatedPost = await posts.update(req.params.id, updatedData);

        res.status(200).json(updatedPost);
    } catch (e) {
        res.status(500).json({
            error: e.toString()
        });
    }
});

router.delete("/:id", async (req, res) => {
    try {
        await posts.getOne(req.params.id);
    } catch (e) {
        res.status(404).json({
            error: "Post not found"
        });
    }
    try {
        const deletedPost = await posts.getOne(req.params.id);
        const deletedData = {
            deleted: true,
            data: deletedPost
        };
        await likes.unLikeOne(deletedPost.author._id, deletedPost._id)

        await posts.removeOne(deletedPost._id);
        res.status(200).json(deletedData);
    } catch (e) {
        res.status(500).json({
            error: e.toString()
        });
    }
});

module.exports = router;
