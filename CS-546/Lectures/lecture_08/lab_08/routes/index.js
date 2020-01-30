const searchRoute = require('./search')
const detailsRoute = require('./details')
const path = require('path')

const constructorMethod = (app) => {
    
    app.get("/", (req, res) => {
        res.sendFile(path.resolve("static/index.html"))
    })

    app.use("/details", detailsRoute)
    app.use("/search", searchRoute)
    
    // All else send 404
    app.use("*", (req, res) => {
        // 404 Not found page if we enter invalid URL
        res.sendStatus(404)
    })
}

module.exports = constructorMethod