from django.forms import widgets


class ThumbnailWidget(widgets.ClearableFileInput):
    template_name = 'thumbnail_widget.html'
