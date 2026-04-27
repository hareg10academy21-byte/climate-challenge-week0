import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ----------------------------
# Load datasets
# ----------------------------
ethiopia = pd.read_csv("data/ethiopia_clean.csv")
kenya = pd.read_csv("data/kenya_clean.csv")
sudan = pd.read_csv("data/sudan_clean.csv")
tanzania = pd.read_csv("data/tanzania_clean.csv")
nigeria = pd.read_csv("data/nigeria_clean.csv")

df = pd.concat([
    ethiopia,
    kenya,
    sudan,
    tanzania,
    nigeria
], ignore_index=True)

# ----------------------------
# Streamlit Title
# ----------------------------
st.title("COP32 African Climate Risk Dashboard")

st.write("""
This dashboard compares climate trends across:
- Ethiopia
- Kenya
- Sudan
- Tanzania
- Nigeria
""")
st.info("""
Purpose:
This dashboard helps Ethiopia analyze regional climate risks before COP32.
Users can compare temperature trends, rainfall variability, and climate patterns
across five African countries to support data-driven climate policy decisions.
""")
# ----------------------------
# Sidebar filters
# ----------------------------
countries = st.sidebar.multiselect(
    "Select Countries",
    df["Country"].unique(),
    default=df["Country"].unique()
)

year_range = st.sidebar.slider(
    "Select Year Range",
    int(df["YEAR"].min()),
    int(df["YEAR"].max()),
    (int(df["YEAR"].min()), int(df["YEAR"].max()))
)

variable = st.sidebar.selectbox(
    "Select Variable",
    ["T2M", "PRECTOTCORR", "RH2M"]
)
st.sidebar.markdown("""
### How to Use
- Select one or multiple countries
- Choose a year range
- Select climate variable
- Explore trends and compare risks
""")
# ----------------------------
# Filter dataset
# ----------------------------
filtered_df = df[
    (df["Country"].isin(countries)) &
    (df["YEAR"] >= year_range[0]) &
    (df["YEAR"] <= year_range[1])
]

# ----------------------------
# Temperature Trend Chart
# ----------------------------
st.subheader("Monthly Climate Trend")

monthly_data = filtered_df.groupby(
    ["Country", "Month"]
)[variable].mean().reset_index()

fig, ax = plt.subplots(figsize=(10,5))

sns.lineplot(
    data=monthly_data,
    x="Month",
    y=variable,
    hue="Country",
    marker="o",
    ax=ax
)






ax.set_title(f"Monthly {variable} Trend")
ax.grid(True)










st.pyplot(fig)
st.markdown("""
**Insight:**  
This chart shows monthly climate trends across selected countries.

- Higher temperature trends may indicate heat stress  
- Higher rainfall trends may indicate flood risk  
- Humidity trends help understand moisture changes  

This supports identifying climate change patterns across Africa.
""")
# ----------------------------
# Precipitation Boxplot
# ----------------------------
st.subheader("Precipitation Distribution")

fig2, ax2 = plt.subplots(figsize=(10,5))

sns.boxplot(
    data=filtered_df,
    x="Country",
    y="PRECTOTCORR",
    ax=ax2
)




ax2.set_title("Rainfall Distribution Across Countries")





st.pyplot(fig2)
st.markdown("""
**Insight:**  
This boxplot compares rainfall variability across countries.

- Wider boxes = more rainfall variability  
- More outliers = extreme rainfall events  
- Lower rainfall distribution = drought risk  

This helps identify countries facing unstable rainfall conditions.
""")
# ----------------------------
# Raw Data
# ----------------------------
st.markdown("""
The table below shows filtered climate records based on your selected countries,
years, and climate variable.
""")
st.subheader("Filtered Dataset Preview")
st.dataframe(filtered_df.head())