from django.db import models

from wagtail.models import Page, Orderable

from wagtail.fields import RichTextField

from wagtail.admin.panels import (
    FieldPanel,
    PageChooserPanel,
    InlinePanel,
    MultiFieldPanel,
)

from wagtail.fields import StreamField

from streams.blocks import TitleAndTextBlock, RichTextBlock, CardBlock, CTABlock

from modelcluster.fields import ParentalKey


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
        MultiFieldPanel(
            [
                FieldPanel("banner_title"),
                FieldPanel("banner_subtitle"),
                FieldPanel("banner_image"),
                PageChooserPanel("banner_cta"),
            ],
            heading="Banner Options",
        ),
        FieldPanel("body"),
        MultiFieldPanel(
            [
                InlinePanel("carousel_images", max_num=5, label="Image"),
            ],
            heading="Carousel Images",
        ),
    ]


# TODO: ADD TAILWIND CSS CAROUSEL
class HomePageCarouselImages(Orderable):
    """Between 1 and 5 images for the home page carousel."""

    page = ParentalKey(
        HomePage, on_delete=models.CASCADE, related_name="carousel_images"
    )
    carousel_image = models.ForeignKey(
        "wagtailimages.Image",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name="+",
    )

    panels = [FieldPanel("carousel_image")]
