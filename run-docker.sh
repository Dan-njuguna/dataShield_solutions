#!/bin/bash

docker build -t backend -f /home/dan/Coding/dataShield_solutions/Dockerfile.backend .
docker run -p 8000:8000 backend

docker build -t frontend -f /home/dan/Coding/dataShield_solutions/Dockerfile.frontend .
docker run -p 3000:3000 frontend