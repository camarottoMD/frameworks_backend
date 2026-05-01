"""
vamos utilizar uvicorn e fast api no projeto
"""
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import uvicorn 
 
app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def fazer_nada():
    #raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
    return "<h1>SSSSSSSSS</h1>" #carga de dados -> é o return da rota, o padrão que o json vai voltar

"""@ quando o app receber uma requisição do tipo .get, vai pra rota nada e vai executar a função que esta abaixo

"""

if __name__ == "__main__":
    uvicorn.run('__main__:app', host='localhost', port=8080) #host, para onde vai subir