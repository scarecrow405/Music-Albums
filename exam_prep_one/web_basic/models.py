from django.core.validators import MinLengthValidator, MinValueValidator
from django.db import models

from exam_prep_one.web_basic.validators import validate_username


class Profile(models.Model):
    MIN_LEN_USERNAME = 2
    MAX_LEN_USERNAME = 15

    username = models.CharField(
        max_length=MAX_LEN_USERNAME,
        blank=False,
        null=False,
        validators=[
            MinLengthValidator(MIN_LEN_USERNAME),
            validate_username,
        ],
    )

    email = models.EmailField(
        blank=False,
        null=False,
    )

    age = models.PositiveIntegerField(
        blank=True,
        null=True,
    )

    profile_picture = models.URLField(
        blank=True,
        null=True,
    )


class Album(models.Model):
    class Genres(models.TextChoices):
        POP = "Pop Music", "Pop Music"
        JAZZ = "Jazz Music", "Jazz Music"
        RNB = "R&B Music", "R&B Music"
        ROCK = "Rock Music", "Rock Music"
        COUNTRY = "Country Music", "Country Music"
        DANCE = "Dance Music", "Dance Music"
        HIP_HOP = "Hip Hop Music", "Hip Hop Music"
        OTHER = "Other", "Other"

    MAX_LEN_ALBUM_NAME = 30
    MAX_LEN_ARTIST = 30
    MAX_LEN_GENRE = 30

    album_name = models.CharField(
        max_length=MAX_LEN_ALBUM_NAME,
        unique=True,
        blank=False,
        null=False,
    )

    artist = models.CharField(
        max_length=MAX_LEN_ARTIST,
        blank=False,
        null=False,
    )

    genre = models.CharField(
        max_length=MAX_LEN_GENRE,
        blank=False,
        null=False,
        choices=Genres.choices,
    )

    description = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=False,
        null=False,
    )

    price = models.FloatField(
        blank=False,
        null=False,
        validators=[
            MinValueValidator(0.0),
        ]
    )
