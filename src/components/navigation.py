##© 2024 Tushar Aggarwal. All rights reserved.(https://tushar-aggarwal.com)
##Botimus[Towards-GenAI] (https://github.com/Towards-GenAI)
##################################################################################################
#Importing dependencies
import streamlit as st
from pathlib import Path
import base64
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))
import warnings
warnings.filterwarnings("ignore")
import os


#######################################################################################################
#Importing from SRC
#######################################################################################################


#######################################################################################################
#Navigation
#######################################################################################################

def custom_style():
    css_file_path = os.path.join('src', 'style', 'custom_styles.css')
    with open(css_file_path) as f:
        css = f.read()
    st.markdown(f'<style>{css}</style>', unsafe_allow_html=True)

def page_config(page_title, page_icon, layout):
    # Page config
    st.set_page_config(
        page_title=page_title,
        page_icon=page_icon,
        layout=layout
    )

def footer():
    footer_style ='''
    <style>
        MainMenu {{visibility: hidden;}}
        footer {{visibility: hidden;}}
        footer:after {{ 
            visibility: visible;
            display: block;
            position: relative;
            padding: 5px;
            top: 2px;
        }}
    </style>
    '''
    
    footer_content = '''
    <style>
        

        .image1,
        .image2 {
            padding: 10px;
            transition: transform .2s;
        }

        .image1:hover,
        .image2:hover {
            /* border: 4px solid green; */
            /* border-radius: 15px; */
            transform: scale(1.5);
            transition: 0.2s;
        }

        

        .footer {
            position: relative;
            width: 100%;
            left: 0;
            bottom: 0;
            background-color: transparent;
            margin-top: auto;
            color: #163172;
            padding: 24px;
            text-align: center;
        }
    </style>

    <div class="footer">
        <p style="font-size: 15px"> Original: © 2024 Tushar Aggarwal. All rights reserved.</p>
        <p style="font-size: 15px">Modified by <a href="https://www.linkedin.com/in/tina-sterite">Tina Sterite</a></p>
        <a href="https://github.com/Tina-Sterite"><img class="image2" src="https://cdn-icons-png.flaticon.com/512/25/25231.png"  width="70" height="70"></a>
        
        
    </div>
    '''
    
    st.markdown(footer_style, unsafe_allow_html=True)
    st.markdown(footer_content, unsafe_allow_html=True)































































































































































