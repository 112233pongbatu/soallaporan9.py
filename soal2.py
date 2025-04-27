def hitung_kata(teks, kata_dicari):
     
    teks = teks.lower()
    kata_dicari = kata_dicari.lower()

    tanda_baca = ['.', ',', ';', '!', '?']
    for tanda in tanda_baca:
        teks = teks.replace(tanda, "")

    kata = ""
    jumlah = 0

    for karakter in teks + " ":    
        if karakter != " ":
            kata += karakter
        else:
            if kata == kata_dicari:
                jumlah += 1
            kata = ""   

    return jumlah

 
kalimat = "Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan"
kata = "makan"

hasil = hitung_kata(kalimat, kata)
print(f'Kata "{kata}" ada {hasil} buah.')
