import tweepy
import json
import random
import os

def run():
    api_key = os.getenv("API_KEY")
    api_secret = os.getenv("API_SECRET")
    access_token = os.getenv("ACCESS_TOKEN")
    access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

    client = tweepy.Client(
        consumer_key=api_key,
        consumer_secret=api_secret,
        access_token=access_token,
        access_token_secret=access_token_secret
    )

    with open('cartas.json', 'r', encoding='utf-8') as f:
        cartas = json.load(f)
    
    escolha = random.choice(cartas)
    
    # Tentamos pegar o conteúdo, não importa se o nome é 'trecho', 'texto' ou 'conteudo'
    conteudo = escolha.get('trecho') or escolha.get('texto') or escolha.get('conteudo')
    autor = escolha.get('autor', 'Virginia/Vita')
    data = escolha.get('data', 'S/D')

    post_final = f"{conteudo}\n\n— {autor}, {data}"

    try:
        # O user_auth=True é o que resolveu o problema do pagamento!
        response = client.create_tweet(text=post_final, user_auth=True)
        print(f"Sucesso! Tweet enviado.")
    except Exception as e:
        print(f"Erro ao postar: {e}")
        raise e

if __name__ == "__main__":
    run()
