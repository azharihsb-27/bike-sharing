import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
sns.set(style='dark')

def create_byyear(df):
  byyear_df = df.groupby("yr").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
  })

  return byyear_df

def create_byseason(df):
  byseason_df = df.groupby("season").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
  })

  return byseason_df

def create_byweekday(df):
  byweekday_df = df.groupby("weekday").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
  }).reset_index()

  return byweekday_df

def create_byhour(df):
  byhour_df = df.groupby("hr").agg({
    "casual": "sum",
    "registered": "sum",
    "cnt": "sum"
  })

  return byhour_df

clear_hour_df = pd.read_csv("clear_hour_df.csv")
clear_hour_df.sort_values(by="dteday", inplace=True)
clear_hour_df.reset_index(inplace=True)
clear_hour_df["dteday"] = pd.to_datetime(clear_hour_df["dteday"])

min_date = clear_hour_df["dteday"].min()
max_date = clear_hour_df["dteday"].max()

with st.sidebar:
  start_date, end_date = st.date_input(
    label="Date Range", 
    min_value=min_date, 
    max_value=max_date, 
    value=[min_date, max_date]
  )

main_df = clear_hour_df[(clear_hour_df["dteday"] >= str(start_date)) & (clear_hour_df["dteday"] <= str(end_date))]


byyear_df = create_byyear(main_df)
byseason_df = create_byseason(main_df)
byweekday_df = create_byweekday(main_df)
byhour_df = create_byhour(main_df)

st.header("Bike Sharing Dashboard :sparkles:")

st.subheader("Hourly Rentals")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
  data=byhour_df,
  x="hr",
  y="cnt",
  ax=ax
)
ax.set_title("Total Hourly Rentals", loc="center", fontsize=50)
ax.set_ylabel("Total Rentals", fontsize=36)
ax.set_xlabel("Hour", fontsize=36)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

st.subheader("Daily Rentals")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
  data=byweekday_df,
  x="weekday",
  y="cnt",
  ax=ax
)
ax.set_title("Total Daily Rentals", loc="center", fontsize=50)
ax.set_ylabel("Total Rentals", fontsize=36)
ax.set_xlabel("Day", fontsize=36)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

st.subheader("Seasonly Rentals")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
  data=byseason_df,
  x="season",
  y="cnt",
  ax=ax
)
ax.set_title("Total Seasonly Rentals", loc="center", fontsize=50)
ax.set_ylabel("Total Rentals", fontsize=36)
ax.set_xlabel("Season", fontsize=36)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)

st.subheader("Yearly Rentals")
fig, ax = plt.subplots(figsize=(20, 10))
sns.barplot(
  data=byyear_df,
  x="yr",
  y="cnt",
  ax=ax
)
ax.set_title("Total Yearly Rentals", loc="center", fontsize=50)
ax.set_ylabel("Total Rentals", fontsize=36)
ax.set_xlabel("Year", fontsize=36)
ax.tick_params(axis='x', labelsize=35)
ax.tick_params(axis='y', labelsize=30)
st.pyplot(fig)
