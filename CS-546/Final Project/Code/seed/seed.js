const connection = require("../data/connection");
const users = require("../data/users");
const posts = require("../data/posts");
const likes = require("../data/likes")


async function main() {
    const db = await connection();
    await db.dropDatabase();

    const daniel = await users.create({
        first_name: "daniel",
        last_name: "kadyrov",
        username: "dkadyrov",
        password: "mypassword",
        email: "dkadyrov@stevens.edu",
        description: "I love CS-546. Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco",
        picture: "http://lh3.googleusercontent.com/-s0NKVMnoZ4Q/AAAAAAAAAAI/AAAAAAAAFe8/3A9XWVes8vo/photo.jpg"
    });

    const phil = await users.create({
        first_name: "Phil",
        last_name: "Barresi",
        username: "pbarresi",
        password: "cs546",
        email: "pbarresi@stevens.edu",
        description: "I'm gonna give this kid an A+",
        picture: "https://pbs.twimg.com/profile_images/454464721991659521/yQqDnFzh_400x400.jpeg"
    });

    const post1 = await posts.create({
            title: "my first text post",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "text",
            url: "",
        },
        daniel
    );

    await likes.likeOne(phil._id, post1._id)

    const post2 = await posts.create({
            title: "my first image post",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "image",
            url: "https://i.imgflip.com/38roz4.jpg"
        },
        daniel
    );

    const post3 = await posts.create({
            title: "a rick roll",
            content: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            type: "video",
            url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        },
        daniel
    );

    await likes.likeOne(phil._id, post3._id)


    const post4 = await posts.create({
            title: "my first text post 4",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "text",
            url: "",
        },
        daniel
    );

    const post5 = await posts.create({
            title: "my first text post 5",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "text",
            url: "",
        },
        daniel
    );

    const post6 = await posts.create({
            title: "my first text post 6",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "text",
            url: "",
        },
        daniel
    );



    const post7 = await posts.create({
            title: "my first text post",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "text",
            url: "",
        },
        phil
    );

    const post8 = await posts.create({
            title: "my first image post",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "image",
            url: "https://i.imgflip.com/38roz4.jpg"
        },
        phil
    );

    await likes.likeOne(daniel._id, post8._id)


    const post9 = await posts.create({
            title: "a rick roll",
            content: "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.",
            type: "video",
            url: "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
        },
        phil
    );

    await likes.likeOne(daniel._id, post9._id)


    const post10 = await posts.create({
            title: "my first text post 10",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "text",
            url: "",
        },
        phil
    );

    const post11 = await posts.create({
            title: "my first text post 11",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "text",
            url: "",
        },
        phil
    );

    await likes.likeOne(daniel._id, post11._id)


    const post12 = await posts.create({
            title: "my first text post 12",
            content: "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
            type: "text",
            url: "",
        },
        phil
    );

    console.log("Done seeding database")
    
    await db.serverConfig.close();
}

main();