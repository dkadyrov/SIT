const express = require("express")
const bodyParser = require("body-parser")
const app = express()
const exphbs = require("express-handlebars")
const Handlebars = require('handlebars')
const cookieParser = require('cookie-parser')
const session = require("express-session")

const configRoutes = require("./routes")

const handlebarsInstance = exphbs.create({
    extname: 'hbs',
    defaultLayout: "main",
    helpers: {
        asJSON: (obj, spacing) => {
            if (typeof spacing === "number")
              return new Handlebars.SafeString(JSON.stringify(obj, null, spacing));
      
            return new Handlebars.SafeString(JSON.stringify(obj));
          }
    },
})

app.use(cookieParser())
app.use("/public", express.static(__dirname + "/public"))
app.use(bodyParser.json())
app.use(bodyParser.urlencoded({extended: true}))

app.engine('hbs', handlebarsInstance.engine)
app.set('view engine', 'hbs')

app.use(session({
    name: "AuthCookie",
    secret: 'some secret string!',
    resave: false,
    saveUninitialized: true
}))

configRoutes(app);

app.listen(3000, () => {
    console.log("Listening on port 3000")
})