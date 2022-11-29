# Generated by Django 4.1.3 on 2022-11-28 12:59

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0006_mytag'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('job', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TaggedWhatever',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.IntegerField(db_index=True, verbose_name='object ID')),
                ('content_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_tagged_items', to='contenttypes.contenttype', verbose_name='content type')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(app_label)s_%(class)s_items', to='taggit.mytag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='job',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='必填', through='job.TaggedWhatever', to='taggit.MyTag', verbose_name='Tags'),
        ),
    ]