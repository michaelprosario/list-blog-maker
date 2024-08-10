import feedparser
import random

blogs = [
    {
        "name": "Dev.to",
        "rss_feed": "https://dev.to/feed"
    },
    {
        "name": "Hacker Noon",
        "rss_feed": "https://hackernoon.com/feed"
    },
    {
        "name": "FreeCodeCamp",
        "rss_feed": "https://www.freecodecamp.org/news/rss/"
    },
    {
        "name": "CSS Tricks",
        "rss_feed": "https://css-tricks.com/feed"
    },
    {
        "name": "Codepen",
        "rss_feed": "https://blog.codepen.io/feed"
    }   
]

# create function to blog posts from a rss feed
def get_blog_posts(rss_feed):    
    feed = feedparser.parse(rss_feed)
    posts = feed.entries
    return posts

all_posts = []
for blog in blogs:
    posts = get_blog_posts(blog["rss_feed"])
    all_posts.extend(posts)

# randomize the order of the posts array
random.shuffle(all_posts)

# convert the list posts to a text file of links
# the file will be saved in the same directory as this script
# with the name web-links.txt
with open("web-links.txt", "w") as file:
    for post in all_posts:
        file.write(f"{post.title} | {post.link}\n\n")
