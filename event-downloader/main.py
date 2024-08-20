import requests
from bs4 import BeautifulSoup
import json

def extract_event_data(url):
    """Extracts event data from a Meetup event page.

    Args:
        url: The URL of the Meetup event page.

    Returns:
        A dictionary containing the event name, date, time, and description.
    """

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
        'tile': event_name,
        'url': url,
        'date': event_date,
        'time': event_time,
        'group_url': event_group_link_url
    }

if __name__ == '__main__':
    url = 'https://www.meetup.com/gdg-central-florida/events/302525771/?eventOrigin=group_upcoming_events'
    event_data = extract_event_data(url)
    print(json.dumps(event_data, indent=2))
    