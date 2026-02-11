import tweepy
import json
import random
import os

def carregar_cartas():
    with open('cartas.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def run():
    # Pega as chaves que você salvou no GitHub Secrets
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # Configuração específica para o plano GRATUITO (v2 com OAuth 1.0a)
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    cartas = carregar_cartas()
    escolha = random.choice(cartas)
    texto = f"{escolha['trecho']}\n\n— {escolha['autor']}, {escolha['data']}"

    print(f"Tentando postar: {texto}")

    # Comando para criar o tweet
    response = client.create_tweet(text=texto)
    print(f"Sucesso! Tweet ID: {response.data['id']}")

if __name__ == "__main__":
    run()
