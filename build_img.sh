#!/bin/bash

docker build . -t gcr.io/assistant-381719/assistant
docker push gcr.io/assistant-381719/assistant
