# 🌺 Subho Sarodiya  — Durga Puja History Analytics Dashboard

**Explore the history and cultural heritage of Durga Puja through data analytics.**

Subho Sarodiya 360° is a beginner-friendly data analytics project built using Python, Pandas, Plotly, and Streamlit. It explores selected historical milestones associated with Durga Puja through an interactive dashboard with charts, historical records, filters, and downloadable data.

The project demonstrates how Python can transform structured historical information into meaningful visual insights.

## 🎯 Project Objectives

- Explore selected historical milestones of Durga Puja.
- Organize historical information using Pandas.
- Build interactive charts using Plotly Express.
- Develop a web-based dashboard using Streamlit.
- Filter historical records by year.
- Present data insights through KPI cards and visualizations.
- Download filtered historical data as a CSV file.

## ✨ Key Features

- **Interactive Dashboard:** Simple and beginner-friendly interface.
- **Historical Timeline:** Visualize the distribution of recorded milestones by year.
- **Historical Events Chart:** Explore selected events by year and category.
- **Cultural Categories:** View the distribution of records using a doughnut chart.
- **KPI Cards:** Display the number of filtered records, earliest year shown, and UNESCO recognition year.
- **Year Filter:** Select a starting year to explore historical records.
- **Historical Data Table:** Inspect event names, categories, and descriptions.
- **Data Download:** Export filtered records as a CSV file.

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Programming language |
| Pandas | Data organization and analysis |
| Plotly Express | Interactive data visualizations |
| Streamlit | Interactive dashboard development |
| CSV | Data export format |
| Git and GitHub | Version control and project hosting |

## 📊 Dashboard Visualizations

### 1. Historical Timeline
Displays the number of records associated with each year in the selected dataset.

### 2. Historical Events Bar Chart
Compares selected historical milestones and displays additional descriptions on hover.

### 3. Cultural and Historical Categories
Shows how the available records are distributed across categories such as traditional practices, community celebrations, social change, and cultural recognition.

### 4. Historical Records Table
Provides an interactive view of the underlying dataset.

### 5. KPI Cards
Summarizes the currently filtered records and highlights the year of UNESCO recognition.

> **Note:** These visualizations summarize the records included in the project. They do not represent measured attendance, economic growth, the total number of Puja celebrations, or the complete historical development of Durga Puja.

## 📁 Project Structure

```text
Durga-Puja-History-Analysis/
│
├── Dashboard.py
├── Durga_Puja_Historical_Data.csv
├── Durga_Puja_Historial_Data.xlsx
├── requirements.txt
└── README.md
```

- `app.py` — Contains the dataset, data filtering, visualizations, and dashboard code.
- `requirements.txt` — Lists the Python libraries required to run the project.
- `README.md` — Documents the project and explains how to use it.

## ⚙️ Installation and Setup

### Step 1: Clone the Repository

Replace `YOUR_USERNAME` with your GitHub username.

```bash
git clone https://github.com/YOUR_USERNAME/Subho-Sarodiya-360.git
```

### Step 2: Open the Project Folder

```bash
cd Subho-Sarodiya-360
```

### Step 3: Install Dependencies

```bash
python -m pip install -r requirements.txt
```

If you have not created `requirements.txt`, add the following:

```text
streamlit
pandas
plotly
```

### Step 4: Run the Dashboard

```bash
streamlit run app.py
```

The dashboard will open in your default web browser.

## 📚 Data Description

The project uses a small historical dataset created directly in Python.

| Column | Description |
|---|---|
| `Year` | Year associated with a selected milestone |
| `Event` | Name or summary of the historical event |
| `Category` | Classification of the event |
| `Description` | Brief explanation of the record |

The dataset contains illustrative descriptions of selected historical milestones. The dates and claims should be verified against reliable historical sources before the project is used for formal research or publication.

## 🧠 Data Analytics Concepts Practiced

This project provides hands-on practice with:

- Creating a Pandas DataFrame.
- Selecting columns and filtering rows.
- Using `groupby()` and `size()`.
- Counting categorical values with `value_counts()`.
- Calculating minimum and maximum values.
- Building interactive line, bar, and doughnut charts.
- Creating KPI cards and sidebar filters.
- Exporting data to CSV format.
- Communicating analytical findings responsibly.

## 🌍 Real-World Applications

The techniques demonstrated in this project can also be applied to:

- Historical event analysis.
- Cultural heritage documentation.
- Museum and archive dashboards.
- Festival research and documentation.
- Educational data visualization.
- Historical record exploration.

These are potential applications of the techniques, not outcomes measured by the current dataset.

## 🔍 Limitations and Future Improvements

The current version is a beginner-level demonstration using a small, predefined dataset. It does not yet contain a complete historical timeline or source verification for every record.

Future improvements may include:

- Adding verified historical sources and reference links.
- Expanding the dataset with documented historical milestones.
- Distinguishing verified facts from traditional accounts.
- Adding year-range and category filters.
- Including historical periods and geographical context.
- Improving chart labels and analytical summaries.
- Deploying the dashboard using Streamlit Community Cloud.

## 🙏 Cultural Significance

Durga Puja is an important cultural and religious festival celebrated with great enthusiasm in West Bengal and other regions. Kolkata's Durga Puja was inscribed on UNESCO's Representative List of the Intangible Cultural Heritage of Humanity in **2021**.

This project aims to encourage exploration of Durga Puja's history and cultural heritage through beginner-friendly data analytics.

For historical verification, consult [UNESCO's official website](https://ich.unesco.org/).

## 👨‍💻 Author

**Keya Karmakar**

BCA Student | Aspiring Data Analyst

Interested in Python, data analytics, data visualization, and solving real-world problems through data.

## ⭐ Support

If you find this project useful for learning Python, Pandas, Plotly, or Streamlit, consider giving the repository a star on GitHub.

---

*🌺 Subho Sarodiya! Celebrate the culture, explore the history, and discover the power of data.*
