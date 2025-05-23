FROM apache/nifi:latest
COPY postgresql-42.7.5.jar /opt/nifi/nifi-current/lib/

USER root
# Copier les scripts dans le conteneur
COPY scripts/ /opt/nifi/scripts/

# Donner les bons droits à l'utilisateur NiFi
RUN chown -R nifi:nifi /opt/nifi/scripts/