from jinja2 import Environment, FileSystemLoader

# Define the list of blog posts. Add several more blogs with fake data.
blogs = [
    {
        "title": "Google I/O 2024: Key AI Announcements Day 1", 
        "summary": "Summary of key AI announcements from Google I/O 2024.", 
        "url": "https://innovativeteams.net/googleio2024-key-ai-announcements-day-1/"
    },
    {
        "title": "Google I/O 2024: Key AI Announcements Day 2", 
        "summary": "Summary of key AI announcements from Google I/O 2024.", 
        "url": "https://innovativeteams.net/googleio2024-key-ai-announcements-day-2/"
    },
    {
        "title": "Google I/O 2024: Key AI Announcements Day 3", 
        "summary": "Summary of key AI announcements from Google I/O 2024.", 
        "url": "https://innovativeteams.net/googleio2024-key-ai-announcements-day-3/"
    }
]

# Set up the Jinja2 environment and load the template
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template('template.md')

# Render the template with the blog posts
output = template.render(posts=blogs)

# Write the output to a file
with open('output.md', 'w') as f:
    f.write(output)
