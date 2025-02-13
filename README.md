# fast-server
this is a small example to show data being send back and forth between a server
and a browser client

run the code and look at the logs in the chrome console and in the 
server output

## Setup + Run
```bash
python -m virtualenv venv
source venv/bin/activate

pip install fastapi
pip install uvicorn
pip install websockets

python server.py
```
## Visit
http://0.0.0.0:8000/static/index.html?hi=yo