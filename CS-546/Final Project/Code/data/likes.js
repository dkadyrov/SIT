const collections = require("./collections");
const users = collections.users

async function likeOne(user, post) {
    let userCollection = await users()

    await userCollection.updateOne({
        _id: user
    }, {
            $addToSet: {
                likes: post
            }
        })

    return
}

async function unLikeOne(user, post) {
    let userCollection = await users()

    await userCollection.updateOne({
        _id: user
    }, {
            $pull: {
                likes: post
            }
        })

    return
}

module.exports = {
    likeOne,
    unLikeOne
}