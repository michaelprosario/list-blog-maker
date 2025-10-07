
from bs4 import BeautifulSoup
from google import genai
from google.genai import types
from jinja2 import Environment, FileSystemLoader
import json
import json
import os
import requests

# load environment variables from .env file
from dotenv import load_dotenv
load_dotenv()

def extract_first_event(group_url):
    response = requests.get(group_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # get the first anchor tag named event-card-e-1
    first_event = soup.find('a', {'data-event-label': 'Event Card'})

    # if first_event is None, return None
    if first_event is None:
        print(f'No upcoming events found for {group_url}')
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
    #event_group_link = soup.find('a', {'id': 'event-group-link'})

    # get the href attribute of the event_group_link
    #event_group_link_url = event_group_link['href']

    return {
        'title': event_name,
        'url': url,
        'date': event_date,
        'time': event_time,        
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
        'https://www.meetup.com/space-coast-devs',
        'https://www.meetup.com/1-million-cups-orlando'
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

def get_url_text(url):
    """
    Fetches the HTML content from a URL and returns only the text content.
    
    Args:
        url (str): The URL to fetch content from
        
    Returns:
        str: The text content from the webpage with HTML tags removed
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for bad status codes
        
        # Parse HTML with BeautifulSoup
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.decompose()
            
        # Get text content
        text = soup.get_text()
        
        # Clean up whitespace
        lines = (line.strip() for line in text.splitlines())
        text = ' '.join(chunk for chunk in lines if chunk)
        
        return text
        
    except requests.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None



def getEventData(eventUrl):
    client = genai.Client()


    pageText = get_url_text(eventUrl)



    ## create multiline prompt
    prompt = f"""
    Please read the following event details:

    # Event Details 
    {pageText}. 
    
    Extract the following information:    
    * **Event Title**: Get event title.
    * **Event Summary**: A brief description of the event.
    * **Event Organizer**: group organizing the event.
    * **Location**: The physical address or location name of the event.
    * **When**: The date and time of the event.

    Return the extracted information as a JSON object with the following keys: **title**,**summary**, **organizer**, **location**, and **when**. Do not include any additional text or markdown.
    """

    

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt,
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0) 
        )
    )

    result = response.text    

    ### search ```json and replace with nothing
    result = result.replace("```json", "")

    ### search for ``` and replace with nothing
    result = result.replace("```", "")    

    return result


def getDataFromMeetup():
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

def getEventDataFromMeetupUrl(groupLink):
    first_event_url = extract_first_event(groupLink)
    if first_event_url != '':
        event_data_json = getEventData(first_event_url)   
        if event_data_json:
            event_data = json.loads(event_data_json.strip())
            event_data['url'] = first_event_url              
            return event_data
        
    return None

if __name__ == '__main__':
    groupLinks = getMeetupGroupList()

    eventData = []
    for groupLink in groupLinks:
        first_event_url = extract_first_event(groupLink)
        print(first_event_url)
        if first_event_url != '':
            event_row = getEventDataFromMeetupUrl(groupLink)

            if event_row is not None:
                eventData.append(event_row)

    # sort eventData by date
    eventData = sorted(eventData, key=lambda x: x['when'])

    print("start rendering")
    renderBlogs(eventData, 'template.md', 'output.md')
    
