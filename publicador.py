import requests

def enviar_mensagem(token, channel_id, text):
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    payload = {"chat_id": channel_id, "text": text, "parse_mode": "HTML"}
    resp = requests.post(url, data=payload)
    resp.raise_for_status()
