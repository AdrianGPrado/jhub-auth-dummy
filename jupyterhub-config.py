import os


c.JupyterHub.confirm_no_ssl = True
c.JupyterHub.db_url = 'sqlite:////tmp/jupyterhub.sqlite'
c.JupyterHub.cookie_secret_file = '/tmp/jupyterhub_cookie_secret'

# # Do not use any authentication at all - any username / password will work.
c.JupyterHub.authenticator_class = 'dummyauthenticator.DummyAuthenticator'
# c.JupyterHub.authenticator_class = 'ldapauthenticator.LDAPAuthenticator'
#
# # ----------------------------------------------------------------------------
# # LDAP configuration
# # ----------------------------------------------------------------------------
#
# # Example: uid={username},ou=people,dc=wikimedia,dc=org
# c.LDAPAuthenticator.bind_dn_template = 'cn={username},cn=jupyterhub,dc=example,dc=org'
# c.LDAPAuthenticator.server_address = '127.0.0.1'
# c.LDAPAuthenticator.server_port = '636'
#
# # Use SSL to communicate with the LDAP server.
# c.LDAPAuthenticator.use_ssl = False
#
# # ----------------------------------------------------------------------------
# # LDAP configuration
# # ----------------------------------------------------------------------------
#
# # Path to the notebook directory for the single-user server.
# c.Spawner.notebook_dir = '/mnt/notebooks/%U'

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
# c.JupyterHub.spawner_class = 'kubernetes_spawner.KubernetesSpawner'
#
# # Kubernetes namespace to spawn user pods in.
# c.KubernetesSpawner.namespace = 'jupyterhub'
#
# c.KubernetesSpawner.singleuser_image_spec = ""
# c.KubernetesSpawner.pod_name_template = ""
# c.KubernetesSpawner.hub_connect_ip = ""
# c.KubernetesSpawner.verify_ssl = False
# c.KubernetesSpawner.hub_ip_from_service = 'jupyterhub'
# c.KubernetesSpawner.container_image = 'danielfrg/jupyterhub-kube-ldap-nfs-singleuser:0.1'
# c.KubernetesSpawner.persistent_volume_claim_name = 'jupyterhub-volume'
# c.KubernetesSpawner.persistent_volume_claim_path = '/mnt'


# ----------------------------------------------------------------------------
# Application configuration
# ----------------------------------------------------------------------------

# This is an application.

# The date format used by logging formatters for %(asctime)s
c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

# The Logging format template
c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

# Set the log level by value or name.
c.Application.log_level = 30
