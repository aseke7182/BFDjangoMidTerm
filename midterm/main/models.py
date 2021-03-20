from django.db import models


# Create your models here.

class BookJournalBase(models.Model):
    name = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.CharField(max_length=200)
    created_at = models.DateTimeField()

    class Meta:
        abstract = True


class Book(BookJournalBase):
    num_page = models.IntegerField()
    genre = models.CharField(max_length=200)


class Journal(BookJournalBase):
    JOURNAL_TYPE = (
        ('BULLET', 'bullet'),
        ('FOOD', 'food'),
        ('TRAVEL', 'travel'),
        ('SPORT', 'sport'),
    )
    type1 = models.CharField(max_length=200, choices=JOURNAL_TYPE, default='SPORT')
    publisher = models.CharField(max_length=200)
