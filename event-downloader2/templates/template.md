## Orlando Tech Meetups

{% for post in posts %}
### [{{ post.title }}]({{ post.url }})
via {{post.organizer}}

{{ post.summary }}

- WHEN: {{ post.when }}
- WHERE: {{ post.location }}

{% endfor %}