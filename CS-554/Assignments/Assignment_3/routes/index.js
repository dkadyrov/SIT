const constructorMethod = app => {
  app.get("/", (req, res) => {
    const data = require("../data/data.json");


    res.render("layouts/main", {
      data: data
    })
  });

  app.use("*", (req, res) => {
    res.render("err/404");
  });
};

module.exports = constructorMethod;