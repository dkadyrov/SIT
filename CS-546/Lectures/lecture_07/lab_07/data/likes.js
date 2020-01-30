const collections = require("./collections")
const animals = collections.animals
   
async function likeOne(animalId, postId) {
    let animalCollection = await animals()
    await animalCollection.updateOne({
        _id: animalId
    }, {
        $addToSet: {
            likes: postId
        }
    })

    return
}

async function unLikeOne(animalId, postId) {
    let animalCollection = await animals()
    let updateInfo = await animalCollection.updateOne({
        _id: animalId
    }, {
        $pull: {
            likes: postId
        }
    })

    return
}

module.exports = {
    likeOne, 
    unLikeOne,
}