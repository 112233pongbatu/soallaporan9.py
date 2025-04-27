def cek_anagram(kata1, kata2):
     
    kata1 = kata1.replace(" ", "").lower()
    kata2 = kata2.replace(" ", "").lower()
    
    return sorted(kata1) == sorted(kata2)

kata_pertama = input("Masukkan kata pertama: ")
kata_kedua = input("Masukkan kata kedua: ")

if cek_anagram(kata_pertama, kata_kedua):
    print(f'"{kata_pertama}" adalah anagram dari "{kata_kedua}".')
else:
    print(f'"{kata_pertama}" bukan anagram dari "{kata_kedua}".')
