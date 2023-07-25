

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle', '0007_feedback'),
    ]

    operations = [
        migrations.AlterField(
            model_name='request',
            name='category',
            field=models.CharField(choices=[('two wheeler with gear', 'two wheeler with gear'), ('two wheeler without gear', 'two wheeler without gear'), ('three wheeler', 'three wheeler'), ('four wheeler', 'four wheeler')], max_length=50),
        ),
    ]
