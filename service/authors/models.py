from uuid import uuid4

from django.db import models
from rest_framework import serializers


class Author(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()


class Book(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=40)
    authors = models.ManyToManyField(Author)


class Biography(models.Model):
    uid = models.UUIDField(primary_key=True, default=uuid4)
    text = models.TextField()
    author = models.OneToOneField(Author, on_delete=models.CASCADE)


class Article(models.Model):
    authors = serializers.StringRelatedField(many=True)

    uid = models.UUIDField(primary_key=True, default=uuid4)
    name = models.CharField(max_length=40)
    author = models.ForeignKey(Author, models.PROTECT)

