

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0005_mechanic_skill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mechanic',
            name='skill',
            field=models.CharField(max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Repairing', 'Repairing'), ('Repairing Done', 'Repairing Done'), ('Released', 'Released')], default='Pending', max_length=50, null=True),
        ),
    ]
