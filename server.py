from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import uvicorn
from starlette.staticfiles import StaticFiles

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

coordinates_to_socket = {}

"""
   # if data['type'] == 'registration':
    #     coordinates_to_socket[data['coordinates']] = websocket
"""

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    # server listens for websocket connections on ws route
    print('connection open')
    await websocket.accept()
    await websocket.send_text('hello from server')

    data = await websocket.receive_text()
    print('data from client', data)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)