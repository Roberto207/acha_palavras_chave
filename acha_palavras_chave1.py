import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
import whisper

# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('tokenizers/punkt_tab/english/')
# nltk.download('punkt_tab')
#talvez na primeira vez que voce rode o codigo,seja necessario fazer download desses nltks acima(exemplo: nltk.download('punkt'))
def transcrever_audio(arquivo_audio):
    model = whisper.load_model("base")  # tiny, base, small, medium, large
    resultado = model.transcribe(arquivo_audio, language='pt')
    return resultado['text']


escolha = str(input("Deseja usar o texto pronto ou um video trasncrito,digite 1 para pronto e 2 para transcrito: "))
if escolha == '1':
    roteiro_manual = str(input("Digite o texto pronto: "))
    roteiro = roteiro_manual
elif escolha == '2':
    caminho_arquivo = (input("Digite o caminho do arquivo do vídeo  a ser transcrito: ")).strip()
    roteiro = transcrever_audio(caminho_arquivo)
    print("\n--- Roteiro transcrito ---\n")
    print(roteiro)
def extrair_palavras_chave(texto, n=5):
    # Tokenização
    palavras = word_tokenize(texto.lower())

    # Remover pontuação e stopwords
    stop_words = set(stopwords.words('portuguese') + list(string.punctuation))
    palavras_filtradas = [p for p in palavras if p not in stop_words and len(p) > 2]

    # Contar frequência
    contagem = Counter(palavras_filtradas)
    
    # Retornar as n palavras mais comuns
    return [palavra for palavra, _ in contagem.most_common(n)]

palavras_chave = extrair_palavras_chave(roteiro)
print("Palavras-chave extraídas:", palavras_chave)


