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
    print("\n--------------------------\n")

response = co.chat(
    model="command-a-03-2025",
    messages=[
        {
            "role": "user",
            "content":(f'make a headline like a subtitle that will be edited and putted in the middle of the video)about this transcription (something with 2 to 4 words) {roteiro}'),
              
        }
    ],
)

print('terceiro metodo,palavras chave:\n',response.message.content[0].text)
