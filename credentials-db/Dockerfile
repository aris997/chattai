FROM postgres:17

# Give the init SQL queries
VOLUME [ "/docker-entrypoint-initdb.d/createTables.sql", "/run/sercrets" ]

# Give the secrets (I love redundancy) 
# COPY ./secrets/ /run/secrets/
# instead of COPY map the volume to the same path in the container

# Tell it where the hell is it
ENV POSTGRES_PASSWORD_FILE=/run/secrets/postgres-passwd
ENV POSTGRES_DB_FILE=/run/secrets/postgres-database

# Sono un italiano vero
RUN localedef -i it_IT -c -f UTF-8 -A /usr/share/locale/locale.alias it_IT.UTF-8
ENV LANG=it_IT.utf8

# un'ora, non è documentato sto fatto p*******o
USER postgres
