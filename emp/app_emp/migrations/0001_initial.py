from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('salary', models.FloatField()),
                ('age', models.IntegerField()),
                ('birthday', models.DateField()),
                ('remarks', models.TextField()),
            ],
            options={
                'db_table': 'Employee_List',
            },
        ),
    ]
