import tweepy
import json
import random
import os

# Autenticação (Pega as chaves que vamos configurar já, já)
api_key = os.environ.get("API_KEY")
api_secret = os.environ.get("API_SECRET")
access_token = os.environ.get("ACCESS_TOKEN")
access_token_secret = os.environ.get("ACCESS_TOKEN_SECRET")

def run():
    # Login no Twitter
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # Ler as cartas
    with open('cartas.json', 'r', encoding='utf-8') as f:
        cartas = json.load(f)

    # Escolher uma aleatória
    escolha = random.choice(cartas)
    texto = f"“{escolha['texto']}”\n\n— {escolha['data']}"

    # Postar
    if len(texto) <= 280:
        client.create_tweet(text=texto)
        print(f"Tweet postado: {texto}")
    else:
        print("Texto muito longo, tentando novamente na próxima...")

if __name__ == "__main__":
    run()
