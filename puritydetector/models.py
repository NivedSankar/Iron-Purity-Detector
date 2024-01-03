from django.db import models

class MLModelData(models.Model):
    iron_feed = models.FloatField()
    silica_feed = models.FloatField()
    starch_flow = models.FloatField()
    amina_flow = models.FloatField()
    ore_pulp_flow = models.FloatField()
    ore_pulp_density = models.FloatField()
    column_04_air_flow = models.FloatField()
    column_05_air_flow = models.FloatField()
    column_06_air_flow = models.FloatField()
    column_07_air_flow = models.FloatField()
    column_01_level = models.FloatField()
    column_02_level = models.FloatField()
    column_03_level = models.FloatField()
    column_04_level = models.FloatField()
    column_05_level = models.FloatField()
    column_06_level = models.FloatField()
    column_07_level = models.FloatField()

    def __str__(self):
        return f"MLModelData: Iron Feed - {self.iron_feed}, Silica Feed - {self.silica_feed}, Starch Flow - {self.starch_flow}, ..."