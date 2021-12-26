# Steps to run this library on your local environment
This library can be used to translate speech in English into speech in Japanese
- Create DeepL api key and ibm watson speech to text api key
  - [DeepL](https://www.deepl.com/ja/translator)
  - [IBM](https://www.ibm.com/jp-ja/cloud/watson-text-to-speech)
- Create local settings.py and set variables: 
  - DEEPL_APIKEY = deepL api key
  - IBM_WATSON_API_KEY = ibm watson speech to text api 
- Install [anaconda](https://www.anaconda.com/products/individual#macos)
- Install brew
```
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
- Create new conda environment
```
conda create -n trans python=3.8.12
```
- Install requirements.txt
```
pip install -r requirements.txt
```
- Install portaudio through brew
```
brew install portaudio
```
- Install pyaudio through conda
```
conda install -c anaconda pyaudio
``` 
- Run main.py
```
python main.py
```
