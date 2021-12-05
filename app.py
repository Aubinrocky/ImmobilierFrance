import streamlit as st
from multiapp import MultiApp
from apps import appNantes  # ,appReims,......  # import your app modules here

app = MultiApp()

st.markdown("""
# Multi-Page App
This multi-page app is using the [streamlit-multiapps](https://github.com/upraneelnihar/streamlit-multiapps) framework developed by [Praneel Nihar](https://medium.com/@u.praneel.nihar). Also check out his [Medium article](https://medium.com/@u.praneel.nihar/building-multi-page-web-app-using-streamlit-7a40d55fa5b4).
""")

# Add all your application here
app.add_app("Nantes", appNantes.app)
# app.add_app("Reims", appReims.app)
# app.add_app("Accueil", appAccueil.app)
# The main app
app.run()
