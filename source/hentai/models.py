from django.db import models

# Create your models here.

# The language
class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

# The series
class Series(models.Model):
    series_name = models.CharField(max_length=255)

    def __str__(self):
        return str(self.id) + ' : ' + self.series_name

# Description, one for each language
class Description(models.Model):
    series_related = models.ForeignKey(Series, related_name='description', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='decription_language', on_delete=models.CASCADE)
    description = models.TextField(default='')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

# The video, episode, tags, etc
class Video(models.Model):
    series = models.ForeignKey(Series, related_name='videos', on_delete=models.CASCADE)
    episode = models.IntegerField()
    upload_date = models.TimeField(auto_now_add=True)
    file_path = models.CharField(max_length=255)
    tags = models.ManyToManyField('VideoTag', related_name='tags')

    def __str__(self):
        return str(self.id) + ' : ' + self.series.series_name + '; Episode: ' + str(self.episode)

# Tags
class VideoTag(models.Model):
    tag_name = models.CharField(max_length=100, default='')

    def __str__(self):
        return str(self.id) + ' : ' + self.tag_name

# Translated tags
class TagLan(models.Model):
    tag = models.ForeignKey(VideoTag, related_name='tag_translation', on_delete=models.CASCADE)
    language = models.ForeignKey(Language, related_name='tag_language', on_delete=models.CASCADE)
    label = models.CharField(max_length=255)

    def __str__(self):
        return self.label