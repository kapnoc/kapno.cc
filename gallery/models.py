from django.db import models


# class GalleryEntry(models.Model):
#     # image = models.ForeignKey(Image, on_delete=models.DO_NOTHING)
#     name = models.CharField(max_length=255, blank=True, default="")
#     description = models.TextField(blank=True, default="")
#     parent = models.ForeignKey(
#         'GalleryEntry', blank=True, null=True, on_delete=models.DO_NOTHING)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)

#     def __str__(self):
#         return f'{self.name} (GalleryEntry {self.pk})'

#     @property
#     def child_count(self):
#         return self.galleryentry_set.count()

#     def save(self, *args, **kwargs):
#         if self.description == "":
#             self.description = self.image.description
#         if self.name == "":
#             self.name = self.image.name
#         super().save(*args, **kwargs)
