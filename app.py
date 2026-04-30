import streamlit as st

# Configuração da página
st.set_page_config(page_title="Para Sofia 🎀", page_icon="💖", layout="centered")

# --- ESTILIZAÇÃO CSS (O "Pulo do Gato" do Design) ---
st.markdown("""
    <style>
    /* Fundo e Fonte Geral */
    .stApp {
        background-color: #fff0f5; /* Rosa bem clarinho */
        font-family: 'Varela Round', sans-serif;
    }

    /* Animação de Flutuar para a Hello Kitty */
    @keyframes float {
        0% { transform: translateY(0px) rotate(0deg); }
        50% { transform: translateY(-20px) rotate(5deg); }
        100% { transform: translateY(0px) rotate(0deg); }
    }
    .kitty-animated {
        display: block;
        margin: 0 auto;
        width: 180px;
        animation: float 4s ease-in-out infinite;
        filter: drop-shadow(0 5px 15px rgba(255,105,180,0.3));
    }

    /* Título principal */
    h1 {
        color: #ff69b4;
        text-align: center;
        font-size: 3rem !important;
        text-shadow: 2px 2px white;
    }

    /* Estilo dos Cards de Poemas */
    .poem-card {
        background-color: white;
        border: 2px solid #ffb7c5;
        border-radius: 20px;
        padding: 20px;
        margin: 10px 0;
        transition: 0.3s;
        box-shadow: 5px 5px 0px #ffb7c5;
    }
    .poem-card:hover {
        transform: scale(1.02);
        border-color: #ff69b4;
        background-color: #fff9fb;
    }
    .poem-card p {
        color: #d02090;
        font-size: 1.1rem;
        line-height: 1.5;
        margin: 0;
        text-align: center;
    }

    /* Rodapé */
    .footer {
        text-align: center;
        color: #ff69b4;
        font-size: 0.8rem;
        margin-top: 50px;
    }
    </style>
    <link href="https://fonts.googleapis.com/css2?family=Varela+Round&display=swap" rel="stylesheet">
    """, unsafe_allow_html=True)

# --- CONTEÚDO DO SITE ---

# 1. Hello Kitty Animada (GIF)
# Usando um GIF oficial para já vir com movimento próprio + animação CSS
st.markdown('<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1eXU2Z3ZwaG9vNm54M2Z4eG54eG54eG54eG54eG54eG54eGZpYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/v6p6S8T0A0XN6/giphy.gif" class="kitty-animated">', unsafe_allow_html=True)

st.write(f" # Para Sofia 🎀")

# 2. Música (Vídeo do YouTube que você pediu)
st.write("### Aperte o play e leia com carinho... 🎶")
st.video("https://youtu.be/l4DAcyXkX0E")

st.write("---")

# 3. Seção de Mini Cards com Poemas
st.subheader("Versos para você ✨")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class="poem-card">
            <p>🌸<br><b>Doce Sofia</b><br>
            Nem o laço mais bonito,<br>
            nem a flor mais colorida,<br>
            superam o teu sorriso,<br>
            que ilumina minha vida.</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class="poem-card">
            <p>🎀<br><b>Simplicidade</b><br>
            Gosto da tua presença,<br>
            desse teu jeito de ser.<br>
            Sofia, o mundo é sorte<br>
            por ter você pra viver.</p>
        </div>
    """, unsafe_allow_html=True)

st.markdown("""
    <div class="poem-card">
        <p>💖<br><b>Nosso Tempo</b><br>
        Como o ritmo dessa canção,<br>
        queria que o tempo parasse.<br>
        Pra eu guardar no coração,<br>
        cada vez que você me olhasse.</p>
    </div>
""", unsafe_allow_html=True)

# 4. Botão de Interação
if st.button("Um mimo para a Sofia 🐾"):
    st.balloons()
    st.snow()
    st.toast('Você é muito especial!', icon='🎀')

st.markdown('<div class="footer">Feito com 💖 para Sofia</div>', unsafe_allow_html=True)
