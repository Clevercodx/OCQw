import streamlit as st
import requests
import json

# Définissez votre clé API Bard
API_KEY = "Votre clé API Bard"

# Définissez la fonction qui interroge l'API Bard
def get_response(query):
    url = "https://bard.ai/v1/query"
    payload = {"query": query, "api_key": API_KEY}
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        return json.loads(response.content)["response"]
    else:
        return None

# Définissez la fonction qui gère l'interface utilisateur
def main():
    st.title("Chatbot Bard")
    query = st.text_input("Entrez votre question ou votre requête")
    response = get_response(query)
    if response is not None:
        st.write(response)

# Lancez l'application
if __name__ == "__main__":
    main()

