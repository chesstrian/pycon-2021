# Pycon 2021

Hello World project with [Sanic](https://sanic.readthedocs.io/en/stable/)

## Run project
```bash
python main.py
```

## Check
```bash
pip install -r requirements.txt
curl http://localhost:8000/
```
```json
{"hello":"Strange!"}
```
---
```bash
curl http://localhost:8000/?iam=Chesstrian
```
```json
{"hello":"Chesstrian!"}
```
