# mock_tts_utils.py
# Este arquivo simula as funcionalidades do tts_utils.py usando gTTS

from gtts import gTTS
from io import BytesIO

def text_to_speech(text: str, lang: str = 'pt-br'):
    """
    Converte o texto fornecido em áudio (bytes) usando gTTS.

    Args:
        text (str): O texto a ser convertido em fala.
        lang (str): O idioma para a conversão de texto em fala (padrão: 'pt-br').

    Returns:
        BytesIO: Um objeto BytesIO contendo os dados de áudio em formato MP3, 
                 ou None se o texto estiver vazio ou ocorrer um erro.
    """
    if not text:
        print("Nenhum texto fornecido para conversão em fala.")
        return None

    try:
        tts = gTTS(text=text, lang=lang, slow=False)
        audio_fp = BytesIO()
        tts.write_to_fp(audio_fp)
        audio_fp.seek(0) # Rebobina o stream para o início para que possa ser lido
        print(f"Áudio gerado com sucesso para o texto: '{text[:50]}...'")
        return audio_fp
    except Exception as e:
        print(f"Erro ao converter texto em fala: {e}")
        return None

