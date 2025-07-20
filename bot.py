import argparse
from analise import get_upcoming_matches
from publicador import enviar_mensagem
import settings

def main(mode):
    matches = get_upcoming_matches(minutes_before=60)
    if matches:
        mensagem = settings.MENSAGEM_TEMPLATE.format(matches="\n\n".join(matches))
        enviar_mensagem(settings.TELEGRAM_TOKEN, settings.CHANNEL_ID, mensagem)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--mode', choices=['scheduled', 'manual'], required=True)
    args = parser.parse_args()
    main(args.mode)
