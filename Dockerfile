# FROM jupyterhub/jupyterhub
#
# RUN apt-get update && apt-get install -y curl
#
# # Authentification
# RUN pip install jupyterhub-dummyauthenticator \
#                 jupyterhub-kubespawner
# RUN /opt/conda/bin/conda install --yes -c conda-forge pycurl
FROM jupyterhub/jupyterhub

RUN apt-get update && apt-get install -y curl
RUN pip install jupyterhub-dummyauthenticator

RUN pip install git+git://github.com/danielfrg/jupyterhub-kubernetes_spawner.git@0.1.1

USER root
COPY startup.sh /startup.sh
RUN chmod +x /startup.sh

CMD ["/startup.sh"]
