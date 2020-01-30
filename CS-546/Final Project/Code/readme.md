# iBLGR

Another generic internet blog for the internet masses to satisfy the requirements for CS-546. 

## Accomplishments 

### Core Features

[x] A user can sign up for the site
[x] Once signed up, a user can make different types of posts:
    [x] Post text (like a blog post, but no formatting needs to be supported) and a title.
    [x] Post a video post; user provide a youtube URL and a description and a title, and the video will be embedded when the post is viewed with the description below it
    [x] Post an image post; user provide a URL to an image and a description and a title, and the image will be embedded when the post is viewed with the description below it
[x] A user can search for posts, and if the term appears in the title or description then it will be shown
[x] The main page of the website will show the last 10 posts made, and allow user to scroll back in history to see all posts (from most to least recent), 10 at a time
[x] A user can favorite posts that other users have created, and can go to a page where they can see a list of their favorited posts
[x] User profles. Upon account creation, user will be prompted to create a username that will serve as the url to their personal profile displaying their posts and likes. The profile will display their username, avatar image, and description. The avatar image and description will be ones they provide at account creation
[x] A share menu to send URL to and description of the post as a email, Facebook Status, or Twitter Tweet
[x] Use Bootstrap CSS framework to provide UX interface

## Extra Features
[ ] Users can edit their profile information, like name, email, password, pro􏰂le picture after account creation
[x] Identicon will be created users who did not provide profile picture.
[x] Users can delete their own posts


## Changes from Original Proposal: 

API routes are provided to manage users, posts, and likes. 

The posts database data has been changed: 

```JSON
{
    "id": "post id"
    "title": "title of post", 
    "author": {
        "_id": "user._id", 
        "username": "username",
        "picture": "picture",
    },
    "content": "content of post", 
    "type": "type of post", 
    "url": "url of content"
}
```

Although the author id and username are used for display and redirection purposes, I did not use the picture parameter. I updated it because initially I wanted to show the profile picture with each blog post on the home page but it became too clustered during my preliminary implementation. 

## Future Development Goals

- Finish extra features
- Extend search features
- Lock API use to access with API key
- Continue working on the UX design such as making it mobile-friendly, fixing possible sizing issues. Choose better colors.

## Use 

CD into the directory. Install all necessary packages: 

```bash
npm install
```

Seed the database

```bash
npm run seed
```

Run the server and enjoy!

```bash 
npm start 
```