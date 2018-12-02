# Generated by Django 2.1.3 on 2018-11-30 23:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0002_auto_20181130_2356'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pupil',
            name='correct_language_cito',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='correct_math_cito',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='correct_study_skills_cito',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='dutch_language_test_9th',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='ever_registered_as_school_drop_out',
            field=models.BooleanField(choices=[(0, 'no'), (1, 'yes')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='exit_school_6th_grade',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='family_both_parents',
            field=models.BooleanField(choices=[(0, 'no'), (1, 'yes')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='gender',
            field=models.BooleanField(choices=[(0, 'male'), (1, 'female')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='home_language',
            field=models.IntegerField(choices=[(0, 'Nederlands'), (1, 'andere taal'), (2, 'dialect')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='iq_6th',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='math_test_9th',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='origin',
            field=models.IntegerField(choices=[(0, 'Limburg'), (1, 'Non-Dutch'), (2, '(Other) Dutch')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='parent_support_home_lessons',
            field=models.IntegerField(choices=[(0, 'no'), (1, 'some'), (2, 'a lot'), (3, 'quite a lot')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='parent_support_homework_help',
            field=models.IntegerField(choices=[(0, 'no'), (1, 'some'), (2, 'a lot'), (3, 'quite a lot')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='parent_support_motivation',
            field=models.IntegerField(choices=[(0, 'no'), (1, 'some'), (2, 'a lot'), (3, 'quite a lot')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='parent_support_professional',
            field=models.IntegerField(choices=[(0, 'no'), (1, 'some'), (2, 'a lot'), (3, 'quite a lot')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='primary_school',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='region',
            field=models.IntegerField(choices=[(0, 'North of South Limburg (Sittard area)'), (1, 'South-East Limburg (Heerlen area)'), (2, 'South-West Limburg (Maastricht area)'), (3, 'Central Limburg'), (4, 'North Limburg')], null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='school_motivation_score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='secondary_school',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='secondary_school_location',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='social_capital_score',
            field=models.FloatField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='student_birth_month',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='student_birth_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='student_end_6th_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='student_end_9th_year',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='pupil',
            name='study_track_9th',
            field=models.IntegerField(choices=[(0, 'vmbo bl/kl'), (1, 'vmbo gl/tl'), (2, 'havo'), (3, 'vwo')], null=True),
        ),
    ]
