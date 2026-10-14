import pandas as p
import numpy as n
import streamlit as st
import plotly.express as px
from io import BytesIO
st.set_page_config(page_title="Subho Sarodiya",page_icon="🌺",layout="wide")
d = {
    "Year": [1610, 1757, 1790, 1910, 1932, 2021, 2021],
    "Event": [
        "Barisha Sabarna Roy Choudhury Puja",
        "Durga Puja associated with Bengal's colonial-era elite",
        "Community Puja traditions develop",
        "Sarbojanin Puja movement",
        "Women participate in public Puja celebrations",
        "UNESCO inscription",
        "Kolkata Durga Puja"
    ],
    "Category": [
        "Traditional", "Historical context",
        "Community", "Community",
        "Social change", "Recognition",
        "Cultural heritage"
    ],
    "Description": [
        "The Sabarna Roy Choudhury family traces its Puja tradition to 1610.",
        "Durga Puja grew in prominence among Bengal's elite.",
        "Community-organized Puja traditions emerged around this period.",
        "Public, community-based celebrations expanded in Bengal.",
        "Women's participation in public celebrations increased over time.",
        "Durga Puja in Kolkata was inscribed on UNESCO's heritage list.",
        "Kolkata Durga Puja was recognized as intangible cultural heritage."
    ]
}
data=p.DataFrame(d)
st.title("🌺 Subho Sarodiya 🌺 ")
st.subheader("Explore The History Of Durga Puja")
st.write(
     "A beginner-friendly historical data analytics project "
    "exploring Durga Puja's cultural journey."
)
st.info(
     "Historical note: Dates and descriptions represent selected "
    "milestones, not a complete or universally agreed timeline."
)
st.sidebar.header("Dashboard Filters..")
start_year=st.sidebar.slider("Select Starting Year",min_value=1610,max_value=2021,value=1610)
filtered=data[data["Year"]>=start_year]
c1,c2,c3=st.columns(3)
c1.metric("Historial Records",len(filtered))
c2.metric("First Shown Year",filtered["Year"].min())
c3.metric(
    "UNESCO Recognition",
    "2021",
    help="Durga Puja in Kolkata was inscribed in 2021."
)
st.divider()
st.subheader("Historical Timeline")
timeline=filtered.groupby("Year").size().reset_index(name="Number Of Records")
f1=px.line(timeline,x="Year",y="Number Of Records",markers=True,title="📈 Recorded Historical Milestones By Year 📈")
st.plotly_chart(f1,use_container_width=True)
st.subheader("Important Historical Events")
f2=px.bar(filtered,x="Year",y="Event",color="Category",hover_data=["Description"],title="Selected Durga Puja Milestones")
st.plotly_chart(f2,use_container_width=True)
st.subheader("Cultural and Historical Categories")
category_data=filtered["Category"].value_counts().reset_index()
category_data.columns=["Category","Records"]
f3=px.pie(category_data,names="Category",values="Records",title="🥁 Historial Records By Category 🥁",hole=0.4)
st.plotly_chart(f3,use_container_width=True)
st.subheader("📚 Explore Historical Records")
st.dataframe(filtered)
st.subheader("💡 Data Analyst's Insight")
if not filtered.empty:
    large=filtered["Year"].max()
    st.write(
        f"The selected dataset contains {len(filtered)} historial records. The latest recorded milestone is form {large} . Use the table to explore individual events . "
             )
st.warning( "The charts summarize the records entered in this project. "
    "They do not measure actual Puja attendance, economic growth, "
    "or the number of celebrations.")
csv_file=filtered.to_csv(index=False).encode("utf-8")
st.download_button("📥 Download Historical Data CSV File📥",
                   data=csv_file,
                   file_name="Durga_Pujo_Historial_Data.csv",
                   mime="text/csv")
excel=BytesIO()
with p.ExcelWriter(excel,engine="openpyxl")as writer:
    (filtered.to_excel(writer,index=False,sheet_name="Durga Puja History"))
st.download_button("📥 Download Historial Data Excel File 📥",
                   data=excel.getvalue(),
                   file_name="Durha_Puja_Historial_Data.xlsx"
                   )
st.divider()
st.caption("🌺 Subho Sarodiya | Durga Puja History Analytics Project")