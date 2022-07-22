# Generated by Django 4.0.6 on 2022-07-22 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sub_app', '0003_alter_papercat_options_alter_papers_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name_plural': 'BlogCategories'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name_plural': 'BlogPosts'},
        ),
        migrations.AlterField(
            model_name='papers',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sub_app.papercat'),
        ),
        migrations.AlterField(
            model_name='papers',
            name='date',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='papers',
            name='github_url',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
