# AI_Translator_EnTr
Utilized Helsinki NLP (Natural Language Processing) AI models to develop a bidirectional English-Turkish and Turkish-English translation software. Operates offline and runs as a Flask web app. 

![image](https://github.com/Burak-Eth/AI_Translator_EnTr/assets/75943885/55a964a5-6d56-44c9-872f-beb4e3b8b958)


---

**Installing Necessary Libraries**

<b> To install the necessary dependencies using the requirements.txt file, follow these instructions: </b>

  1. Open a terminal or command prompt on your system.
  2. Navigate to the directory where your Python script and requirements.txt file are located. You can use the cd command to change directories.
  3. Run the following command to install the required packages using pip:
     
     ```

     pip install -r requirements.txt

     ```

---

**Starting the Program**

Run Translator.py file for the initial setup. It will download the required models to the program directory on the first run. Afterward, the Flask server will start in the command prompt. Upon completion, two folders will be created in your directory as follows:

![image](https://github.com/Burak-Eth/AI_Translator_EnTr/assets/75943885/b2e70cc2-f688-4b02-98ba-93f409c512ca)

After the Flask server is launched in the command prompt, simply navigate to localhost:6161 in your browser. For automation, an optional start.py file is provided. Running start.py initiates the Flask server and automatically opens localhost:6161 in your browser after a 60-second delay.

---

**Changing max output lenght** 

If you need to translate longer texts (exceeding 1000 characters), open Translator.py and replace the variable seen in the image below with your desired value in the code.

![image](https://github.com/Burak-Eth/AI_Translator_EnTr/assets/75943885/f67a61f0-545d-49a5-ad2c-2e3eb0340ad7)

---

**Port Conflict** 
In case of port conflict, use the command below by ***running PowerShell as an administrator***:

```
Stop-Process -Id (Get-NetTCPConnection -LocalPort 6161).OwningProcess
```

---

***Do NOT MOVE or DELETE program model files. Otherwise, the program will reload model files. If you don't delete the model files, the program can work completely offline.***


