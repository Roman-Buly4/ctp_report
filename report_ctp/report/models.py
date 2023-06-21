from django.db import models

# class Birthday(models.Model):
#     first_name = models.CharField('Имя', max_length=20)
#     last_name = models.CharField(
#         'Фамилия', blank=True, help_text='Необязательное поле', max_length=20
#     )
#     birthday = models.DateField('Дата рождения') 


class AuthorRep(models.Model):
    name = models.CharField(
        verbose_name='Тех.писатель',
        max_length=256,
    )

    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'Авторы'

    def __str__(self):
        return self.name

class Type(models.Model):
    name = models.CharField(
        max_length=256,
        verbose_name='Тип работы',
    )
    class Meta:
        verbose_name = 'тип работы'
        verbose_name_plural = 'Тип работ'

    def __str__(self):
        return self.name

class Report(models.Model):
    number_report = models.CharField(
        'Номер запроса',
        max_length=40,
    )
    date_add_report = models.DateField(
        'Дата поступления запроса',
    )
    about_report = models.CharField(
        'Краткое описание запроса или задачи',
        max_length=256,
        blank=True,
        help_text='Необязательное поле',
    )
    type = models.ForeignKey(
        Type,
        on_delete=models.CASCADE,
        verbose_name='Тип работы',
    ) 
    MD = models.CharField(
        'Результат работы',
        max_length=40,
        blank=True,
        help_text='Номер редактируемой или новой ДЕ/ Результат работы',
    )
    author_report = models.ForeignKey(
        AuthorRep,
        on_delete=models.CASCADE,
        verbose_name='Исполнитель',
    ) 
    report = models.CharField(
        'Трудозатраты',
        max_length=40,
        blank=True,
        help_text='нормо/час',
    )
    no_field = models.CharField(
        'не заполняется',
        max_length=40,
        blank=True,
    )
    date_end_report = models.DateField(
        'Дата закрытия запроса',
    )



