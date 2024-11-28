CREATE TABLE "public".credentials
(
    id          serial             NOT NULL,
    username    varchar(16) UNIQUE NOT NULL,
    salt        varchar(32)        NOT NULL,
    hash_passwd varchar(32)        NOT NULL,
    ts_create   timestamp(0) DEFAULT CURRENT_TIMESTAMP,
    ts_update   timestamp    DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT pk_credentials PRIMARY KEY (id)
);