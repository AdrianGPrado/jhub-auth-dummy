#!/bin/bash


docker run --name jupyterhub-http \
           --hostname jupyterhub-http \
           --detach jupyterhub/configurable-http-proxy:2.0.1

docker run --name jupyterhub \
           --hostname jupyterhub \
           --publish 7800:8000 \
           --volume ${PWD}/jupyterhub-config.py:/srv/jupyterhub/jupyterhub-config.py \
           --detach jupyterhub-auth-ldap:latest
