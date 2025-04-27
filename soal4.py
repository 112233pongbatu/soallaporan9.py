def cari_kata_terpendek_terpanjang(kalimat):
    # Hilangkan spasi berlebih
    kalimat = " ".join(kalimat.split())
    # Pisahkan kalimat menjadi daftar kata
    kata_list = kalimat.split()
    
    # Cari kata terpendek dan terpanjang
    kata_terpendek = min(kata_list, key=len)
    kata_terpanjang = max(kata_list, key=len)
    
    return kata_terpendek, kata_terpanjang

def main():
    kalimat = input("Masukkan kalimat: ")
    pendek, panjang = cari_kata_terpendek_terpanjang(kalimat)
    print(f"Terpendek: {pendek}")
    print(f"Terpanjang: {panjang}")

if __name__ == "__main__":
    main()
