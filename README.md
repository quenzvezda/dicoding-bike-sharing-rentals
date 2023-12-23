# Analisis Permintaan Penyewaan Sepeda

Selamat datang di proyek Analisis Permintaan Penyewaan Sepeda! Proyek ini bertujuan untuk mengungkap faktor-faktor yang mempengaruhi penggunaan sistem penyewaan sepeda dan untuk memahami pola penggunaan selama berbagai waktu dalam sehari, kondisi cuaca yang bervariasi, dan sepanjang musim.

## Ikhtisar Proyek

Sistem penyewaan sepeda telah mendapatkan popularitas di seluruh dunia sebagai bentuk transportasi perkotaan yang ramah lingkungan, sehat, dan nyaman. Proyek ini memanfaatkan data dari [Nama Penyedia Penyewaan Sepeda/Sumber Dataset] untuk menganalisis dan memvisualisasikan permintaan penyewaan sepeda di bawah berbagai skenario lingkungan dan waktu.

### Pertanyaan Kunci yang Ditangani:
- Bagaimana kondisi cuaca dan musim mempengaruhi penggunaan penyewaan sepeda?
- Apa pola penggunaan penyewaan sepeda selama hari kerja dan akhir pekan?

## Dataset

Analisis ini didasarkan pada dua dataset utama:
- `day.csv`: Catatan penyewaan sepeda harian dengan informasi cuaca dan musiman.
- `hour.csv`: Catatan penyewaan sepeda per jam dengan informasi cuaca dan musiman.

_Dataset per jam telah dievaluasi tetapi tidak dimasukkan dalam analisis akhir._

## Analisis Data Eksploratif (EDA)

Bagian EDA memberikan gambaran komprehensif dari data penyewaan harian, dengan visualisasi detail yang mengeksplorasi:
- Dampak kondisi cuaca terhadap penyewaan sepeda.
- Permintaan musiman untuk penyewaan sepeda.
- Perbedaan pola penyewaan antara hari kerja dan akhir pekan.

## Visualisasi & Analisis Penjelasan

Dalam bagian Visualisasi & Analisis Penjelasan, kami menyelami data lebih dalam dengan representasi visual untuk memahami dinamika penggunaan penyewaan sepeda. Bagian ini bertujuan untuk memberikan jawaban visual atas pertanyaan kunci kami.

## Cara Menggunakan Dashboard Streamlit

Proyek ini juga menyertakan sebuah dashboard interaktif yang dibuat dengan Streamlit, memungkinkan pengguna untuk menjelajahi data dan analisis secara visual.

Untuk menjalankan dashboard:

1. Pastikan Anda telah menginstal Streamlit dan semua dependensi yang diperlukan. Jika belum, instal dengan menjalankan `pip install -r requirements.txt` di terminal Anda.
2. Jalankan aplikasi Streamlit dengan memasukkan perintah `streamlit run app.py` di terminal pada direktori proyek.
3. Aplikasi akan terbuka di browser Anda. Gunakan sidebar untuk berinteraksi dengan visualisasi dan melihat analisis berdasarkan filter yang Anda terapkan.

## Kesimpulan

Bagian Kesimpulan merangkum temuan dari EDA kami dan analisis visual, menyediakan wawasan yang dapat dijalankan untuk perusahaan penyewaan sepeda dan perencana perkotaan.

## Alat & Teknologi yang Digunakan

- Python
- Pandas untuk manipulasi data
- Matplotlib dan Seaborn untuk visualisasi data
- Jupyter Notebook

## Cara Menggunakan

1. Klon repositori ini ke mesin lokal Anda.
2. Install Python dan semua dependensi yang dibutuhkan dengan menjalankan `pip install -r requirements.txt` di terminal Anda.
3. Buka dan jalankan Jupyter Notebook untuk melakukan analisis.
