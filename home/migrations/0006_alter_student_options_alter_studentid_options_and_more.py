# Generated by Django 4.2.11 on 2024-04-07 10:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("home", "0005_subject_subjectmarks"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="student",
            options={"ordering": ["student_id"], "verbose_name": "student"},
        ),
        migrations.AlterModelOptions(
            name="studentid", options={"ordering": ["student_id"]},
        ),
        migrations.AlterModelOptions(
            name="subject", options={"ordering": ["subject_name"]},
        ),
        migrations.AlterModelOptions(
            name="subjectmarks", options={"ordering": ["student", "subject"]},
        ),
        migrations.CreateModel(
            name="ReportCard",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date_of_generation", models.DateField(auto_created=True)),
                ("student_rank", models.IntegerField()),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="studentreportcard",
                        to="home.student",
                    ),
                ),
            ],
            options={"unique_together": {("student_rank", "date_of_generation")},},
        ),
    ]
