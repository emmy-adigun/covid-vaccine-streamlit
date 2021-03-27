import numpy as np
import seaborn as sns
import streamlit as st
import pandas as pd
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

# Text/Title
st.title("COVID Vaccination update")

# load csv data


def load_data():
    df_vaccines = pd.read_csv(
        r"https://raw.githubusercontent.com/owid/covid-19-data/master/public/data/vaccinations/vaccinations.csv")
    return df_vaccines


# let variable df_vaccines contain the data
df_vaccines = load_data()


# Perform data cleaning and grouping
data = df_vaccines.loc[(df_vaccines["location"] != 'World') & (df_vaccines["location"] != 'Africa') & (
    df_vaccines["location"] != 'Asia') & (df_vaccines["location"] != 'Europe') &
    (df_vaccines["location"] != 'European Union') & (df_vaccines["location"] != 'North America') &
    (df_vaccines["location"] != 'Northern Cyprus') & (df_vaccines["location"] != 'Northern Ireland')]


# Group data based on location and replace 'NaN' values with zeros
df_category = data[['location', 'date', 'total_vaccinations',
                    'people_vaccinated', 'people_fully_vaccinated']]
df_group = df_category.groupby("location")[
    "location", "date", "total_vaccinations", "people_vaccinated", "people_fully_vaccinated"].max()
df_result = pd.DataFrame(df_group).replace(np.NaN, 0)

# show result

# Status declaration
total_locations = data["location"].nunique()
total_vaccinations = df_result["total_vaccinations"].sum()
people_vaccinated = df_result["people_vaccinated"].sum()
people_fully_vaccinated = df_result["people_fully_vaccinated"].sum()


# using streamlit column layout to display cumulative status result
col1, col2 = st.beta_columns(2)
col1.text("No. of locations")
col1.success(total_locations)
col2.text("Total vaccinations (Cumulative)")
col2.success(f"{total_vaccinations:,.2f}")

col1, col2 = st.beta_columns(2)
col1.text("No. of people vaccinated (Cumulative)")
col1.success(f"{people_vaccinated:,.2f}")
col2.text("People fully vaccinated (Cumulative)")
col2.success(f"{people_fully_vaccinated:,.2f}")


# Using streamlit select option for vaccine 'location'
st.sidebar.checkbox("Show Analysis by Location", True, key=1)
country_select = st.sidebar.selectbox(
    'Select a Location', df_result['location'])
selected_country = df_result[df_result['location'] == country_select]


def get_vaccine_analysis(dataresult):
    total_res = pd.DataFrame({'Status': ['Total vaccination', 'People Vaccinated', 'People fully vaccinated'],
                              'Figure': (dataresult.iloc[0]['total_vaccinations'], dataresult.iloc[0]['people_vaccinated'],
                                         dataresult.iloc[0]['people_fully_vaccinated'])
                              })
    return total_res


total_country = get_vaccine_analysis(selected_country)

# using stremlit column layout to display status result based on location selected
st.markdown("## **Location level analysis**")
location_total_vaccinations = total_country.Figure[0]
location_people_vaccinated = total_country.Figure[1]
location_people_fully_vaccinated = total_country.Figure[2]

col1, col2 = st.beta_columns(2)
col1.text("Location")
col1.info(country_select)
col2.text("Total vaccinations (Cumulative)")
col2.info(f"{location_total_vaccinations:,}")

col1, col2 = st.beta_columns(2)
col1.text("No. of people vaccinated (Cumulative)")
col1.info(f"{location_people_vaccinated:,}")
col2.text("People fully vaccinated (Cumulative)")
col2.info(f"{location_people_fully_vaccinated:,}")

# Visualization part using bar chart
if st.sidebar.checkbox("Show Analysis by Location", True, key=2):
    st.markdown("## **Location level analysis - Visualization**")
    st.markdown("### Total vaccination, People Vaccinated and " +
                "People fully vaccinated in %s " % (country_select))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
            total_country,
            x='Status',
            y='Figure',
            labels={'Figure': 'Figure in %s ' % (country_select)},
            color='Status')
        st.plotly_chart(state_total_graph)


# st.write(df_vaccines.head())

# st.write(df_vaccines['location'].head())

# update_df = (((df_vaccines['location']) == 'World').sum())
# new_mod = update_df.drop()
# st.write(new_mod)

# for index, row in df_vaccines.iterrows():
#     if (row['location']) == 'World':
#         #des = pd.DataFrame(row)
#         st.write(row.sum())


# st.write(data)

# drop_location = data['location'].value_counts()


# st.write(df_vaccines["date"].value_counts())
