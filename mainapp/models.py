from __future__ import unicode_literals

from django.db import models


# Create your models here.
class Article(models.Model):
    id = models.AutoField(primary_key=True)
    type = models.CharField(max_length=16)
    content = models.TextField()

    def __repr__(self):
        return "{}, {}, {}".format(self.id, self.type, self.content)


class Company(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    name = models.CharField(max_length=128, blank=True)
    description = models.TextField(blank=True)
    country = models.CharField(max_length=32, default='', blank=True)
    city = models.CharField(max_length=32, blank=True)
    site = models.CharField(max_length=32, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    def __repr__(self):
        return "{}".format(self.name)


class Work(models.Model):
    # id = models.PositiveIntegerField(primary_key=True)
    company = models.ForeignKey(Company)
    position = models.CharField(max_length=32, blank=True)
    duties = models.CharField(max_length=128, blank=True)
    date_from = models.DateField(blank=True)
    date_to = models.DateField(blank=True)

    def __str__(self):
        return "{}, {}".format(self.company, self.position)

    def __repr__(self):
        return "{}, {}".format(self.company, self.position)


class Study(models.Model):
    id = models.AutoField(primary_key=True)
    school_name = models.CharField(max_length=32)
    course_name = models.CharField(max_length=256)
    date_from = models.DateField()
    date_to = models.DateField()

    def __str__(self):
        return "{}".format(self.school_name)

    def __repr__(self):
        return "{}".format(self.school_name)


class Skill(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    describe = models.TextField()

    def __str__(self):
        return "{}".format(self.name)


class About(models.Model):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=32)
    last_name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)
    phone = models.CharField(max_length=10)
    story = models.TextField()

    def __str__(self):
        return "{}".format(self.first_name)


class Hobby(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=256)
