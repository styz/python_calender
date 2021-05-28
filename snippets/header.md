{% if git.status %}
This page was last updated: {{ page.meta.git_revision_date_localized }}  
This page was created: {{ page.meta.git_creation_date_localized }}  
Authors: {{ git_page_authors }}  
{% endif %}
