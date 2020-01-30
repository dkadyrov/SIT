const express = require("express");
const router = express.Router();
const data = require("../data");
const likes = data.likes;
const posts = data.posts;
const animals = data.animals;

router.post("/:id", async (req, res) => {
    const animalId = req.params.id
    const postId = req.query.postId

    let animal
    try {
        animal = await animals.getOne(animalId)
    } catch (e) {
        res.status(404).json({
            error: "No animal with that ID found"
        })
        return
    }

    if (!postId) {
        res.status(400).json({
            error: "No ID parameter passed"
        })
        return
    }

    // Try to get the post
    let post
    try {
        post = await posts.getOne(postId)
    } catch (e) {
        res.status(404).json({
            error: "No post with that ID found"
        })
        return
    }

    for (let i = 0; i < animal.likes.length; i++) {
        if (String(post._id) === String(animal.likes[i])) {
            res.sendStatus(200)
            return
        }
    }

    try {
        await likes.likeOne(animal._id, post._id)
        res.sendStatus(200)
    } catch (e) {
        res.sendStatus(500)
        return
    }

});

router.delete("/:id", async (req, res) => {
    const animalId = req.params.id
    const postId = req.query.postId

    let animal
    try {
        animal = await animals.getOne(animalId)
    } catch (e) {
        res.status(404).json({
            error: "No animal with that ID found"
        })
        return
    }

    // Error check to ensure parameter is passed
    if (!postId) {
        res.status(400).json({
            error: "No postID parameter passed"
        })
        return
    }

    // Try to get the post
    let post
    try {
        post = await posts.getOne(postId)
    } catch (e) {
        res.status(404).json({
            error: "No post with that ID found"
        })
        return
    }

    try {
        await likes.unLikeOne(animal._id, post._id)
        res.sendStatus(200)
    } catch (e) {
        res.sendStatus(500).json({
            error: e.toString()
        })
    }
});

module.exports = router;
