# Generated by Django 4.1.4 on 2023-01-06 14:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ("book_manager", "0003_alter_book_author_alter_book_kind"),
    ]

    operations = [
        migrations.AddField(
            model_name="book",
            name="is_out",
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AddField(
            model_name="book",
            name="last_update",
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now),
        ),
    ]
