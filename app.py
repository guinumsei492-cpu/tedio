st.markdown("""
<style>

/* FUNDO HELLO KITTY REPETIDO */
.stApp {
    background-image: url("https://i.imgur.com/3ZQ3Z4R.png");
    background-size: 120px;
    background-repeat: repeat;
    background-attachment: fixed;
}

/* camada rosa por cima pra ficar bonito */
.stApp::before {
    content: "";
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(255, 182, 217, 0.85);
    z-index: -1;
}

/* título */
.title {
    text-align: center;
    color: #ff2e7a;
    font-size: 50px;
    font-weight: bold;
}

/* subtitulo */
.subtitle {
    text-align: center;
    color: #ff4d88;
    font-size: 20px;
}

/* cards */
.card {
    background: #fff0f6;
    padding: 20px;
    margin: 20px;
    border-radius: 30px;
    box-shadow: 0px 8px 20px rgba(255,105,180,0.4);
    text-align: center;
    animation: float 4s infinite ease-in-out;
}

/* animação */
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-10px);}
    100% {transform: translateY(0px);}
}

/* corações */
.heart {
    position: fixed;
    bottom: -20px;
    font-size: 24px;
    animation: subir 6s linear infinite;
}

@keyframes subir {
    0% {transform: translateY(0); opacity:1;}
    100% {transform: translateY(-900px); opacity:0;}
}

</style>
""", unsafe_allow_html=True)
