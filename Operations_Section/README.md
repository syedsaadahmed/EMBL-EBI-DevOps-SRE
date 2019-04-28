# Server Monitoring Via Prometheus and Docker

For monitoring a server memory, CPU, disk and other stats, we are here using Docker, Prometheus and Grafana in our whole stack.
In particular, we have used prometheus an open-source monitoring system with a dimensional data model, flexible query language, efficient time series database and modern alerting approach. for keeping the stack in separate containers and spaces we have kept every service in a separate docker container. Furthermore for scraping the metrics we have used a node-exporter which was provided by the community.

# Pre-requisites, requirements & Compiling the Stack

One must have docker and docker-compose intalled in his local system for deploying this stack easily.

## Installing Docker

```curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -```
```sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"```
```sudo apt-get update```
```sudo apt-get install -y docker-ce```
```sudo systemctl status docker```

## Installing docker-compose

```sudo curl -L https://github.com/docker/compose/releases/download/1.18.0/docker-compose-`uname -s`-`uname -m` -o /usr/local/bin/docker-compose```

```sudo chmod +x /usr/local/bin/docker-compose```

```docker-compose --version```

## Running the monitoring stack

sudo docker-compose up -d

It will deploy whole stack, no need of any manual or human intervention. 

## Checking the Grafana User Interface

https://localhost:3000/

Credentials are (username:admin & Password:admin), you can change it in docker-compose.yml file as desired.


# Why Docker, Prometheus and Grafana