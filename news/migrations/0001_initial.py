# Generated by Django 5.0.2 on 2024-02-15 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='newsImage/')),
                ('desc', models.TextField(null=True)),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
    ]