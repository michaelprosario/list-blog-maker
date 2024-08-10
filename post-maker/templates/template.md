{% for post in posts %}
## [{{ post.title }}]({{ post.url }})
{{ post.summary }}

{% endfor %}