from django.contrib import admin
from forum.models import Discussion, Post, Section


class DiscussionModelAdmin(admin.ModelAdmin):
    """
    Settings to improve management and visualization of Discussion's page in the admin panel.

    Displayed attributes: title, section, author.
    'author' need '__username' in order to get the parameter as a string and execute the query.
    """

    model = Discussion
    list_display = ['title', 'discussion_section', 'discussion_author']
    search_fields = ['title', 'discussion_author__username']
    list_filter = ['discussion_section', 'creation_date']


class PostModelAdmin(admin.ModelAdmin):
    """
    Settings in order to improve management and visualization of Post's page in the admin panel.

    Displayed attributes: author, discussion.
    """

    model = Post
    list_display = ['post_author', 'post_discussion']
    search_fields = ['content']
    list_filter = ['creation_date', 'post_author']


class SectionModelAdmin(admin.ModelAdmin):
    """
    Settings in order to improve management and visualization of Post's page in the admin panel.

    Displayed attributes: section, description.
    """

    model = Section
    list_display = ['name', 'description']


admin.site.register(Discussion, DiscussionModelAdmin)
admin.site.register(Post, PostModelAdmin)
admin.site.register(Section, SectionModelAdmin)
