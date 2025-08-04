import feedparser

def getBlogs():
    blogs = [
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
            "name": "Coding Newbie",
            "rss_feed": "http://feeds.codenewbie.org/cnpodcast.xml"
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

def getBlogs2():
    blogs = [
    {
        "name": "Innovate Orlando",
        "rss_feed": "https://innovateorlando.com/feed"
    },
    {
    "name": "Google Cloud Blog",
    "rss_feed": "https://cloud.google.com/blog/products/gcp/rss.xml"
    },
    {
    "name": "Google Developers Blog",
    "rss_feed": "https://developers.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Google AI Blog",
    "rss_feed": "https://ai.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Google Workspace Updates Blog",
    "rss_feed": "https://workspaceupdates.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Android Developers Blog",
    "rss_feed": "https://android-developers.googleblog.com/feeds/posts/default"
    },
    {
    "name": "web.dev",
    "rss_feed": "https://web.dev/feed.xml"
    },
    {
    "name": "Chrome Developers Blog",
    "rss_feed": "https://developer.chrome.com/blog/feed.xml"
    },
    {
    "name": "Firebase Blog",
    "rss_feed": "https://firebase.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Google Security Blog",
    "rss_feed": "https://security.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Google Search Central Blog",
    "rss_feed": "https://developers.google.com/search/blog/rss.xml"
    },
    {
    "name": "DEV Community (general)",
    "rss_feed": "https://dev.to/feed"
    },
    {
    "name": "Hacker Noon (general)",
    "rss_feed": "https://hackernoon.com/feed"
    },
    {
    "name": "InfoQ - Cloud",
    "rss_feed": "https://www.infoq.com/feed/cloud/"
    },
    {
    "name": "DZone - Cloud",
    "rss_feed": "https://dzone.com/articles/rss.xml?section=cloud"
    },
    {
    "name": "The New Stack",
    "rss_feed": "https://thenewstack.io/feed/"
    },
    {
    "name": "Serverless.com Blog",
    "rss_feed": "https://www.serverless.com/blog/rss.xml"
    },
    {
    "name": "Towards Data Science (publication feed)",
    "rss_feed": "https://towardsdatascience.com/feed"
    },
    {
    "name": "Cloud Native Computing Foundation (CNCF) Blog",
    "rss_feed": "https://www.cncf.io/feed/"
    },
    {
    "name": "Google Cloud Community Blogs",
    "rss_feed": "No single RSS feed available for this section"
    },
    {
    "name": "Google Open Source Blog",
    "rss_feed": "https://opensource.googleblog.com/feeds/posts/default"
    },
    {
    "name": "Open Source Initiative Blog",
    "rss_feed": "https://opensource.org/feed/"
    },
    {
    "name": "The GitHub Blog (Open Source section)",
    "rss_feed": "https://github.blog/category/open-source/feed/"
    },
    {
    "name": "ZDNET (Open Source section)",
    "rss_feed": "https://www.zdnet.com/topic/open-source/rss.xml"
    },
    {
    "name": "Open Source For You",
    "rss_feed": "https://opensourceforu.com/feed/"
    },
    {
    "name": "Red Hat Blog (Open Source section)",
    "rss_feed": "https://www.redhat.com/en/blog/feed/rss"
    },
    {
    "name": "Planet GNOME",
    "rss_feed": "https://planet.gnome.org/rss20.xml"
    },
    {
    "name": "Free Software Foundation (FSF) News",
    "rss_feed": "https://www.fsf.org/news/rss.xml"
    },
    {
    "name": "DEV Community (Open Source tag)",
    "rss_feed": "https://dev.to/feed/tag/opensource"
    },
    {
    "name": "TechRepublic (Open Source section)",
    "rss_feed": "https://www.techrepublic.com/rssfeeds/topic/open-source/"
    },

    ]
    return blogs
    
blogs = getBlogs2()

# create function to blog posts from a rss feed
def get_blog_posts(rss_feed):    
    feed = feedparser.parse(rss_feed)
    posts = feed.entries
    return posts

def getPostsFromBlogs(blogs):
    all_posts = []
    for blog in blogs:
        
        posts = get_blog_posts(blog["rss_feed"])

        for post in posts:
            post_data = {
                "title": post.title,
                "link": post.link,
                "blog_name": blog["name"]
            }
            all_posts.append(post_data)

    # randomize the order of the posts array
    #random.shuffle(all_posts)
    return all_posts

all_posts = getPostsFromBlogs(blogs)

# convert the list posts to a text file of links
# the file will be saved in the same directory as this script
# with the name web-links.txt
with open("posts__8_4_2025.txt", "w") as file:
    for post in all_posts:
        file.write(f"{post['title']} | {post['link']}\n\n")
