from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from analise import carregar_jogos, gerar_mensagem
import settings

def analisar(update: Update, context: CallbackContext):
    if not context.args:
        update.message.reply_text("Por favor, envie o nome do jogo após o comando.\nEx: /analisar Flamengo vs Palmeiras")
        return
    
    jogo_nome = " ".join(context.args).lower()
    jogos = carregar_jogos()
    jogos_filtrados = [j for j in jogos if jogo_nome in j.nome.lower()]
    
    if not jogos_filtrados:
        update.message.reply_text(f"Jogo '{jogo_nome}' não encontrado.")
        return
    
    for jogo in jogos_filtrados:
        mensagem = gerar_mensagem(jogo)
        update.message.reply_text(mensagem)

def main():
    updater = Updater(settings.TELEGRAM_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("analisar", analisar))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
