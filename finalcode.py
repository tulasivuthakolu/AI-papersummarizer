#IMPORTING LIBRARIES
import streamlit as st
from elsapy.elsclient import ElsClient
from elsapy.elsdoc import FullDoc
from metaphor_python import Metaphor
import requests
import concurrent.futures
import re

#OPEN AI API KEY DECLARATION
api_key = 'give your api key'
endpoint = 'https://api.openai.com/v1/chat/completions'

#FUNCTION TO GENERATE SUMMARY
def generate_summary(prompt):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {api_key}',
        }
            
        data = {
            'model': 'gpt-3.5-turbo',
            'messages': [{'role': 'system', 'content': 'You are an intelligent Summarizer.'}, {'role': 'user', 'content': prompt}],
        }
        response = requests.post(endpoint, json=data, headers=headers)
        return response.json()['choices'][0]['message']['content']

#RETURN THE URLS
def get_metaphor_articles(query, num_results=10, include_domains=['www.sciencedirect.com']):
        try:
            api_key = "7cfc68fb-5d3f-42a8-bb5d-3dc310c38f41"
            final_list = []
            client = Metaphor(api_key=api_key)
            response = client.search(query, num_results=num_results, include_domains=include_domains)
            articles = [{"url": result.url} for result in response.results]
            pattern = re.compile(r'pii/(.*?)$')
            for article in articles:
                url = article["url"]
                match = pattern.search(url)
                if match:
                    final_list.append(match.group(1))
                else:
                    pass
            return final_list
        except Exception as e:
            print(f"An error occurred: {e}")
            return None


client = ElsClient('8587565025ca7f1e6e0a3f026b32f6eb')


st.title("Research Summarizer")


query = st.text_input("Enter the Topic of the paper")

def paperonefun(id_one):
                pii_doc = FullDoc(sd_pii=id_one)
                try:
                    if pii_doc.read(client):
                        abstract_org = pii_doc.data['coredata']['dc:description']
                        pre_prompt = """Explain the following research abstract in simple terms, using everyday language. Keep it short and clear, around 100 words. Assume the audience has little prior knowledge.The abstract is"""
                        fin = " ".join([pre_prompt, abstract_org])
                        summary = generate_summary(fin)
                        st.header(pii_doc.title+" "+"("+"Paper Id:"+" "+id_one+")")
                        st.write(summary)
                    else:
                        st.write("Failed to read document.")
                except:
                      pass

def papertwofun(id_two):
                
                pii_doc = FullDoc(sd_pii=id_two)
                try:
                    if pii_doc.read(client):
                        abstract_org = pii_doc.data['coredata']['dc:description']
                        pre_prompt = """Explain the following research abstract in simple terms, using everyday language. Keep it short and clear, around 100 words. Assume the audience has little prior knowledge.The abstract is"""
                        fin = " ".join([pre_prompt, abstract_org])
                        summary = generate_summary(fin)
                        st.header(pii_doc.title+" "+"("+"Paper Id:"+" "+id_two+")")
                        st.write(summary)
                    else:
                        st.write("Failed to read document.")
                except:
                      pass

def paperthreefun(id_three):
                pii_doc = FullDoc(sd_pii=id_three)
                try:
                    if pii_doc.read(client):
                        abstract_org = pii_doc.data['coredata']['dc:description']
                        pre_prompt = """Explain the following research abstract in simple terms, using everyday language. Keep it short and clear, around 100 words. Assume the audience has little prior knowledge.The abstract is"""
                        fin = " ".join([pre_prompt, abstract_org])
                        summary = generate_summary(fin)
                        st.header(pii_doc.title+" "+"("+"Paper Id:"+" "+id_three+")")
                        st.write(summary)
                    else:
                        st.write("Failed to read document.")
                except:
                      pass

def paperfourfun(id_four):
                
                pii_doc = FullDoc(sd_pii=id_four)
                try:
                    if pii_doc.read(client):
                        abstract_org = pii_doc.data['coredata']['dc:description']
                        pre_prompt = """Explain the following research abstract in simple terms, using everyday language. Keep it short and clear, around 100 words. Assume the audience has little prior knowledge.The abstract is"""
                        fin = " ".join([pre_prompt, abstract_org])
                        summary = generate_summary(fin)
                        st.header(pii_doc.title+" "+"("+"Paper Id:"+" "+id_four+")")
                        st.write(summary)
                    else:
                        st.write("Failed to read document.")
                except:
                      pass

def paperfivefun(id_five):
                
                pii_doc = FullDoc(sd_pii=id_five)
                try:
                    if pii_doc.read(client):
                        abstract_org = pii_doc.data['coredata']['dc:description']
                        pre_prompt = """Explain the following research abstract in simple terms, using everyday language. Keep it short and clear, around 100 words. Assume the audience has little prior knowledge.The abstract is"""
                        fin = " ".join([pre_prompt, abstract_org])
                        summary = generate_summary(fin)
                        st.header(pii_doc.title+" "+"("+"Paper Id:"+" "+id_five+")")
                        st.write(summary)
                    else:
                        st.write("Failed to read document.")
                except:
                      pass


if st.button('Search'):
        paper_id = get_metaphor_articles(query)
        if paper_id:
            id_one = paper_id[0]
            id_two = paper_id[1]
            id_three = paper_id[2]
            id_four = paper_id[3]
            id_five = paper_id[4]
            
            with concurrent.futures.ThreadPoolExecutor() as executor:
            
                future_1 = executor.submit(paperonefun(id_one))
                future_2 = executor.submit(papertwofun(id_two))
                future_3 = executor.submit(paperthreefun(id_three))
                future_4 = executor.submit(paperfourfun(id_four))
                future_5 = executor.submit(paperfivefun(id_five))


            concurrent.futures.wait([future_1, future_2, future_3,future_4,future_5])