import feedparser
import random

# make a list of blogs with their rss feeds related to gaming
# put 5 blogs in the list
def getGamingBlogs():
    blogs = [
        {
            "name": "Kotaku",
            "rss_feed": "https://kotaku.com/rss"
        },
        {
            "name": "Rock Paper Shotgun",
            "rss_feed": "https://www.rockpapershotgun.com/feed"
        },
        {
            "name": "Polygon",
            "rss_feed": "https://www.polygon.com/rss/index.xml"
        },
        {
            "name": "PC Gamer",
            "rss_feed": "https://www.pcgamer.com/rss/"
        },
        {
            "name": "Game Informer",
            "rss_feed": "https://www.gameinformer.com/feed"
        }
    ]
    
    return blogs

def getWebDevBlogs():
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
    
    return blogs

def getWebDevBlogs2():
    blogs = [
        {
            "name": "Dev.to",
            "rss_feed": "https://dev.to/feed"
        },
    ]
    
    return blogs

def getAndroidDevBlogs():
    blogs = [
        {
            "name": "Android Developers Blog",
            "rss_feed": "https://medium.com/feed/androiddevelopers"
        },
        {
            "name": "Android Developers News",
            "rss_feed": "https://android-developers.googleblog.com/feeds/posts/default"
        },
        {
            "name": "ProAndroidDev",
            "rss_feed": "https://proandroiddev.com/feed"
        },
        {
            "name": "Ionic Blog",
            "rss_feed": "https://ionicframework.com/blog/feed.xml"
        },
        {
            "name": "Unity codeer blog",
            "rss_feed": "https://unitycoder.com/blog/feed/"
        },
        {
            "name": "The Knights of Unity Blog",
            "rss_feed": "https://blog.theknightsofunity.com/feed"
        }
        
    ]
    
    return blogs

blogs = getWebDevBlogs2()

# create function to blog posts from a rss feed
def get_blog_posts(rss_feed):    
    feed = feedparser.parse(rss_feed)
    posts = feed.entries
    return posts

def getPostsFromBlogs(blogs):
    all_posts = []
    for blog in blogs:
        posts = get_blog_posts(blog["rss_feed"])
        all_posts.extend(posts)

    # randomize the order of the posts array
    random.shuffle(all_posts)
    return all_posts

all_posts = getPostsFromBlogs(blogs)

# convert the list posts to a text file of links
# the file will be saved in the same directory as this script
# with the name web-links.txt
with open("posts.txt", "w") as file:
    for post in all_posts:
        file.write(f"{post.title} | {post.link}\n\n")
