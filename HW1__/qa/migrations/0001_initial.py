# Generated by Django 4.0.5 on 2022-06-08 21:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.AutoField(primary_key=True, serialize=False)),
                ('question_title', models.CharField(max_length=50)),
                ('question_body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.TextField(max_length=50)),
                ('slug', models.SlugField()),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('answer_id', models.AutoField(primary_key=True, serialize=False)),
                ('answer_body', models.TextField()),
                ('date_posted', models.DateTimeField(auto_now_add=True)),
                ('posted_by', models.CharField(max_length=50)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='qa.questions')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
