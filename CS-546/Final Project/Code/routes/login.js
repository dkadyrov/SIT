const express = require("express")
const router = express.Router()
const users = require("../data/users")
const bcrypt = require("bcrypt")


router.get("/", async(req, res) => {
    res.render("login/login");
})

router.post("/", async (req, res) => {
    let user;
    try { 
        user = await users.username(req.body.username);
        const hashcmp = await bcrypt.compare(req.body.password, user.password)
        if (hashcmp) {
            req.session.userId = String(user._id);
            req.session.loggedin = true
            res.redirect("/")
            return
        }
    } catch(e) { 
        res.status(401).render("login/login", {
            error: "Incorrect user name or password"
        })
        return
    }
    return
});

module.exports = router