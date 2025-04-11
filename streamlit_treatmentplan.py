import streamlit as st

# Streamlit UI
st.title("Lung Cancer Detection💻")
st.markdown(
    """
    <style>
    body {
        background-color: #ADD8E6; /* Light blue color */
    }
    .section {
        background-image: url('https://jnj-content-lab2.brightspotcdn.com/dims4/default/78c6313/2147483647/strip/false/crop/1440x666+0+0/resize/1440x666!/quality/90/?url=https%3A%2F%2Fjnj-production-jnj.s3.us-east-1.amazonaws.com%2Fbrightspot%2F1b%2F32%2F2e138abbf1792e49103c9e3516a8%2Fno-one-would-believe-me-when-i-suspected-i-had-lung-cancer-0923-new.jpg');
        background-size: cover; 
        background-repeat: no-repeat;
        background-position: center;
        padding: 60px; 
        border-radius: 10px;
        color: black; 
        margin: 20px 0;
        height: 400px; 
    }
    .sidebar .sidebar-content {
        background-color: #ADD8E6; 
        color: black; 
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="section">', unsafe_allow_html=True)
st.header("Thank you for using ONCO AI🌐")
st.write("CNNs are the preferred network for detecting lung cancer due to their ability to process image data. They can perform tasks such as classification, segmentation, and object recognition. In the case of lung cancer detection, CNNs have surpassed radiologists.")
st.markdown('</div>', unsafe_allow_html=True)
st.markdown("Visit [ONCO AI](https://readymag.website/u4174625345/5256774/) for more information.")
st.markdown("Visit the [previous](https://lung-cancer-detection-appgit-sjmaymnetmmtmuny7ux2op.streamlit.app/#thank-you-for-using-oncoscan) page.")
st.markdown("Visit my [GitHub](https://github.com/HeavenlyCloudz/lung-cancer-detection-app) repository for insight on my code.")
st.write("In the case of this project, CT scans display the full outlook of the lungs condensed into an image with a strictly two-dimensional, flat appearance, serving a pivotal role in the identification of early-stage diseases due to the clarity of the images, and the noticeable lack of noise in the scans. ​The presence of white marks, or nodules, in the scan might point towards the presence of cancer.")


# Symptoms checkboxes
symptoms = [
    "Persistent cough",
    "Shortness of breath",
    "Chest pain",
    "Fatigue",
    "Weight loss",
    "Wheezing",
    "Coughing up blood"
]

# Multi-select for symptoms
selected_symptoms = st.multiselect("Select any symptoms you're experiencing:", symptoms)

# Detailed follow-up questions based on selected symptoms
if st.button("Done"):
    if "Persistent cough" in selected_symptoms:
        cough_severity = st.selectbox("How severe is your cough?", ["Mild", "Moderate", "Severe"])
        cough_duration = st.selectbox("How long have you been experiencing this?", ["Less than a week", "1-2 weeks", "More than 2 weeks"])
        
        if cough_severity == "Mild":
            st.write("A mild cough may be manageable at home. You might consider using **over-the-counter cough suppressants**.")
        elif cough_severity == "Moderate":
            st.write("Moderate cough could benefit from **bronchodilators**. Discuss this with your healthcare provider.")
        elif cough_severity == "Severe":
            st.write("Severe cough requires immediate medical evaluation. Seek help to determine the cause.")
        
        if cough_duration == "Less than a week":
            st.write("A cough lasting less than a week may be due to a cold or allergy. Monitor your symptoms.")
        elif cough_duration == "1-2 weeks":
            st.write("If your cough has persisted for 1-2 weeks, it's advisable to consult a doctor.")
        elif cough_duration == "More than 2 weeks":
            st.write("A cough lasting more than 2 weeks should be evaluated by a healthcare provider.")

    if "Shortness of breath" in selected_symptoms:
        breath_severity = st.selectbox("How severe is your shortness of breath?", ["Mild", "Moderate", "Severe"])
        breath_duration = st.selectbox("How long have you been experiencing this?", ["Less than a week", "1-2 weeks", "More than 2 weeks"])
        
        if breath_severity == "Mild":
            st.write("Mild shortness of breath can often be managed with lifestyle changes. Discuss this with your healthcare provider.")
        elif breath_severity == "Moderate":
            st.write("Moderate shortness of breath may require **oxygen therapy**. Consult your doctor for evaluation.")
        elif breath_severity == "Severe":
            st.write("Severe shortness of breath is a medical emergency. Seek immediate medical attention.")
        
        if breath_duration == "Less than a week":
            st.write("Shortness of breath lasting less than a week could be due to a recent illness. Monitor your symptoms.")
        elif breath_duration == "1-2 weeks":
            st.write("If you've had shortness of breath for 1-2 weeks, it's important to get evaluated.")
        elif breath_duration == "More than 2 weeks":
            st.write("Persistent shortness of breath for more than 2 weeks should prompt a visit to your healthcare provider.")

    if "Chest pain" in selected_symptoms:
        chest_pain_degree = st.selectbox("How would you describe your chest pain?", ["Mild", "Moderate", "Severe"])
        chest_pain_duration = st.selectbox("How long have you been experiencing this?", ["Less than a week", "1-2 weeks", "More than 2 weeks"])
        
        if chest_pain_degree == "Mild":
            st.write("For mild chest pain, consider **Ibuprofen** or **Acetaminophen** for relief.")
        elif chest_pain_degree == "Moderate":
            st.write("Moderate chest pain may require stronger medications. Consult your healthcare provider.")
        elif chest_pain_degree == "Severe":
            st.write("Severe chest pain is serious. Seek immediate medical help.")
        
        if chest_pain_duration == "Less than a week":
            st.write("Mild chest pain lasting less than a week may not be serious, but monitor closely.")
        elif chest_pain_duration == "1-2 weeks":
            st.write("Chest pain lasting 1-2 weeks should be evaluated by a doctor.")
        elif chest_pain_duration == "More than 2 weeks":
            st.write("Persistent chest pain for more than 2 weeks warrants immediate medical attention.")

    if "Fatigue" in selected_symptoms:
        fatigue_severity = st.selectbox("How severe is your fatigue?", ["Mild", "Moderate", "Severe"])
        fatigue_duration = st.selectbox("How long have you been experiencing this?", ["Less than a week", "1-2 weeks", "More than 2 weeks"])
        
        if fatigue_severity == "Mild":
            st.write("Mild fatigue can often be managed with rest and proper nutrition.")
        elif fatigue_severity == "Moderate":
            st.write("Moderate fatigue may require lifestyle changes and possibly a consultation with a healthcare provider.")
        elif fatigue_severity == "Severe":
            st.write("Severe fatigue should be evaluated by a doctor to rule out underlying conditions.")
        
        if fatigue_duration == "Less than a week":
            st.write("Fatigue lasting less than a week may be due to temporary factors like stress or lack of sleep.")
        elif fatigue_duration == "1-2 weeks":
            st.write("Fatigue lasting 1-2 weeks should prompt a medical evaluation.")
        elif fatigue_duration == "More than 2 weeks":
            st.write("Persistent fatigue for more than 2 weeks is concerning and requires medical attention.")

    if "Weight loss" in selected_symptoms:
        weight_loss_severity = st.selectbox("How significant is your weight loss?", ["Mild", "Moderate", "Severe"])
        weight_loss_duration = st.selectbox("How long have you been experiencing this?", ["Less than a week", "1-2 weeks", "More than 2 weeks"])
        
        if weight_loss_severity == "Mild":
            st.write("Mild weight loss may not be concerning, but keep an eye on it.")
        elif weight_loss_severity == "Moderate":
            st.write("Moderate weight loss should be discussed with your healthcare provider for further evaluation.")
        elif weight_loss_severity == "Severe":
            st.write("Severe weight loss is a serious symptom. Seek immediate medical attention.")
        
        if weight_loss_duration == "Less than a week":
            st.write("Weight loss lasting less than a week may be temporary, but monitor your intake.")
        elif weight_loss_duration == "1-2 weeks":
            st.write("Weight loss lasting 1-2 weeks warrants a medical evaluation.")
        elif weight_loss_duration == "More than 2 weeks":
            st.write("Persistent weight loss for more than 2 weeks is concerning and should be assessed by a doctor.")

    if "Wheezing" in selected_symptoms:
        wheezing_type = st.selectbox("What type of wheezing are you experiencing?", ["Dry", "Moist", "Intermittent", "Persistent"])
        wheezing_duration = st.selectbox("How long have you been experiencing this?", ["Less than a week", "1-2 weeks", "More than 2 weeks"])
        
        if wheezing_type == "Dry":
            st.write("For dry wheezing, an **Albuterol Inhaler** may help. Consult your doctor.")
        elif wheezing_type == "Moist":
            st.write("Moist wheezing could indicate fluid in the lungs. Discuss this with a healthcare provider.")
        elif wheezing_type == "Intermittent":
            st.write("Intermittent wheezing can often be managed with a rescue inhaler. Talk to your doctor.")
        elif wheezing_type == "Persistent":
            st.write("Persistent wheezing should be evaluated to determine a long-term management plan.")

        if wheezing_duration == "Less than a week":
            st.write("Wheezing lasting less than a week may be due to allergies or a recent illness. Monitor your symptoms.")
        elif wheezing_duration == "1-2 weeks":
            st.write("Wheezing lasting 1-2 weeks should be evaluated by your healthcare provider.")
        elif wheezing_duration == "More than 2 weeks":
            st.write("Persistent wheezing for more than 2 weeks needs further investigation by a doctor.")

    if "Coughing up blood" in selected_symptoms:
        st.write("Coughing up blood is a serious symptom. Please seek immediate medical attention.")
