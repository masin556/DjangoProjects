# Generated by Django 4.0.3 on 2023-12-10 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pybo', '0005_answer_voter_question_voter_alter_answer_author_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Picture',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='pictures/')),
                ('description', models.TextField(blank=True)),
                ('hashtags', models.CharField(blank=True, max_length=255)),
            ],
        ),
    ]
