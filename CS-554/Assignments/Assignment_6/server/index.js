const express = require("express");
const bodyParser = require("body-parser");
const redisConnection = require("../redis-connection");
const nrpSender = require("../nrp-sender-shim");
const worker = require("../worker");

const app = express();
app.use(bodyParser.json());

app.get("/api/people/:id", async (req, res) => {
    try {
        let response = await nrpSender.sendMessage({
            redis: redisConnection,
            eventName: "get-user",
            data: {
                message: req.params.id
            },
            expectsResponse: true
        })

        res.json(response);
    } catch (error) {
        res.send({
            status: error.message
        });
    }
});

app.post("/api/people", async (req, res) => {
    try {
        let response = await nrpSender.sendMessage({
            redis: redisConnection,
            eventName: "push-user",
            data: {
                message: req.body
            },
            expectResponse: true,
        });
        res.json(response);
    } catch (error) {
        res.send({
            status: error.message
        });
        return
    }
});

app.delete("/api/people/:id", async (req, res) => {
    try {
        let response = await nrpSender.sendMessage({
            redis: redisConnection,
            eventName: "delete-data",
            data: {
                message: req.params.id
            },
            expectResponse: true,
        });
        res.json(response);
    } catch (error) {
        res.send({
            status: error.message
        });
        return
    }
});

app.put("/api/people/:id", async (req, res) => {
    try {
        let response = await nrpSender.sendMessage({
            redis: redisConnection,
            eventName: "update-data",
            data: {
                message: req.params.id,
                updates: req.body
            },
            expectResponse: true,
        });
        res.json(response);
    } catch (error) {
        res.send({
            status: error.message
        });
        return
    }
});

app.listen(3000, () => {
    console.log("We've now got a server!");
    console.log("Your routes will be running on http://localhost:3000");
});