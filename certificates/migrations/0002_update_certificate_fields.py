import uuid

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('certificates', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='certificate',
            old_name='user',
            new_name='student',
        ),
        migrations.RemoveField(
            model_name='certificate',
            name='pdf_file',
        ),
        migrations.AlterUniqueTogether(
            name='certificate',
            unique_together={('student', 'course')},
        ),
    ]
