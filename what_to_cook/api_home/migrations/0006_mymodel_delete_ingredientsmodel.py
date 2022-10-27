# Generated by Django 4.1.2 on 2022-10-26 05:26

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api_home', '0005_ingredientsmodel_remove_ingredients_ingredients_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('my_field2', multiselectfield.db.fields.MultiSelectField(choices=[(1, 'Item title 2.1'), (2, 'Item title 2.2'), (3, 'Item title 2.3'), (4, 'Item title 2.4'), (5, 'Item title 2.5')], max_length=3)),
            ],
        ),
        migrations.DeleteModel(
            name='IngredientsModel',
        ),
    ]