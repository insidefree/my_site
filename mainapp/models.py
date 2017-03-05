from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    type = models.CharField(max_length=16)
    content = models.TextField()

    def __repr__(self):
        return "{}, {}, {}".format(self.id, self.type, self.content)


class Work(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    describe = models.CharField(max_length=256)

    def __str__(self):
        return "{}, {}".format(self.name, self.describe)

    def __repr__(self):
        return "{}, {}".format(self.name, self.describe)


class Study(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    date_start = models.DateField()
    date_end = models.DateField()
    describe = models.CharField(max_length=256)

    def __str__(self):
        return "{}, {}, {}, {}".format(self.name, self.date_start, self.date_end, self.describe)

    def __repr__(self):
        return "{}, {}, {}, {}".format(self.name, self.date_start, self.date_end, self.describe)


class Company(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    describe = models.CharField(max_length=256)

    def __str__(self):
        return "{}, {}".format(self.name, self.describe)

    def __repr__(self):
        return "{}, {}".format(self.name, self.describe)

class Skill(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    describe = models.TextField()

    def __str__(self):
        return "{} - {}".format(self.name, self.describe)

class About_me(models.Model):
    id = models.PositiveIntegerField(primary_key=True)
    content = models.TextField()

    def __str__(self):
        return "{}".format(self.content)