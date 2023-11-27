# Generated by Django 4.2.4 on 2023-11-06 17:19

from django.db import migrations, models
import django.db.models.deletion
import main_app.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assassin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('weapon_type', models.CharField(max_length=100)),
                ('assassination_technique', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DemonHunter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('weapon_type', models.CharField(max_length=100)),
                ('demon_slaying_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('elemental_power', models.CharField(max_length=100)),
                ('spellbook_type', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('student_id', main_app.models.StudentIDField()),
            ],
        ),
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=70, unique=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='FelbladeDemonHunter',
            fields=[
                ('demonhunter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.demonhunter')),
                ('felblade_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.demonhunter',),
        ),
        migrations.CreateModel(
            name='Necromancer',
            fields=[
                ('mage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.mage')),
                ('raise_dead_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.mage',),
        ),
        migrations.CreateModel(
            name='ShadowbladeAssassin',
            fields=[
                ('assassin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.assassin')),
                ('shadowstep_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.assassin',),
        ),
        migrations.CreateModel(
            name='TimeMage',
            fields=[
                ('mage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.mage')),
                ('time_magic_mastery', models.CharField(max_length=100)),
                ('temporal_shift_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.mage',),
        ),
        migrations.CreateModel(
            name='VengeanceDemonHunter',
            fields=[
                ('demonhunter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.demonhunter')),
                ('vengeance_mastery', models.CharField(max_length=100)),
                ('retribution_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.demonhunter',),
        ),
        migrations.CreateModel(
            name='ViperAssassin',
            fields=[
                ('assassin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.assassin')),
                ('venomous_strikes_mastery', models.CharField(max_length=100)),
                ('venomous_bite_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.assassin',),
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('receiver', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='received_messages', to='main_app.userprofile')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='sent_messages', to='main_app.userprofile')),
            ],
        ),
    ]
