# Generated by Django 4.2.3 on 2023-07-17 05:36

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("books", "0001_initial"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="book",
            options={"ordering": ["pk"]},
        ),
    ]