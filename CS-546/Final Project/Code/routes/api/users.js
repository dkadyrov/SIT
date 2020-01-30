const express = require("express");
const router = express.Router();
const data = require("../../data");
const users = data.users;
const posts = data.posts;
const likes = data.likes; 

router.get("/", async (req, res) => {
    try {
        let allUsers = await users.getAll();
        res.status(200).json(allUsers);
    } catch (e) {
        res.status(500).json({
            error: e.toString()
        });
        return
    }
})

router.get("/:id", async(req, res) => {
    try { 
        const user = await users.get(req.params.id)

        res.status(200).json(user)
    } catch(e) { 
        res.status(404).json({
            error: e.toString()
        });
        return
    }
})

router.post("/", async (req, res) => {
    try {
        const user = await users.create(req.body);

        res.status(200).json(user);
    } catch (e) {
        res.status(500).json({
            error: e.toString()
        });
        return
    }
});

router.put("/:id", async (req, res) => {
    try {
        try {
            await users.get(req.params.id)
        } catch (e) {
            res.status(404).json({
                error: "User not found"
            });
            return
        }

        const user = await users.update(req.params.id, req.body)

        res.status(200).json(user)
    } catch (e) {
        res.status(404).json({
            error: e.toString()
        })
        return
    }

});

router.delete("/:id", async (req, res) => {
    try {
        let user 
        try {
            user = await users.get(req.params.id)
        } catch (e) {
            res.status(404).json({
                error: "User not found"
            });
            return
        }
        
        await users.remove(req.params.id)

        res.status(200).json(user)
    } catch (e) {
        res.status(404).json({
            error: e.toString()
        })
        return
    }

});

module.exports = router;