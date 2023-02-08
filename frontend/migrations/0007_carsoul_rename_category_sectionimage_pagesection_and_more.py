# Generated by Django 4.1.5 on 2023-01-09 23:01

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0006_remove_pagesectioncategory_section_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carsoul',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=250, null=True)),
                ('subTitle', models.CharField(blank=True, max_length=250, null=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('query_text', models.CharField(blank=True, max_length=250, null=True)),
                ('created', models.DateField(auto_now_add=True)),
                ('updated', models.DateField(auto_now=True)),
            ],
        ),
        migrations.RenameField(
            model_name='sectionimage',
            old_name='category',
            new_name='pageSection',
        ),
        migrations.RenameField(
            model_name='sectionimage',
            old_name='query',
            new_name='query_text',
        ),
        migrations.RenameField(
            model_name='sectiontext',
            old_name='category',
            new_name='pageSection',
        ),
        migrations.RemoveField(
            model_name='pagesection',
            name='sectionCategory',
        ),
        migrations.AddField(
            model_name='pagesection',
            name='created',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagesection',
            name='pageCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='allPageSection', to='frontend.pagecategory'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pagesection',
            name='updated',
            field=models.DateField(auto_now=True),
        ),
        migrations.DeleteModel(
            name='PageSectionCategory',
        ),
        migrations.AddField(
            model_name='carsoul',
            name='pageSection',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='carousel', to='frontend.pagesection'),
        ),
    ]