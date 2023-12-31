# Generated by Django 4.1 on 2023-09-02 06:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Exam', '0006_alter_exam_description_alter_question_op1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Results',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.PositiveIntegerField(default=0)),
                ('exam', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Exam.exam')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
