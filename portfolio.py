import streamlit as st

# Portfolio Title
st.title("👨‍💻 My Data Engineering Portfolio")

# About Section
st.header("About Me")
st.write("I'm a data engineer passionate about building scalable pipelines and working with big data.")

# Project Showcase
st.header("Projects")

st.subheader("1. Real-time Stock Market Data Pipeline")
st.write("Built a real-time data pipeline using Kafka, Spark, and PostgreSQL.")
st.markdown("[🔗 GitHub Repo](https://github.com/yourusername/stock-pipeline)")

st.subheader("2. ETL Pipeline for Public COVID-19 Data")
st.write("Automated ETL pipeline using Airflow to extract and process COVID-19 data.")
st.markdown("[🔗 GitHub Repo](https://github.com/yourusername/covid-etl)")

st.subheader("3. Twitter Sentiment Analysis")
st.write("Streamed and analyzed tweets in real-time using PySpark and MongoDB.")
st.markdown("[🔗 GitHub Repo](https://github.com/yourusername/twitter-sentiment)")

# Contact Information
st.header("📬 Contact")
st.write("Reach out to me via [LinkedIn](https://www.linkedin.com/in/yourprofile).")

