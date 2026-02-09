# OCR Engine Developed using paddleOCR
OCR Engine for extracting and parceing texts from pdf and image

## Pre-requisite 
- Python 3.11 should be installed on your system
- The project uses Ollama api for structuring OCR output

## Installation
- Clone repository
``` 
git clone <repo_id>
```
- Create environment 
```
python -m venv env
# activate your environment
pip install paddlepaddle-gpu==3.2.0 -i https://www.paddlepaddle.org.cn/packages/stable/cu126/
pip install -r requirements.txt
```
`Note: There might be incompatability issue with paddlepaddle-OCR langchain and langchain-ollama. The project fix it by modifing the source code for paddle-ocr langchain usage `

- Running OCR Inference
```
# for single document
python app/main.py --mode single --file "./absolute/path/to/document.jpg"
# for api inferencing
python  app/_main.py --mode api --port 8000
```


