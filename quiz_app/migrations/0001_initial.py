# Generated by Django 3.2.6 on 2021-11-26 07:07

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_text', models.CharField(max_length=100)),
                ('correct', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Questions',
            fields=[
                ('question_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('question_text', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('MCQ', 'Multiple Choice Question'), ('FIB', 'Fill In the Blank Question')], max_length=3)),
                ('marks', models.PositiveIntegerField()),
                ('time', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('quiz_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('topic', models.CharField(max_length=100)),
                ('desc', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='QuizTaken',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer_id', models.CharField(blank=True, max_length=1, null=True)),
                ('answer_text', models.CharField(blank=True, max_length=100, null=True)),
                ('question_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='quiz_app.questions')),
            ],
        ),
    ]
