from django.db import models
from core.models import CreateUpdateMixin


class Charity(CreateUpdateMixin):
    id = models.AutoField(primary_key=True, null=False)
    starting = models.DateField('Дата начала сбора', null=False)
    ending = models.DateField('Дата окончания сбора', null=False)
    name = models.CharField('Имя', max_length=100, null=False)
    surname = models.CharField('Фамилия', max_length=100, null=False)
    middle_name = models.CharField('Отчество', max_length=100,
                                   null=False, blank=True,
                                   help_text='Необязательное поле')
    birth_date = models.DateField('Дата рожения', null=False)
    locality = models.CharField('Населённый пункт', max_length=100,
                                null=False, blank=True,
                                help_text='Необязательное поле')
    amount = models.FloatField(
        'Сумма на данный момент', null=False, default=0.00)
    final_amount = models.FloatField('Нужно собрать', null=False)
    diagnosis = models.CharField('Диагноз', max_length=100, null=False)
    goal = models.TextField('Цель', null=False)
    story = models.TextField('История', null=False)
    display = models.BooleanField('Опубликовано', default=False,
                                  help_text='Отметка отсутствует — запись'
                                  'не будет передана в МП (черновик)')

    class Meta:
        db_table = 'charity'
        verbose_name = 'Благотворительность'
        verbose_name_plural = 'Благотворительность'

    def __str__(self):
        return f'{self.surname} {self.name} {self.middle_name}'


class CharityPhoto(models.Model):
    charity = models.ForeignKey(Charity, on_delete=models.CASCADE,
                                verbose_name='Благотворительность')
    path = models.ImageField('Фото', upload_to='charity/')

    class Meta:
        db_table = 'charity_photo'
        verbose_name = 'Фото ребёнка'
        verbose_name_plural = 'Фотографии ребёнка'
