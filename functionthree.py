
#this is an open ai function which is used to summarize the abstract
#it takes input of abstract, it adds with a pre defined prompt which says " summarize easily in 100 words"
# concatinates the abstract with the pre defined prompt and pass it open ai api
# it will return the summary


import requests
api_key = 'sk-proj-d8MRwCbb10D752RlFPSST3BlbkFJbuyNId2Bq3EjPN4a8BDX'
endpoint = 'https://api.openai.com/v1/chat/completions'
abstract_org="The discovery of new materials is one of the driving forces to promote the development of modern society and technology innovation, the traditional materials research mainly depended on the trial-and-error method, which is time-consuming and laborious. Recently, machine learning (ML) methods have made great progress in the researches of materials science with the arrival of the big-data era, which gives a deep revolution in human society and advance science greatly. However, there exist few systematic generalization and summaries about the applications of ML methods in materials science. In this review, we first provide a brief account of the progress of researches on materials science with ML employed, the main ideas and basic procedures of this method are emphatically introduced. Then the algorithms of ML which were frequently used in the researches of materials science are classified and compared. Finally, the recent meaningful applications of ML in metal materials, battery materials, photovoltaic materials and metallic glass are reviewed."

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

pre_prompt = """Explain the following research abstract in simple terms, using everyday language. Keep it short and clear, around 100 words. Assume the audience has little prior knowledge.The abstract is"""
fin = " ".join([pre_prompt, abstract_org])
summary = generate_summary(fin)
