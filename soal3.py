def hapus_spasi_berlebih(teks):
    
    teks_bersih = " ".join(teks.split())
    return teks_bersih

def main():
    kalimat = "saya    tidak   suka    memancing   ikan   "
    hasil = hapus_spasi_berlebih(kalimat)
    print(f"Hasil: '{hasil}'")

if __name__ == "__main__":
    main()
