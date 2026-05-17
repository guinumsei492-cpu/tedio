st.components.v1.html("""
<!DOCTYPE html>
<html>
<head>
<style>
body {
    text-align: center;
}

/* mensagem */
#mensagem {
    font-size: 28px;
    color: #ff0066;
    margin-top: 20px;
    font-weight: bold;
    animation: fade 1s;
}

@keyframes fade {
    from {opacity: 0;}
    to {opacity: 1;}
}
</style>
</head>

<body>

<!-- PLAYER YOUTUBE -->
<div id="player"></div>

<!-- MENSAGEM -->
<div id="mensagem">💖</div>

<script>
var tag = document.createElement('script');
tag.src = "https://www.youtube.com/iframe_api";
document.body.appendChild(tag);

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
            'onReady': onPlayerReady
        }
    });
}

function onPlayerReady(event) {
    setInterval(updateMensagem, 500);
}

function updateMensagem() {
    if (!player || !player.getCurrentTime) return;

    var tempo = player.getCurrentTime();
    var msg = "";

    if (tempo < 10) msg = "Sofia... 💖";
    else if (tempo < 20) msg = "Desde que você entrou na minha vida...";
    else if (tempo < 30) msg = "Tudo ficou mais bonito ✨";
    else if (tempo < 40) msg = "Você é minha paz...";
    else if (tempo < 50) msg = "Minha felicidade...";
    else if (tempo < 60) msg = "Minha Pitica 🐱💕";
    else if (tempo < 75) msg = "Eu te amo mais do que palavras podem explicar...";
    else if (tempo < 90) msg = "E escolheria você...";
    else if (tempo < 110) msg = "Em todas as vidas 💞";
    else if (tempo < 140) msg = "Obrigado por existir, Sofia...";
    else msg = "Você é tudo pra mim 💖";

    document.getElementById("mensagem").innerText = "✨ " + msg;
}
</script>

</body>
</html>
""", height=350)
