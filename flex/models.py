from django.db import models

from wagtail.models import Page

from wagtail.admin.panels import FieldPanel
from wagtail.fields import StreamField

from streams.blocks import TitleAndTextBlock, RichTextBlock


class FlexPage(Page):
    """Flexible page class"""

    template = "flex/flex_page.html"

    body = StreamField(
        [
            ("title_and_text", TitleAndTextBlock()),
            ("full_richtext", RichTextBlock()),
        ],
        null=True,
        blank=True,
    )

    subtitle = models.CharField(max_length=100, null=True, blank=True)

    content_panels = Page.content_panels + [
        # todo
        FieldPanel("subtitle"),
        FieldPanel("body"),
    ]

    class Meta:
        verbose_name = "Flexible Page"
        verbose_name_plural = "Flexible Pages"
