# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Institusi pendidikan tinggi menghadapi tantangan besar terkait tingkat *dropout* (putus kuliah) mahasiswa, yang tidak hanya berdampak pada pendapatan institusi (hilangnya uang kuliah), tetapi juga mencoreng reputasi akademik universitas di mata publik dan lembaga akreditasi. Mengetahui mahasiswa mana yang berisiko gagal lebih awal sangat krusial bagi manajemen untuk dapat memberikan intervensi tepat waktu.

### Permasalahan Bisnis
1. Bagaimana cara mendeteksi dini mahasiswa yang memiliki probabilitas tinggi untuk *dropout* sebelum mereka benar-benar keluar dari institusi?
2. Faktor-faktor utama apa saja yang secara signifikan mendorong mahasiswa untuk *dropout*?
3. Langkah pencegahan atau intervensi seperti apa yang bisa diterapkan institusi untuk menekan persentase *Dropout*?

### Cakupan Proyek
1. **Eksplorasi Data (EDA):** Mengidentifikasi korelasi antar variabel akademik dan non-akademik menggunakan metode univariat dan bivariat.
2. **Data Preparation (Binary Classification):** Memfilter data untuk hanya melibatkan mahasiswa dengan status akhir yang jelas (*Graduate* vs *Dropout*) dalam pelatihan model (Label 0 dan 1). Data mahasiswa yang masih aktif (*Enrolled*) disisihkan sepenuhnya untuk dijadikan data uji prediksi di masa depan.
3. **Pembuatan Dashboard:** Merancang *Business Dashboard* interaktif untuk memudahkan manajemen memantau metrik kelulusan.
4. **Pembangunan Model Prediktif:** Membangun dan melatih model *Machine Learning* biner untuk memprediksi probabilitas risiko *dropout*.
5. **Deployment:** Menyediakan antarmuka prototipe interaktif (berbasis *Cloud*) agar konselor akademik dapat menguji prediksi risiko per individu.

## Persiapan
* **Sumber Data:** Dataset "[Predict students' dropout and academic success](https://archive.ics.uci.edu/dataset/697/predict+students+dropout+and+academic+success)" (Realinho et al., 2021).
* **Setup Environment:**
  * IDE: Google Colab (EDA & Modeling) / VS Code (Streamlit)
  * Pustaka Python Utama: Pandas, Matplotlib, Seaborn, Scikit-Learn, Streamlit, Joblib.

## Business Dashboard
*Business Dashboard* telah dirancang menggunakan Looker Studio guna memberikan alat pantau strategis bagi petinggi universitas. Terdapat visualisasi *Scatter Plot* (Korelasi Akademik) yang dengan jelas memetakan bagaimana penurunan jumlah SKS yang dilulusi berkorelasi langsung dengan kepastian *dropout*.
👉 **[Klik untuk Mengakses Business Dashboard (Looker Studio)](https://datastudio.google.com/reporting/a5637ebd-5e69-4b1d-8064-a362a1c541aa)**

## Menjalankan Sistem Machine Learning
Prototipe Sistem Machine Learning ini dibangun menggunakan algoritma `RandomForestClassifier` (Binary Classification) dan diluncurkan melalui Streamlit Community Cloud.

**Cara Penggunaan:**
1. Buka tautan prototipe aplikasi.
2. Pada panel navigasi di sebelah kiri, masukkan data simulasi atau data nyata dari profil seorang mahasiswa.
3. Klik tombol **Prediksi Status Risiko**.
4. Sistem akan mengeksekusi model *Random Forest* untuk menampilkan klasifikasi (Beresiko Dropout / Aman) beserta tingkat probabilitasnya.
👉 **[Klik untuk Mengakses Prototipe Machine Learning (Streamlit)](https://edutech-prediction-app.streamlit.app/)**

## Conclusion
Berdasarkan hasil pemodelan klasifikasi biner dan analisis Exploratory Data Analysis (EDA), disimpulkan bahwa faktor makroekonomi (seperti Inflasi) **tidak memiliki pengaruh** terhadap kelulusan individu. Sebaliknya, dua faktor mikro yang paling deterministik penyebab *dropout* adalah **stabilitas finansial** (tunggakan uang kuliah) dan **performa semester awal**. Model *Random Forest* biner terbukti mampu memetakan kompleksitas fitur tersebut dan memberikan probabilitas prediksi dengan keandalan yang jauh lebih tinggi dan fokus dibandingkan klasifikasi multikelas.

## Rekomendasi Action Items
Guna memitigasi tingkat *dropout*, pihak manajemen universitas direkomendasikan untuk menerapkan langkah-langkah konkret berikut:
- **Prioritaskan Mahasiswa 'Enrolled' Berisiko Tinggi:** Ekstrak data probabilitas *dropout* dari mahasiswa yang berstatus `Enrolled` menggunakan model ini. Panggil mahasiswa dengan probabilitas *dropout* di atas 70% untuk sesi konseling segera.
- **Restrukturisasi Kebijakan Finansial:** Tawarkan skema cicilan fleksibel (*installment plan*) untuk kelompok rentan agar tidak langsung mengambil keputusan untuk berhenti kuliah saat menunggak.
- **Program Tutoring Khusus Mahasiswa Pria di Semester Dasar:** Data menunjukkan gender pria rentan gagal. Selenggarakan sesi kelas tambahan atau kelompok pendampingan sebaya (*peer-tutoring*) di semester pertama.