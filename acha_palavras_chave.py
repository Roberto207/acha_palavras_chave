import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import string
import cohere
import whisper
co = cohere.ClientV2(api_key="jgZB8bBEvGDomXoPFOV8EBPgbM30CDsDwMw2QKy0")
# nltk.download('punkt')
# nltk.download('stopwords')
# nltk.download('tokenizers/punkt_tab/english/')
# nltk.download('punkt_tab')
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

#outr modo de fazer 
def achar_pchaves(roteieo):
    # Estratégia simples: usar os 8 primeiros tokens relevantes
    palavras = roteiro.split() #pegamo o texto trasncrito e fazemos uma lista com suas palavras
    palavras_chave = [p for p in palavras if len(p) > 3][:8] #pegando as 8 palavras/tokens mais relevantes
    consulta = ' '.join(palavras_chave) #ajustando a lista pra consulta
    return consulta
print(f'as palavras chave pelo metodo 2 foram :{achar_pchaves(roteiro)}')

#outro modo de fazer

response = co.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content":(f'make a headline like a subtitle that will be edited and putted in the middle of the video)about this transcription (something with 2 to 4 words) {roteiro}'),
              
        }
    ],
)
print('terceiro metodo:\n',response.message.content[0].text)