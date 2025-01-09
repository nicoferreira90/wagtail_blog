from wagtail import blocks


class TitleAndTextBlock(blocks.StructBlock):

    title = blocks.CharBlock(required=True, help_text="Add your title")
    text = blocks.TextBlock(required=True, help_text="Add additional text")

    class Meta:
        template = "streams/title_and_text_block.html"
        icon = "edit"
        label = "Title and Text"


class RichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Full RichText"


class SimpleRichTextBlock(blocks.RichTextBlock):

    class Meta:
        template = "streams/rich_text_block.html"
        icon = "edit"
        label = "Full RichText"
