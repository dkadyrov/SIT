const collections = require("./collections");
const utils = require("../utils/utils");
const users = collections.users;
const posts = require("./posts")
const likes = require("./likes")

const bcrypt = require("bcrypt")
const isImageUrl = require('is-image-url');


async function get(id) { 
    if (!id) {
        throw ("Error: id was not defined")
    }

    if (typeof(id) !== Object){
        id = utils.sanitizeID(id)
    }

    const userCollection = await users()

    const user = await userCollection.findOne({
            _id: id
        })
    
    if (user === null) throw "No user with that id";

    return user
};

async function username(username) { 
    const userCollection = await users()

    const user = await userCollection.findOne({
        username: username
    })

    return user
};

async function getAll() {
    const userCollection = await users();

    const allUsers = await userCollection.find({}).toArray();

    return allUsers
}

async function create(data) {
    const userCollection = await users();

    if (await this.username(data.username)){
        throw new Error("Username already exists")
    }

    let picture
    if (isImageUrl(data.picture)){
        picture = data.picture
    }
    else {
        picture = "https://identicon-api.herokuapp.com/"+data.username+"/250?format=png"
    }

    const password = bcrypt.hashSync(data.password, 10);
    
    const user = {
        first_name: data.first_name,
        last_name: data.last_name,
        username: data.username,
        password: password,
        email: data.email,
        description: data.description,
        picture: picture,
        posts: [],
        likes: [],
    };

    const insertInfo = await userCollection.insertOne(user);

    if (insertInfo.insertedCount === 0){
        throw new Error("Could not add user");
    }

    const newId = insertInfo.insertedId;

    const checkUser = await this.get(newId);

    return checkUser
};

async function update(id, data) { 
    if (!id) throw new Error("ID must be provided");

    if (typeof (id) !== Object) {
        id = utils.sanitizeID(id)
    };

    const userCollection = await users();

    const updatedUser = {
        $set: data,
    };

    const updatedInfo = await userCollection.updateOne({
        _id: id
    }, updatedUser);

    const user = await this.get(id)

    return user;
}

async function remove(id) {
    if (!id) throw new Error("ID must be provided");

    if (typeof (id) !== Object) {
        id = utils.sanitizeID(id)
    };

    const userCollection = await users();

    const user = await this.get(id)

    for (i = 0; i < user.likes.length; i++) {
        await likes.unLikeOne(user._id, user.likes[i])
    }

    for (i = 0; i < user.posts.length; i++) {
        await posts.remove(user.posts[i])
    }

    const deletion = await userCollection.deleteOne({
        _id: id
    });

    if (deletion.deletedCount === 0) {
        throw `Could not delete user with id of ${id}`;
    };

    return {
        "deleted": true,
        "data": user
    };
}

module.exports = { 
    get,
    username,
    getAll,
    create,
    update,
    remove
}