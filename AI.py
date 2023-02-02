import streamlit as st
import openai
import os
from GoogleNews import GoogleNews


st.set_page_config(
    page_title="Assistant",
    page_icon="🎇",
    layout="wide"
 )

CURRENT_THEME = "dark"
googlenews = GoogleNews()



openai.api_key = "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"

st.header('I am your Assistant')



def call_ai(result):
	model_engine = "text-davinci-003"
	completion = openai.Completion.create(
		engine=model_engine,
        prompt=result,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=1,
        )
	response = completion.choices[0].text
	return response

col1, col2= st.columns((3,3))
with col1:
	data = st.text_area('Write your command')

with col2:
	st.markdown("![Alt Text](https://media.tenor.com/SW48eIrW9F0AAAAC/jarvisfullgui.gif)")


#result = data.upper()




if st.button('Button'):
    #st.write('You Clicked on button')
    data = call_ai(data)
    st.write(data)
    news_info = googlenews.get_news(data)
    st.write(news_info)

