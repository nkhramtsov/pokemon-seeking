from django.db import models  # noqa F401


class Pokemon(models.Model):
    title = models.CharField(max_length=200, verbose_name='Название')
    title_en = models.CharField(max_length=200, blank=True, verbose_name='Название англ.')
    title_jp = models.CharField(max_length=200, blank=True, verbose_name='Название яп.')
    description = models.TextField(verbose_name='Описание', blank=True, )
    image = models.ImageField(upload_to='pokemon_images', verbose_name='Изображение')
    previous_evolution = models.ForeignKey(
        'self', on_delete=models.CASCADE,
        null=True, blank=True,
        related_name='next_evolutions',
        verbose_name='Эволюционировал из'
    )

    def __str__(self):
        return self.title


class PokemonEntity(models.Model):
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE, verbose_name='Покемон',
                                related_name='entities')

    lat = models.FloatField(verbose_name='Широта')
    lon = models.FloatField(verbose_name='Долгота')

    appeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Появился в')
    disappeared_at = models.DateTimeField(blank=True, null=True, verbose_name='Исчез в')

    level = models.IntegerField(null=True, blank=True, verbose_name='Уровень')
    health = models.IntegerField(null=True, blank=True, verbose_name='Здоровье')
    strength = models.IntegerField(null=True, blank=True, verbose_name='Сила')
    defence = models.IntegerField(null=True, blank=True, verbose_name='Защита')
    stamina = models.IntegerField(null=True, blank=True, verbose_name='Выносливость')
