{% for post in posts %}
## [{{ post.title }}]({{ post.url }}) from {{ post.blogName }}
{{ post.summary }}

{% endfor %}