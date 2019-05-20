# Generated by Django 2.2.1 on 2019-05-16 17:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
                ('quantity', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='stock.Order')),
            ],
        ),
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('orderitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.OrderItem')),
                ('capacity', models.IntegerField()),
            ],
            bases=('stock.orderitem',),
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('orderitem_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.OrderItem')),
                ('category', models.CharField(choices=[('starter', 'starter'), ('main', 'main'), ('dessert', 'dessert')], default='starter', max_length=100)),
            ],
            bases=('stock.orderitem',),
        ),
        migrations.CreateModel(
            name='Hard',
            fields=[
                ('drink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Drink')),
                ('time', models.CharField(choices=[('pre-dinner', 'pre-dinner'), ('dinner', 'dinner'), ('post-dinner', 'post-dinner'), ('all-round', 'all-round')], default='starter', max_length=100)),
            ],
            bases=('stock.drink',),
        ),
        migrations.CreateModel(
            name='Soft',
            fields=[
                ('drink_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Drink')),
                ('category', models.CharField(choices=[('hot', 'hot'), ('cold', 'cold')], default='cold', max_length=100)),
            ],
            bases=('stock.drink',),
        ),
        migrations.CreateModel(
            name='Beer',
            fields=[
                ('hard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Hard')),
                ('genre', models.CharField(choices=[('white', 'white'), ('pale', 'pale'), ('IPA', 'IPA'), ('Belgium', 'Belgium')], default='pale', max_length=100)),
            ],
            bases=('stock.hard',),
        ),
        migrations.CreateModel(
            name='FruitJuice',
            fields=[
                ('soft_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Soft')),
                ('fruit', models.CharField(choices=[('melon', 'melon'), ('strawberry', 'strawberry'), ('orange', 'orange'), ('lemon', 'lemon')], default='lemon', max_length=100)),
            ],
            bases=('stock.soft',),
        ),
        migrations.CreateModel(
            name='Soda',
            fields=[
                ('soft_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Soft')),
                ('manufacturer', models.CharField(choices=[('pepsi', 'pepsi'), ('coca', 'coca'), ('inhouse', 'inhouse'), ('other', 'other')], default='pepsi', max_length=100)),
            ],
            bases=('stock.soft',),
        ),
        migrations.CreateModel(
            name='StrongAlcool',
            fields=[
                ('hard_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='stock.Hard')),
                ('type', models.CharField(choices=[('white', 'white'), ('brown', 'brown'), ('other', 'other')], default='white', max_length=100)),
            ],
            bases=('stock.hard',),
        ),
    ]