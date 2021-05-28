
Version Info
:   {% if extra.version -%}
    Version:     v{{ extra.version }}  
    {% endif -%}
    {% if git.status -%}
    Revision:     {{ git.short_commit }}  
    Last Updated: {{ git.date }}  
    Author:       {{ git.author }}  
    {% endif -%}
