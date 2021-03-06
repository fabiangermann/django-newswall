from django.contrib import admin

from newswall.models import Source, Story


admin.site.register(Source,
    list_display=('name', 'source', 'is_active', 'priority'),
    list_editable=('is_active', 'priority'),
    list_filter=('is_active', 'source'),
    prepopulated_fields={'slug': ('name',)},
    )

admin.site.register(Story,
    date_hierarchy='timestamp',
    list_display=('title', 'source', 'is_active', 'timestamp'),
    list_editable=('is_active',),
    list_filter=('source', 'is_active'),
    search_fields=('object_url', 'title', 'author', 'body'),
    )
