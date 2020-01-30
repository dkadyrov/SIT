const express = require("express")
const router = express.Router()
const posts = require("../data/posts")
const users = require("../data/users")
const likes = require("../data/likes")

// router.get("/", async (req, res) => {
//     const allPosts = await posts.getAll();

//     res.render("posts/posts", {
//         posts: allPosts
//     });
// });

router.get("/post/:id", async (req, res) => {
    const post = await posts.get(req.params.id);

    if (req.session.userId) {
        const user = await users.get(req.session.userId)

        if (post.type === "video") { 
            post.video = true;
        } else if (post.type === "image"){ 
            post.image = true;
        }

        if(String(post.author.username) === String(user.username)){
            post.deletable = true;
        };

        for(i=0; i<user.likes.length; i++){
            if(String(user.likes[i]) === String(post._id)){
                post.liked = true;
            } 
        };

        if(!post.liked) { 
            post.notliked = true;
        };

        res.render("posts/post", {
            user: user,
            posts: [post]
        })

    } else {
        if (post.type === "video") {
            post.video = true;
        } else if (post.type === "image") {
            post.image = true;
        }

        res.render("posts/post", {
            posts: [post]
        });
    }
});

router.get("/create", async (req, res) => {
    try {
        if (req.session.userId) {
            const user = await users.get(String(req.session.userId))
            res.render("posts/create", {
                user: user
            });
        } else {
            res.redirect("posts")
        }
    } catch (e) {
        res.status(500).render("posts/create", {
            error: e.toString()
        });
    }
});

router.post("/create", async (req, res) => {

    const user = await users.get(String(req.session.userId))

    const data = {
        title: req.body.title,
        content: req.body.content,
        type: req.body.postType,
        url: req.body.url
    }

    try {
        const post = await posts.create(data, user)
        res.redirect("/post/"+post._id)
    } catch (e) {
        res.status(500).render("posts/create", {
            error: e.toString()
        });
        return
    };
});

router.post("/delete", async (req, res) => {
    try {
        await posts.remove(req.body.id)
        res.status(200).redirect("/")
    } catch (e) {
        res.status(404).redirect("/", {
            error: e.toString()
        });
        return
    };

});

router.post("/like", async (req, res) => {
    try {
        const user = await users.get(req.session.userId)
        const post = await posts.get(req.body.id)

        for (i = 0; i < user.likes.length; i++) {
            if (String(user.likes[i]._id) === String(post._id)) {
                res.status(200).redirect("/users/" + user.username)
                return
            };
        };

        await likes.likeOne(user._id, post._id)

        res.status(200).redirect("/users/" + user.username)
    } catch (e) {
        res.status(500).redirect("/posts")
        return
    }
})

router.post("/unlike", async (req, res) => {
    try {
        const user = await users.get(req.session.userId)
        const post = await posts.get(req.body.id)

        for (i = 0; i < user.likes.length; i++) {
            if (String(user.likes[i]) === String(post._id)) {
                await likes.unLikeOne(user._id, post._id)
                break
            }
        };
        res.status(200).redirect("/users/" + user.username)
    } catch (e) {
        res.status(500).redirect("/posts")
        return
    }
})

module.exports = router