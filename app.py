import streamlit as st
import pandas as pd
import joblib

# 1. Load Model Biner dan Scaler
@st.cache_resource
def load_model():
    # Load model yang sudah di-training HANYA dengan kelas Dropout (1) dan Graduate (0)
    model = joblib.load('student_binary_model.pkl')
    scaler = joblib.load('scaler.pkl')
    return model, scaler

model, scaler = load_model()

# 2. Judul Aplikasi
st.title('🎓 Sistem Deteksi Dini Risiko Dropout Mahasiswa')
st.write('Aplikasi ini menggunakan model klasifikasi biner untuk memprediksi probabilitas seorang mahasiswa berisiko tinggi putus kuliah (Dropout) atau berpotensi lulus (Graduate) berdasarkan data akademik dan sosial ekonominya.')

# 3. Form Input Data
st.sidebar.header('Masukkan Data Mahasiswa')

def user_input_features():
    tuition_fees = st.sidebar.selectbox('Tuition fees up to date (Uang Kuliah Lunas)', (0, 1))
    scholarship = st.sidebar.selectbox('Scholarship holder (Penerima Beasiswa)', (0, 1))
    gender = st.sidebar.selectbox('Gender (1: Pria, 0: Wanita)', (0, 1))
    debtor = st.sidebar.selectbox('Debtor (Punya Tunggakan/Hutang)', (0, 1))
    
    age = st.sidebar.number_input('Age at enrollment (Usia Mendaftar)', min_value=15, max_value=80, value=20)
    sem1_grade = st.sidebar.slider('Grade Semester 1 (0-20)', 0.0, 20.0, 12.0)
    sem2_grade = st.sidebar.slider('Grade Semester 2 (0-20)', 0.0, 20.0, 12.0)
    sem1_approved = st.sidebar.number_input('SKS Sem 1 Lulus', min_value=0, max_value=20, value=5)
    sem2_approved = st.sidebar.number_input('SKS Sem 2 Lulus', min_value=0, max_value=20, value=5)

    # Dictionary harus menyesuaikan jumlah fitur (32 fitur) persis dengan X_train
    data = {
        'Marital_status': 1,
        'Application_mode': 1,
        'Application_order': 1,
        'Course': 9119,
        'Daytime_evening_attendance': 1,
        'Previous_qualification': 1,
        'Previous_qualification_grade': 130.0, 
        'Nacionality': 1,
        'Mothers_qualification': 1,
        'Fathers_qualification': 1,
        'Mothers_occupation': 1,
        'Fathers_occupation': 1,
        'Admission_grade': 120.0,               
        'Displaced': 1,
        'Educational_special_needs': 0,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_fees,
        'Gender': gender,
        'Scholarship_holder': scholarship,
        'Age_at_enrollment': age,
        'International': 0,
        'Curricular_units_1st_sem_credited': 0,
        'Curricular_units_1st_sem_enrolled': 6,
        'Curricular_units_1st_sem_evaluations': 6,
        'Curricular_units_1st_sem_approved': sem1_approved,
        'Curricular_units_1st_sem_grade': sem1_grade,
        'Curricular_units_1st_sem_without_evaluations': 0,
        'Curricular_units_2nd_sem_credited': 0,
        'Curricular_units_2nd_sem_enrolled': 6,
        'Curricular_units_2nd_sem_evaluations': 6,
        'Curricular_units_2nd_sem_approved': sem2_approved,
        'Curricular_units_2nd_sem_grade': sem2_grade,
        'Curricular_units_2nd_sem_without_evaluations': 0
    }
    features = pd.DataFrame(data, index=[0])
    return features

input_df = user_input_features()

st.subheader('Data Input Mahasiswa')
st.write(input_df)

# 4. Melakukan Prediksi
if st.button('Prediksi Risiko'):
    # Scaling
    scaled_input = scaler.transform(input_df)
    
    # Memprediksi (0 = Graduate, 1 = Dropout)
    prediction = model.predict(scaled_input)[0]
    prediction_proba = model.predict_proba(scaled_input)[0]
    
    st.subheader('Hasil Prediksi:')
    if prediction == 1:
        st.error(f'⚠️ PERINGATAN: Mahasiswa diprediksi berisiko tinggi DROPOUT (Probabilitas: {prediction_proba[1]*100:.1f}%)')
    else:
        st.success(f'✅ AMAN: Mahasiswa diprediksi GRADUATE (Probabilitas Lulus: {prediction_proba[0]*100:.1f}%)')
        
    st.write('---')
    st.caption('Detail Probabilitas Model: Graduate (0): {:.1f}% | Dropout (1): {:.1f}%'.format(prediction_proba[0]*100, prediction_proba[1]*100))