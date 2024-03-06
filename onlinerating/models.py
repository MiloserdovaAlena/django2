from django.db import models
from django.contrib.auth.models import User
from simple_history.models import HistoricalRecords


# Модель для анкеты
class Questionnaire(models.Model):
    title = models.CharField(max_length=255, verbose_name="Название анкеты")
    description = models.TextField(verbose_name="Описание анкеты")
    history = HistoricalRecords()

    def __str__(self):
        return self.title

    # Другие поля для вашей анкеты

    class Meta:
        verbose_name = "Анкета"
        verbose_name_plural = "Анкеты"


# Модель для ответов
class Answer(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, verbose_name="Анкета")
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    anonymous_user = models.CharField(max_length=255, blank=True, null=True, verbose_name="Анонимный пользователь")
    history = HistoricalRecords()
    
    # Другие поля для ответов

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"

    def __str__(self):
        return f"Ответ пользователя {self.user.username} на анкету '{self.questionnaire.title}'"


# Модель для таблицы "Права доступа"
class AccessRights(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, verbose_name="Анкета")
    can_view_answers = models.BooleanField(default=False, verbose_name="Просмотр ответов")
    history = HistoricalRecords()
    

    class Meta:
        verbose_name = "Права доступа"
        verbose_name_plural = "Права доступа"

    def __str__(self):
        return f"Права доступа пользователя {self.user.username} к анкете '{self.questionnaire.title}'"


# Модель для отзывов о сотрудниках
class EmployeeFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    anonymous_user = models.CharField(max_length=255, blank=True, null=True, verbose_name="Анонимный пользователь")
    feedback = models.TextField(verbose_name="Отзыв о сотруднике")
    rating = models.PositiveIntegerField(default=0, verbose_name="Оценка")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    history = HistoricalRecords()
    
    
    class Meta:
        verbose_name = "Отзыв о сотруднике"
        verbose_name_plural = "Отзывы о сотрудниках"

    def __str__(self):
        return f"Отзыв от пользователя {self.user.username} о сотруднике"

    # Кастомный метод для вычисления средней оценки
    def calculate_average_rating(self):
        feedbacks = EmployeeFeedback.objects.filter(user=self.user)
        total_rating = sum(feedback.rating for feedback in feedbacks)
        if feedbacks.count() > 0:
            return total_rating / feedbacks.count()
        else:
            return 0


# Модель для таблицы "Ответы на вопросы о руководителе"
class ManagerFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    feedback = models.TextField(verbose_name="Отзыв о руководителе")
    history = HistoricalRecords()
    

    class Meta:
        verbose_name = "Отзыв о руководителе"
        verbose_name_plural = "Отзывы о руководителях"

    def __str__(self):
        return f"Отзыв от пользователя {self.user.username} о руководителе"


# Модель для таблицы "Ответы руководителя о себе"
class SelfFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    feedback = models.TextField(verbose_name="Отзыв руководителя о себе")
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = "Отзыв руководителя о себе"
        verbose_name_plural = "Отзывы руководителей о себе"

    def __str__(self):
        return f"Отзыв от пользователя {self.user.username} о себе"


# Модель для таблицы "Отзывы о коллегах" (с отношением M2M)
class ColleagueFeedback(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    colleagues = models.ManyToManyField(User, related_name='colleague_feedback', verbose_name="Коллеги")
    feedback = models.TextField(verbose_name="Отзыв о коллегах")
    history = HistoricalRecords()
    
    class Meta:
        verbose_name = "Отзыв о коллегах"
        verbose_name_plural = "Отзывы о коллегах"

    def __str__(self):
        return f"Отзыв от пользователя {self.user.username} о коллегах"
