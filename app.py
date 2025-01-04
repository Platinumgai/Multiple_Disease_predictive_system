
import pickle
import streamlit as st
import streamlit_option_menu
from streamlit_option_menu import option_menu


#loading the saved model

diabetes_model=pickle.load(open('diabetes.sav','rb'))

heart_model=pickle.load(open('heart.sav','rb'))

parkinsons_model=pickle.load(open('parkinson.sav','rb'))

#Sidebar for navigator

with st.sidebar:
    
    selected=option_menu('Multiple Disease prediction system',
                         ['Diabetes Prediction',
                          'Heart Disease Prediction',
                          'Parkinsons Prediction'],
                         icons=['activity','heart','person'],
                         default_index=0)
    
    
#Diabetes Prediction page
if(selected=='Diabetes Prediction'):
    
    #page Title
    st.title('Diabetes Prediction using ML')
    
    #getting the input data from the user
    col1,col2,col3=st.columns(3)
    
    with col1:
        Pregnancies=st.text_input('Number of Pregnancies')
    with col2:
        Glucose=st.text_input('Glucose level')
    with col3:
        BloodPressure=st.text_input('Blood Pressure value')
    with col1:
        SkinThickness=st.text_input('Skin Thickness Value')
    with col2:
        Insulin=st.text_input('Insulin level')
    with col3:
        BMI=st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction=st.text_input('Diabetes Pedigree Function Value')
    
        
    #code for prediction
    diab_diagnosis=''
    
    #creating a button for prediction
    
    if st.button('Diabetes Test Result'):
        diab_prediction=diabetes_model.predict([[Pregnancies,Glucose,BloodPressure,SkinThickness,Insulin,BMI,DiabetesPedigreeFunction]])
        
        if (diab_prediction[0]==1):
            diab_diagnosis='The Person is Diabetic'
        else:
            diab_diagnosis='The Person is Non-Diabetic'
            
    st.success(diab_diagnosis)
 
 
if selected == 'Heart Disease Prediction':
    
    # Page title
    st.title('Heart Disease Prediction using ML')
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        # Increment and Decrement buttons using number_input
        age = st.text_input('Age')
    
    with col2:
        # Dropdown for sex
        sex = st.selectbox('Sex', ['Male', 'Female'])
        sex_value = 1 if sex == 'Male' else 0
    
    with col3:
        # Dropdown for Chest Pain types
        cp = st.selectbox('Chest Pain types', [
            '0 = Typical angina',
            '1 = Atypical angina',
            '2 = Non-anginal pain',
            '3 = Asymptomatic'
        ])
        cp_value = int(cp.split('=')[0].strip())
    
    with col1:
        trestbps = st.text_input('Resting Blood Pressure')
    
    with col2:
        chol = st.text_input('Serum Cholestoral in mg/dl')
    
    with col3:
        fbs = st.selectbox('Fasting Blood Sugar > 120 mg/dl', [
            '1 = True',
            '0 = False'
        ])
        fbs_value = int(fbs.split('=')[0].strip())
    
    with col1:
        restecg = st.selectbox('Resting Electrocardiographic results', [
            '0 = Normal',
            '1 = ST-T wave abnormality',
            '2 = Left ventricular hypertrophy'
        ])
        restecg_value = int(restecg.split('=')[0].strip())
    
    with col2:
        thalach = st.text_input('Maximum Heart Rate achieved')
    
    with col3:
        exang = st.selectbox('Exercise Induced Angina', [
            '1 = Yes',
            '0 = No'
        ])
        exang_value = int(exang.split('=')[0].strip())
    
    with col1:
        oldpeak = st.text_input('ST depression induced by exercise')
    
    with col2:
        slope = st.selectbox('Slope of the peak', [
            '0 = Upsloping',
            '1 = Flat',
            '2 = Downsloping'
        ])
        slope_value = int(slope.split('=')[0].strip())
    
    with col3:
        ca = st.text_input('Major vessels colored by flouroscopy')
    
    with col1:
        thal = st.selectbox('Thalassemia types', [
            '1 = Normal',
            '2 = Fixed defect',
            '3 = Reversible defect'
        ])
        thal_value = int(thal.split('=')[0].strip())
    
    # Code for Prediction
    heart_diagnosis = ''
    
    # Creating a button for Prediction
    if st.button('Heart Disease Test Result'):
        try:
            input_data = [
                float(age), 
                sex_value, 
                cp_value, 
                float(trestbps), 
                float(chol), 
                fbs_value, 
                restecg_value, 
                float(thalach), 
                exang_value, 
                float(oldpeak), 
                slope_value, 
                int(ca), 
                thal_value
            ]
            
            heart_prediction = heart_model.predict([input_data])
            
            if heart_prediction[0] == 1:
                heart_diagnosis = 'The person is having heart disease'
            else:
                heart_diagnosis = 'The person does not have any heart disease'
        
        except ValueError:
            heart_diagnosis = "Please enter valid numeric inputs."
        
    st.success(heart_diagnosis)

       
       
    
    

       
   
   
    
if(selected=='Parkinsons Prediction'):
    
    #page title
    st.title('Parkinsons Prediction using ML')
    
    
    col1, col2, col3, col4, col5 = st.columns(5)  
  
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
      
    with col2:
        fhi = st.text_input('MDVP:Fhi(Hz)')
      
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')
      
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
      
    with col5:
        Jitter_Abs = st.text_input('MDVP:Jitter(Abs)')
      
    with col1:
        RAP = st.text_input('MDVP:RAP')
      
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
      
    with col3:
        DDP = st.text_input('Jitter:DDP')
      
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
      
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
      
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')
      
    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
      
    with col3:
        APQ = st.text_input('MDVP:APQ')
      
    with col4:
        DDA = st.text_input('Shimmer:DDA')
      
    with col5:
        NHR = st.text_input('NHR')
      
    with col1:
        HNR = st.text_input('HNR')
      
    with col2:
        RPDE = st.text_input('RPDE')
      
    with col3:
        DFA = st.text_input('DFA')
      
    with col4:
        spread1 = st.text_input('spread1')
      
    with col5:
        spread2 = st.text_input('spread2')
      
    with col1:
        D2 = st.text_input('D2')
      
    with col2:
        PPE = st.text_input('PPE')
      
  
  
    # code for Prediction
    parkinsons_diagnosis = ''
  
    # creating a button for Prediction    
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = parkinsons_model.predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ,DDP,Shimmer,Shimmer_dB,APQ3,APQ5,APQ,DDA,NHR,HNR,RPDE,DFA,spread1,spread2,D2,PPE]])                          
        
        if (parkinsons_prediction[0] == 1):
            parkinsons_diagnosis = "The person has Parkinson's disease"
        else:
            parkinsons_diagnosis = "The person does not have Parkinson's disease"
      
        st.success(parkinsons_diagnosis)
