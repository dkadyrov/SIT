const login = require("./login")
const private = require("./private")
const logout = require("./logout")

const constructorMethod = (app) => {
    app.use(function (request, response, next) {
        let curtime = new Date().toUTCString()
        let curMethod = request.method
        let routeReq = request.originalUrl
        let authString = ""
        if (request.session.loggedin) {
            authString = "(Authenticated User)"
        } else {
            authString = "(Non-Authenticated User)"
        }
        console.log('[' + curtime + ']: ' + curMethod + ' ' + routeReq + ' ' + authString)
        next()
    })

    app.get("/", (req, res) => {
        if (req.session.loggedin === true) {
            res.redirect("/private")
        } else {
            res.render("login/login")
        }
    })

    app.use("/login", login)
    app.use("/private", private)
    app.use("/logout", logout)

    // All else send 404
    app.use("*", (req, res) => {
        res.sendStatus(404)
    })
}

module.exports = constructorMethod