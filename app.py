import streamlit as st

# 1. Configuração da Página (Isso tem que ser a primeira coisa!)
st.set_page_config(page_title="Para Sofia 🎀", page_icon="💖")

# 2. Estilo Visual (CSS)
st.markdown("""
    <style>
    .stApp {
        background-color: #fff0f5;
    }
    .kitty-flutuando {
        display: block;
        margin: auto;
        width: 200px;
        animation: float 3s ease-in-out infinite;
    }
    @keyframes float {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
        100% { transform: translateY(0px); }
    }
    .card {
        background: white;
        padding: 20px;
        border-radius: 15px;
        border: 2px solid #ff69b4;
        text-align: center;
        margin-bottom: 10px;
        color: #d02090;
    }
    </style>
    """, unsafe_allow_html=True)

# 3. Imagem da Hello Kitty (Link do Giphy que é o mais estável do mundo)
st.markdown('<img src="https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExOHp1eXU2Z3ZwaG9vNm54M2Z4eG54eG54eG54eG54eG54eG54eGZpYyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/v6p6S8T0A0XN6/giphy.gif" class="kitty-flutuando">', unsafe_allow_html=True)

# 4. Título
st.write(f"<h1 style='text-align: center; color: #ff69b4;'>Para Sofia 🎀</h1>", unsafe_allow_html=True)

# 5. Música (Mandei o embed do YouTube)
st.video("https://youtu.be/l4DAcyXkX0E")

st.write("---")

# 6. Mini Cards com Poemas
st.markdown('<div class="card">🌸 <b>Doce Sofia</b><br>Nem o laço mais bonito,<br>nem a flor mais colorida,<br>superam o teu sorriso,<br>que ilumina minha vida.</div>', unsafe_allow_html=True)

st.markdown('<div class="card">🎀 <b>Simplicidade</b><br>Gosto da tua presença,<br>desse teu jeito de ser.<br>Sofia, o mundo é sorte<br>por ter você pra viver.</div>', unsafe_allow_html=True)

# 7. Botão de Interação
if st.button("Clique para um carinho 🐾"):
    st.balloons()
    st.snow()
    st.success("Você é especial, Sofia!")
