from django.contrib import admin
from .models import Takımlar,Maclar,Futbolcu,GolEkle,AsistEkle

# Register your models here.
admin.site.register(Takımlar)
admin.site.register(Maclar)
admin.site.register(Futbolcu)
admin.site.register(GolEkle)
admin.site.register(AsistEkle)