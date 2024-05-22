from django.db import models



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
    review = models.TextField()
    movie = models.ForeignKey(Movie, models.SET_NULL, related_name="reviews", null=True)
    rating = models.PositiveIntegerField()

    def __str__(self):
        return self.review