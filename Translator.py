from flask import Flask, request, render_template, jsonify
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM

from os import getcwd

app = Flask(__name__, template_folder='templates')

cache_dir = getcwd()  # modelin yükleneceği dizini bulunduğumuz dizin seçiyoruz.

# Türkçe-İngilizce modelinin load edilmesi
turkish_model_name = "Helsinki-NLP/opus-tatoeba-en-tr"
turkish_tokenizer = AutoTokenizer.from_pretrained(turkish_model_name, cache_dir=cache_dir)
turkish_model = AutoModelForSeq2SeqLM.from_pretrained(turkish_model_name, cache_dir=cache_dir)

# İngilizce-Türkçe modelinin load edilmesi
english_model_name = "Helsinki-NLP/opus-mt-tr-en"
english_tokenizer = AutoTokenizer.from_pretrained(english_model_name, cache_dir=cache_dir)
english_model = AutoModelForSeq2SeqLM.from_pretrained(english_model_name, cache_dir=cache_dir)

current_model = "turkish"  # Başlangıçta Türkçe-İngilizce çeviri modeli seçili olsun

# Çeviri yapacak fonksiyon
def translate_text(text, to_english):
    if to_english== "turkish":
        tokenizer = turkish_tokenizer
        model = turkish_model
    else:
        tokenizer = english_tokenizer
        model = english_model

    inputs = tokenizer.encode(text, return_tensors="pt")
    outputs = model.generate(inputs, max_length=1000)
    translated_text = clean_special_tokens(tokenizer.decode(outputs[0]), tokenizer)
    return translated_text

@app.route('/switch_model', methods=['GET'])
def switch_model():
    global current_model
    if current_model == "turkish":
        current_model = "english"
    else:
        current_model = "turkish"
    return "Model changed successfully."

def clean_special_tokens(text, tokenizer):
    # <pad> ve </s> etiketlerini temizleyelim
    text = text.replace(tokenizer.pad_token, "").replace(tokenizer.eos_token, "")
    return text.strip()

# index.html gösterme
@app.route('/', methods=['GET'])
def home():
    return render_template('index.html')

# Çeviri apisi
@app.route('/translate', methods=['POST'])
def translate():
    if request.method == 'POST':
        turkish_text = request.form['turkish_text']
        to_english = current_model

        translated_text = translate_text(turkish_text, to_english)
        return jsonify({"translated_text": translated_text})

if __name__ == '__main__':
    app.run(port=6161)

