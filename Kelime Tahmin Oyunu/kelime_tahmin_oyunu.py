#Nursena Taskopru
import random

kelime_listesi = ["system", "data", "algorithm", "such", "base", "node", "model", "case", "program", "information",
                  "set", "code", "function",
                  "process", "application", "software", "class", "point", "type", "network", "tree", "object",
                  "element", "input", "operation",
                  "level", "memory", "table", "order", "file", "variable", "language", "write", "list", "structure",
                  "compute", "sequence",
                  "computer", "bit", "probability", "machine", "array", "page", "error", "step", "search", "most",
                  "path", "graph", "web", "length",
                  "several", "security", "proof", "access", "obtain", "matrix", "task", "image", "form", "return",
                  "interface", "resource", "address",
                  "implementation", "loop", "first", "read", "location", "hardware", "behavior", "programming", "field",
                  "key", "parameter",
                  "distribution", "definition", "instance", "interaction", "internet", "representation", "edge",
                  "stack", "return", "procedure",
                  "link", "output", "block", "domain", "store", "call", "device", "server", "static", "dataset",
                  "detection", "write",
                  "execute", "least", "key"]
kelime = random.choice(kelime_listesi)
harf_sayisi = 0  # harf birden fazla varsa puanın dogru hessaplanabilmesi icin
k_uzunlugu = len(kelime)
max_yanlis_hakki = (k_uzunlugu + 1) // 2
yanlis_tahmin = 0
puan = 0
gizli_kelime = ["_"] * k_uzunlugu
turkce_karakter = 'ğüşıöç'
while True:  # oyunun cıkıs yapılana kadar devam edebilmesi icin
    print("1)Yeni Oyun\n2)Cikis")
    secim = input("Seciminizi giriniz:")
    if secim == '1':
        while yanlis_tahmin < max_yanlis_hakki:
            print("Kalan Tahmin Hakkı:{}\tPuan:{}".format(max_yanlis_hakki - yanlis_tahmin, puan))
            print(f"Kelime: {' '.join(gizli_kelime)}")
            tahmin = input("Harf giriniz:").lower()
            if tahmin in turkce_karakter:
                print("!Turkce karakter girmeyiniz!")
                continue
            if tahmin in kelime:
                for harf in kelime:
                    if harf == tahmin:
                        harf_sayisi += 1
                for i in range(k_uzunlugu):
                    if kelime[i] == tahmin:
                        gizli_kelime[
                            i] = tahmin  # dogru tahminde gizli kelimede yerine yazmak icin liste yapisi kullandim
                if tahmin in ["a", "e", "i", "o", "u"]:
                    puan += 3 * harf_sayisi
                    harf_sayisi = 0
                else:
                    puan += 2 * harf_sayisi
                    harf_sayisi = 0
                if "_" not in gizli_kelime:  # gizli kelimede hic _ yoksa kelime bulunmus oluyor
                    print("Tebrikler, kelimeyi buldunuz!:{}\nPuan:{}".format(kelime, puan))
                    print("---------------------")
                    print("1)Yeni Oyun\n2)Cikis")
                    istek = input("Seciminizi giriniz:")
                    if istek == '1':  # oyunu kazansa da kaybetse de tekrar oynamak istediginde oynayabilmesi icin iki duruma da bu if blogunu ekledim
                        kelime = random.choice(kelime_listesi)
                        k_uzunlugu = len(kelime)
                        max_yanlis_hakki = (k_uzunlugu + 1) // 2
                        puan = 0
                        yanlis_tahmin = 0
                        gizli_kelime = ["_"] * k_uzunlugu
                        harf_sayisi = 0  # oyunun tekrar oynanacagı zaman hatasız calısabilmesi icin degiskenleri sıfırladım
                    else:
                        print("Cikis yapiliyor...")
                        exit()
            else:
                print("Kelime bu harfi içermiyor:{}".format(tahmin))
                yanlis_tahmin += 1
                puan -= 4
                if yanlis_tahmin == max_yanlis_hakki:
                    print("Tahmin hakkınız bitti!\nKelime:{}\tPuan:{}".format(kelime, puan))
                    print("---------------------")
                    print("1)Yeni Oyun\n2)Cikis")
                    istek = input("Seciminizi giriniz:")
                    if istek == '1':  # oyunu kazansa da kaybetse de tekrar oynamak istediginde oynayabilmesi icin iki duruma da bu if blogunu ekledim
                        kelime = random.choice(kelime_listesi)
                        k_uzunlugu = len(kelime)
                        max_yanlis_hakki = (k_uzunlugu + 1) // 2
                        puan = 0
                        yanlis_tahmin = 0
                        gizli_kelime = ["_"] * k_uzunlugu
                        harf_sayisi = 0  # oyunun tekrar oynanacagı zaman hatasız calısabilmesi icin degiskenleri sıfırladım
                    else:
                        print("Cikis yapiliyor...")
                        exit()
    else:
        print("Cikis yapiliyor...")
        exit()
