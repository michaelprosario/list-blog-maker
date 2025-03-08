import feedparser
import random


def getBlogs():
    blogs = [
        {
            "name": "InspiredToEducate.NET",
            "rss_feed": "https://inspiredtoeducate.net/inspiredtoeducate/feed"
        },
        {
            "name": "InnovativeTeams.NET",
            "rss_feed": "https://InnovativeTeams.NET/feed"
        },
        {
            "name": "Google Developers Blog",
            "rss_feed": "http://feeds.feedburner.com/GDBcode"
        },
        {
            "name": "The GitHub Blog",
            "rss_feed": "https://github.blog/feed/"
        },
        {
            "name": "Smashing Magazine",
            "rss_feed": "http://www.smashingmagazine.com/feed/"
        },
        {
            "name": "web.dev: Blog",
            "rss_feed": "https://web.dev/static/blog/feed.xml"
        },
        {
            "name": "web.dev: Articles",
            "rss_feed": "https://web.dev/static/articles/feed.xml"
        },
        {
            "name": "SitePoint",
            "rss_feed": "https://www.sitepoint.com/sitepoint.rss"
        },
        {
            "name": "dev.to",
            "rss_feed": "https://dev.to/feed"
        },
        {
            "name": "MDN Blog",
            "rss_feed": "https://developer.mozilla.org/en-US/blog/rss.xml"
        },
        {
            "name": "ChangeLog",
            "rss_feed": "https://changelog.com/feed"
        },
        {
            "name": "Facebook Engineering blog",
            "rss_feed": "https://engineering.fb.com/feed/"
        },
        {
            "name": "InfoQ",
            "rss_feed": "https://feed.infoq.com"
        },
        {
            "name": "Martin Fowler",
            "rss_feed": "https://martinfowler.com/feed.atom"
        },
        {
            "name": "coolcatteacher.com",
            "rss_feed": "https://www.coolcatteacher.com/feed/"
        },
        {
            "name": "FLOSS Weekly",
            "rss_feed": "https://feeds.twit.tv/floss.xml"
        },
        {
            "name": "Coding Newbie",
            "rss_feed": "http://feeds.codenewbie.org/cnpodcast.xml"
        },
        {
            "name": "Leadership freak",
            "rss_feed": "https://leadershipfreak.blog/feed"
        },
        {
            "name": "VSCode Blog",
            "rss_feed": "https://code.visualstudio.com/feed.xml"
        },
        {
            "name": "Dzone",
            "rss_feed": "https://feeds.dzone.com/javascript"
        },
        {
            "name": "Google TechTalks",
            "rss_feed": "https://www.youtube.com/feeds/videos.xml?user=GoogleTechTalks"
        },
        {
            "name": "Facebook Engineering",
            "rss_feed": "https://engineering.fb.com/feed/"
        },
        {
            "name": "Coding Horror",
            "rss_feed": "https://feeds.feedburner.com/codinghorror"
        },
        {
            "name": "LinkedIn Engineering",
            "rss_feed": "https://engineering.linkedin.com/blog.rss.html"
        }
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

blogs = getBlogs()

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
