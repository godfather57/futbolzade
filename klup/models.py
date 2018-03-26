from django.db import models
from django.db.models import Q

# Create your models here.
class Ülke(models.Model):
	isim = models.CharField(max_length=100)
	def __str__(self):
		return self.isim

class Futbolcu(models.Model):
	isim = models.CharField(max_length=100)
	dogum_tarihi=models.DateTimeField(verbose_name="Doğum Tarihi",blank=True)
	yaş = models.IntegerField(verbose_name="Yaş",blank=True)
	deger = models.CharField(max_length=20,blank=True)
	ülke = models.ForeignKey(Ülke, on_delete=models.CASCADE)
	maas = models.CharField(max_length=20,blank=True,null=True)
	sözlesme_baslangıc_tarihi = models.DateTimeField(verbose_name="Sözleşme Başlangıç Tarihi",blank=True)
	sözlesme_bitiş_tarihi = models.DateTimeField(verbose_name="Sözleşme Bitiş Tarihi",blank=True)
	

	toplam_maç_sayısı = models.IntegerField(default=0,verbose_name="Maç sayısı")
	toplam_gol_sayısı = models.IntegerField(default=0,verbose_name="Gol sayısı")
	toplam_asist_sayısı = models.IntegerField(default=0,verbose_name="Asist sayısı")
	toplam_sarıkart_sayısı = models.IntegerField(default=0,verbose_name="Sarı Kart sayısı")
	toplam_kırmızı_sayısı = models.IntegerField(default=0,verbose_name="Kırmızı Kart sayısı")
	toplam_onbir_sayısı = models.IntegerField(default=0,verbose_name="Onbir çıktığı maç sayısı")
	
	
	def __str__(self):
		return self.isim
	
class Takımlar(models.Model):
	isim = models.CharField(max_length=100)
	def __str__(self):
		return self.isim

class Maclar(models.Model):
	takım1 = models.ForeignKey(Takımlar, on_delete=models.CASCADE,verbose_name="Takım1",related_name="evsahibi")
	takım2 = models.ForeignKey(Takımlar, on_delete=models.CASCADE,verbose_name="Takım2",related_name="konuktakım")
	takım1_skor= models.IntegerField(default=0,verbose_name="Takım1 skor")
	takım2_skor= models.IntegerField(default=0,verbose_name="Takım2 skor")
	
	goller = models.ManyToManyField(Futbolcu, through='GolEkle',related_name="goller",blank=True)
	asistler = models.ManyToManyField(Futbolcu, through='AsistEkle',related_name="asistler",blank=True)
	sarıkartlar = models.ManyToManyField(Futbolcu, related_name="sarıar",blank=True)
	kırmızıkartlar = models.ManyToManyField(Futbolcu, related_name="kırmızılar",blank=True)
	ilkonbir1 = models.ManyToManyField(Futbolcu, related_name="ilkonbir1")
	ilkonbir2 = models.ManyToManyField(Futbolcu, related_name="ilkonbir2")
	giren_oyuncular1=models.ManyToManyField(Futbolcu, related_name="girenler1",blank=True)
	giren_oyuncular2=models.ManyToManyField(Futbolcu, related_name="girenler2",blank=True)
	cıkan_oyuncular1=models.ManyToManyField(Futbolcu, related_name="çıkanlar1",blank=True)
	cıkan_oyuncular2=models.ManyToManyField(Futbolcu, related_name="cıkanlar2",blank=True)
	
	hafta = models.IntegerField(default=0,verbose_name="Hafta")
	macın_durumu=models.CharField(max_length=200,default="baslamadı")
	kontrol=models.IntegerField(default=0,verbose_name="ikinci kez kontrol etme ")
	
	topla_oynama_yüzdesi1 = models.IntegerField(default=0,verbose_name="topla_oynama_yüzdesi1")
	kaleyi_bulan_şut1 = models.IntegerField(default=0,verbose_name="kaleyi_bulan_şut1")
	kaleyi_bulmayan_şut1 = models.IntegerField(default=0,verbose_name="kaleyi_bulmayan_şut1")
	kornerler1 = models.IntegerField(default=0,verbose_name="kornerler1")
	ofsaytlar1 = models.IntegerField(default=0,verbose_name="ofsaytlar1")
	taclar1 = models.IntegerField(default=0,verbose_name="taclar1")
	kaleci_kurtarıslari1 = models.IntegerField(default=0,verbose_name="kaleci_kurtarıslari1")
	fauller1 = models.IntegerField(default=0,verbose_name="fauller1")
	kırmızı_kartlar1 = models.IntegerField(default=0,verbose_name="kırmızı_kartlar1")
	sarıkartlar1 = models.IntegerField(default=0,verbose_name="sarıkartlar1")
	
	
	topla_oynama_yüzdesi2 = models.IntegerField(default=0,verbose_name="topla_oynama_yüzdesi2")
	kaleyi_bulan_şut2 = models.IntegerField(default=0,verbose_name="kaleyi_bulan_şut2")
	kaleyi_bulmayan_şut2 = models.IntegerField(default=0,verbose_name="kaleyi_bulmayan_şut2")
	kornerler2 = models.IntegerField(default=0,verbose_name="kornerler2")
	ofsaytlar2 = models.IntegerField(default=0,verbose_name="ofsaytlar2")
	kaleci_kurtarıslari2 = models.IntegerField(default=0,verbose_name="kaleci_kurtarıslari2")
	taclar2 = models.IntegerField(default=0,verbose_name="taclar2")
	fauller2 = models.IntegerField(default=0,verbose_name="fauller2")
	kırmızı_kartlar2 = models.IntegerField(default=0,verbose_name="kırmızı_kartlar2")
	sarıkartlar2 = models.IntegerField(default=0,verbose_name="sarıkartlar2")
	
	
	
	oynadıgı_mac1 = models.IntegerField(default=0,verbose_name="Oynadığı Maç1")
	galibiyet1 = models.IntegerField(default=0,verbose_name="Galibiyet")
	beraberlik1 = models.IntegerField(default=0,verbose_name="Beraberlik")
	maglubiyet1 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	averaj1 = models.IntegerField(default=0,verbose_name="Averaj")
	puan1 = models.IntegerField(default=0,verbose_name="Puan")

	oynadıgı_mac2 = models.IntegerField(default=0,verbose_name="Oynadığı Maç2")
	galibiyet2 = models.IntegerField(default=0,verbose_name="Galibiyet")
	beraberlik2 = models.IntegerField(default=0,verbose_name="Beraberlik")
	maglubiyet2 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	averaj2 = models.IntegerField(default=0,verbose_name="Averaj")
	puan2 = models.IntegerField(default=0,verbose_name="Puan")
	
	ev_oynadıgı_mac1 = models.IntegerField(default=0,verbose_name="Ev sahibi Oynadığı Maç Sayısı1")
	ev_galibiyet1 = models.IntegerField(default=0,verbose_name="Galibiyet")
	ev_beraberlik1 = models.IntegerField(default=0,verbose_name="Beraberlik")
	ev_maglubiyet1 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	ev_averaj1 = models.IntegerField(default=0,verbose_name="Averaj")
	ev_puan1 = models.IntegerField(default=0,verbose_name="Puan")
	
	
	ev_oynadıgı_mac2 = models.IntegerField(default=0,verbose_name="Ev Oynadığı Maç Sayısı2")
	ev_galibiyet2 = models.IntegerField(default=0,verbose_name="Galibiyet")
	ev_beraberlik2 = models.IntegerField(default=0,verbose_name="Beraberlik")
	ev_maglubiyet2 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	ev_averaj2 = models.IntegerField(default=0,verbose_name="Averaj")
	ev_puan2 = models.IntegerField(default=0,verbose_name="Puan")
	
	dep_oynadıgı_mac1 = models.IntegerField(default=0,verbose_name="Deplasman Oynadığı Maç Sayısı1")
	dep_galibiyet1 = models.IntegerField(default=0,verbose_name="Galibiyet")
	dep_beraberlik1 = models.IntegerField(default=0,verbose_name="Beraberlik")
	dep_maglubiyet1 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	dep_averaj1 = models.IntegerField(default=0,verbose_name="Averaj")
	dep_puan1 = models.IntegerField(default=0,verbose_name="Puan")
	
		
	dep_oynadıgı_mac2 = models.IntegerField(default=0,verbose_name="Deplasman Oynadığı Maç Sayısı2")
	dep_galibiyet2 = models.IntegerField(default=0,verbose_name="Galibiyet")
	dep_beraberlik2 = models.IntegerField(default=0,verbose_name="Beraberlik")
	dep_maglubiyet2 = models.IntegerField(default=0,verbose_name="Mağlubiyet")
	dep_averaj2 = models.IntegerField(default=0,verbose_name="Averaj")
	dep_puan2 = models.IntegerField(default=0,verbose_name="Puan")
	
	def __str__(self):
		return self.takım1.isim + "-" + self.takım2.isim
	
	def save(self,*args,**kwargs):
		if self.macın_durumu=="bitti" and self.kontrol==0 and self.hafta==1:
			#self.takım1.hafta_puan_hesapla(self.hafta.kacıncı_hafta)
			#self.takım2.hafta_puan_hesapla(self.hafta.kacıncı_hafta)
			self.kontrol += 1
			
			self.oynadıgı_mac1 = 1
			self.ev_oynadıgı_mac1 = 1
			self.oynadıgı_mac2 = 1
			self.dep_oynadıgı_mac2 = 1
			
			self.averaj1 =self.takım1_skor-self.takım2_skor
			self.ev_averaj1 =self.takım1_skor-self.takım2_skor
			self.averaj2 =self.takım2_skor-self.takım1_skor
			self.dep_averaj2 =self.takım1_skor-self.takım2_skor

			if self.takım1_skor > self.takım2_skor:
				self.puan1 = 3
				self.ev_puan1 =3
				
				self.galibiyet1 = 1
				self.ev_galibiyet1 = 1
				self.maglubiyet2 =1
				self.dep_maglubiyet2 =1
			
			if self.takım1_skor < self.takım2_skor:
				self.puan2 = 3
				self.dep_puan =3
				
				self.galibiyet2 = 1
				self.dep_galibiyet2 = 1
				self.maglubiyet1 =1
				self.ev_maglubiyet1 =1
				
				
			if self.takım1_skor == self.takım2_skor:
				self.puan1 = 1
				self.puan2 = 1
				self.ev_puan1 = 1
				self.dep_puan2 = 1
				self.beraberlik2 = 1
				self.dep_beraberlik2=1
				self.beraberlik1 = 1
				self.ev_beraberlik1 =1
	
		if self.macın_durumu=="bitti" and self.kontrol==0 and self.hafta > 1:
			onceki_hafta=Maclar.objects.filter(hafta=self.hafta-1)
			onceki_takım1 = onceki_hafta.get(Q(takım1__isim=self.takım1)| Q(takım2__isim=self.takım1))
			
			onceki_takım2 = onceki_hafta.get(Q(takım1__isim=self.takım2)| Q(takım2__isim=self.takım2))
		
			#self.takım1.hafta_puan_hesapla(self.hafta.kacıncı_hafta)
			#self.takım2.hafta_puan_hesapla(self.hafta.kacıncı_hafta)
			self.kontrol += 1
			
				
			if onceki_takım1.takım2.isim ==self.takım1.isim:
				self.oynadıgı_mac1 = 1 + onceki_takım1.oynadıgı_mac2 
				self.ev_oynadıgı_mac1 = 1+ onceki_takım1.ev_oynadıgı_mac2
				self.dep_oynadıgı_mac1 = onceki_takım1.dep_oynadıgı_mac2 
				
			
				self.averaj1 =self.takım1_skor-self.takım2_skor +onceki_takım1.averaj2
				self.ev_averaj1 =self.takım1_skor-self.takım2_skor + onceki_takım1.ev_averaj2
				self.dep_averaj1 =onceki_takım1.dep_averaj2
			
			if onceki_takım1.takım1.isim ==self.takım1.isim:
				
				self.oynadıgı_mac1 = 1 + onceki_takım1.oynadıgı_mac1 
				self.ev_oynadıgı_mac1 = 1+ onceki_takım1.ev_oynadıgı_mac1 
				self.dep_oynadıgı_mac1 = onceki_takım1.dep_oynadıgı_mac1 
				
			
				self.averaj1 =self.takım1_skor-self.takım2_skor +onceki_takım1.averaj1
				self.ev_averaj1 =self.takım1_skor-self.takım2_skor + onceki_takım1.ev_averaj1
				self.dep_averaj1 =onceki_takım1.dep_averaj1
			
			if onceki_takım2.takım1.isim ==self.takım2.isim:
			
				self.oynadıgı_mac2 = 1 + onceki_takım2.oynadıgı_mac1 
				self.ev_oynadıgı_mac2 = onceki_takım2.ev_oynadıgı_mac1 
				self.dep_oynadıgı_mac2 = 1+ onceki_takım2.dep_oynadıgı_mac1 
				
			
				self.averaj2 =self.takım2_skor-self.takım1_skor +onceki_takım2.averaj1
				self.ev_averaj2 =onceki_takım2.ev_averaj1
				self.dep_averaj2 =self.takım2_skor-self.takım1_skor + onceki_takım2.dep_averaj1
				
			if onceki_takım2.takım2.isim ==self.takım2.isim:
				self.oynadıgı_mac2 = 1 + onceki_takım2.oynadıgı_mac2 
				self.ev_oynadıgı_mac2 = onceki_takım2.ev_oynadıgı_mac2
				self.dep_oynadıgı_mac2 = onceki_takım2.dep_oynadıgı_mac2 + 1
				
			
				self.averaj2 =self.takım2_skor-self.takım1_skor +onceki_takım2.averaj2
				self.ev_averaj2 =onceki_takım2.ev_averaj2
				self.dep_averaj2 =onceki_takım2.dep_averaj2+ onceki_takım2.dep_averaj2
			
		
			if self.takım1_skor > self.takım2_skor:
				
				if onceki_takım1.takım1.isim ==self.takım1.isim:
					self.puan1 = 3 + onceki_takım1.puan1
					self.ev_puan1 = onceki_takım1.ev_puan1 + 3
					self.dep_puan1 = onceki_takım1.dep_puan1 

					self.galibiyet1 = 1+ onceki_takım1.galibiyet1
					self.ev_galibiyet1 = 1 + onceki_takım1.ev_galibiyet1
					self.dep_galibiyet1 = onceki_takım1.dep_galibiyet1
					
					self.beraberlik1 = onceki_takım1.beraberlik1 
					self.ev_beraberlik1 = onceki_takım1.ev_beraberlik1 
					self.dep_beraberlik1 = onceki_takım1.dep_beraberlik1
					
					
					self.maglubiyet1 = onceki_takım1.maglubiyet1 
					self.ev_maglubiyet1 = onceki_takım1.ev_maglubiyet1 
					self.dep_maglubiyet1 = onceki_takım1.dep_maglubiyet1
				
				if onceki_takım1.takım2.isim ==self.takım1.isim:
					self.puan1 = 3 + onceki_takım1.puan2
					self.ev_puan1 = onceki_takım1.ev_puan2 + 3
					self.dep_puan1 = onceki_takım1.dep_puan2 

					self.galibiyet1 = 1+ onceki_takım1.galibiyet2
					self.ev_galibiyet1 = 1 + onceki_takım1.ev_galibiyet2
					self.dep_galibiyet1 = onceki_takım1.dep_galibiyet2
					
					self.beraberlik1 = onceki_takım1.beraberlik2
					self.ev_beraberlik1 = onceki_takım1.ev_beraberlik2 
					self.dep_beraberlik1 = onceki_takım1.dep_beraberlik2
					
					self.maglubiyet1 = onceki_takım1.maglubiyet2 
					self.ev_maglubiyet1 = onceki_takım1.ev_maglubiyet2 
					self.dep_maglubiyet1 = onceki_takım1.dep_maglubiyet2
				
				if onceki_takım2.takım1.isim ==self.takım2.isim:
					self.puan2 = onceki_takım2.puan1
					self.ev_puan2 = onceki_takım2.ev_puan1
					self.dep_puan2 = onceki_takım2.dep_puan1
					
					self.maglubiyet2 = onceki_takım2.maglubiyet1 + 1
					self.dep_maglubiyet2 = onceki_takım2.dep_maglubiyet1+1
					self.ev_maglubiyet2 = onceki_takım2.ev_maglubiyet1
					
					self.galibiyet2 = onceki_takım2.galibiyet1
					self.ev_galibiyet2 =  onceki_takım2.ev_galibiyet1
					self.dep_galibiyet2 = onceki_takım2.dep_galibiyet1
					
					self.beraberlik2 = onceki_takım2.beraberlik1
					self.ev_beraberlik2 = onceki_takım2.ev_beraberlik1
					self.dep_beraberlik2 = onceki_takım2.dep_beraberlik1
				
				if onceki_takım2.takım2.isim ==self.takım2.isim:
					self.puan2 = onceki_takım2.puan2
					self.ev_puan2 = onceki_takım2.ev_puan2
					self.dep_puan2 = onceki_takım2.dep_puan2
					
					self.maglubiyet2 = onceki_takım2.maglubiyet2 + 1
					self.dep_maglubiyet2 = onceki_takım2.dep_maglubiyet2 + 1
					self.ev_maglubiyet2 = onceki_takım2.ev_maglubiyet2
					
					self.galibiyet2 = onceki_takım2.galibiyet2
					self.ev_galibiyet2 =  onceki_takım2.ev_galibiyet2
					self.dep_galibiyet2 = onceki_takım2.dep_galibiyet2
					
					self.beraberlik2 = onceki_takım2.beraberlik2
					self.ev_beraberlik2 = onceki_takım2.ev_beraberlik2
					self.dep_beraberlik2 = onceki_takım2.dep_beraberlik2
			
			if self.takım1_skor < self.takım2_skor:
				if onceki_takım1.takım1.isim ==self.takım1.isim:
					self.puan1 = onceki_takım1.puan1
					self.ev_puan1 = onceki_takım1.ev_puan1 
					self.dep_puan1 = onceki_takım1.dep_puan1 

					self.maglubiyet1 = onceki_takım1.maglubiyet1 +1
					self.ev_maglubiyet1 = onceki_takım1.ev_maglubiyet1 +1
					self.dep_maglubiyet1 = onceki_takım1.dep_maglubiyet1
					
					self.galibiyet1 = onceki_takım1.galibiyet1
					self.ev_galibiyet1 =  onceki_takım1.ev_galibiyet1
					self.dep_galibiyet2 = onceki_takım1.dep_galibiyet1
					
					self.beraberlik1 = onceki_takım1.beraberlik1
					self.ev_beraberlik1 = onceki_takım1.ev_beraberlik1
					self.dep_beraberlik1 = onceki_takım1.dep_beraberlik1
				
				if onceki_takım1.takım2.isim ==self.takım1.isim:
					self.puan1 = onceki_takım1.puan2
					self.ev_puan1 = onceki_takım1.ev_puan2 
					self.dep_puan1 = onceki_takım1.dep_puan2 

					self.maglubiyet1 = onceki_takım1.maglubiyet2 +1
					self.ev_maglubiyet1 = onceki_takım1.ev_maglubiyet2 
					self.dep_maglubiyet1 = onceki_takım1.dep_maglubiyet2 +1
					
					self.galibiyet1 = onceki_takım1.galibiyet2
					self.ev_galibiyet1 =  onceki_takım1.ev_galibiyet2
					self.dep_galibiyet2 = onceki_takım1.dep_galibiyet2
					
					self.beraberlik1 = onceki_takım1.beraberlik2
					self.ev_beraberlik1 = onceki_takım1.ev_beraberlik2
					self.dep_beraberlik1 = onceki_takım1.dep_beraberlik2
				
				if onceki_takım2.takım1.isim ==self.takım2.isim:
					self.puan2 = onceki_takım2.puan1 +3
					self.ev_puan2 = onceki_takım2.ev_puan1
					self.dep_puan2 = onceki_takım2.dep_puan1 +3
					
					self.galibiyet2 = onceki_takım2.galibiyet1 + 1
					self.dep_galibiyet2 = onceki_takım2.dep_galibiyet1+1
					self.ev_galibiyet2 = onceki_takım2.ev_galibiyet1
					
					self.maglubiyet2 = onceki_takım2.maglubiyet1
					self.dep_maglubiyet2 = onceki_takım2.dep_maglubiyet1
					self.ev_maglubiyet2 = onceki_takım2.ev_maglubiyet1
					
					self.beraberlik2 = onceki_takım1.beraberlik1
					self.ev_beraberlik2 = onceki_takım1.ev_beraberlik1
					self.dep_beraberlik2 = onceki_takım1.dep_beraberlik1
				
				if onceki_takım2.takım2.isim ==self.takım2.isim:
					self.puan2 = onceki_takım2.puan2 +3
					self.ev_puan2 = onceki_takım2.ev_puan2
					self.dep_puan2 = onceki_takım2.dep_puan2 +3
					
					self.galibiyet2 = onceki_takım2.galibiyet2 + 1
					self.dep_galibiyet2 = onceki_takım2.dep_galibiyet2+1
					self.ev_galibiyet2 = onceki_takım2.ev_galibiyet2
					
					self.maglubiyet2 = onceki_takım2.maglubiyet2
					self.dep_maglubiyet2 = onceki_takım2.dep_maglubiyet2
					self.ev_maglubiyet2 = onceki_takım2.ev_maglubiyet2
					
					self.beraberlik2 = onceki_takım1.beraberlik2
					self.ev_beraberlik2 = onceki_takım1.ev_beraberlik2
					self.dep_beraberlik2 = onceki_takım1.dep_beraberlik2
				
			if self.takım1_skor == self.takım2_skor:
				if onceki_takım1.takım1.isim ==self.takım1.isim:
					self.puan1 = onceki_takım1.puan1+1
					self.ev_puan1 = onceki_takım1.ev_puan1+1
					self.dep_puan1 = onceki_takım1.dep_puan1 

					self.beraberlik1 = onceki_takım1.beraberlik1 +1
					self.ev_beraberlik1 = onceki_takım1.ev_beraberlik1 +1
					self.dep_beraberlik1 = onceki_takım1.dep_beraberlik1
					
					
					self.maglubiyet1 = onceki_takım1.maglubiyet1 
					self.ev_maglubiyet1 = onceki_takım1.ev_maglubiyet1 
					self.dep_maglubiyet1 = onceki_takım1.dep_maglubiyet1
					
					self.galibiyet1 = onceki_takım2.galibiyet1
					self.dep_galibiyet1 = onceki_takım2.dep_galibiyet1
					self.ev_galibiyet1 = onceki_takım2.ev_galibiyet1
				
				if onceki_takım1.takım2.isim ==self.takım1.isim:
					self.puan1 = onceki_takım1.puan2+1
					self.ev_puan1 = onceki_takım1.ev_puan2
					self.dep_puan1 = onceki_takım1.dep_puan2+1 

					self.beraberlik1 = onceki_takım1.beraberlik2 +1
					self.ev_beraberlik1 = onceki_takım1.ev_beraberlik2 
					self.dep_beraberlik1 = onceki_takım1.dep_beraberlik2 +1
					
					
					self.maglubiyet1 = onceki_takım1.maglubiyet2 
					self.ev_maglubiyet1 = onceki_takım1.ev_maglubiyet2 
					self.dep_maglubiyet1 = onceki_takım1.dep_maglubiyet2
					
					self.galibiyet1 = onceki_takım2.galibiyet2 
					self.dep_galibiyet1 = onceki_takım2.dep_galibiyet2
					self.ev_galibiyet1 = onceki_takım2.ev_galibiyet2
				
				if onceki_takım2.takım1.isim ==self.takım2.isim:
					self.puan2 = onceki_takım2.puan1 +1
					self.ev_puan2 = onceki_takım2.ev_puan1
					self.dep_puan2 = onceki_takım2.dep_puan1 +1
					
					self.beraberlik2 = onceki_takım2.beraberlik1 +1
					self.dep_beraberlik2 = onceki_takım2.dep_beraberlik1+1
					self.ev_beraberlik2 = onceki_takım2.ev_beraberlik1
					
					self.galibiyet2 = onceki_takım2.galibiyet1 
					self.dep_galibiyet2 = onceki_takım2.dep_galibiyet1
					self.ev_galibiyet2 = onceki_takım2.ev_galibiyet1
					
					self.maglubiyet2 = onceki_takım2.maglubiyet1
					self.dep_maglubiyet2 = onceki_takım2.dep_maglubiyet1
					self.ev_maglubiyet2 = onceki_takım2.ev_maglubiyet1
				
				if onceki_takım2.takım2.isim ==self.takım2.isim:
					self.puan2 = onceki_takım2.puan2 +1
					self.ev_puan2 = onceki_takım2.ev_puan2
					self.dep_puan2 = onceki_takım2.dep_puan2 +1
					
					self.beraberlik2 = onceki_takım2.beraberlik2 +1
					self.dep_beraberlik2 = onceki_takım2.dep_beraberlik2+1
					self.ev_beraberlik2 = onceki_takım2.ev_beraberlik2
					
					self.galibiyet2 = onceki_takım2.galibiyet2 
					self.dep_galibiyet2 = onceki_takım2.dep_galibiyet2
					self.ev_galibiyet2 = onceki_takım2.ev_galibiyet2
					
					self.maglubiyet2 = onceki_takım2.maglubiyet2
					self.dep_maglubiyet2 = onceki_takım2.dep_maglubiyet2
					self.ev_maglubiyet2 = onceki_takım2.ev_maglubiyet2

		if self.sarıkartlar.exists():
		    for futbolcu in self.sarıkartlar.all():
			    futbolcu.toplam_sarıkart_sayısı+=1
			    futbolcu.save()
				
		if self.kırmızıkartlar.exists():
		    for futbolcu in self.kırmızıkartlar.all():
			    futbolcu.toplam_kırmızı_sayısı+=1
			    futbolcu.save()
				
		if self.sarıkartlar.exists():
		    for futbolcu in self.sarıkartlar.all():
			    futbolcu.toplam_sarıkart_sayısı+=1
			    futbolcu.save()
		
		if self.ilkonbir1.exists():
		    for futbolcu in self.ilkonbir1.all():
			    futbolcu.toplam_onbir_sayısı+=1
			    futbolcu.toplam_maç_sayısı+=1
			    futbolcu.save()
		
		if self.ilkonbir2.exists():
		    for futbolcu in self.ilkonbir2.all():
			    futbolcu.toplam_onbir_sayısı+=1
			    futbolcu.toplam_maç_sayısı+=1
			    futbolcu.save()
		
		if self.giren_oyuncular1:
		    for futbolcu in self.ilkonbir1.all():
			    futbolcu.toplam_maç_sayısı+=1
			    futbolcu.save()
		
		if self.giren_oyuncular2:
		    for futbolcu in self.ilkonbir2.all():
			    futbolcu.toplam_maç_sayısı+=1
			    futbolcu.save()
		
		if self.goller:
		    for futbolcu in self.goller.all():
			    a=self.goller.filter(isim=futbolcu.isim).count()
			    futbolcu.toplam_gol_sayısı+=a
			    #print(futbolcu)
			    #print(futbolcu.toplam_gol_sayısı)
			    futbolcu.save()
			    #print(futbolcu.toplam_gol_sayısı)
		
		if self.asistler:
		    for futbolcu in self.asistler.all():
			    a=self.asistler.filter(isim=futbolcu.isim).count()
			    futbolcu.toplam_asist_sayısı+=a
			    #print(futbolcu)
			    #print(futbolcu.toplam_gol_sayısı)
			    futbolcu.save()
			    #print(futbolcu.toplam_gol_sayısı)
			    
		
		
		
		return super(Maclar,self).save(*args,*kwargs)

class GolEkle(models.Model):
	futbolcu = models.ForeignKey(Futbolcu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Maclar,on_delete=models.CASCADE)

class AsistEkle(models.Model):
	futbolcu = models.ForeignKey(Futbolcu,on_delete=models.CASCADE)
	mac = models.ForeignKey(Maclar,on_delete=models.CASCADE)
	