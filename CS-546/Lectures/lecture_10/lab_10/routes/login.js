const express = require("express")
const router = express.Router()
const users = require("../data/users")
const bcrypt = require("bcrypt")


router.post("/", async (req, res) => {
    for (let i = 0; i < users.length; i++) {
        if (users[i].username === req.body.username) {
            let hashcmp = await bcrypt.compare(req.body.password, users[i].hashedPassword)
            if (hashcmp) {
                req.session.userId = String(users[i]._id)
                req.session.loggedin = true
                res.redirect("/private")
                return
            }
            else {
                break
            }
        }
    }

    res.status(401).render("register/login", {
        error: "Incorrect user name or password"
    })
    return
})

module.exports = router