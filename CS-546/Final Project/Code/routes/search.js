const express = require("express");
const router = express.Router();
const users = require("../data/users");
const posts = require("../data/posts");

router.post("/", async (req, res) => {

    try {
        const results = await posts.search(req.body.search)

        if (req.session.userId) {
            const user = await users.get(req.session.userId)

            for (i = 0; i < results.length; i++) {
                results[i].user = true

                if (results[i].type === "video") {
                    results[i].video = true;
                } else if (results[i].type === "image") {
                    results[i].image = true;
                }

                if (String(results[i].author.username) === String(user.username)) {
                    results[i].deletable = true;
                };

                if (user.likes.length > 0) {
                    for (j = 0; j < user.likes.length; j++) {
                        if (String(results[i]._id) === String(user.likes[j])) {
                            results[i].liked = true;
                        };
                    };
                };

                if (!results[i].liked) {
                    results[i].notliked = true;
                }
            };

            res.render("posts/results", {
                user: user,
                posts: results
            });
        } else {

            for (i = 0; i < results.length; i++) {
                if (results[i].type === "video") {
                    results[i].video = true;
                } else if (results[i].type === "image") {
                    results[i].image = true;
                }
            };

            res.render("posts/results", {
                posts: results
            });
        }
    } catch (e) {
        res.status(404).render("posts/results", {
            error: e.toString()
        });
        return
    };

});

module.exports = router;