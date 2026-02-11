import tweepy
import json
import random
import os

def run():
    # Coleta as chaves
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # Configuração focada 100% na API V2 (Plano Free atual)
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # Carrega as cartas
    with open('cartas.json', 'r', encoding='utf-8') as f:
        cartas = json.load(f)
    
    escolha = random.choice(cartas)
    texto = f"{escolha['trecho']}\n\n— {escolha['autor']}, {escolha['data']}"

    # O segredo para o plano Free: usar user_auth=True
    try:
        response = client.create_tweet(text=texto, user_auth=True)
        print(f"Sucesso! Tweet enviado.")
    except Exception as e:
        print(f"Erro detalhado: {e}")
        raise e

if __name__ == "__main__":
    run()
