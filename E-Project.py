import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Dashboard by Rabia Zaheer",
    layout="wide"
)
st.title("📊E-Commerce Sales Insights Dashboard")


df = pd.read_excel(
    "ecommerce_dataset.xlsx",
    sheet_name="sheet1"
    )

#filters
st.sidebar.header("Dashboard Filters")

#filter by date
date = sorted(df["Date"].unique())
select_date = st.sidebar.multiselect(
    "Select Date",
    date,
    default=date
)

#filter by Category
category =df["Category"].unique()
select_category= st.sidebar.multiselect(
    "Select Category",
    category,
    default=category
)

#filter by city
city = df["City"].unique()
select_city= st.sidebar.multiselect(
    "Select City",
    city,
    default=city
)

# Filter dataset

filtered_df= df[
    (df["Date"].isin(select_date))&
    (df["Category"].isin(select_category))&
    (df["City"].isin(select_city))
]

#show
st.subheader("Filtered Dataset")
st.dataframe(filtered_df)

#kpi 
revenue= filtered_df["Total"].sum()
ordertotal= filtered_df["Order_ID"].count()

#kpi columns
col1,col2= st.columns(2)
col1.metric("Total Revenue",revenue)
col2.metric("Total Orders",ordertotal)

row1_col1, row1_col2 = st.columns(2)

#sale by city
with row1_col1:   #bar
    st.subheader("Sales by City")
    sale=(filtered_df.groupby("City")["Total"].sum())

    fig1,ax1=plt.subplots(figsize= (6,5))

    sale.plot(
    kind="bar",
    ax=ax1,
    color="cyan")
    fig1.tight_layout()
    st.pyplot(fig1)

#sale by category
with row1_col2:   #pie
    st.subheader("Sales by Category")
    profit= (filtered_df.groupby("Category")["Total"].sum())

    fig2,ax2= plt.subplots(figsize=(3.7,3.7))

    profit.plot(
        kind="pie",
        autopct= "%1.1f%%",
        ax= ax2,
    )
    fig2.tight_layout()
    st.pyplot(fig2)


row2_col1, row2_col2 = st.columns(2)

#payment method distribution
with row2_col1:  #donut
    st.subheader("Payment Method Distribution")
    sale=(filtered_df.groupby("Payment")["Total"].sum())

    fig3,ax3=plt.subplots(figsize= (2.7,2.7))
    sale.plot(
    kind="pie",
    autopct="%1.1f%%",
    ax=ax3,
    pctdistance=0.75)

    centre_circle = plt.Circle((0,0),0.50,fc='white')
    ax3.add_artist(centre_circle)
    
    fig3.tight_layout()
    st.pyplot(fig3)

#Top-Selling Products
with row2_col2:    #bar
    st.subheader("Top 5 Selling Products")
    sale=(filtered_df.groupby("Product")["Total"].sum()).sort_values(ascending=False).head(5)

    fig4,ax4=plt.subplots(figsize= (7,6.5))

    sale.plot(
    kind="bar",
    ax=ax4,
    color="red")
    fig4.tight_layout()
    st.pyplot(fig4)

st.success("Interactive Dashboard Created Successfully By Rabia Zaheer...")