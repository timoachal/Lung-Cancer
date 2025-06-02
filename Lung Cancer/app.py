import os
import pickle
import time
import numpy as np
import streamlit as st
from streamlit_option_menu import option_menu

# Set page configuration
st.set_page_config(page_title="Lung Cancer Prediction App",
                   layout="wide")
    

# getting the working directory 
working_dir = os.path.dirname(os.path.abspath(__file__))

Lung_model = pickle.load(open(f'{working_dir}/models/Lung_Can_model.sav', 'rb'))

with st.sidebar:
    selected = option_menu('Lung Cancer Screening Tool',

                           ['Home','Lung Cancer'],
                            #st.image()
                           #menu_icon='hospital-fill',
                           icons=['home'],
                           default_index=0)
    
if selected == "Home":
    st.title("Lung Cancer Details")
    st.markdown("""
    ### Lung Cancer Overview
    <p><strong>Lung Cancer</strong> is a serious disease characterized by uncontrolled cell growth tissues of the lung. It is one
                    of the leading causes of Cancer deaths worldwide.</p>                 
    """, unsafe_allow_html=True )  
    with st.expander("Causes and Risks Factors"):
        st.markdown("""
        <ul>
            <li>Smoking </li>                    
            <li>Exposure to radom, asbestos or Industrial Chemicals</li>
            <li>Air Pollution</li>
            <li>Genetic Predisposition</li>
        </ul>
        """, unsafe_allow_html=True)                                        

    with st.expander("Symptoms"):
        st.markdown("""
        <ul>
            <li>Persistent Cough</li>                    
            <li>Coughing up Blood</li>
            <li>Shortness of Breath</li>
            <li>Chest Pains</li>
            <li>Weight Loss and Fatigue</li> 
            <li>Recurrent Lung Infections.</li>             
        </ul>
        """, unsafe_allow_html=True)  

    with st.expander("Diagnosis"):
        st.markdown("""
        <ul>
            <li>Imaging: X-Ray, CT scan</li>                    
            <li>Biopsy</li>
            <li>Sputum Cytology</li>
            <li>Genetic or Molecular Testing</li>            
        </ul>
        """, unsafe_allow_html=True)  

    with st.expander("Treatment Options"):
        st.markdown("""
        <ul>
            <li><strong>Surgery</strong>: Removing the tumor or Lung Sections</li>                    
            <li><strong>Radiation Therapy</strong></li>
            <li><strong>Chemotherapy</strong></li>
            <li><strong>Targeted Therapy</li>            
        </ul>
        """, unsafe_allow_html=True)  

    with st.expander("Prevention"):
        st.markdown("""
        <ul>
            <li><strong>Quit Smoking</li>                    
            <li>Reduce exposure to known Carcinogens</li>
            <li>Maintain a Healthy Lifestyle</li>            
        </ul>
        """, unsafe_allow_html=True) 

    st.markdown("<p style='color:gray; font-style: italic;'>Always Consult a medical Professional for Health-related decisions.</p>", unsafe_allow_html=True)              

if selected == 'Lung Cancer':

    # page title
    st.title('Lung Cancer Screening App:\n Please fill in your Details below')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)
    

    with col1:
        Age = st.number_input('Your specified Age',min_value=0, max_value=120, step = 1)

    with col2:
        Gender = st.selectbox('Select your Gender',["Male","Female"])
          
    with col3:
        Tumor_Size_mm = st.number_input('Tumor Size',min_value=0.0, step = 0.1)   

    with col1:
        Tumor_Location = st.selectbox('Tumor Location',["Middle Lobe","Upper Lobe","Lower Lobe"])

    with col2:
        Smoking_History = st.selectbox('Smoking Status',["Former Smoker","Current Smoker","Never Smoker"])

    with col3:
        Treatment = st.selectbox('Treatment Type',["Targeted Therapy","Radiation Therapy","Surgery","Chemotherapy"])

    with col1:
        Family_History = st.selectbox('Do members of Your Family have Lung Cancer?', ["No","Yes"])

    with col2:
        Comorbidity_Diabetes = st.selectbox('Are you Diabetic?',["No","Yes"])

    with col3:
        Comorbidity_Hypertension = st.selectbox('Do you have Hypertension?',["No","Yes"])    

    with col1:
        Comorbidity_Heart_Disease = st.selectbox('Do you have Heart Disease?',["No","Yes"])

    with col2:
        Comorbidity_Chronic_Lung_Disease = st.selectbox('Do you have Lung Disease?',["No","Yes"])   
    
    with col3:
        Hemoglobin_Level = st.number_input('Your Hemoglobin Level', min_value=0.0, step = 0.1)   

    with col1:
        White_Blood_Cell_Count = st.number_input('White Blood Cell Count', min_value=0.0, step = 0.1)   

    with col2:
        Platelet_Count = st.number_input('Platelet Count', min_value=0.0, step = 0.1)  

    with col3:
        Albumin_Level = st.number_input('Albumin Level', min_value=0.0, step = 0.1)              

    with col1:
        Alkaline_Phosphatase_Level = st.number_input('Alkaline Phosphatase Level', min_value=0.0, step = 0.1)  

    with col2:
        Alanine_Aminotransferase_Level = st.number_input('Alanine Aminotransferase Level', min_value=0.0, step = 0.1)  

    with col3:
        Aspartate_Aminotransferase_Level = st.number_input('Aspartate Aminotransferase Level', min_value=0.0, step = 0.1)           

    with col1:
        Creatinine_Level = st.number_input('Creatinine Level', min_value=0.0, step = 0.1)   

    with col2:
        LDH_Level = st.number_input('LDH_Level', min_value=0.0, step = 1.0) 

    with col3:
        Sodium_Level = st.number_input('Sodium Level', min_value=0.0, step = 1.0)       
     

    # Map categorical values to numericals
    gender_map = {"Male": 1, "Female": 0}
    tumor_map = {"Middle Lobe": 1,"Upper Lobe": 2,"Lower Lobe": 3}
    smoke_map = {"Former Smoker": 1,"Current Smoker": 2,"Never Smoker": 3}
    famil_map = {"No": 1,"Yes": 2}
    diab_map = {"No": 1,"Yes": 2}
    hyper_map = {"No": 1,"Yes": 2}
    heart_map = {"No": 1,"Yes": 2}
    lung_map = {"No": 1,"Yes": 2}
    treat_map = {"Targeted Therapy": 1,"Radiation Therapy": 2,"Surgery": 3,"Chemotherapy": 4}

    # Stage mapping
    stage_mapping = {
        0: "Stage 1",
        1: "Stage 2",
        2: "Stage 3",
        3: "Stage 4"
    }

    # code for Prediction
    lung_diagnosis = ''

    # creating a button for Prediction

    if st.button('Lung Cancer Predict Stage'):
        with st.spinner("Searching..."):
            time.sleep(3)

        user_input = [
            Age,
            gender_map[Gender],
            tumor_map[Tumor_Location],
            smoke_map[Smoking_History],
            famil_map[Family_History],
            treat_map[Treatment],
            diab_map[Comorbidity_Diabetes],
            hyper_map[Comorbidity_Hypertension],
            heart_map[Comorbidity_Heart_Disease],
            lung_map[Comorbidity_Chronic_Lung_Disease],
            Tumor_Size_mm,
            Hemoglobin_Level,
            White_Blood_Cell_Count,
            Platelet_Count,
            Albumin_Level,
            Alkaline_Phosphatase_Level,
            Alanine_Aminotransferase_Level,
            Aspartate_Aminotransferase_Level,
            Creatinine_Level,
            LDH_Level,
            Sodium_Level

        ] 
        
        user_input = [float(x) for x in user_input]
        user_input_array = np.array(user_input).reshape(1,-1)
        prediction = Lung_model.predict(user_input_array)[0]
        prediction_proba = Lung_model.predict_proba(user_input_array)[0]
        stage = stage_mapping[prediction]

        st.subheader('Prediction Result')
        st.write(f"Predicted Cancer Stage:{stage}")
        st.subheader("Recommendations")

        if stage == "Stage 1":
            st.markdown("""
            <div style="background-color:#006400; padding:15px; border-radius:10px">
                <h4 style="color:#FFFFF;">Stage 1 - Early Stage</h4>
                <ul>
                    <li>Consider surgical removal of tumor (lobectomy or segmentectomy).</li>
                    <li>Low-dose CT scans for ongoing monitoring.</li>
                    <li>Adjuvant therapy may be discussed depending on tumor size.</li>
                    <li>Quit smoking if applicable and adopt a healthy lifestyle.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        elif stage == "Stage 2":
            st.markdown("""
            <div style="background-color:green; padding:15px; border-radius:10px">
                <h4 style="color:#FFFFFF;">Stage 2 - Localized Spread</h4>
                <ul>
                    <li>Surgery usually combined with chemotherapy (adjuvant).</li>
                    <li>Regular follow-up scans and physical exams.</li>
                    <li>Discuss radiation if surgery is not an option.</li>
                    <li>Nutrition and physical activity counseling recommended.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        elif stage == "Stage 3":
            st.markdown("""
            <div style="background-color:blue; padding:15px; border-radius:10px">
                <h4 style="color:#f9a825;">Stage 3 - Regional Spread</h4>
                <ul>
                    <li>Combination of chemotherapy and radiation therapy is typical.</li>
                    <li>Targeted therapy or immunotherapy may be introduced.</li>
                    <li>Consider clinical trials for new treatment options.</li>
                    <li>Pulmonary rehab and psychological support are important.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

        elif stage == "Stage 4":
            st.markdown("""
            <div style="background-color:black; padding:15px; border-radius:10px">
                <h4 style="color:#c62828;">Stage 4 - Advanced/Metastatic</h4>
                <ul>
                    <li>Focus on palliative care to manage symptoms and improve quality of life.</li>
                    <li>Targeted therapy, immunotherapy, or chemotherapy depending on biomarkers.</li>
                    <li>Strong support system and advanced care planning.</li>
                    <li>Regular discussions with oncology and palliative teams.</li>
                </ul>
            </div>
            """, unsafe_allow_html=True)

   

        




       