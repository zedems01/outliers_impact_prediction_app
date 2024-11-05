import streamlit as st
import pickle
import pandas as pd

# model = pickle.load(open("../data/regmodel.pkl", 'rb'))
# scaler = pickle.load(open('../data/stdscaler.pkl', 'rb'))
with open('CatBoostRegressor.pkl', 'rb') as f:
    best_model = pickle.load(f)

# Title
st.set_page_config(page_title="California House Price Prediction", page_icon="🏠")
st.markdown("<h1 style='text-align: center; color: #2C3E50;'>House Price Prediction</h1>", unsafe_allow_html=True)
st.write("## Enter the following details to predict the house price:")


# Inputs
with st.container():
    st.markdown("<div style='background-color: #f9f9f9; padding: 10px; border-radius: 8px;'>", unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        feature1 = st.slider("Median Income (x100k)", min_value=0.0, max_value=20.0, step=0.1, value=5.0)
        feature3 = st.slider("Average Rooms", min_value=1.0, max_value=20.0, step=0.1, value=5.0)
        feature5 = st.slider("Population", min_value=0, max_value=50000, step=100, value=25000)
        feature7 = st.slider("Latitude", min_value=32.0, max_value=42.0, step=0.1, value=36.5)

    with col2:
        feature2 = st.slider("Median House Age", min_value=0.0, max_value=100.0, step=1.0, value=20.0)
        feature4 = st.slider("Average Bedrooms", min_value=1.0, max_value=10.0, step=0.1, value=3.0)
        feature6 = st.slider("Average Occupants", min_value=1.0, max_value=10.0, step=0.1, value=3.5)
        feature8 = st.slider("Longitude", min_value=-124.0, max_value=-114.0, step=0.1, value=-118.0)

    st.markdown("</div>", unsafe_allow_html=True)

st.write(" ")
predict_button = st.button("💡 Predict House Price")

# Show prediction
if predict_button:
    columns = ['MedInc', 'HouseAge', 'AveRooms', 'AveBedrms', 'Population', 'AveOccup', 'Latitude', 'Longitude']
    data = [[feature1, feature2, feature3, feature4, feature5, feature6, feature7, feature8]]
    input_data = pd.DataFrame(data, columns=columns)
    # scaled_data = scaler.transform(input_data)
    prediction = best_model.predict(input_data)
    
    st.markdown(f"<div style='background-color: #f9f9f9; color: white; padding: 10px; border-radius: 8px; text-align: center;'>"
            f"<h3>🏠 Predicted Median House Price: ${round(prediction[0]*100)}k</h3></div>", unsafe_allow_html=True)



footer = """
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
<style>
footer {
    position: fixed;
    left: 0;
    bottom: 0;
    width: 100%;
    background-color: #2C3E50;
    color: white;
    text-align: center;
    padding: 10px 0;
    font-size: 14px;
}
footer .footer-content {
    display: flex;
    justify-content: center;
    align-items: center;
    gap: 15px;
}
footer a {
    color: white;
    text-decoration: none;
    font-size: 18px;
}
footer a:hover {
    color: #18BC9C;
}
</style>
<footer>
        <p>&copy; 2024 Achille Nguessie</p>
        <div class="icon-links">
            <a href="https://github.com/zedems01" target="_blank"><i class="fab fa-github">&nbsp&nbsp&nbsp&nbsp</i></a> 
            <a href="https://linkedin.com/in/achille-nguessie-419614230" target="_blank"><i class="fab fa-linkedin">&nbsp&nbsp&nbsp&nbsp</i></a>
            <a href="tel:+33629736246" target="_blank"><i class="fas fa-phone">&nbsp&nbsp&nbsp&nbsp</i></a>
            <a href="mailto:nguessiek@gmail.com" target="_blank"><i class="fas fa-envelope">&nbsp&nbsp&nbsp&nbsp</i></a>
        </div>
    </footer>
"""

st.markdown(footer, unsafe_allow_html=True)