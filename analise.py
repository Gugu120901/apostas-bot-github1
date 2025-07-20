import requests
import datetime
import settings

def get_upcoming_matches(minutes_before=60):
    now = datetime.datetime.utcnow()
    upcoming = []
    for liga in settings.LIGAS:
        try:
            resp = requests.get(f"{settings.API_URL}/odds", params={"league": liga})
            data = resp.json()
        except Exception as e:
            upcoming.append(f"Erro ao obter jogos da liga {liga}: {e}")
            continue

        for jogo in data.get("games", []):
            try:
                start = datetime.datetime.fromisoformat(jogo["start_time"])
                delta = (start - now).total_seconds() / 60
                ev = jogo["prob_home"] * jogo["odd_home"] + jogo["prob_away"] * jogo["odd_away"] - 1
                stake = settings.BANKROLL * settings.STAKE_PERCENT
                msg = (
                    f"<b>{jogo['home_team']} vs {jogo['away_team']}</b>\n"
                    f"⏰ Início: {jogo['start_time']} UTC ({delta:.1f} min)\n"
                    f"📊 Odds: {jogo['odd_home']}/{jogo['odd_draw']}/{jogo['odd_away']}\n"
                    f"💰 EV: {ev:.2%} | Stake: {stake:.2f}"
                )
                upcoming.append(msg)
            except Exception as e:
                upcoming.append(f"Erro ao processar jogo: {e}")
    return upcoming
