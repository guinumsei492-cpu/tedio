import streamlit as st

# 1. Configuração da Página
st.set_page_config(page_title="Para Sofia 🎀", page_icon="💖")

# 2. CSS - Estilo Hello Kitty e Animações
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f5;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    
    /* Animação de flutuar */
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-15px); }
        100% { transform: translateY(0px); }
    }

    .kitty-img {
        display: block;
        margin-left: auto;
        margin-right: auto;
        width: 180px;
        animation: float 3s ease-in-out infinite;
    }

    .poem-card {
        background-color: white;
        border: 2px solid #ff69b4;
        border-radius: 15px;
        padding: 15px;
        margin-bottom: 15px;
        text-align: center;
        box-shadow: 4px 4px 10px rgba(255, 105, 180, 0.2);
    }

    h1 {
        color: #ff69b4;
        text-align: center;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Hello Kitty Animada
# Link de um PNG transparente que funciona bem em fundos claros
st.markdown('<img src="https://raw.githubusercontent.com/souzapxl/images/main/hello_kitty.png" class="kitty-img" onerror="this.src=\'https://www.hellokitty.com/images/character_hello_kitty.png\'">', unsafe_allow_html=True)

st.title("Para Sofia 🎀")

# 4. Música (Portugal - Kawe & Ananda)
st.write("### Solta o som... 🎶")
st.video("https://youtu.be/l4DAcyXkX0E")

st.write("---")

# 5. Mini Cards com Poemas
st.write("### Versos para você ✨")

poemas = [
    "🌸 **Doce Sofia**<br>Nem o laço mais bonito,<br>nem a flor mais colorida,<br>superam o teu sorriso,<br>que ilumina minha vida.",
    "🎀 **Simplicidade**<br>Gosto da tua presença,<br>desse teu jeito de ser.<br>Sofia, o mundo é sorte<br>por ter você pra viver.",
    "💖 **Nosso Tempo**<br>Como o ritmo dessa canção,<br>queria que o tempo parasse.<br>Pra eu guardar no coração,<br>cada vez que você me olhasse."
]

for p in poemas:
    st.markdown(f'<div class="poem-card"><p>{p}</p></div>', unsafe_allow_html=True)

# 6. Botão Interativo
if st.button("Um carinho para a Sofia 🐾"):
    st.balloons()
    st.snow()
    st.success("Você é incrível!")
