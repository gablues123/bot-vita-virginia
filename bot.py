import tweepy
import json
import random
import os

def run():
    # Coleta os segredos do GitHub
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    # Autenticação direta (OAuth 1.0a) - a mais estável para o plano Free
    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    # Carrega as cartas e garante que não dê erro de 'Key'
    with open('cartas.json', 'r', encoding='utf-8') as f:
        cartas = json.load(f)
    
    escolha = random.choice(cartas)
    
    # Pega o conteúdo de forma segura
    trecho = escolha.get('trecho') or escolha.get('texto') or "Sem conteúdo"
    autor = escolha.get('autor', 'Virginia/Vita')
    data = escolha.get('data', 's/d')

    post = f"{trecho}\n\n— {autor}, {data}"

    # Tenta postar. O segredo está no user_auth=True
    try:
        client.create_tweet(text=post, user_auth=True)
        print("Mágica feita! Tweet enviado.")
    except Exception as e:
        print(f"Erro: {e}")
        raise e

if __name__ == "__main__":
    run()
