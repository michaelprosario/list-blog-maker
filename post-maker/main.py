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
  system_instruction="Extract the following data from the input.  Return data json.  Return the following.\n- title: title of the web page\n- summary: summary should be limited to 3 sentences\n- tags: recommended hash tags based on summary\n- blogName: blog name",
)

def buildPosts(urls):
    posts = []
    for url in urls:
        jsonString = getPostDataFromUrl(url)
        # Change jsonString; remove first and last line
        jsonString = jsonString.split('\n', 1)[1]
        jsonString = jsonString.rsplit('\n', 1)[0]

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

urls = ['https://innovativeteams.net/librechat-ai-privacy-focused-client-to-your-favorite-llm-tools/']
posts = buildPosts(urls)
#print(posts)
renderBlogs(posts, 'template.md', 'output.md')

