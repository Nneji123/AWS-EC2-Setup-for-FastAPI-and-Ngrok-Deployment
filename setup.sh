# Update and install requirements
sudo apt-get update
sudo apt install python3-pip
sudo apt install uvicorn
sudo apt install nginx
sudo cp -R fastapi_setup /etc/nginx/sites-enabled/
sudo service nginx restart
cd ~/AWS-EC2-Setup-for-FastAPI-and-Ngrok-Deployment
pip3 install -r requirements.txt
sudo kill -9 $(sudo lsof -t -i:80)
python3 -m uvicorn app:app --reload --port 8000

