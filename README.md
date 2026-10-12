# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech 🎓

## Business Understanding
Institusi pendidikan tinggi menghadapi tantangan besar terkait tingkat *dropout* (putus kuliah) mahasiswa, yang tidak hanya berdampak pada pendapatan institusi (hilangnya uang kuliah), tetapi juga mencoreng reputasi akademik universitas di mata publik dan lembaga akreditasi. Mengetahui mahasiswa mana yang berisiko gagal lebih awal sangat krusial bagi manajemen untuk dapat memberikan intervensi tepat waktu.

### Permasalahan Bisnis
1. Bagaimana cara mendeteksi dini mahasiswa yang memiliki probabilitas tinggi untuk *dropout* sebelum mereka benar-benar keluar dari institusi?
2. Karakteristik dan faktor-faktor utama apa saja yang secara signifikan mendorong mahasiswa untuk *dropout*?
3. Langkah pencegahan atau intervensi seperti apa yang bisa diterapkan institusi untuk menekan persentase *Dropout*?

### Cakupan Proyek
1. **Eksplorasi Data (EDA):** Mengidentifikasi korelasi antar variabel akademik dan non-akademik menggunakan metode univariat dan bivariat.
2. **Data Preparation (Binary Classification):** Memfilter data untuk hanya melibatkan mahasiswa dengan status akhir yang jelas (*Graduate* vs *Dropout*) dalam pelatihan model (Label 0 dan 1). Data mahasiswa yang masih aktif (*Enrolled*) disisihkan sepenuhnya untuk dijadikan data uji prediksi masa depan guna menghindari ambiguitas target kelas.
3. **Pembangunan Model Prediktif:** Membangun dan melatih model klasifikasi *Machine Learning* untuk memprediksi probabilitas risiko *dropout*.
4. **Pembuatan Dashboard:** Merancang *Business Dashboard* interaktif untuk memantau tren metrik kelulusan.
5. **Deployment:** Menyediakan prototipe interaktif (berbasis Streamlit) agar konselor akademik dapat menguji prediksi risiko per individu.

## Persiapan
* **Sumber Data:** Dataset "[Predict students' dropout and academic success](https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/README.md)" (Realinho et al., 2021) dari UCI Machine Learning.

### Setup Environment
Untuk menjalankan proyek ini secara lokal, Anda perlu menyiapkan *environment* Python dan menginstal seluruh dependensi yang dibutuhkan. Pastikan Anda sudah menginstal Python (disarankan versi 3.9).

**Opsi 1: Setup Environment - Anaconda**
1. Buka Anaconda Prompt.
2. Buat *environment* baru dan aktifkan:
   ```bash
   conda create --name main-ds python=3.9
   conda activate main-ds
   ```
3. Instal semua pustaka (packages) yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

**Opsi 2: Setup Environment - Shell/Terminal (Pipenv)**
1. Buka Terminal / Command Prompt.
2. Instal `pipenv` dan buat *virtual environment*:
   ```bash
   pip install pipenv
   pipenv install
   pipenv shell
   ```
3. Instal semua pustaka (packages) yang dibutuhkan:
   ```bash
   pip install -r requirements.txt
   ```

### Cara Menjalankan Skrip Prediksi Python (.py)
Untuk menjalankan prototipe aplikasi prediksi (Dashboard berbasis Streamlit) di komputer lokal Anda:
```bash
streamlit run app.py
```

## Business Dashboard
*Business Dashboard* dirancang menggunakan Looker Studio untuk memberikan alat pantau makro bagi petinggi universitas. Terdapat visualisasi distribusi status mahasiswa, korelasi finansial dengan *dropout*, serta metrik performa akademik yang dengan jelas memetakan bagaimana penurunan kelulusan SKS berujung pada *dropout*.

👉 **[Klik untuk Mengakses Business Dashboard (Looker Studio)](#)** *https://datastudio.google.com/reporting/a5637ebd-5e69-4b1d-8064-a362a1c541aa/page/le1AG*

## Menjalankan Sistem Machine Learning
Prototipe Sistem Machine Learning ini dibangun menggunakan algoritma **Random Forest Classifier** dan di-*deploy* melalui Streamlit Community Cloud. Sistem ini menerima input data historis mahasiswa dan secara instan mengeluarkan probabilitas (persentase) risiko *dropout*.

👉 **[Klik untuk Mengakses Prototipe Machine Learning (Streamlit)](#)** *https://edutech-prediction-app.streamlit.app/*

## Conclusion
Berdasarkan serangkaian proses *Exploratory Data Analysis* (EDA) dan pengujian *Machine Learning*, berikut adalah kesimpulan utuh dari proyek ini:

1. **Karakteristik Umum Siswa Dropout:** Mahasiswa yang rentan mengalami *dropout* memiliki profil yang khas, yakni didominasi oleh mahasiswa laki-laki, tidak memiliki beasiswa, memiliki tunggakan biaya kuliah (berstatus debitor), dan menunjukkan performa akademik yang sangat buruk sejak tahun pertama (rendahnya jumlah SKS mata kuliah yang berhasil dilulusi atau *approved* pada semester 1 dan 2).
2. **Ringkasan Performa Model:** Pemodelan menggunakan *Random Forest Classifier* (dengan metode *Binary Classification*: 1 = Dropout, 0 = Graduate) menunjukkan performa klasifikasi yang sangat baik. Model mampu membedakan kedua kelas dengan tingkat akurasi yang tinggi dan keandalan prediksi (F1-Score) yang solid berkat penanganan data imbang (*class_weight='balanced'*), sehingga sangat layak digunakan di dunia nyata.
3. **Insight Utama yang Diperoleh:** Kelulusan sangat bergantung pada interaksi antara **stabilitas finansial mikro** dan **kesuksesan akademik di fase transisi/awal perkuliahan**. Sementara itu, faktor makroekonomi (Tingkat Inflasi, Pengangguran, dan GDP) terbukti secara empiris tidak relevan terhadap keputusan *dropout* mahasiswa.
4. **Implikasi Berdasarkan Hasil Prediksi:** Melalui pemisahan data `Enrolled` sebagai data simulasi *unseen*, model ini secara praktis mampu berfungsi sebagai alat skoring atau **Early Warning System (EWS)**. Universitas dapat memproses data ratusan mahasiswa aktif (*Enrolled*) ke dalam model ini untuk mendapatkan daftar prioritas mahasiswa mana yang membutuhkan perhatian khusus sebelum mereka secara resmi mengajukan pengunduran diri.

## Rekomendasi Action Items
Berdasarkan *insight* dan implikasi di atas, berikut adalah langkah aksi (*action items*) konkret yang direkomendasikan bagi universitas:

- **Action Item 1: Restrukturisasi Pembayaran & Bantuan Finansial Tepat Sasaran**
  Biro Administrasi/Keuangan harus proaktif menawarkan restrukturisasi cicilan pembayaran (*installment plans*) atau mencarikan alternatif beasiswa darurat secara spesifik bagi mahasiswa (terutama pria) yang terdeteksi mulai menunggak biaya kuliah di semester awal, guna menahan laju *dropout* akibat kendala ekonomi murni.
- **Action Item 2: Konseling Akademik Prediktif Berbasis Data (Early Warning System)**
  Integrasikan probabilitas output dari model klasifikasi *Machine Learning* ini ke dasbor dosen wali (konselor akademik). Dosen wali diwajibkan untuk langsung menjadwalkan sesi konseling khusus dan *peer-tutoring* bagi mahasiswa `Enrolled` yang mendapatkan skor probabilitas *dropout* > 65% berdasarkan anjloknya nilai serta gagalnya SKS di Semester 1.