const express = require("express")
const router = express.Router()
const users = require("../data/users")

router.use(function(request, response, next){
    if(request.session.loggedin === true){
        next()
    }
    else{
        response.status(403).render("private/privatenoauth")
    }
})

router.get("/", async (req, res) => {
    for(let i=0; i < users.length; i++){
        if(String(req.session.userId) === String(users[i]._id)){
            res.render("private/private", {user: users[i]})
            return
        }
    }
    
    res.send("Error")
    return
})

module.exports = router