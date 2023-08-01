import pandas as pd
from django.db import models
from joblib import load

model = load('../house_price_prediction_xgb_model.joblib')


class House(models.Model):
    ILCE_CHOICES = (
        (0, "Bünyan"),
        (1, "Develi"),
        (2, "Hacılar"),
        (3, "Kocasinan"),
        (4, "Melikgazi"),
        (5, "Sarıoğlan"),
        (6, "Sarız"),
        (7, "Talas"),
        (8, "Tomarza"),
        (9, "Yeşilhisar"),
        (10, "İncesu"),
    )

    KULLANIM_DURUMU_CHOICES = (
        (0, "Boş"),
        (1, "Kiracı Oturuyor"),
        (2, "Mülk Sahibi Oturuyor"),
    )

    BULUNDUGU_KAT_CHOICES = (
        (0, "- Kat"),
        (1, "1-10"),
        (2, "10-20.Kat"),
        (3, "Bahçe Dublex"),
        (4, "Bahçe Katı"),
        (5, "Bodrum"),
        (6, "Müstakil Kat"),
        (7, "Villa Tipi"),
        (8, "Zemin"),
        (9, "Çatı Dubleks"),
        (10, "Çatı Katı"),
    )

    BINANIN_YASI_CHOICES = (
        (0, "0 (Yeni)"),
        (1, "1"),
        (2, "11-15"),
        (3, "16-20"),
        (4, "2"),
        (5, "21 Ve Üzeri"),
        (6, "3"),
        (7, "4"),
        (8, "5-10"),
    )

    TURU_CHOICES = (
        (0, "Konut"),
    )

    ODA_SAYISI_CHOICES = (
        (0, "1 Oda"),
        (1, "1+1"),
        (2, "1.5+1"),
        (3, "2+0"),
        (4, "2+1"),
        (5, "2.5+1"),
        (6, "3+0"),
        (7, "3+1"),
        (8, "3+2"),
        (9, "3.5+1"),
        (10, "4+0"),
        (11, "4+1"),
        (12, "4+2"),
        (13, "4+3"),
        (14, "4.5+1"),
        (15, "5+0"),
        (16, "5+1"),
        (17, "5+2"),
        (18, "5+3"),
        (19, "5+4"),
        (20, "6+1"),
        (21, "6+2"),
        (22, "6+4"),
        (23, "7+1"),
        (24, "7+2"),
        (25, "7+3"),
        (26, "8+1"),
        (27, "8+2"),
        (28, "9+ Oda"),
        (29, "Stüdyo"),
    )

    SEHIR_CHOICES = (
        (0, "Kayseri"),
    )

    MAHALLE_CHOICES = (
        (0, "19 Mayıs Mahallesi"),
        (1, "30 Ağustos Mahallesi"),
        (2, "Ahi Evran Mahallesi"),
        (3, "Akdam Mahallesi"),
        (4, "Akyazı Mahallesi"),
        (5, "Alpaslan Mahallesi"),
        (6, "Alsancak Mahallesi"),
        (7, "Altınoluk Mahallesi"),
        (8, "Anafartalar Mahallesi"),
        (9, "Anbar Mahallesi"),
        (10, "Argıncık Mahallesi"),
        (11, "Aydınlıkevler Mahallesi"),
        (12, "Ağırnas Mahallesi"),
        (13, "Aşağıeverek Mahallesi"),
        (14, "Aşık Seyrani Mahallesi"),
        (15, "Bahçelievler Mahallesi"),
        (16, "Barbaros Mahallesi"),
        (17, "Battalgazi Mahallesi"),
        (18, "Bağpınar Mahallesi"),
        (19, "Becen Mahallesi"),
        (20, "Beyazşehir Mahallesi"),
        (21, "Beğendik Mahallesi"),
        (22, "Boyacı Mahallesi"),
        (23, "Boztepe Mahallesi"),
        (24, "Buğdaylı Mahallesi"),
        (25, "Büyüktuzhisar Mahallesi"),
        (26, "Camiicedit Mahallesi"),
        (27, "Camiikebir Mahallesi"),
        (28, "Cumhuriyet Mahallesi"),
        (29, "Cırgalan Mahallesi"),
        (30, "Danişmend Gazi Mahallesi"),
        (31, "Demokrasi Mahallesi"),
        (32, "Develi Camikebir Mahallesi"),
        (33, "Erciyesevler Mahallesi"),
        (34, "Erenköy Mahallesi"),
        (35, "Erkilet Mahallesi"),
        (36, "Ertuğrul Gazi Mahallesi"),
        (37, "Esentepe Mahallesi"),
        (38, "Esenyurt Mahallesi"),
        (39, "Eğribucak Mahallesi"),
        (40, "Fatih Mahallesi"),
        (41, "Feneseaşağı Mahallesi"),
        (42, "Feneseyukarı Mahallesi"),
        (43, "Fevzi Çakmak Mahallesi"),
        (44, "Garipçe Mahallesi"),
        (45, "Gaziler Mahallesi"),
        (46, "General Emir Mahallesi"),
        (47, "Germir Mahallesi"),
        (48, "Gesi Fatih Mahallesi"),
        (49, "Gesi Mahallesi"),
        (50, "Gevhernesibe Mahallesi"),
        (51, "Gökkent Mahallesi"),
        (52, "Gömeç Mahallesi"),
        (53, "Gönenkent Mahallesi"),
        (54, "Gültepe Mahallesi"),
        (55, "Gülveren Mahallesi"),
        (56, "Gülük Mahallesi"),
        (57, "Güneyyukarı Mahallesi"),
        (58, "Güneşli Mahallesi"),
        (59, "Gürpınar Mahallesi"),
        (60, "Güzelköy Mahallesi"),
        (61, "Hacı Saki Mahallesi"),
        (62, "Han Mahallesi"),
        (63, "Harman Mahallesi"),
        (64, "Hisarcık Mahallesi"),
        (65, "Hoca Ahmet Yesevi Mahallesi"),
        (66, "Hunat Mahallesi"),
        (67, "Hürriyet Mahallesi"),
        (68, "Karacabey Mahallesi"),
        (69, "Karakoyunlu Mahallesi"),
        (70, "Karamustafapaşa Mahallesi"),
        (71, "Karpuzsekisi Mahallesi"),
        (72, "Kayabağ Mahallesi"),
        (73, "Kayabaşı Mahallesi"),
        (74, "Kazımkarabekir Mahallesi"),
        (75, "Kemer Mahallesi"),
        (76, "Keykubat Mahallesi"),
        (77, "Kiçiköy Mahallesi"),
        (78, "Kocasinan Mahallesi"),
        (79, "Kocatepe Mahallesi"),
        (80, "Kuruköprü Mahallesi"),
        (81, "Köşk Mahallesi"),
        (82, "Kılıçaslan Mahallesi"),
        (83, "Kıranardı Mahallesi"),
        (84, "Kızık Mahallesi"),
        (85, "Mehmet Akif Ersoy Mahallesi"),
        (86, "Mevlana Mahallesi"),
        (87, "Mimarsinan Mahallesi"),
        (88, "Mithatpaşa Mahallesi"),
        (89, "Mustafa Asım Köksal Mahallesi"),
        (90, "Oruçreis Mahallesi"),
        (91, "Osman Kavuncu Mahallesi"),
        (92, "Osmangazi Mahallesi"),
        (93, "Osmanlı Mahallesi"),
        (94, "Oymaağaç Mahallesi"),
        (95, "Reşadiye Mahallesi"),
        (96, "Sahabiye Mahallesi"),
        (97, "Sakarya Mahallesi"),
        (98, "Sanayi Mahallesi"),
        (99, "Sancaktepe Mahallesi"),
        (100, "Saray Bosna Mahallesi"),
        (101, "Saraycık Mahallesi"),
        (102, "Sarımsaklı Mahallesi"),
        (103, "Selimiye Mahallesi"),
        (104, "Selçuklu Mahallesi"),
        (105, "Seyrani Mahallesi"),
        (106, "Süksün Hürriyet Mahallesi"),
        (107, "Sümer Mahallesi"),
        (108, "Tablakaya Mahallesi"),
        (109, "Tacettin Veli Mahallesi"),
        (110, "Tavlusun Mahallesi"),
        (111, "Turgut Reis Mahallesi"),
        (112, "Tınaztepe Mahallesi"),
        (113, "Uğurevler Mahallesi"),
        (114, "Yakut Mahallesi"),
        (115, "Yavuz Selim Mahallesi"),
        (116, "Yavuzlar Mahallesi"),
        (117, "Yediağaç Mahallesi"),
        (118, "Yeni Mahallesi"),
        (119, "Yenidoğan Mahallesi"),
        (120, "Yeniköy Mahallesi"),
        (121, "Yenişehir Mahallesi"),
        (122, "Yeşil Mahallesi"),
        (123, "Yeşilkent Mahallesi"),
        (124, "Yeşilyurt Mahallesi"),
        (125, "Yukarı Mahallesi"),
        (126, "Yunusemre Mahallesi"),
        (127, "Yıldırım Beyazıt Mahallesi"),
        (128, "Yıldızevler Mahallesi"),
        (129, "Zile Mahallesi"),
        (130, "Ziyagökalp Mahallesi"),
        (131, "Zümrüt Mahallesi"),
        (132, "Çevril Mahallesi"),
        (133, "İbrahimağa Mahallesi"),
        (134, "İbrahimbey Mahallesi"),
        (135, "İldem Cumhuriyet Mahallesi"),
        (136, "Şehit Üsteğmen Hasan Şahan Mahallesi"),
        (137, "Şeker Mahallesi"),
        (138, "Şirintepe Mahallesi"),
    )

    ISITMA_TIPI_CHOICES = (
        (0, "Doğalgaz Sobalı"),
        (1, "Güneş Enerjisi"),
        (2, "Isıtma Yok"),
        (3, "Kat Kaloriferi"),
        (4, "Klimalı"),
        (5, "Kombi Doğalgaz"),
        (6, "Merkezi (Pay Ölçer)"),
        (7, "Merkezi Doğalgaz"),
        (8, "Merkezi Fueloil"),
        (9, "Sobalı"),
        (10, "Yerden Isıtma"),
        (11, "Şömine"),
    )

    ilce = models.CharField(max_length=50, choices=ILCE_CHOICES, null=False, blank=False)
    kullanım_durumu = models.CharField(max_length=50, choices=KULLANIM_DURUMU_CHOICES, null=False, blank=False)
    bulundugu_kat = models.CharField(max_length=50, choices=BULUNDUGU_KAT_CHOICES, null=False, blank=False)
    bina_yasi = models.CharField(max_length=50, choices=BINANIN_YASI_CHOICES, null=False, blank=False)
    turu = models.CharField(max_length=50, choices=TURU_CHOICES, null=True, blank=True)
    oda_sayisi = models.CharField(max_length=50, choices=ODA_SAYISI_CHOICES, null=False, blank=False)
    sehir = models.CharField(max_length=50, choices=SEHIR_CHOICES, null=True, blank=True)
    mahalle = models.CharField(max_length=50, choices=MAHALLE_CHOICES, null=False, blank=False)
    isitma_tipi = models.CharField(max_length=50, choices=ISITMA_TIPI_CHOICES, null=False, blank=False)
    bina_kat_sayisi = models.IntegerField(null=False, blank=False)
    net_metrekare = models.IntegerField(null=False, blank=False)
    ev_fiyati = models.IntegerField(editable=False, null=True, blank=True)

    class Meta:
        verbose_name_plural = "Houses"
        db_table = "house"

    def predict_house_price(self):

        # data = [self.bina_yasi, self.bina_kat_sayisi, self.kullanım_durumu, self.net_metrekare,
        #         self.oda_sayisi, self.bulundugu_kat, self.isitma_tipi, self.ilce, self.mahalle]

        new_data = pd.DataFrame({'Binanın Yaşı': [self.bina_yasi],
                                 'Binanın Kat Sayısı': [self.bina_kat_sayisi],
                                 'Kullanım Durumu': [self.kullanım_durumu],
                                 'Net Metrekare': [self.net_metrekare],
                                 'Oda Sayısı': [self.oda_sayisi],
                                 'Bulunduğu Kat': [self.bulundugu_kat],
                                 'Isıtma Tipi': [self.isitma_tipi],
                                 'İlçe': [self.ilce],
                                 'Mahalle': [self.mahalle],
                                 })

        predicted_price = model.predict(new_data)

        self.ev_fiyati = predicted_price
