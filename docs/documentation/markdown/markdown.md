{% include 'version.md' %}

:fa-external-link: [MkDocs](http://www.mkdocs.org/)

(c)

{% if git.status %}
This page was last updated: {{ page.meta.git_revision_date_localized }} <br>
This page was created: {{ page.meta.git_creation_date_localized }} <br>
Authors: {{ git_page_authors }} <br>
{% endif %}

{{ macros_info() }}