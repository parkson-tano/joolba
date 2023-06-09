# Generated by Django 4.2 on 2023-04-28 09:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='View',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('view_date', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='news',
            new_name='article',
        ),
        migrations.RenameField(
            model_name='newsmodel',
            old_name='image',
            new_name='featured_image',
        ),
        migrations.RenameField(
            model_name='newsmodel',
            old_name='deleted',
            new_name='is_deleted',
        ),
        migrations.RemoveField(
            model_name='newsmodel',
            name='category',
        ),
        migrations.RemoveField(
            model_name='newsmodel',
            name='images',
        ),
        migrations.RemoveField(
            model_name='newsmodel',
            name='section',
        ),
        migrations.RemoveField(
            model_name='newsmodel',
            name='subcategory',
        ),
        migrations.RemoveField(
            model_name='newsmodel',
            name='updated_at',
        ),
        migrations.RemoveField(
            model_name='newsmodel',
            name='view_count',
        ),
        migrations.AddField(
            model_name='comment',
            name='liked',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='is_draft',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='is_published',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='newsmodel',
            name='other_image',
            field=models.ImageField(blank=True, upload_to='news'),
        ),
        migrations.DeleteModel(
            name='Like',
        ),
        migrations.AddField(
            model_name='view',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='views', to='news.newsmodel'),
        ),
    ]
