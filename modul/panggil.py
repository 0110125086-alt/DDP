import bangun_ruang as br
import bangun_datar as bd

print("~~~~ BANGUN RUANG ~~~~")
print(f"Volume Kubus dengan sisi 3 adalah {br.kubus(3)}")
print(f"Volume balok adalah {br.balok(4, 5, 2)}")
print(f"Volume prisma segitiga adalah {br.prisma(5,4,2)}")
print(f"Volume tabung adalah {br.tabung(6,15)}")
print(f"Volume kerucut adalah {br.kerucut(4,14)}")

print("~~~~ BANGUN DATAR ~~~~")
print(f"Luas Persegi adalah {bd.persegi(5)}")
print(f"Luas Persegi Panjang adalah {bd.persegi_panjang(8,5)}")
print(f"Luas Segitiga adalah {bd.segitiga(20,4)}")
print(f"Luas Lingkaran adalah {bd.lingkaran(6)}")
print(f"Luas Jajargenjang adalah {bd.jajargenjang(4,7)}")