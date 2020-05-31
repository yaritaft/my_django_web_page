from django.core.management.base import BaseCommand
from books.models import BookTag, Book
from youtube.models import YoutubeVideo
from django.utils.timezone import now


class Command(BaseCommand):
    def handle(self, *args, **options):
        new_book_tag = BookTag.objects.get_or_create(keyword="python")[0]
        new_book_tag.save()

        new_book = Book.objects.get_or_create(
            title='Lorem ipsum',
            created_date=now(),
            updated_date=now(),
            summary="Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum Lorem ipsum",
            rate=9,
            link="crazy link",
            author='Adam Linc',
            edition='3rd'

        )[0]
        new_book.save()
        if new_book.tags is None:
            new_book.tags.add(new_book_tag)

        new_youtube_video = YoutubeVideo.objects.get_or_create(
            title='Welcome video',
            video_youtube_id='2uHezsGVzIk',
            created_date=now()
        )[0]
        new_youtube_video.save()
