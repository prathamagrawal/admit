import joblib
import streamlit as st
import pandas


def pred(gre,toefl,univ,SOP,LOR,CGPA,research,sports,certificate):
    d = {"GRE Score": gre, "TOEFL Score": toefl, 'University Rating': univ, "SOP": SOP, "LOR": LOR, "CGPA": CGPA,
         "Research": research, 'sports': sports, 'certifications': certificate}
    x_test = pandas.DataFrame(d, index=[0])

    import pickle

    loaded_model = pickle.load(open('model.sav', 'rb'))
    result = loaded_model.predict(x_test)
    joblib.dump(loaded_model, 'finalized_model.sav')
    return result



def main():
    st.title('College Prediction!')
    st.subheader("Predict your chances of Admittance for a US college.")

    st.subheader("GRE score: ")
    gre = st.text_input("Enter your GRE score: ", 0)

    st.subheader("TOEFL score: ")
    toefl = st.text_input("Enter your TOEFL Score", 0)

    st.subheader("Which level of University you want: ")
    st.text('1 - being the Highest and 5 being the lowest!')
    univ = int(st.selectbox("Enter University Rankings", (1,2,3,4,5)))

    st.subheader("SOP Score: ")
    st.text("Out of 5.")
    SOP = float(st.text_input("Enter your SOP Score", 0))

    st.subheader("LOR score: ")
    st.text('Rate it yourself, based on the activities and diversification. ')
    LOR = float(st.text_input("Enter your LOR Score", 0))

    st.subheader("CGPA: ")
    st.text("Enter the CGPA out of 10.")
    CGPA = float(st.text_input("Enter your CGPA", 0))

    st.subheader("Research Work:")
    research = st.selectbox('CLick yes, if you have research experience and have one publication, otherwise No.',('No', 'Yes'),)
    if (research=='Yes'):
        research=1
    else:
        research=0

    st.subheader('Sports: ')
    st.text('Select the option that best matches your No. of Wins in sports Competition.')
    sports=st.selectbox("Choose from the below options.",('0','0-5','5-10','10-15','15+'))
    if (sports=='0'):
        sports=0
    elif (sports=='0-5'):
        sports=1
    elif (sports=='5-10'):
        sports=2
    elif (sports=='10-15'):
        sports=3
    else:
        sports=4

    st.subheader('Certifications: ')
    st.text('Select the option that best matches your No. of Certifications you possess: ')
    certificate =st.selectbox("Choose from the below options.",('0','0-10','10-15','15-20','20+'))
    if (certificate=='0'):
        certificate=0
    elif (certificate=='0-10'):
        certificate=1
    elif (certificate=='10-15'):
        certificate=2
    elif (certificate=='15-20'):
        certificate=3
    else:
        certificate=4

    if (gre==0) and (toefl==0):
        result1=0
        flag1=1
        print('Wrong')
    else:
        flag1=0

    if(st.button('Result')):
        st.subheader('Your Chances of Admit are: ')
        result=pred(gre,toefl,univ,SOP,LOR,CGPA,research,sports,certificate)
        st.title((result[0]*100))

if __name__ == '__main__':
    main()
