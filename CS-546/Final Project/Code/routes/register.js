const express = require("express")
const router = express.Router()
const users = require("../data/users")

router.use(function(request, response, next) { 
    if(request.session.loggedin === true) { 
        response.redirect('/')
    } else {
        next();
    }
});

router.get("/", async (req, res) => {
    res.render("register/register");
})

router.post("/", async (req, res) => {
    let user;
    try { 
        user = await users.create(req.body);

        req.session.userId = user._id;
        req.session.loggedin = true;

        res.redirect("/");
    } catch(e) { 
        res.status(500).render("register/register", { 
            error: e.toString()
        });
        return
    };
})

module.exports = router