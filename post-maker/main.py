from jinja2 import Environment, FileSystemLoader
from google import genai
from google.genai import types
import os
import json

# load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

client = genai.Client(api_key=os.environ["GOOGLE_API_KEY"])

MODEL_NAME = "gemini-3-flash-preview"

SYSTEM_INSTRUCTION = (
    "Extract the following data from the input.  Return data json.  Return the following.\n"
    "- title: title of the web page\n"
    "- summary: summary should be limited to 4 sentences\n"
    "- tags: recommended hash tags based on summary\n"
    "- blogName: blog name"
)

generation_config = types.GenerateContentConfig(
    temperature=1,
    top_p=0.95,
    top_k=64,
    max_output_tokens=8192,
    system_instruction=SYSTEM_INSTRUCTION,
)

def buildPosts(urls):
    posts = []
    for url in urls:
        jsonString = getPostDataFromUrl(url)
        # Change jsonString; remove first and last line
        jsonString = jsonString.split('\n', 1)[1]
        jsonString = jsonString.rsplit('\n', 1)[0]

        ## find ''' and replace with empty string
        jsonString = jsonString.replace("```", "")

        # trim up the jsonString
        jsonString = jsonString.strip()


        # write json string to file for debugging
        with open('debug.json', 'w') as f:
            f.write(jsonString)



        jData = json.loads(jsonString)



        posts.append({
            'title': jData['title'],
            'summary': jData['summary'],
            'url': url,
            'blogName': jData['blogName'],
            'tags': jData['tags']
        })
    return posts

def renderBlogs(blogs, template, outputFile):
    # Set up the Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template)

    # Render the template with the blog posts
    output = template.render(posts=blogs)

    # Write the output to a file
    with open(outputFile, 'w') as f:
        f.write(output)

def getPostDataFromUrl(url):
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=url,
        config=generation_config,
    )
    return response.text

urls = [
'https://www.android.com/xr/',
'https://xrblocks.github.io/',
'https://playcanvas.com/',
'https://aframe.io/',
'https://r3f.docs.pmnd.rs/',
'https://thepolys.com/',
'https://discord.com/invite/webxr',
'https://googledevscentralflorida.com/',
'https://www.orlandocodecamp.com/'
]
posts = buildPosts(urls)
#print(posts)
renderBlogs(posts, 'template.md', 'output.md')

