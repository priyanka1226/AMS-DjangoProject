

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0002_mechanic_request'),
    ]

    operations = [
        migrations.AddField(
            model_name='request',
            name='status',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Approved', 'Approved'), ('Released', 'Released')], default='Pending', max_length=50, null=True),
        ),
    ]