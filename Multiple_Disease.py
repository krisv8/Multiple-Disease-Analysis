#Create a streamlit app to predict liver disease
import streamlit as st
import pandas as pd
import joblib
from streamlit_option_menu import option_menu
import base64



#Load the model
model_liver = joblib.load('liver_disease_model.pkl')
model_kidney = joblib.load('kidney_model.pkl')
model_parkinson = joblib.load('parkinsons_model.pkl')

#Header

st.markdown(f'<h1 style="color:black;font-size:48px;"><marquee><I>{"Multiple Disease Prediction App"}</I></marquee></h1>', unsafe_allow_html=True)



# sidebar for navigation
with st.sidebar:
    
    st.sidebar.image("Multiple Disease/Hospital.jpg",use_container_width=True)

    selected = option_menu('Multiple Disease Prediction System',
                          
                          ['Kidney Prediction',
                           'Liver Disease Prediction',
                           'Parkinsons Prediction'],
                          icons=['hospital','activity','person'],
                          default_index=0)
                    
if (selected == 'Kidney Prediction'):
  
    # page title
    st.title('Kidney Prediction')
    st.subheader('Prediction accuracy is expected to be 96%')
    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQYvoikvthR2gztyNXyPx_2OaFrN8Ax_s5ruw&s");
    background-size: cover;
    }
    </style>
    """

    st.markdown(page_element, unsafe_allow_html=True)
    
    
    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.text_input('Age of the Person',value='10')
    with col2:
        blood_pressure = st.text_input('Blood Pressure value',value='80')
    with col3:
        specific_gravity = st.text_input('Specific Gravity value',value='1')
    with col1:
        sugar = st.text_input('Sugar value',value='0')
    with col2:
        red_blood_cells = st.selectbox('Red Blood Cells', ('normal', 'abnormal'))
    with col3:
        pus_cell = st.selectbox('Pus Cell', ('normal', 'abnormal'))
    with col1:
        bacteria = st.selectbox('Bacteria', ('notpresent', 'present'))
    with col2:
        sodium = st.text_input('Sodium value',value='0')
    with col3:
        potassium = st.text_input('Potassium value',value='0')
    with col1:
        haemoglobin = st.text_input('Haemoglobin value',value='0')
    with col2:
        packedVol = st.text_input('Packed cell volume',value='0')
    with col3:
        RBCcount = st.text_input('RBC Count',value='0')
    

    #convert categorical inputs to numerical values
    #red_blood_cell,Pus cell, pus cell count,bacteria, Hypertension, Diabetes Mellitus, Coronary Artery Disease, Appetite, Pedal Edema, Anemia
    red_blood_cells = 1 if red_blood_cells.lower() == 'normal' else 0
    pus_cell = 1 if pus_cell.lower() == 'normal' else 0
    bacteria = 1 if bacteria.lower() == 'notpresent' else 0      

    # convert other inputs to float
    age= age.replace(' ', '')
    blood_pressure = blood_pressure.replace(' ', '')
    age = float(age)
    blood_pressure = float(blood_pressure)
    specific_gravity = float(specific_gravity)
    sugar = float(sugar)
    sodium = float(sodium)
    potassium = float(potassium)
    haemoglobin = float(haemoglobin)
    packedVol = float(packedVol)
    RBCcount = float(RBCcount)



    # code for Prediction
    kidney_diagnosis = ''

    # creating a button for Prediction
    if st.button('Kidney Test Result'):
        kidney_prediction = model_kidney.predict([[age, blood_pressure, specific_gravity, sugar, red_blood_cells, pus_cell,bacteria, sodium, potassium, haemoglobin, packedVol, RBCcount]])
    
        if (kidney_prediction[0] == 0):
            kidney_diagnosis = 'The person is having kidney disease'
            st.markdown(f'<p style="background-color:#0066cc;color:#db2742;font-size:24px;border-radius:2%;">{kidney_diagnosis}</p>', unsafe_allow_html=True)
        else:
            kidney_diagnosis = 'The person does not have any kidney disease'
            
            st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{kidney_diagnosis}</p>', unsafe_allow_html=True)

    
    




# Liver Disease Prediction Page
if (selected == 'Liver Disease Prediction'):

    # page title
    st.title('Liver Disease Prediction')
    st.subheader('Prediction accuracy is expected to be 99%')
    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("data:image/jpeg;base64,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");
    background-size: cover;
    }
    </style>
    """

    st.markdown(page_element, unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)
    
    with col1:
        age = st.number_input('Age')
    with col2:
        Genders = st.selectbox(options=["Male","Female"],label='Gender')  
    with col3:
        Total_Bilirubin = st.number_input('Total_Bilirubin')
    with col1:
        Direct_Bilirubin = st.number_input('Direct_Bilirubin')
    with col2:
        Alkaline_Phosphotase = st.number_input('Alkaline_Phosphotase')
    with col3:
        Alamine_Aminotransferase = st.number_input('Alamine_Aminotransferase')
    with col1:
        Aspartate_Aminotransferase = st.number_input('Aspartate_Aminotransferase')
    with col2:
        Total_Protiens = st.number_input('Total_Protiens')
    with col3:
        Albumin = float(st.number_input('Albumin'))
    with col1:
        Albumin_and_Globulin_Ratio = st.number_input('Albumin_and_Globulin_Ratio')

     #convert categorical inputs to numerical values
    Genders = 1 if Genders == "Male" else 0
    
    # convert other inputs to float

    # code for Prediction
    liver_diagnosis = ''
    
    # creating a button for Prediction
    
    if st.button('Liver Disease Test Result'):
        liver_diagnosis = model_liver.predict([[age,Genders,Total_Bilirubin,Direct_Bilirubin,Alkaline_Phosphotase,Alamine_Aminotransferase,Aspartate_Aminotransferase,Total_Protiens, Albumin,Albumin_and_Globulin_Ratio]])                          
        
        if (liver_diagnosis[0] == 1):
          liver_diagnosis = 'The person is having liver disease'
          st.markdown(f'<p style="background-color:#0066cc;color:#db2742;font-size:24px;border-radius:2%;">{liver_diagnosis}</p>', unsafe_allow_html=True)
        else:
          liver_diagnosis = 'The person does not have any liver disease'
          st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{liver_diagnosis}</p>', unsafe_allow_html=True)
        
    
        
    
    

# Parkinson's Prediction Page
if (selected == "Parkinsons Prediction"):
    
    # page title
    st.title("Parkinson's Disease Prediction")
    st.subheader('Prediction accuracy is expected to be 95%')
    page_element="""
    <style>
    [data-testid="stAppViewContainer"]{
    background-image: url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRZZyY7HbJW-yMm-okA9N8kGipjQIaONPjCJQ&s");
    background-size: cover;
    }
    </style>
    """

    st.markdown(page_element, unsafe_allow_html=True)
    
    col1, col2, col3, col4 = st.columns(4)  
    
    with col1:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
        
    with col2:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
        
    with col3:
        RAP = st.text_input('MDVP:RAP')
        
    with col4:
        PPQ = st.text_input('MDVP:PPQ')
        
    with col1:
        DDP = st.text_input('Jitter:DDP')
        
    with col2:
        Shimmer = st.text_input('MDVP:Shimmer')
        
    with col3:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
        
    with col4:
        APQ3 = st.text_input('Shimmer:APQ3')
        
    with col1:
        APQ5 = st.text_input('Shimmer:APQ5')
        
    with col2:
        APQ = st.text_input('MDVP:APQ')
        
    with col3:
        spread1 = st.text_input('spread1')
        
    with col4:
        spread2 = st.text_input('spread2')
        
    
    
    # code for Prediction
    parkinsons_diagnosis = ''
    
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = model_parkinson.predict([[Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,spread1,spread2]])                          
        
        if (parkinsons_prediction[0] == 1):
          parkinsons_diagnosis = "The person has Parkinson's disease"
          st.markdown(f'<p style="background-color:#0066cc;color:#db2742;font-size:24px;border-radius:2%;">{parkinsons_diagnosis}</p>', unsafe_allow_html=True)
        else:
          parkinsons_diagnosis = "The person does not have Parkinson's disease"
          st.markdown(f'<p style="background-color:#0066cc;color:#33ff33;font-size:24px;border-radius:2%;">{parkinsons_diagnosis}</p>', unsafe_allow_html=True)
        
    


