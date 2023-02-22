# BAE 146 Web Based Annunciator Panel

This reproduces the BAE 146 annunciator panel from MSFS2020 in a webpage, for use on a tablet or phone.

![2023-02-19 20_58_31-Microsoft Flight Simulator - 1 30 12 0](https://user-images.githubusercontent.com/131580/220485761-7dec152e-67d8-4938-9772-74d09ac3e117.png)

![2023-02-21 15_50_03-Socket IO Demo — Mozilla Firefox](https://user-images.githubusercontent.com/131580/220485540-5196750c-4ab5-43ad-b417-eb5f85024dd4.png)

This setup uses the python-based mobiflight simconnect libraries ([source](https://github.com/Koseng/MSFSPythonSimConnectMobiFlightExtension/tree/main/prototype)) to subscribe to the status of the annunciator panel. It then starts a webserver hosting a javascript client which is displayed via a browser. The two communicator via socketio (i.e. websockets), and should update in real time.

## Setup & Run

This has to run under Windows for it to be able to talk to MSFS2020.

```
python -m venv .
.\Scripts\Activate.ps1
pip install -r .\requirements.txt
uvicorn --reload app:app
```

http://127.0.0.1:8000/
