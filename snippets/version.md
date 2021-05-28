{% if git.status %}
Revision: {{ git.short_commit }}  
Last Updated: {{ git.date }}  
Author: {{ git.author }}  
{% endif %}