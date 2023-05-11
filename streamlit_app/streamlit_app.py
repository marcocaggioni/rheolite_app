import streamlit as st
import lmfit
import io
import pandas as pd
import matplotlib.pyplot as plt
import pybroom
from PIL import Image

from md_text import *
from functions import *

logo=Image.open('logo.png')
st.image(logo, width=64)
st.markdown(model_description)
st.divider()

"## Upload Data"

file = st.file_uploader ('Upload a xls exported from trios (multitab)')

st.divider()

"## Select data"

with st.form("Select"):
    try:
        Excel_file=pd.ExcelFile(file.read())
        step=st.selectbox('pick step', Excel_file.sheet_names)

        data = Excel_file.parse(sheet_name=step, sep='\t', skiprows=[0,2])
        st.write(data.head())

        submitted = st.form_submit_button("Submit")
        if submitted:
            st.write('Analizing' + st)
    except:
        pass


"## Analyze data"

def analyze_data():
    res_fit=TCC_model.fit(data['Stress'],x=data['Shear rate'], weights=1/data['Stress'])
    
    fig, ax = plt.subplots()
    ax.plot(data['Shear rate'],data['Stress']/data['Shear rate'], 'o', label='Data')
    ax.plot(data['Shear rate'],res_fit.best_fit/data['Shear rate'], label='TCC fit')
    ax.plot(data['Shear rate'],res_fit.eval_components(x=data['Shear rate'])['TC_']/data['Shear rate'], label='TC_component fit')
    ax.plot(data['Shear rate'],res_fit.eval_components(x=data['Shear rate'])['carreau_']/data['Shear rate'], label='carreau_component fit')
    ax.set_xlabel('$\dot\gamma [1/s]$')
    ax.set_ylabel('Viscosity [Pa s]')

    ax.set_yscale('log')
    ax.set_xscale('log')
    ax.set_title('Plot of data and model')
    plt.legend()

    return res_fit, fig

analyze_button = st.button("Analyze data")

if analyze_button:
    res_fit, ax = analyze_data()
    st.write(res_fit, unsafe_allow_html=True)
    st.pyplot(ax)
    res_table=pybroom.tidy(res_fit)[['name','value','stderr']]
    st.write(res_table)

    st.download_button(
    "Press to Download",
    res_table.to_csv().encode('utf-8'),
    "result.csv",
    "text/csv",
    key='browser-data'
    )
    
