sudo apt-get update
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
unzip ngrok-v3-stable-linux-amd64.tgz
ngrok config add-authtoken 29vr8YhWZ9CDHrUq2kr0CpUA0e8_6ik4hU5GjJZeAYagTH5i4
ngrok http 80
USE_NGROK=True uvicorn app:app --reload 8081