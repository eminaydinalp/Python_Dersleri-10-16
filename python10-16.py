# Sözlükler 

dic1 = {"ball" : "top", "pen" : "kalem", "cheese" : "peynir"}
print(dic1["ball"])
print(dic1["pen"])

dic2 = {1 : "istanbul", "a" : [1,23,5], "b" : "Ankara", "c" : [[1,2,3],[5,55,6]]}
print(dic2["a"][1])
print(dic2["c"][0][2])
print(dic2[1][2])

print(dic2.keys())
print(dic2.values())
print(dic2.items())

dic2["d"] = 5

# İnput Alma

sayi = int(input("Bir değer giriniz :"))
yazi = input("Bir Åehi ismi giriniz :")

a = int(input("bir sayi giriniz: "))
b = int(input("bir sayi giriniz: "))
c = int(input("bir sayi giriniz: "))

ortalama = int((a+b+c)/3)
print(ortalama)


# Boolean Veri Tipi 

x = True
y = False

# Karşılaştırma Op.

print(10==10)
print(10==5)
print(10>10)
print(10<12)
print(10<=12)
print(10<=10)
print(10!=12)

# Mantıksal Bağlaçlar

print(10==10 and 20<10)
print(10==10 and 20>10)
print(10>10 or 20<10)
print(not 5<2 and 20>10)

if 10==10 :
    print("merhaba")
    
if (10==5) :
    
    print("Merhaba")

if (10==10 and 20<10):
    
    print("Benim adım ali")
    
if (10==10 or 20<10):
    
    print("**")
    
# if - elif - else
    
if 10==10 and 2>100:
    
    print("----------")
    
elif 10==10 and 2>10 : 
    
    print("*********")
    
elif not 5<20 and 20>10 :
    
    print("#######")
          
else:
    print("^^^^^^")
    
sayi1 = 0

if sayi1 > 0:
    
    print("pozitif sayi")
    
elif sayi1 == 0:
    
    print("sifir")
    
else:
    
    print("negatif sayidir.")


sayi2 = int(input("Bir sayi giriniz: "))

if sayi2 >= 0:
    
    if sayi2 > 0:
        
        print("pozitif sayi")
    else:
        
        print("sifir")
        
elif sayi2 < 0:
    
    print("negatif sayi")
    
    
    
# Geometrik Şekil Bulma 

sekil = input("Bir Şekil Giriniz: ")

if sekil == "Dörtgen":
    print("*******")
    
    print("Dörgenin Kenarlarını Giriniz : ")
    a = int(input("1.Kenarı Giriniz : "))
    b = int(input("2.Kenarı Giriniz : "))
    c = int(input("3.Kenarı Giriniz : "))
    d = int(input("4.Kenarı Giriniz : "))
    
    if (a == b and a == c and a == d):
        print("Karedir.")
    elif (a == c and b == d):
        print("Dikdötgendir.")
    else:
        print("Normal Dörtgen")
        
    
    
elif sekil == "Üçgen":
    print("********")
    
    print("Üçgen kenarlarını giriniz :")
    e = int(input("1.Kenarı Giriniz : "))
    f = int(input("2.Kenarı Giriniz : "))
    g = int(input("3.Kenarı Giriniz : "))
    
    if (abs(f-g)<e<f+g) and (abs(e-g)<f<e+g) and (abs(f-e)<g<f+e):
        
        if (e == f and e == g):
            print("Eşkenardır.")
            
        elif (e == f and e!=g) or (e == g and e!=f) or (g == f and e!=g):
            
            print("İkizkenar")
            
        else:
            print("Çeşitkenardır.")
            
    else:
        print("Girilen Değerler Üçgen değildir.")
        
        
    
    
    
else:
    print("Geçersiz işlem")
  
    
    
    
    
    
    



























