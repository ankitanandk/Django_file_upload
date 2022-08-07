from django.db import models


class Document(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    email1 = models.EmailField(max_length=254, blank=True)
    email2 = models.EmailField(max_length=254, blank=True)
    email3 = models.EmailField(max_length=254, blank=True)
    email4 = models.EmailField(max_length=254, blank=True)
    email5 = models.EmailField(max_length=254, blank=True)
    pdf = models.FileField(upload_to='pdf/')

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super(Document, self).delete(*args, **kwargs)

    def __str__(self):
        return self.title
