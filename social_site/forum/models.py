from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from math import ceil


class BaseModel(models.Model):
    """ Base Model class for explicit objects attribute to avoid 'Unresolved attribute reference...' """
    objects = models.Manager()

    class Meta:
        abstract = True


class Section(BaseModel):
    """
    The 'Sections' divide the site in discussion categories.
    Each 'Section' contains several 'Discussions'.
    Only site administrators can create 'Sections'.
    """

    name = models.CharField(max_length=80)
    description = models.CharField(max_length=150, blank=True, null=True)
    logo = models.ImageField(blank=True, null=True, default='image_empty.png')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('section_view', kwargs={'pk': self.pk})

    def get_last_discussions(self):
        return Discussion.objects.filter(discussion_section=self).order_by('-creation_date')[:2]

    def get_number_of_posts_in_section(self):
        return Post.objects.filter(post_discussion__discussion_section=self).count()

    class Meta:
        verbose_name = 'Sezione'
        verbose_name_plural = 'Sezioni'
        ordering = ['name']


class Discussion(BaseModel):
    """
    'Discussions' are created by 'Users'.
    Each 'Discussion' belongs to a 'Section'.
    Each 'Discussion' contains several 'Posts'.
    """

    title = models.CharField(max_length=120)
    creation_date = models.DateTimeField(auto_now_add=True)
    discussion_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='discussions')
    discussion_section = models.ForeignKey(Section, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('discussion_view', kwargs={'pk': self.pk})

    def get_n_pages(self):
        discussion_posts = self.post_set.count()
        pages = ceil(discussion_posts / 5)
        return pages

    class Meta:
        verbose_name = 'Discussione'
        verbose_name_plural = 'Discussioni'
        ordering = ['creation_date']


class Post(BaseModel):
    """
    'Posts' are created by 'Users'.
    Each 'Post' belongs to a 'Discussion'.
    """

    post_author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    content = models.TextField()
    creation_date = models.DateTimeField(auto_now_add=True)
    post_discussion = models.ForeignKey(Discussion, on_delete=models.CASCADE)

    def __str__(self):
        return self.post_author.username

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Post'
        ordering = ['creation_date']
