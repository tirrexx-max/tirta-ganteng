import math

#header

print(">>====================================<<")
print("||                                    ||")
print("||  Welcome to Dek Depe's Calculator  ||")
print("||                                    ||")
print(">>====================================<<")



#Input user
nama = input("Nama:")
tanggal_lahir = input("Tanggal Lahir:")
jurusan = input("jurusan:")
kelompok_mentoring = int(input("Kelompok Mentoring:"))
motto = input("motto:") 
alas = int(input("Masukkan alas(cm):"))
tinggi = int(input("Masukkan tinggi(cm):"))

#rumus luas segitiga

sisi_miring = math.sqrt(alas**2 + tinggi**2)
keliling = round (sisi_miring + alas + tinggi) +1
luas= (alas*tinggi) / 2



print(f"Halo {nama} dari jurusan {jurusan}.")
print(f"{nama} berasal dari kelompok mentoring {kelompok_mentoring}.")
print(f"{nama} lahir pada {tanggal_lahir} dengan motto \"{motto}\"!t")
print(f"Luas dari segitiga yang dimiliki {nama} adalah {luas}.")
print(f"Keliling dari segitiga yang dimiliki {nama} adalah {keliling} dengan sisi miring sepanjang {sisi_miring}.")

#footer 
print(">>==========================================<<")
print("||                                          ||")
print("||  Thanks for using Dek Depe's Calculator  ||")
print("||                                          ||")
print(">>==========================================<<")
