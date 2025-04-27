import re
from datetime import datetime

def cari_tanggal(teks):
     
    pola = r'\d{4}-\d{2}-\d{2}'
    tanggal_ditemukan = re.findall(pola, teks)
    return tanggal_ditemukan

def format_ulang_dan_hitung_selisih(tanggal_list):
    hari_ini = datetime.now()
    for tgl_str in tanggal_list:
        tanggal_obj = datetime.strptime(tgl_str, "%Y-%m-%d")
        selisih = (hari_ini - tanggal_obj).days
        
        tgl_format_baru = tanggal_obj.strftime("%d-%m-%Y")
        print(f"{tgl_format_baru} selisih {selisih} hari")

def main():
    teks = """Pada tanggal 1945-08-17 Indonesia merdeka. 
    Indonesia memiliki beberapa pahlawan nasional, seperti Pangeran Diponegoro (TL: 1785-11-11),
    Pattimura (TL: 1783-06-08) dan Ki Hajar Dewantara (1889-05-02)."""
    
    tanggal_ditemukan = cari_tanggal(teks)
    format_ulang_dan_hitung_selisih(tanggal_ditemukan)

if __name__ == "__main__":
    main()
