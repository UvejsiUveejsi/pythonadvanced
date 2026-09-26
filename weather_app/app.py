import streamlit as st
import pandas as pd


st.set_page_config(
    page_title="Weather App",
    layout="wide"
)


st.title(" Weather App")
st.write("Monthly Average Temperature Calculator")


data = pd.read_csv("weather_data.csv")


data["date"] = pd.to_datetime(data["date"])


data["month"] = data["date"].dt.month


month_names = {
    1: "January",
    2: "February",
    3: "March",
    4: "April",
    5: "May",
    6: "June",
    7: "July",
    8: "August",
    9: "September",
    10: "October",
    11: "November",
    12: "December"
}


monthly_average = (
    data.groupby("month")["temperature"]
    .mean()
    .reset_index()
)

monthly_average["month"] = monthly_average["month"].map(month_names)


st.subheader("📊 Monthly Average Temperatures")

st.dataframe(
    monthly_average,
    use_container_width=True
)

hottest_days = (
    data.sort_values("temperature", ascending=False)
    .head(5)
)

coldest_days = (
    data.sort_values("temperature", ascending=True)
    .head(5)
)

st.subheader(" 5 Hottest Days")

st.dataframe(
    hottest_days[["date", "temperature"]],
    use_container_width=True
)


st.subheader(" 5 Coldest Days")

st.dataframe(
    coldest_days[["date", "temperature"]],
    use_container_width=True
)



