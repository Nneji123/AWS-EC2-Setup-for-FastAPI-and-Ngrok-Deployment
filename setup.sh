# Update and install requirements
sudo apt-get update
sudo apt install -y python3-pip nginx
sudo apt install -y uvicorn
sudo cp -R fastapi_setup /etc/nginx/sites-enabled/
sudo service nginx restart
cd ~/AWS-EC2-Setup-for-FastAPI-and-Ngrok-Deployment
pip3 install -r requirements.txt
sudo kill -9 $(sudo lsof -t -i:80)
sudo service nginx restart
python3 -m uvicorn app:app --reload --host 0.0.0.0

