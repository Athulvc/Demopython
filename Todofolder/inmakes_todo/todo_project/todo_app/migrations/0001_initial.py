from django.db import migrations, models

class Migration(migrations.Migration):
    dependencies = []

    operations = [
        migrations.CreateModel(
            name='Tasks1',  # Replace 'Task' with your model's name
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('priority', models.IntegerField()),
                ('date', models.DateField()),
            ],
        ),
        # Add more CreateModel operations for other models if necessary
    ]
