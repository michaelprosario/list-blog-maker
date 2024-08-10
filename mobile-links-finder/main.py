import feedparser
import random

# list blogs with their rss feeds. blogs should be related to android development, ionic development or react native development
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
with open("links.txt", "w") as file:
    for post in all_posts:
        file.write(f"{post.title} | {post.link}\n\n")
