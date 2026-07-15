# 🐍 E-Commerce Sales Insights - Python Dashboard

![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)

An interactive, live sales dashboard built using **Streamlit**, **Pandas**, and **Matplotlib**. This web application provides business stakeholder insights, dynamically tracking key performance indicators (KPIs), regional sales distribution, and top-selling products.

---

## 📈 Key Business Insights (Based on 300 Orders)

After cleaning and exploring the underlying dataset, here are the major business takeaways:

*   **Total Performance:** The store generated a total of **2,347,955 PKR** in revenue across **300 total transactions**.
*   **Top Regional Market:** **Multan** is the highest-grossing city, bringing in **628,595 PKR**, followed closely by Faisalabad (533,135 PKR).
*   **Dominant Product Category:** **Clothing** is the clear winner, accounting for **997,540 PKR** (nearly 42% of total revenue).
*   **Star Products:** **Jackets** and **Sneakers** are the top-grossing individual products, generating 577,000 PKR and 558,900 PKR respectively.
*   **Payment Preferences:** Cash on Delivery (COD) remains the most popular payment method (862,320 PKR), though Cards and Digital Wallets follow closely behind.

---

## 🖥️ Dashboard Preview

<img width="892" height="401" alt="python-dashboard1" src="https://github.com/user-attachments/assets/0ae64c5d-309f-4b3d-98d0-e88961d56c9c" />
<img width="897" height="394" alt="python-dashboard2" src="https://github.com/user-attachments/assets/c88fb255-3a43-4a8c-a602-c2542ff4dcc1" />
<img width="900" height="397" alt="python-dashboard3" src="https://github.com/user-attachments/assets/328ce754-4dbb-4b17-b9c9-f9363c462c2b" />


---

## ⚙️ Application Features
*   **Dynamic KPIs:** Real-time updates for Total Revenue and Order Count.
*   **Multi-select Sidebar Filters:** Easily drill down by Date, Category, and City.
*   **Data Visualizations:** 
    *   Bar chart highlighting **Sales by City**.
    *   Pie chart mapping **Sales by Category**.
    *   Donut chart illustrating **Payment Method Distribution**.
    *   Bar chart displaying the **Top 5 Selling Products**.

---

## 🚀 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/rz-rabiaZ/E-Commerce-Sales-Python-Dashboard.git](https://github.com/rz-rabiaZ/E-Commerce-Sales-Python-Dashboard.git)
    cd E-Commerce-Sales-Python-Dashboard
    ```
2.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Streamlit application:**
    ```bash
    streamlit run E-Project_2.py
    ```
