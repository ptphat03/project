# Generated by Django 5.1.1 on 2024-09-23 01:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("course", "0005_alter_course_course_id"),
        ("test_group", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="testgroup",
            name="test_group_name",
            field=models.CharField(max_length=255, unique=True),
        ),
        migrations.CreateModel(
            name="Test",
            fields=[
                ("test_id", models.AutoField(primary_key=True, serialize=False)),
                ("test_name", models.CharField(max_length=255)),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="course.course"
                    ),
                ),
                (
                    "test_group",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="test_group.testgroup",
                    ),
                ),
            ],
        ),
    ]
