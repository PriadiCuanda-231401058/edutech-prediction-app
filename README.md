# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech 🎓

## 1. Business Understanding
**Latar Belakang:**
Sebuah institusi pendidikan tinggi (Edutech) menghadapi tantangan berupa tingginya angka mahasiswa yang putus kuliah (*dropout*). Fenomena ini tidak hanya berdampak negatif pada reputasi institusi, tetapi juga mengganggu stabilitas finansial operasional kampus. 

**Tujuan Bisnis (*Business Objective*):**
1. Mengidentifikasi faktor-faktor utama yang berkontribusi terhadap keputusan mahasiswa untuk *dropout*.
2. Membangun model *Machine Learning* untuk memprediksi probabilitas kelulusan atau *dropout* sejak dini.
3. Menciptakan dasbor interaktif (*Business Dashboard*) untuk memantau performa mahasiswa secara *real-time*.

**Metrik Keberhasilan Bisnis:**
- Menurunkan tingkat *dropout* mahasiswa sebesar 10-15% dalam satu tahun akademik berkat intervensi dini.
- Meningkatkan *retention rate* (tingkat retensi) mahasiswa aktif.

---

## 2. Business Dashboard
Untuk memantau kondisi demografi dan akademik mahasiswa, kami telah membangun sebuah **Business Dashboard** interaktif. Dasbor ini dirancang khusus untuk pihak manajemen kampus, seperti dekan dan biro keuangan, agar dapat melihat metrik-metrik krusial secara sekilas.

**Komponen Utama Dasbor:**
- **Scorecard Metrik Utama:** Menampilkan jumlah total mahasiswa, rata-rata usia, dan rata-rata nilai masuk.
- **Distribusi Status Mahasiswa (Pie Chart):** Proporsi *real-time* dari mahasiswa yang berstatus Lulus (*Graduate*), Terdaftar (*Enrolled*), dan Putus Kuliah (*Dropout*).
- **Analisis Finansial vs Dropout (100% Stacked Bar):** Menyoroti seberapa besar rasio *dropout* pada mahasiswa yang menunggak biaya kuliah dibandingkan yang lunas.
- **Korelasi Akademik (Combo/Scatter Chart):** Memvisualisasikan perbandingan SKS yang diambil vs SKS yang berhasil lulus, serta hubungan nilai antar semester.

🔗 **[Akses Looker Studio Dashboard di Sini](#)** *(Ganti tanda # dengan link Looker Studio Anda)*

---

## 3. Cara Penggunaan Model & Dashboard

### A. Penggunaan Business Dashboard (Looker Studio)
1. Buka tautan dasbor melalui web browser 
🔗 **[Akses Dashboard di Sini](https://datastudio.google.com/reporting/a5637ebd-5e69-4b1d-8064-a362a1c541aa)**
2. Gunakan **Panel Filter** di bagian atas (atau samping) untuk menyaring data spesifik. 
   - Contoh: Pilih filter "Jurusan" untuk melihat tingkat kelulusan khusus pada jurusan *Informatics Engineering*.
   - Pilih filter "Gender" untuk membandingkan performa antara mahasiswa laki-laki dan perempuan.
3. Arahkan kursor (*hover*) ke berbagai elemen grafik untuk melihat angka riil dari persentase data.

### B. Penggunaan Aplikasi Prediksi (Streamlit)
Aplikasi ini digunakan oleh staf akademik untuk memprediksi status individu mahasiswa baru/aktif.
🔗 **[Akses Streamlit Prediction App di Sini](https://edutech-prediction-app.streamlit.app/)**

**Langkah Penggunaan:**
1. Buka tautan Streamlit App.
2. Di panel sebelah kiri (*sidebar*), masukkan profil data mahasiswa (contoh: Status Uang Kuliah, Penerima Beasiswa, Usia, Nilai Semester 1 dan 2).
3. Setelah data lengkap, klik tombol **"Prediksi Status"** di layar utama.
4. Sistem akan mengeluarkan hasil (Lulus / Dropout / Masih Terdaftar) lengkap beserta tingkat keyakinan (*probability*) dari model tersebut.

---

## 4. Conclusion (Kesimpulan Analisis)
Berdasarkan proses *Exploratory Data Analysis* (EDA) dan *Machine Learning Modeling* menggunakan *Random Forest Classifier*, kami menyimpulkan bahwa:

1. **Faktor Finansial adalah Kunci Utama:** Mahasiswa yang memiliki tunggakan uang kuliah (`Tuition_fees_up_to_date = 0`) atau berstatus debitor memiliki persentase *dropout* yang sangat ekstrem (di atas 80%). Sebaliknya, kepemilikan beasiswa hampir menjamin retensi mahasiswa.
2. **Kinerja Akademik Semester Awal Sangat Prediktif:** Jumlah unit mata kuliah (SKS) yang berhasil diselesaikan (*approved*) pada Semester 1 dan Semester 2 adalah prediktor terbaik. Kegagalan di awal masa studi berujung langsung pada potensi *dropout*.
3. **Faktor Makroekonomi Tidak Signifikan:** Metrik seperti Inflasi, Tingkat Pengangguran (*Unemployment rate*), dan GDP memiliki korelasi linear mendekati nol, membuktikan keputusan *dropout* lebih dipengaruhi oleh faktor internal individu (akademik & ekonomi personal) dibanding kondisi negara secara umum.

---

## 5. Rekomendasi Action Item
Untuk menekan angka *dropout*, institusi/kampus direkomendasikan untuk melakukan tindak lanjut (*action item*) secara nyata berikut:

1. **Intervensi Finansial Dini (Restrukturisasi Pembayaran):** 
   - Biro Keuangan harus segera menghubungi mahasiswa yang status uang kuliahnya mulai menunggak sebelum Ujian Akhir Semester (UAS). 
   - *Action:* Tawarkan program cicilan khusus (*installment plan*) atau keringanan tenggat waktu untuk mencegah mahasiswa mundur karena tekanan biaya secara mendadak.
2. **Sistem Peringatan Dini Akademik (Early Warning System):**
   - *Action:* Integrasikan model *Machine Learning* ini ke portal akademik Dosen Wali/Pembimbing Akademik. 
   - Jika sistem mendeteksi nilai Semester 1 seorang mahasiswa berada di bawah rata-rata (terutama jika ia laki-laki tanpa beasiswa), Dosen Wali diwajibkan melakukan sesi konseling sebelum Semester 2 dimulai.
3. **Pemberdayaan Beasiswa Tepat Sasaran:**
   - Mengingat fitur `Scholarship_holder` memiliki dampak masif terhadap kelulusan, institusi disarankan menjalin kemitraan dengan pihak swasta/pemerintah untuk menambah kuota beasiswa, dengan memprioritaskan mahasiswa yang memiliki nilai baik namun berisiko tinggi secara finansial (*Debtor*).

---
**Dibuat oleh:** Priadi Cuanda  
**Email:** priadicuanda2904@gmail.com
**ID Dicoding:** CDCC319D6Y0576