from django.contrib.auth.models import AbstractUser
from django.db import models
from django.core.validators import MinValueValidator

from courses.models import Course


class CustomUser(AbstractUser):
    """Кастомная модель пользователя - студента."""

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        max_length=250,
        unique=True
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = (
        'username',
        'first_name',
        'last_name',
        'password'
    )

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        ordering = ('-id',)

    def __str__(self):
        return self.get_full_name()


class Balance(models.Model):
    """Модель баланса пользователя."""

    # TODO
    user = models.OneToOneField(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Пользователь',
    )
    bonus_balance = models.PositiveIntegerField(
        verbose_name='Баланс бонусов',
        default=1000,
        validators=(
            MinValueValidator(
                0,
                message='Значение должно быть больше 0.'
            ),
        )
    )

    class Meta:
        verbose_name = 'Баланс'
        verbose_name_plural = 'Балансы'
        ordering = ('-id',)


class Subscription(models.Model):
    """Модель подписки пользователя на курс."""

    # TODO
    student = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        verbose_name='Студенты',
    )
    course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        verbose_name='Курс',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
        ordering = ('-id',)
        default_related_name = 'subscriptions'
        constraints = (
            models.UniqueConstraint(
                fields=('student', 'course'),
                name='Unique_student_course',
            ),
        )
