from django.db import models


class YoutubeVideo(models.Model):
    title = models.CharField(max_length=300, null=False)
    video_youtube_id = models.CharField(max_length=700, null=False)
    created_date = models.DateTimeField(null=False, blank=True)

    @property
    def youtube_url(self):
        return "https://www.youtube.com/embed/" + str(self.video_youtube_id)

    def __str__(self):
        return "%s" % (str(self.title),)
