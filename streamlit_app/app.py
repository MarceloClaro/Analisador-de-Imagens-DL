import streamlit as st
from PIL import Image
from utils.gemini_utils import get_gemini_response
from utils.tts_utils import text_to_speech

# Configuração da página (opcional, mas bom para UX)
st.set_page_config(page_title="Analisador de Imagens DL", layout="wide")

# --- Funções Auxiliares (Lógica de Negócio/Controladores) ---
def handle_image_analysis(image_file):
    """
    Processa a imagem, obtém a análise do Gemini e o áudio.
    """
    if image_file is not None:
        try:
            image = Image.open(image_file)
            st.image(image, caption="Imagem Carregada", use_column_width=True)
            
            # Botão para iniciar a análise só aparece depois do upload
            if st.button("Analisar Imagem"):
                with st.spinner("Analisando a imagem... Por favor, aguarde."):
                    # Obter descrição da imagem do Gemini
                    description = get_gemini_response(image)
                    
                    if description:
                        st.subheader("Descrição da Imagem:")
                        st.markdown(description)
                        
                        # Gerar e exibir áudio da descrição
                        audio_bytes = text_to_speech(description)
                        if audio_bytes:
                            st.audio(audio_bytes, format="audio/mp3")
                        else:
                            st.error("Não foi possível gerar o áudio da descrição.")
                    else:
                        st.error("Não foi possível obter a descrição da imagem.")
        except Exception as e:
            st.error(f"Erro ao processar a imagem: {e}")
    else:
        st.info("Por favor, carregue um arquivo de imagem para análise.")

# --- Interface do Usuário (Componentes Visuais) ---
st.title("🖼️ Analisador de Imagens com Deep Learning")
st.markdown("""
Bem-vindo ao Analisador de Imagens! Faça o upload de uma imagem e nossa IA 
irá fornecer uma descrição detalhada e a narração em áudio dessa descrição.
""")

# Upload de Imagem
uploaded_file = st.file_uploader("Escolha uma imagem...", type=["jpg", "jpeg", "png"])

# Lógica de controle principal da UI baseada no estado do upload
if uploaded_file:
    handle_image_analysis(uploaded_file)
else:
    st.markdown("---")
    st.subheader("Como funciona?")
    st.markdown("""
    1.  **Faça o Upload:** Clique em 'Browse files' e selecione uma imagem (JPG, JPEG, PNG).
    2.  **Análise:** Após o upload, clique no botão "Analisar Imagem".
    3.  **Resultados:** A descrição da imagem e um player de áudio aparecerão abaixo.
    """)
    st.markdown("---")

# Rodapé (opcional)
st.markdown("---")
st.markdown("Desenvolvido com Streamlit e Google Gemini.")
