from django.db import migrations


def create_update_joke_periodic_task(apps, schema_editor):
    IntervalSchedule = apps.get_model('django_celery_beat', 'IntervalSchedule')
    PeriodicTask = apps.get_model('django_celery_beat', 'PeriodicTask')

    schedule, _ = IntervalSchedule.objects.get_or_create(
        every=2,
        period='seconds',
    )

    PeriodicTask.objects.update_or_create(
        name='update-joke-every-2-seconds',
        defaults={
            'task': 'api.tasks.update_joke',
            'interval': schedule,
            'enabled': True,
        },
    )


def delete_update_joke_periodic_task(apps, schema_editor):
    PeriodicTask = apps.get_model('django_celery_beat', 'PeriodicTask')
    PeriodicTask.objects.filter(name='update-joke-every-2-seconds').delete()


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
        ('django_celery_beat', '0019_alter_periodictasks_options'),
    ]

    operations = [
        migrations.RunPython(create_update_joke_periodic_task, delete_update_joke_periodic_task),
    ]
