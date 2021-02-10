from django.db import models
from django.urls import reverse
from hashids import Hashids

hashids = Hashids()


class Link(models.Model):
    class Meta:
        db_table = 'link'
        verbose_name = 'url'
        verbose_name_plural = 'urls'

    url = models.URLField(max_length=200)

    def get_absolute_url(self):
        return reverse("link_show", kwargs={"pk": self.pk})

    # Encodes Url to a short url
    @staticmethod
    def shorten(link):
        l, _ = Link.objects.get_or_create(url=link.url)
        # using library to encrypt id
        return str(hashids.encrypt(l.pk))

    # Decodes short url to original url
    @staticmethod
    def expand(slug):
        # Decrypting slug and getting '(12,)'
        dirty_str = str(hashids.decrypt(slug))
        # stripping out '(,)'
        clean_id = dirty_str.strip("(,)")
        # now converting '12' into 12
        link_id = int(clean_id)
        l = Link.objects.get(pk=link_id)
        return l.url

    def short_url(self):
        return reverse("redirect_short_url",
                       kwargs={"short_url": Link.shorten(self)})


# class UrlData(models.Model):
#     class Meta:
#         db_table = 'url_data'
#         verbose_name = 'url'
#         verbose_name_plural = 'urls'
#
#     url = models.CharField(max_length=200)
#     date_submitted = models.DateTimeField(auto_now_add=True)
#     usage_count = models.PositiveIntegerField(default=None)
#
#
# def __str__(self):
#     return f"Short Url for: {self.url} is"
