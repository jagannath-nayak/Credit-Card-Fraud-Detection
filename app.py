import streamlit as st
import pickle
import pandas as pd
import sklearn

# Load trained model
pickle_in = open("classifier.pkl", 'rb')
classifier = pickle.load(pickle_in)

# Simulated columns from X_train (replace with actual order if needed)
feature_columns = ['id', 'V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V8', 'V9', 'V10', 'V11', 'V12', 'V13', 'V14', 'V15', 'V16', 'V17', 'V18',
                   'V19', 'V20', 'V21', 'V22', 'V23', 'V24', 'V25', 'V26', 'V27', 'V28', 'Amount', 'Time', 'Time_Interval' ]

# Use only the 15 fields you are collecting
input_fields = ['V1', 'V2', 'V3', 'V4', 'V5', 'V6', 'V7', 'V9', 'V10', 'V11', 'V12', 'V14', 'V16', 'V17', 'V18']

def predict_cc_fraud(user_inputs):
    # Create dataframe from user input
    input_data = pd.DataFrame([user_inputs], columns=input_fields)

    # Fill missing columns with zeros to match model's expected input
    for col in feature_columns:
        if col not in input_data.columns:
            input_data[col] = 0

    # Reorder columns to match the training data
    input_data = input_data[feature_columns]

    # Predict
    prediction = classifier.predict(input_data)
    return prediction


def main():
    st.title('Credit Card Detection')
    st.divider()
    st.subheader('Model for Prediction', divider='rainbow')

    user_inputs = []
    for field in input_fields:
        val = st.text_input(f"Input {field}:", "Type Here")
        try:
            val = float(val)
        except ValueError:
            st.warning(f"Please enter a valid number for {field}")
            return
        user_inputs.append(val)

    result = ''
    if st.button("Predict"):
        result = predict_cc_fraud(user_inputs)
        if result == [0]:
            st.text('This is NOT a Fraud')
        else:
            st.text('This is a Fraud')

    st.success(f"The Prediction is {result}")
    st.divider()

if __name__ == '__main__':
    main()
