FROM jupyterhub/jupyterhub

RUN apt-get update && apt-get install -y curl

# Authentification
RUN pip install jupyterhub-dummyauthenticator \
                jupyterhub-kubespawner
RUN /opt/conda/bin/conda install --yes -c conda-forge pycurl
