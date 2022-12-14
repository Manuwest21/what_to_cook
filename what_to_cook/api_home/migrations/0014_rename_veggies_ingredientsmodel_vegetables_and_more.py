# Generated by Django 4.1.2 on 2022-10-26 21:50

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('api_home', '0013_alter_ingredientsmodel_proteins_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredientsmodel',
            old_name='veggies',
            new_name='vegetables',
        ),
        migrations.AddField(
            model_name='ingredientsmodel',
            name='legumes',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[[1, 'Beef'], [2, 'Chicken'], [3, 'Cod'], [4, 'Ground beef'], [5, 'Lamb'], [6, 'Monk fish'], [7, 'Pork'], [8, 'Salmon'], [9, 'Shrimps'], [10, 'Smoked salmon'], [11, 'Trout'], [12, 'Tuna'], [13, 'Turkey'], [14, 'Veal']], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='ingredientsmodel',
            name='spices_and_herbs',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[[1, 'Broccoli'], [2, 'Carrot'], [3, 'Cauliflower'], [4, 'Cucumber'], [5, 'Eggplant'], [6, 'Fennel'], [7, 'Garlic'], [8, 'Green bean'], [9, 'Onion'], [10, 'Shallot'], [11, 'Spinach'], [12, 'Tomato'], [13, 'Zucchini']], max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='ingredientsmodel',
            name='starch',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[[1, 'Broccoli'], [2, 'Carrot'], [3, 'Cauliflower'], [4, 'Cucumber'], [5, 'Eggplant'], [6, 'Fennel'], [7, 'Garlic'], [8, 'Green bean'], [9, 'Onion'], [10, 'Shallot'], [11, 'Spinach'], [12, 'Tomato'], [13, 'Zucchini']], max_length=500, null=True),
        ),
    ]
