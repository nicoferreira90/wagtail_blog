from django.db import models

from wagtail.models import Page

from wagtail.fields import StreamField

from wagtail.admin.panels import FieldPanel

from streams.blocks import TitleAndTextBlock, RichTextBlock, CardBlock, CTABlock


class BlogListingPage(Page):
    """Listing Page lists all blog detail pages"""

    template = "blog_pages/blog_listing_page.html"

    custom_title = models.CharField(
        max_length=100, blank=False, null=False, help_text="Page title"
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
    ]

    def get_context(self, request, *args, **kwargs):
        context = super().get_context(request, *args, **kwargs)
        context["posts"] = BlogDetailPage.objects.live().public()
        return context


class BlogDetailPage(Page):

    template = "blog_pages/blog.html"

    custom_title = models.CharField(
        max_length=100, blank=False, null=False, help_text="Page title"
    )
    blog_banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    body = StreamField(
        [
            ("title_and_text", TitleAndTextBlock()),
            ("full_richtext", RichTextBlock()),
            ("cards", CardBlock()),
            ("cta", CTABlock()),
        ],
        null=True,
        blank=True,
    )

    content_panels = Page.content_panels + [
        FieldPanel("custom_title"),
        FieldPanel("blog_banner_image"),
        FieldPanel("body"),
    ]
