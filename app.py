import streamlit as st
from datetime import datetime
from streamlit_autorefresh import st_autorefresh

# AUTO REFRESH (1 segundo)
st_autorefresh(interval=1000, key="refresh")

st.set_page_config(page_title="Para minha Pitica 💖", layout="centered")

# 🎀 CSS
st.markdown("""
<style>
body {
    background: linear-gradient(180deg, #ffc0cb, #ff99cc);
}

.title {
    text-align: center;
    color: #ff0066;
    font-size: 42px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: #cc0052;
    font-size: 18px;
}

.counter {
    text-align: center;
    font-size: 24px;
    color: #cc0052;
}

.card {
    background: white;
    padding: 20px;
    margin: 20px;
    border-radius: 25px;
    box-shadow: 0px 6px 15px rgba(255,105,180,0.5);
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# 💖 TÍTULO
st.markdown('<h1 class="title">Para minha Pitica 💖</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Sofia, você é tudo pra mim 🐱💕</p>', unsafe_allow_html=True)

# 🐱 HELLO KITTY
st.image("https://i.imgur.com/OdL0XPt.png", width=150)

# ⏱ CONTADOR
inicio = datetime(2025, 5, 21, 0, 0)
agora = datetime.now()
tempo = agora - inicio

dias = tempo.days
horas = tempo.seconds // 3600
minutos = (tempo.seconds % 3600) // 60
segundos = tempo.seconds % 60

st.markdown(f"""
<div class="counter">
💖 Eu e minha Pitica há:<br>
<b>{dias} dias {horas}h {minutos}m {segundos}s</b>
</div>
""", unsafe_allow_html=True)

# 🎬 PLAYER + SINCRONIZAÇÃO REAL
st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<style>
#mensagem {
    font-size: 26px;
    color: #ff0066;
    text-align: center;
    margin-top: 10px;
}
</style>
</head>
<body>

<div id="player"></div>
<div id="mensagem">💖</div>

<script src="https://www.youtube.com/iframe_api"></script>

<script>
var player;

function onYouTubeIframeAPIReady() {
    player = new YT.Player('player', {
        height: '200',
        width: '300',
        videoId: '7lNfLy6-xxE',
        playerVars: {
            'autoplay': 1,
            'controls': 1
        },
        events: {
            'onReady': function(event) {
                setInterval(updateMensagem, 500);
            }
        }
    });
}

function updateMensagem() {
    if (!player || !player.getCurrentTime) return;

    var t = player.getCurrentTime();
    var msg = "";

    if (t < 10) msg = "Sofia... 💖";
    else if (t < 20) msg = "Desde que você entrou na minha vida...";
    else if (t < 30) msg = "Tudo ficou mais bonito ✨";
    else if (t < 40) msg = "Você é minha paz...";
    else if (t < 50) msg = "Minha felicidade...";
    else if (t < 60) msg = "Minha Pitica 🐱💕";
    else if (t < 75) msg = "Eu te amo mais do que palavras podem explicar...";
    else if (t < 90) msg = "E escolheria você...";
    else if (t < 110) msg = "Em todas as vidas 💞";
    else if (t < 140) msg = "Obrigado por existir, Sofia...";
    else msg = "Você é tudo pra mim 💖";

    document.getElementById("mensagem").innerText = "✨ " + msg;
}
</script>

</body>
</html>
""", height=350)

# 💌 CARDS
def card(titulo, texto):
    st.markdown(f"""
    <div class="card">
        <h3>{titulo}</h3>
        <p>{texto}</p>
    </div>
    """, unsafe_allow_html=True)

card("Minha Pitica 💕", "Sofia, você é a melhor coisa da minha vida.")
card("Meu Lugar ❤️", "Meu lugar favorito é ao seu lado.")
card("Pra Sempre 💖", "Isso aqui nunca vai acabar.")

# 🎁 BOTÃO
if st.button("Clica aqui ❤️"):
    st.balloons()
    st.success("Eu te amo muito, Sofia 💖")
