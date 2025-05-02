from jinja2 import Environment, FileSystemLoader
import os
import json
import requests
from bs4 import BeautifulSoup
import json

def extract_first_event(group_url):
    response = requests.get(group_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # get the first anchor tag named event-card-e-1
    first_event = soup.find('a', {'id': 'event-card-e-1'})

    # if first_event is None, return None
    if first_event is None:
        return ''

    # get the href attribute of the first_event
    first_event_url = first_event['href']
    return first_event_url

def extract_event_data(url):
    """Extracts event data from a Meetup event page.

    Args:
        url: The URL of the Meetup event page.

    Returns:
        A dictionary containing the event name, date, time, and description.
    """

    # using url remove https://www.meetup.com and assign to variable called meetup_name
    meetup_name = url.split('/')[3]
    print(meetup_name)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Get title of the webpage
    event_name = soup.title.text

    # replace "| Meetup" with empty string
    event_name = event_name.replace(' | Meetup', '')

    # trim whitespace
    event_name = event_name.strip()

    # split the event name by comma
    event_parts = event_name.split(',')

    # get the last element of event_parts
    event_time = event_parts[-1].strip()
    event_date = event_parts[-3].strip()

    # get href element with id of event-group-link
    event_group_link = soup.find('a', {'id': 'event-group-link'})

    # get the href attribute of the event_group_link
    event_group_link_url = event_group_link['href']

    return {
        'title': event_name,
        'url': url,
        'date': event_date,
        'time': event_time,
        'group_url': event_group_link_url,
        'meetup_name': meetup_name
    }

def getMeetupGroupList():
    return [
        'https://www.meetup.com/gdg-central-florida',
        'https://www.meetup.com/Orlando-Developers-Meetup',
        'https://www.meetup.com/florida-software-school',
        'https://www.meetup.com/orlando-devops',
        'https://www.meetup.com/orlandopython',
        'https://www.meetup.com/oviedo-codes',
        'https://www.meetup.com/orlando-chatgpt-meetup',
        'https://www.meetup.com/orlandoaws',
        'https://www.meetup.com/orlando-ai-ml-study-group',
        'https://www.meetup.com/orlandojs',
        'https://www.meetup.com/indienomicon',
        'https://www.meetup.com/hacktivate',
        'https://www.meetup.com/angularcommunity',
        'https://www.meetup.com/Beginning-Web-Development',
        'https://www.meetup.com/meetup-group-sklbvjas',
        'https://www.meetup.com/orlando-innovation-league',
        'https://www.meetup.com/awe-nite-orlando',
        'https://www.meetup.com/producttank-orlando',
        'https://www.meetup.com/agile-orlando',
        'https://www.meetup.com/onetug',
        'https://www.meetup.com/data-tech-florida',
        'https://www.meetup.com/dba-fundamentals-group',
        'https://www.meetup.com/wordpress-orlando',
        'https://www.meetup.com/orlando-lady-developers-meetup',
        'https://www.meetup.com/space-coast-devs'
    ]

def renderBlogs(records, template, outputFile):
    # Set up the Jinja2 environment and load the template
    env = Environment(loader=FileSystemLoader('templates'))
    template = env.get_template(template)

    # Render the template with the blog posts
    output = template.render(posts=records)

    # Write the output to a file
    with open(outputFile, 'w') as f:
        f.write(output)


if __name__ == '__main__':
    groupLinks = getMeetupGroupList()
    eventData = []
    for groupLink in groupLinks:
        first_event_url = extract_first_event(groupLink)
        if first_event_url != '':
            event_data = extract_event_data(first_event_url)
            eventData.append(event_data)

    # sort eventData by date
    eventData = sorted(eventData, key=lambda x: x['date'])

    renderBlogs(eventData, 'template.md', 'output.md')
    

