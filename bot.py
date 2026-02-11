import tweepy
import json
import random
import os

def carregar_cartas():
    with open('cartas.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def run():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # Autenticação para o plano Gratuito
    auth = tweepy.OAuth1UserHandler(api_key, api_secret, access_token, access_token_secret)
    api = tweepy.API(auth)

    cartas = carregar_cartas()
    escolha = random.choice(cartas)
    texto = f"{escolha['trecho']}\n\n— {escolha['autor']}, {escolha['data']}"

    # Tentando postar usando o método v1.1 (mais compatível)
    try:
        api.update_status(status=texto)
        print("Sucesso!")
    except Exception as e:
        # Se falhar, tenta o método v2
        client = tweepy.Client(
            consumer_key=api_key, consumer_secret=api_secret,
            access_token=access_token, access_token_secret=access_token_secret
        )
        client.create_tweet(text=texto)
        print("Sucesso via V2!")

if __name__ == "__main__":
    run()
