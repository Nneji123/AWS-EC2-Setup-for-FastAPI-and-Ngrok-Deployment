# How to Deploy FastAPI Application with AWS EC2 and Ngrok
This repository contains a shell script and an example of a FastAPI application. The shell script is used to deploy the application on the AWS EC2 instance and expose the IP address so that the application can be seen on the internet.

## Steps on how to deploy application using the script
### 1. Fork this repository
### 2. Login to AWS, create a new AWS EC2 instance and make sure to allow outside traffic as shown in the screenshots below:
![Screenshot (150)](https://user-images.githubusercontent.com/101701760/178163373-e4bb2c92-0f47-4a22-9556-dfc470fd7e8a.png)
![Screenshot (156)](https://user-images.githubusercontent.com/101701760/178163392-3c9fc8ec-e58a-420d-a6bb-2885215d8105.png)
### 3. When the instance has been launched, copy the Public IP address of your instance and paste it in the 'fastapi_setup' file of your cloned repository as shown below 
![Screenshot (163)](https://user-images.githubusercontent.com/101701760/178163457-2e156379-b542-4d24-aebf-e202dd44ae2c.png)
![Screenshot (164)](https://user-images.githubusercontent.com/101701760/178163536-918818ee-563d-4b0d-a5ec-5c265a75b2b4.png)
### 4. Connect to your instance and clone your forked repository, an example in my case:
```bash
git clone https://github.com/Nneji123/AWS-EC2-Setup-for-FastAPI-and-Ngrok-Deployment.git
```
### 5. cd into your repository which is probably named 'AWS-EC2-Setup-for-FastAPI-and-Ngrok-Deployment'. You can do that by running:
```bash
cd AWS-EC2-Setup-for-FastAPI-and-Ngrok-Deployment
```
### 6. Then run the setup.sh file to get your application up and running:
```bash
./fastapi-setup.sh
```
### You can then view the application by going to your Public IP's location, an example in my case will be:
http://3.95.202.74:80/

