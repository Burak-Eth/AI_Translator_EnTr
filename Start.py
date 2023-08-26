import subprocess
import time
import webbrowser

def start_flask_app():
    # translator.py'yi çalıştırın
    process = subprocess.Popen(["python", "translator.py"])
    # 20 saniye bekleyin
    time.sleep(60)
    # localhost:6161'i web tarayıcısında açın
    webbrowser.open("http://localhost:6161")

if __name__ == "__main__":
    start_flask_app()
