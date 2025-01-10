from django.db import models

from wagtail.models import Page

from wagtail.fields import RichTextField

from wagtail.admin.panels import FieldPanel, PageChooserPanel

from wagtail.fields import StreamField

from streams.blocks import TitleAndTextBlock, RichTextBlock, CardBlock, CTABlock


class HomePage(Page):
    """Home page model."""

    template = "home/home_page.html"

    max_count = 1
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"])
    banner_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )
    banner_cta = models.URLField(
        blank=True,
        null=True,
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
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        FieldPanel("banner_image"),
        PageChooserPanel("banner_cta"),
        FieldPanel("body"),
    ]
