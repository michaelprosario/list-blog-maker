from jinja2 import Environment, FileSystemLoader
import google.generativeai as genai
import os
import json

genai.configure(api_key=os.environ["GOOGLE_API_KEY"])

# Create the model
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="Extract the following data from the input.  Return data json.  Return the following.\n- title: title of the web page\n- summary: summary should be limited to 4 sentences\n- tags: recommended hash tags based on summary\n- blogName: blog name",
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
    response = model.generate_content(url)
    return response.text

urls = [
'https://blog.streamlit.io/hackathon-101-5-simple-tips-for-beginners/',
'https://firebase.google.com/docs/firestore',
'https://supabase.com/docs/guides/getting-started/features',
'https://ai.google.dev/',
'https://codelabs.developers.google.com/codelabs/cloud-vision-api-python',
'https://stitch.withgoogle.com',
'https://data.cityoforlando.net/',
'https://data.nasa.gov/',
'https://data.gov/',
'https://ml5js.org/',
'https://www.kaggle.com/models',
'https://learn.microsoft.com/en-us/semantic-kernel/get-started/quick-start-guide?pivots=programming-language-csharp',
'https://google.github.io/adk-docs/#what-is-agent-development-kit',
'https://dotnet.microsoft.com/en-us/learn/aspnet/blazor-tutorial/intro',
'https://fastapi.tiangolo.com/',
'https://benavlabs.github.io/FastAPI-boilerplate/'
]
posts = buildPosts(urls)
#print(posts)
renderBlogs(posts, 'template.md', 'output.md')

