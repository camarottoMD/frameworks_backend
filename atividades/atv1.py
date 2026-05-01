from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.post("/autenticar")
def auth(payload):
    if payload.get('token') == '123t' and payload.get('user') == 'admin' and payload.get('pass') == 'ad123':
        return {
            'success': True,
            'message': 'Credenciais corretas'
        }
    raise Exception("Dados incorretos. Verifique e tente novamente")

if __name__ == "__main__":
    uvicorn.run("__main__:app", host="localhost", port=8000)