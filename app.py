import streamlit as st
import pandas as pd
import joblib

# 1. Load Model dan Scaler
@st.cache_resource
def load_model():
    model = joblib.load('student_model.pkl')
    scaler = joblib.load('scaler.pkl')
    le = joblib.load('label_encoder.pkl')
    return model, scaler, le

model, scaler, le = load_model()

# 2. Judul Aplikasi
st.title('🎓 Prediksi Status Mahasiswa (Dropout / Graduate)')
st.write('Aplikasi ini memprediksi apakah seorang mahasiswa berisiko dropout atau akan lulus berdasarkan profil akademik dan demografinya.')

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

    data = {
        'Marital_status': 1, # Set nilai default untuk kolom yang tidak diisi manual di form
        'Application_mode': 1,
        'Application_order': 1,
        'Course': 9119,
        'Daytime_evening_attendance': 1,
        'Previous_qualification': 1,
        'Nacionality': 1,
        'Mothers_qualification': 1,
        'Fathers_qualification': 1,
        'Mothers_occupation': 1,
        'Fathers_occupation': 1,
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

# Menampilkan input user
st.subheader('Data Input Mahasiswa')
st.write(input_df)

# 4. Melakukan Prediksi
if st.button('Prediksi Status'):
    # Melakukan scaling terlebih dahulu
    scaled_input = scaler.transform(input_df)
    
    # Prediksi dengan model
    prediction = model.predict(scaled_input)
    prediction_proba = model.predict_proba(scaled_input)
    
    # Mengubah angka (0,1,2) kembali ke teks (Dropout, Enrolled, Graduate)
    status = le.inverse_transform(prediction)[0]
    
    st.subheader('Hasil Prediksi:')
    if status == 'Dropout':
        st.error(f'⚠️ Mahasiswa ini berisiko: {status}')
    elif status == 'Graduate':
        st.success(f'✅ Mahasiswa ini diprediksi: {status}')
    else:
        st.warning(f'⏳ Status mahasiswa diprediksi: {status}')
    
    st.write('Probabilitas Prediksi:')
    proba_df = pd.DataFrame(prediction_proba, columns=le.classes_)
    st.write(proba_df)