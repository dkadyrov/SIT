const express = require("express");
const router = express.Router();

const data = require("../../data");
const users = data.users;
const posts = data.posts;
const likes = data.likes;

router.post("/", async (req, res) => {
    let user
    try {
        user = await users.get(req.body.user)
    } catch (e) {
        res.status(404).json({
            error: "No user with that ID found"
        })
        return
    }

    let post
    try {
        post = await posts.get(req.body.post)
    } catch (e) {
        res.status(404).json({
            error: "No post with that ID found"
        })
        return
    }

    for (let i = 0; i < user.likes.length; i++) {
        if (String(post._id) === String(user.likes[i])) {
            res.status(200);
            return
        }
    }

    try {
        await likes.likeOne(user._id, post._id);
        res.sendStatus(200);
        return
    } catch (e) {
        res.status(500).json({
            error: e.toString()
        })
        return
    }
});

router.delete("/", async (req, res) => {
    let user
    try {
        user = await users.get(req.body.user)
    } catch (e) {
        res.status(404).json({
            error: "No user with that ID found"
        })
        return
    }

    let post
    try {
        post = await posts.get(req.body.post)
    } catch (e) {
        res.status(404).json({
            error: "No post with that ID found"
        })
        return
    }


    try {

        for (let i = 0; i < user.likes.length; i++) {
            if (String(post._id) === String(user.likes[i])) {
                await likes.unLikeOne(user._id, post._id)
                res.sendStatus(200);
                return
            } else {
                res.sendStatus(200);
                return
            }
        }
    } catch(e) { 
        res.status(500).json({
            error: e.toString()
        })
        return
    }
})

module.exports = router;