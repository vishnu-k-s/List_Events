# Generated by Django 4.0 on 2022-02-18 05:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Events',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image', models.ImageField(blank=True, default=None, null=True, upload_to='Images/')),
                ('description', models.TextField()),
                ('location', models.CharField(max_length=255)),
                ('start_Date', models.DateField()),
                ('end_Date', models.DateField()),
                ('published', models.BooleanField(default=False)),
                ('paid', models.BooleanField(default=False)),
                ('categories', models.ManyToManyField(related_name='events', to='show_events.Categories')),
            ],
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField()),
                ('event', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='show_events.events')),
            ],
        ),
    ]
