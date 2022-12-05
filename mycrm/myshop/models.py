from django.db import models
from django.urls import reverse


# Единицы измерения
class UnitIzm(models.Model):
    """
    Описание единиц измерения
    """
    title = models.CharField(max_length=50)
    short_title = models.CharField(max_length=5)

    def __str__(self):
         return self.short_title

    class Meta:
         verbose_name = 'Единицы измерения'
         verbose_name_plural = 'Единица измерения'


# Организации
class Companies(models.Model):
    """
    Описание наших организаций
    """
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=30)
    inn = models.CharField(max_length=12)
    address = models.CharField(max_length=250)

    def __str__(self):
         return self.title

    class Meta:
         verbose_name = 'Организации'
         verbose_name_plural = 'Организация'


# Контрагенты
class Partners(models.Model):
    """
    Описание контрагентов
    """
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=30)
    inn = models.CharField(max_length=12)
    address = models.CharField(max_length=250)
    comment = models.TextField(blank=True)
    provider = models.BooleanField(blank=True, verbose_name='Поставщик')
    buyer = models.BooleanField(blank=True, verbose_name='Покупатель')


    def __str__(self):
         return self.title

    class Meta:
         verbose_name = 'Партнеры'
         verbose_name_plural = 'Партнер'


#Договоры
class Orders(models.Model):
    title = models.CharField(max_length=150)
    company = models.ForeignKey(Companies, on_delete=models.PROTECT)
    partner = models.ForeignKey(Partners, on_delete=models.PROTECT)
    date = models.DateTimeField()
    number = models.CharField(max_length=10)

    def __str__(self):
         return f'{self.title} {self.company} {self.partner}'

    class Meta:
         verbose_name = 'Договоры'
         verbose_name_plural = 'Договор'



# Товары
class Goods(models.Model):
    """
    Описание номенклатуры
    """
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=30)
    unit_izm = models.ForeignKey(UnitIzm, on_delete=models.PROTECT)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)

    def __str__(self):
         return self.title

    class Meta:
         verbose_name = 'Номенклатура'
         verbose_name_plural = 'Товар/Услуга'

# Банки
class Banks(models.Model):
    """
    Справочник банки
    """
    title = models.CharField(max_length=150)
    short_title = models.CharField(max_length=30)
    bik = models.CharField(max_length=9)
    korr = models.CharField(max_length=30)

    def __str__(self):
         return self.title

    class Meta:
         verbose_name = 'Банки'
         verbose_name_plural = 'Банк'


#Банковские счета
class BankAccount(models.Model):
    """
    Справочник банковские счета
    """
    title = models.CharField(max_length=150)
    number = models.CharField(max_length=30)
    bank = models.ForeignKey(Banks, on_delete=models.PROTECT)
    company = models.ForeignKey(Companies, on_delete=models.PROTECT, blank=True)
    partner = models.ForeignKey(Partners, on_delete=models.PROTECT, blank=True)

    def __str__(self):
         return self.title

    class Meta:
         verbose_name = 'Банковские счета'
         verbose_name_plural = 'Банковский счет'


# Документ Поступление товаров
#class BuyProducts(models.Model):
    """
    Документ покупки товаров
    """


# Продажа товаров
#class SellProducts(models.Model):
    """
    Документ продажи товаров
    """


# Расход денег
#class BankPay(models.Model):
    """
    Документ расхода с банковского счета
    """


# Поступление денег
#class BankFromClient(models.Model):
    """
    Документ поступления денег на банковский счет
    """


# Взаиморасчеты с контрагентами
#class MutualSettlements(models.Model):
    """
    Регистр взаиморасчетов с контрагентами
    """


# Остатки товаров
#class RemainingGoods(models.Model):
    """
    Регистр остатков товаров
    """


# Выручка
#class Revenue(models.Model):
    """
    Регистр выручки от продажи
    """


