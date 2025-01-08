from django.db import models

from wagtail.models import Page

from wagtail.admin.panels import FieldPanel


class FlexPage(Page):
    """Flexible page class"""

    template = "flex/flex_page.html"

    # todo
    # content = StreamField()

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        # todo
        # StreamFieldPanel("content"),
        FieldPanel("subtitle"),
    ]

    class Meta:
        verbose_name = "Flexible Page"
        verbose_name_plural = "Flexible Pages"
