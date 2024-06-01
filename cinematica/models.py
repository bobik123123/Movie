from django.contrib.auth.models import User
from django.db import models

nb = {'null': True, 'blank': True}

class Janr(models.Model):
    name = models.CharField()

    def __str__(self):
        return self.name

class Author(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, null=True, blank=True)

    @property
    def full_name(self):
        return f'{self.last_name} {self.first_name}{" " + self.middle_name if self.middle_name else ""}'

    def __str__(self):
        return self.full_name



class Movie(models.Model):
    name = models.CharField('Название фильма', db_index=True)
    janr = models.ForeignKey(Janr, models.CASCADE, related_name='movies')
    description = models.TextField()
    authors = models.ManyToManyField(Author)
    avatar = models.ImageField(upload_to='media/avatars')
    main_artists = models.TextField()
    artists = models.TextField()
    created_at = models.DateField(db_index=True)

    def __str__(self):
        return self.name


class Reviews(models.Model):
    STARS = [
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 4),
        (5, 5),
    ]
    user = models.ForeignKey(User, models.SET_NULL, **nb, verbose_name="Owner")
    movie = models.ForeignKey(Movie, models.SET_NULL, **nb, verbose_name="Movie", related_name="reviews")
    stars = models.PositiveSmallIntegerField("Stars", choices=STARS, **nb)
    text = models.TextField("Text", **nb)
    created = models.DateField("Created at", auto_now_add=True)
    updated_date = models.DateField("Updated date", auto_now=True)

    class Meta:
        verbose_name = "Review"
        verbose_name_plural = "Reviews"


class Comment(models.Model):
    user = models.ForeignKey(User, models.SET_NULL, **nb, verbose_name="Comment")
    text = models.TextField("Text", **nb)
    movie = models.ForeignKey(Movie, models.SET_NULL, **nb, verbose_name="Movie", related_name="comments")

    class Meta:
        verbose_name = "Comment"
        verbose_name_plural = "Comments"


# class View(models.Model, ABSModel):
#     user = models.ForeignKey(User, models.SET_NULL, related_name='views', **nb)
#     movie = models.ForeignKey(Movie, models.CASCADE, related_name='views')
#     total_view_time = models.PositiveIntegerField(**nb)