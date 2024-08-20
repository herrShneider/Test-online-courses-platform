from django.db.models import Count
from django.db.models.signals import post_save
from django.dispatch import receiver

from courses.models import Group
from users.models import Subscription


@receiver(post_save, sender=Subscription)
def post_save_subscription(sender, instance: Subscription, created, **kwargs):
    """
    Распределение нового студента в группу курса.

    """

    if created:
        pass
        # TODO
        course = instance.course

        for group_number in range(1, 11):
            Group.objects.get_or_create(
                course=course,
                name=f'Группа номер {group_number}. Курс {course.title}.'
            )

        smallest_group = Group.objects.filter(
            course=course
        ).annotate(
            student_count=Count('students')
        ).order_by(
            'student_count'
        ).first()

        if smallest_group:
            smallest_group.students.add(instance.student)
