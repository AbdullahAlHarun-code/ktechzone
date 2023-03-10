# Generated by Django 4.1.5 on 2023-01-09 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('frontend', '0005_pagesectioncategory_section_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='pagesectioncategory',
            name='section',
        ),
        migrations.AddField(
            model_name='pagesection',
            name='sectionCategory',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='sectionCategory', to='frontend.pagesectioncategory'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='pagesectioncategory',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='PageSectionCategory', to='frontend.pagecategory'),
        ),
    ]
