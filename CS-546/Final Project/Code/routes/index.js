const home = require("./home");
const users = require("./users");
const register = require("./register");
const login = require("./login");
const logout = require("./logout");
const posts = require("./posts")
const search = require("./search")

const apiUsers = require("./api/users");
const apiPosts = require("./api/posts");
const apiLikes = require("./api/likes");

const constructorMethod = app => {
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
    });

    app.use("/api/users", apiUsers);
    app.use("/api/posts", apiPosts);
    app.use("/api/likes", apiLikes);

    app.use("/", home);

    app.use("/users", users);

    app.use("/register", register);
    app.use("/login", login);
    app.use("/logout", logout);

    app.use("/posts", posts);
    app.use("/posts/search", search);

    app.use("*", (req, res) => {
        res.redirect("/")
        // res.status(404).json({
        //     error: "Not found"
        // });
    });
};

module.exports = constructorMethod;