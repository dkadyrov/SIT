const collections = require("./collections");
const posts = collections.posts;
const animals = require("./animals");
const ObjectID = require('mongodb').ObjectID
const likes = collections.likes;

function sanitizeID(id) {
    if (typeof id === "string") {
        return ObjectID(id);
    }
    return id;
}

async function getOne(id) {
    if (!id) throw new Error("ID must be provided");

    if (typeof (id) !== Object) {
        id = sanitizeID(id)
    }

    const postCollection = await posts();
    const post = await postCollection.findOne({
        _id: id
    });

    if (post === null) throw "No post with that id";

    return post
}

async function getAll() {
    const postCollection = await posts();

    const allPosts = await postCollection.find({}).toArray();

    return allPosts
}

async function createOne(title, author, content){
    const animalCollection = await animals;

    if (!title || !content){
        throw "title and content need to be provided, and in string form"
    }

    const animal = await animalCollection.getOne(author);
    const postCollection = await posts();

    let newPost = {
        title: title,
        content: content,
        author: {
            _id: animal._id, 
            name: animal.name
        }
    }

    const insertInfo = await postCollection.insertOne(newPost);

    if (insertInfo.insertedCount === 0) throw new Error ("Could not add post");

    const newID = insertInfo.insertedId;

    const post = await this.getOne(newID);

    return post
}

async function removeOne(id) { 
    if (!id) throw new Error("ID must be provided");

    if (typeof (id) !== Object) {
        id = sanitizeID(id)
    }

    const postCollection = await posts();
    
    const post = await getOne(id)

    const deletionInfo = await postCollection.deleteOne({
        _id: post._id
    });

    if (deletionInfo.deletedCount === 0) {
        throw `Could not delete post with id of ${id}`;
    }

    return
}

async function update(id, updateData) {
    if (!id) throw new Error("ID must be provided");

    if (typeof (id) !== Object) {
        id = sanitizeID(id)
    }

    if (!updateData || typeof (updateData) !== "object") throw new Error("Data must be provided and in object form");

    if (!updateData.newTitle && !updateData.newContent){
        throw "newTitle or newContent must be provided"
    }

    let update = {}

    if (updateData.newTitle) {
        update.title = updateData.newTitle
    }
    
    if (updateData.newContent) {
        update.content = updateData.newContent
    };

    const postCollection = await posts();

    const updatedPost = {
        $set: update,
    };

    const updatedInfo = await postCollection.updateOne({
        _id: id
    }, updatedPost);

    return await this.getOne(id);
};

async function postsByAuthor(authorId) { 
    const postCollection = await posts();

    const foundPosts = await postCollection.find({
        "author._id": authorId
    }).toArray()

    const results = [];
    foundPosts.forEach(function(row){
        results.push(row._id)
    }) 

    return results
}

module.exports = {
    createOne,
    getOne,
    getAll,
    removeOne,
    update,
    postsByAuthor,
}

