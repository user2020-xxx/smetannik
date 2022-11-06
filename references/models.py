from django.db import models


class GroupReferencesModel(models.Model):
    """
        Модель для хранение видов справочников. Пример данных: имя СН-2012, также у этого поля есть идентификатор родителя,
        который указывает, что СН-2012 находится в СН
    """
    parent = models.IntegerField(null=True)
    name = models.CharField(max_length=255, null=True)
    folder = models.BooleanField(default=False)


class TzModel(models.Model):
    name = models.CharField(max_length=2000, default='', null=True)
    kpgz = models.CharField(max_length=2000)
    id_spgz = models.IntegerField()
    spgz = models.CharField(max_length=2000)


class SPGZKPGZModel(models.Model):
    kpgz = models.CharField(max_length=2000)
    spgz = models.CharField(max_length=2000)
    units = models.CharField(max_length=20)
    okpd = models.CharField(max_length=128)
    okpd2 = models.CharField(max_length=128)


class EstimateModel(models.Model):
    sub_item_number = models.IntegerField()
    code_document = models.CharField(max_length=255)
    type_document = models.CharField(max_length=255)
    addition = models.CharField(max_length=255)
    number_document = models.CharField(max_length=255)
    date_document = models.CharField(max_length=50)
    id_sub_chapter = models.IntegerField()
    name_works_and_costs = models.CharField(max_length=255)
    unit = models.CharField(max_length=255)
    count_units = models.IntegerField(null=True)
    cost_item = models.CharField(max_length=255)
    correction_coefficient = models.FloatField(null=True)
    winter_coefficient = models.FloatField(null=True)
    basic_costs = models.FloatField(null=True)
    conversion_coefficient = models.FloatField(null=True)
    total_costs_at_the_current_price_level = models.FloatField(null=True)
    total_costs_for_the_work_name = models.FloatField(null=True)
    total_by_sub_chapter = models.FloatField(null=True)
    total_by_chapter = models.FloatField(null=True)
    total = models.FloatField(null=True)
    nds = models.FloatField(null=True)
    final_sum = models.FloatField(null=True)
    final_sum_with_coefficient = models.FloatField(null=True)
    price_per_unit = models.FloatField(null=True)


class ReferencesModel(models.Model):
    document = models.ForeignKey(GroupReferencesModel, on_delete=models.CASCADE, related_name='document')
    sub_item_number = models.IntegerField()
    code_document = models.CharField(max_length=255)
    type_document = models.CharField(max_length=255, null=True)
    addition = models.CharField(max_length=255, null=True)
    number_document = models.CharField(max_length=255, null=True)
    date_document = models.CharField(max_length=100, null=True)
    id_sub_chapter = models.IntegerField()
    name_works_and_costs = models.CharField(max_length=2000)
    unit = models.CharField(max_length=255)
    count_units = models.IntegerField(null=True)
    cost_item = models.CharField(max_length=255)
    correction_coefficient = models.FloatField(null=True)
    winter_coefficient = models.FloatField(null=True)
    basic_costs = models.FloatField(null=True)
    conversion_coefficient = models.FloatField(null=True)
    total_costs_at_the_current_price_level = models.FloatField(null=True)
    total_costs_for_the_work_name = models.FloatField(null=True)
    total_by_sub_chapter = models.FloatField(null=True)
    total_by_chapter = models.FloatField(null=True)
    total = models.FloatField(null=True)
    nds = models.FloatField(null=True)
    final_sum = models.FloatField(null=True)
    final_sum_with_coefficient = models.FloatField(null=True)
    price_per_unit = models.FloatField(null=True)


class ConformityModel(models.Model):
    code_work = models.CharField(max_length=500)
    name_work = models.CharField(max_length=500)
    spgz = models.CharField(max_length=2000)
    id_spgz = models.IntegerField(null=True)


class RelationKeyWordModel(models.Model):
    key_word = models.CharField(max_length=500)
    spgz = models.CharField(max_length=2000)

class File(models.Model):
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name