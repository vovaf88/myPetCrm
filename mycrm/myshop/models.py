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
        verbose_name = 'Единица измерения'
        verbose_name_plural = 'Единицы измерения'


# Контрагенты
class Partners(models.Model):
    """
    Описание контрагентов
    """


# Товары
class Products(models.Model):
    """
    Описание номенклатуры
    """


# Банки
class Banks(models.Model):
    """
    Справочник банковские счета
    """


#Банковские счета
class
    """
    Справочник банковские счета
    """


# Документ Поступление товаров
class BuyProducts(models.Model):
    """
    Документ покупки товаров
    """


# Продажа товаров
class SellProducts(models.Model):
    """
    Документ продажи товаров
    """


# Расход денег
class BankPay(models.Model):
    """
    Документ расхода с банковского счета
    """


# Поступление денег
class BankFromClient(models.Model):
    """
    Документ поступления денег на банковский счет
    """


# Взаиморасчеты с контрагентами
class MutualSettlements(models.Model):
    """
    Регистр взаиморасчетов с контрагентами
    """


# Остатки товаров
class RemainingGoods(models.Model):
    """
    Регистр остатков товаров
    """


# Выручка
class Revenue(models.Model):
    """
    Регистр выручки от продажи
    """


