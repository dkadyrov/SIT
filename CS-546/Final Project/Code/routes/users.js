const express = require("express");
const router = express.Router();

const data = require("../data");
const users = data.users;
const posts = data.posts;

router.get('/', async (req, res) => {
    const allPosts = (await posts.getAll()).reverse();

    res.render('index', {
        users: allUsers
    });
});

router.get('/:username', async (req, res) => {
    const user_profile = await users.username(req.params.username);

    let user_posts = [];
    for (i = 0; i < user_profile.posts.length; i++) {
        user_posts.push(await posts.get(user_profile.posts[i]));
    };

    for (i = 0; i < user_profile.likes.length; i++) {
        user_posts.push(await posts.get(user_profile.likes[i]));
    };

    if (req.session.userId) {
        const user = await users.get(req.session.userId);

        for (i = 0; i < user_posts.length; i++) {
            user_posts[i].user = true

            if (user_posts[i].type === "video") {
                user_posts[i].video = true;
            } else if (user_posts[i].type === "image") {
                user_posts[i].image = true;
            };

            if (String(user_posts[i].author.username) === String(user.username)) {
                user_posts[i].deletable = true;
            };

            if (user.likes.length > 0) {
                for (j = 0; j < user.likes.length; j++) {
                    if (String(user_posts[i]._id) === String(user.likes[j])) {
                        user_posts[i].liked = true;
                    };
                };
            };

            if (!user_posts[i].liked) {
                user_posts[i].notliked = true;
            }
        };

        res.render('profile/profile', {
            user: user,
            user_profile: user_profile,
            posts: user_posts,
        });
    } else {

        for (i = 0; i < user_posts.length; i++) {
            if (user_posts[i].type === "video") {
                user_posts[i].video = true;
            } else if (user_posts[i].type === "image") {
                user_posts[i].image = true;
            }
        };

        res.render('profile/profile', {
            user_profile: user_profile,
            posts: user_posts,
        });
    }

})

module.exports = router;