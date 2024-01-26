# user/migrations/0002_auto_20240124_2316.py
from django.db import migrations
from django.contrib.auth.models import Group

def create_groups(apps, schema_editor):
    Group = apps.get_model('auth', 'Group')
    
    # Create 'Owner' group
    owner_group, created = Group.objects.get_or_create(name='Owner')
    
    # Create 'Employee' group
    employee_group, created = Group.objects.get_or_create(name='Employee')

class Migration(migrations.Migration):

    dependencies = [
        # Previous dependencies
        ('user', '0001_initial')
    ]

    operations = [
        # Previous operations

        # Add this RunPython operation
        migrations.RunPython(create_groups),
    ]
