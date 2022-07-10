sudo apt-get update
sudo apt-get install docker-ce docker-ce-cli containerd.io
sudo apt install nginx
# Official Latest Docker Install
curl -fsSL https://get.docker.com -o get-docker.sh
# Run the file
sudo sh get-docker.sh
wget https://bin.equinox.io/c/bNyj1mQVY4c/ngrok-v3-stable-linux-amd64.tgz
sudo tar -xvzf ngrok-v3-stable-linux-amd64.tgz
sudo ngrok authtoken 29vr8YhWZ9CDHrUq2kr0CpUA0e8_6ik4hU5GjJZeAYagTH5i4
USE_NGROK=True uvicorn app:app --reload --port 80
