const bluebird = require("bluebird");
const express = require("express");
const redis = require("redis");
const getById = require("./data/data")

const app = express();

bluebird.promisifyAll(redis);

const client = redis.createClient();
const visitor = "persons:id:list"

app.get("/api/people/history", async (req, res) => {
  let people;
  try {
    people = await client.lrangeAsync(visitor, 0, 19);
  }
  catch (error) {
    res.send({ status: error.message });
    return
  }

  let arr = [];

  for (i = 0; i < people.length; i++) {
    let person = await client.getAsync(people[i]);
    arr.push(JSON.parse(person));
  }

  res.json(arr);
  return;
});

app.get("/api/people/:id", async (req, res) => {
  let id = await client.existsAsync(req.params.id);

  if (id === 1) {
    let user = await client.getAsync(req.params.id);
    let person = JSON.parse(user);

    await client.lpushAsync(visitor, req.params.id);
    res.json(person);
  } else {
    let user;

    try {
      user = await getById(parseInt(req.params.id));
    } catch (error) {
      res.send({
        status: error.message
      });
      return
    }

    let person = JSON.stringify(user);

    await client.setAsync(req.params.id, person);
    await client.lpushAsync(visitor, req.params.id);
    res.json(person);
  }
  return;
});

app.listen(3000, () => {
  console.log("We've now got a server!");
  console.log("Your routes will be running on http://localhost:3000");
});