const express = require("express");
const router = express.Router();
const data = require("../data");
const animals = data.animals;
const posts = data.posts;
const likes = data.likes; 

const fillArray = async (postsArray) => {
    let filledArray = []
    for (let i = 0; i < postsArray.length; i++) {
        let onePost = await posts.getOne(postsArray[i])
        let id = {
            _id: onePost._id,
            title: onePost.title
        }
        filledArray.push(id)
    }
    return (filledArray)
}

router.get("/", async (req, res) => {
    try {
        let animalList = await animals.getAll();

        for (let i = 0; i < animalList.length; i++) {
            const animalPost = await posts.postsByAuthor(animalList[i]._id)
            if (animalPost.length > 0) {
                animalList[i].posts = await fillArray(animalPost)
            }
            else { 
                animalList[i].posts = [];
            };
            if (animalList[i].likes.length > 0) {
                animalList[i].likes = await fillArray(animalList[i].likes);
            };

        }
        
        res.status(200).json(animalList);
    } catch (e) {
        res.sendStatus(500);
    }
});

router.post("/", async (req, res) => {
    const animalInfo = req.body;

    if (!animalInfo) {
        res.status(400).json({
            error: "You must provide data to create a user"
        });
        return;
    }

    if (!animalInfo.name) {
        res.status(400).json({
            error: "You must provide a name"
        });
        return;
    }

    if (!animalInfo.animalType) {
        res.status(400).json({
            error: "You must provide an animal type"
        });
        return;
    }

    try {
        const newAnimal = await animals.createOne(
            animalInfo.name,
            animalInfo.animalType
        );
            
        newAnimal.posts = []
        res.status(200).json(newAnimal);
    } catch (e) {
        res.sendStatus(500).json({
            error: e.toString()
        });
    }
});

router.get("/:id", async (req, res) => {
    try { 
        try {
            await animals.getOne(req.params.id);
        } catch (e) {
            res.status(404).json({
                error: "Animal not found"
            });
            return;
        }

        let animal = await animals.getOne(req.params.id);
        const post = await posts.postsByAuthor(animal._id)
        
        if (post.length > 0) {
            animal.posts = await fillArray(post)
        }
        else {
            animal.posts = []
        }
        if (animal.likes.length > 0) {
            animal.likes = await fillArray(animal.likes)
        }
       
        res.status(200).json(animal);
    } catch (e) {
        res.sendStatus(404).json({
            error: e.toString()
        });
    }
});

router.put("/:id", async (req, res) => {
    const animalInfo = req.body;
    if (!animalInfo) {
        res.status(400).json({
            error: "You must provide data to update a user"
        });
        return;
    }

    if (!animalInfo.newName || !animalInfo.newType) {
        res.status(400).json({
            error: "You must provide a newName or a newType"
        });
        return;
    }

    try {
        await animals.getOne(req.params.id);
    } catch (e) {
        res.status(404).json({
            error: "Animal not found"
        });
        return;
    }

    try {
        const newData = {
            name: animalInfo.newName,
            animalType: animalInfo.newType
        };

        const updatedAnimal = await animals.update(req.params.id, newData);

        const postArray = await posts.postsByAuthor(req.params.id);

        if (postArray.length > 0) {
            updatedAnimal.posts = await fillArray(postArray)
        }
        else {
            updatedAnimal.posts = []
        }
        if (updatedAnimal.likes.length > 0) {
            updatedAnimal.likes = await fillArray(updatedAnimal.likes)
        }
        res.status(200).json(updatedAnimal);
    } catch (e) {
        res.sendStatus(500).json({
            error: e.toString()
        });
    }
});

router.delete("/:id", async (req, res) => {
    try {
        await animals.getOne(req.params.id);
    } catch (e) {
        res.status(404).json({
            error: "Animal not found"
        });
        return;
    }

    try {
        const deletedAnimal = await animals.getOne(req.params.id);
        
        const deletedPosts = await posts.postsByAuthor(deletedAnimal._id);

        let likesArray = [];
        let postsArray = [];

        if (deletedAnimal.likes.length > 0) {
            likesArray = await fillArray(deletedAnimal.likes)
        };

        if (deletedPosts.length > 0) {
            postsArray = await fillArray(deletedPosts)
        };

        for (let i = 0; i < deletedAnimal.likes.length; i++) {
            await likes.unLikeOne(deletedAnimal.id, deletedAnimal.likes[i])
        };

        for (let i = 0; i < deletedPosts.length; i++) {
            await posts.removeOne(deletedPosts[i]);
        };

        deletedAnimal.likes = likesArray;
        deletedAnimal.posts = postsArray;

        const deletedData = {
            deleted: true,
            data: deletedAnimal
        };

        await animals.removeOne(req.params.id);

        res.json(deletedData);
    } catch (e) {
        console.log(e)
        res.sendStatus(500).json({
            error: e.toString()
        });
        return;
    }
});

module.exports = router;
