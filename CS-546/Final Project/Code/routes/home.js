const express = require("express");
const router = express.Router();

const data = require("../data");
const users = data.users;
const posts = data.posts;


router.get('/', async(req, res) => {
    const allPosts = (await posts.getAll()).reverse();


    let page = 1
    
    if (req.query.page) {
        page = req.query.page 
    }

    const pageNumber = Math.ceil(allPosts.length / 10);

    const pagePosts = allPosts.slice(((page-1)*10), ((page-1)*10+10));

    if(req.session.userId) { 
        const user = await users.get(req.session.userId);

        for (i = 0; i < pagePosts.length; i++) {
            pagePosts[i].user = true

            if (pagePosts[i].type === "video") {
                pagePosts[i].video = true;
            } else if (pagePosts[i].type === "image") {
                pagePosts[i].image = true;
            }
            
            if (String(pagePosts[i].author.username) === String(user.username)) {
                pagePosts[i].deletable = true;
            };

            if (user.likes.length > 0) {
                for (j = 0; j < user.likes.length; j++) {
                    if (String(pagePosts[i]._id) === String(user.likes[j])) {
                        pagePosts[i].liked = true;
                    };
                };
            };

            if (!pagePosts[i].liked) {
                pagePosts[i].notliked = true;
            }
        };

        res.render('index', {
            user: user,
            posts: pagePosts,
            pagination: {
                page: page,
                pageCount: pageNumber
            }
        })
    } else { 
        for (i = 0; i < pagePosts.length; i++) {
            if (pagePosts[i].type === "video") {
                pagePosts[i].video = true;
            } else if (pagePosts[i].type === "image") {
                pagePosts[i].image = true;
            }
        }

        res.render('index', {
            posts: pagePosts,
            pagination: {
                    page: page,
                    pageCount: pageNumber,
                },
        });
    };
});

module.exports = router;