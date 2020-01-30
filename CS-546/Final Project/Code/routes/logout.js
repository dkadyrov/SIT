const express = require("express")
const router = express.Router()

router.get("/", async (req, res) => {
    res.clearCookie("AuthCookie")
    res.redirect("/")
    return
})

module.exports = router