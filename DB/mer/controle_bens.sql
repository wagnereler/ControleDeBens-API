DROP TABLE empresa_telefone;

DROP TABLE usuario_telefone;

DROP TABLE log_acao;

DROP TABLE log_acesso;

DROP TABLE usuario_setor;

DROP TABLE usuario_papel;

DROP TABLE empresa_usuario;

DROP TABLE telefone;

DROP TABLE movimentacao;

DROP TABLE usuario;

DROP TABLE papel_rotina;

DROP TABLE papel;

DROP TABLE rotina;

DROP TABLE bem;

DROP TABLE motivo_baixa;

DROP TABLE setor;

DROP TABLE empresa;

DROP TABLE endereco;

DROP TABLE logradouro;

DROP TABLE municipio;

DROP TABLE estado;

CREATE TABLE bem (
    id               SERIAL NOT NULL,
    id_setor         INTEGER NOT NULL,
    id_empesa        INTEGER NOT NULL,
    plaqueta         VARCHAR(30),
    data_compra      DATE,
    data_tombamento  DATE,
    data_baixa       DATE,
    valor_compra     DECIMAL(10, 2),
    valor_depreciado DECIMAL(10, 2),
    valor_contabil   DECIMAL(10, 2),
    data_cadastro    DATE,
    data_atualizacao DATE,
    id_motivo_baixa  INTEGER NOT NULL
);

ALTER TABLE bem ADD CONSTRAINT bem_pk PRIMARY KEY ( id );

CREATE TABLE empresa (
    id            SERIAL NOT NULL,
    nome_fantasia VARCHAR(60),
    razao_social  VARCHAR(100),
    cnpj          VARCHAR(14),
    id_enderco    INTEGER NOT NULL
);

ALTER TABLE empresa ADD CONSTRAINT empresa_pk PRIMARY KEY ( id );

CREATE TABLE empresa_telefone (
    id          SERIAL NOT NULL,
    id_empresa  INTEGER NOT NULL,
    id_telefone INTEGER,
    telefone_id INTEGER NOT NULL
);

ALTER TABLE empresa_telefone ADD CONSTRAINT empresa_telefone_pk PRIMARY KEY ( id );

CREATE TABLE empresa_usuario (
    id         SERIAL NOT NULL,
    id_empresa INTEGER NOT NULL,
    id_usuario INTEGER NOT NULL
);

ALTER TABLE empresa_usuario ADD CONSTRAINT empresa_usuario_pk PRIMARY KEY ( id );

CREATE TABLE endereco (
    id            SERIAL NOT NULL,
    id_muncipo    INTEGER NOT NULL,
    id_estado     INTEGER NOT NULL,
    id_logradouro INTEGER NOT NULL,
    endereco      VARCHAR(60),
    numero        VARCHAR(10),
    complemento   VARCHAR(60),
    bairro        VARCHAR(60),
    cep           VARCHAR(8)
);

ALTER TABLE endereco ADD CONSTRAINT endereco_pk PRIMARY KEY ( id );

CREATE TABLE estado (
    id          SERIAL NOT NULL,
    uf          CHAR(2),
    nome        VARCHAR(40),
    codigo_ibge VARCHAR(2)
);

ALTER TABLE estado ADD CONSTRAINT estado_pk PRIMARY KEY ( id );

CREATE TABLE log_acao (
    id        SERIAL NOT NULL,
    id_usurio INTEGER NOT NULL,
    id_rotina INTEGER,
    acao      VARCHAR(255),
    data_acao DATE,
    status    INTEGER
);

ALTER TABLE log_acao ADD CONSTRAINT log_acao_pk PRIMARY KEY ( id );

CREATE TABLE log_acesso (
    id          SERIAL NOT NULL,
    id_usurio   INTEGER NOT NULL,
    data_acesso DATE,
    status      INTEGER
);

ALTER TABLE log_acesso ADD CONSTRAINT log_acesso_pk PRIMARY KEY ( id );

CREATE TABLE logradouro (
    id          SERIAL NOT NULL,
    nome        VARCHAR(60),
    codigo_ibge VARCHAR(3)
);

ALTER TABLE logradouro ADD CONSTRAINT logradouo_pk PRIMARY KEY ( id );

CREATE TABLE motivo_baixa (
    id     SERIAL NOT NULL,
    motivo VARCHAR(60)
);

ALTER TABLE motivo_baixa ADD CONSTRAINT motivo_baixa_pk PRIMARY KEY ( id );

CREATE TABLE movimentacao (
    id                 SERIAL NOT NULL,
    id_bem             INTEGER NOT NULL,
    data_movimentacao  DATE,
    id_setor_saida     INTEGER NOT NULL,
    id_setor_entrada   INTEGER NOT NULL,
    id_empresa_saida   INTEGER NOT NULL,
    id_empresa_entrada INTEGER NOT NULL,
    id_usuario         INTEGER NOT NULL
);

ALTER TABLE movimentacao ADD CONSTRAINT movimentacao_pk PRIMARY KEY ( id );

CREATE TABLE municipio (
    id          SERIAL NOT NULL,
    id_estado   INTEGER NOT NULL,
    nome        VARCHAR(100),
    codigo_ibge VARCHAR(8)
);

ALTER TABLE municipio ADD CONSTRAINT municipio_pk PRIMARY KEY ( id );

CREATE TABLE papel (
    id        SERIAL NOT NULL,
    id_rotina INTEGER,
    nome      VARCHAR(60)
);

ALTER TABLE papel ADD CONSTRAINT papel_pk PRIMARY KEY ( id );

CREATE TABLE papel_rotina (
    id        SERIAL NOT NULL,
    id_papel  INTEGER NOT NULL,
    id_rotina INTEGER NOT NULL
);

ALTER TABLE papel_rotina ADD CONSTRAINT papel_rotina_pk PRIMARY KEY ( id );

CREATE TABLE rotina (
    id   SERIAL NOT NULL,
    nome VARCHAR(60)
);

ALTER TABLE rotina ADD CONSTRAINT rotina_pk PRIMARY KEY ( id );

CREATE TABLE setor (
    id         INTEGER NOT NULL,
    id_empresa INTEGER NOT NULL,
    nome       VARCHAR(100)
);

ALTER TABLE setor ADD CONSTRAINT setor_pk PRIMARY KEY ( id );

CREATE TABLE telefone (
    id     SERIAL NOT NULL,
    ddi    VARCHAR(4) DEFAULT '+55',
    dd     VARCHAR(2),
    numero VARCHAR(9),
    tipo   INTEGER
);

ALTER TABLE telefone ADD CONSTRAINT telefone_pk PRIMARY KEY ( id );

CREATE TABLE usuario (
    id               SERIAL NOT NULL,
    nome             VARCHAR(100) NOT NULL,
    cpf              VARCHAR(11) NOT NULL,
    usuario          VARCHAR(40) NOT NULL,
    email            VARCHAR(60) NOT NULL,
    id_endereco      INTEGER NOT NULL,
    data_cadastro    DATE,
    data_atualizacao DATE
);

ALTER TABLE usuario ADD CONSTRAINT usuario_pk PRIMARY KEY ( id );

ALTER TABLE usuario ADD CONSTRAINT un_usuario_cpf UNIQUE ( cpf );

ALTER TABLE usuario ADD CONSTRAINT un_usuario_cpf_usuaro UNIQUE ( usuario );

ALTER TABLE usuario ADD CONSTRAINT un_usuario_email UNIQUE ( email );

CREATE TABLE usuario_papel (
    id         SERIAL NOT NULL,
    id_usuario INTEGER NOT NULL,
    id_papel   INTEGER NOT NULL
);

ALTER TABLE usuario_papel ADD CONSTRAINT usuario_papel_pk PRIMARY KEY ( id );

CREATE TABLE usuario_setor (
    id        SERIAL NOT NULL,
    id_setor  INTEGER NOT NULL,
    id_usuaro INTEGER NOT NULL
);

ALTER TABLE usuario_setor ADD CONSTRAINT usuario_setor_pk PRIMARY KEY ( id );

CREATE TABLE usuario_telefone (
    id          SERIAL NOT NULL,
    id_usuario  INTEGER NOT NULL,
    id_telefone INTEGER NOT NULL
);

ALTER TABLE usuario_telefone ADD CONSTRAINT usuario_telefone_pk PRIMARY KEY ( id );

ALTER TABLE bem
    ADD CONSTRAINT bem_empresa_fk FOREIGN KEY ( id_empesa )
        REFERENCES empresa ( id );

ALTER TABLE bem
    ADD CONSTRAINT bem_motivo_baixa_fk FOREIGN KEY ( id_motivo_baixa )
        REFERENCES motivo_baixa ( id );

ALTER TABLE bem
    ADD CONSTRAINT bem_setor_fk FOREIGN KEY ( id_setor )
        REFERENCES setor ( id );

ALTER TABLE empresa
    ADD CONSTRAINT empresa_endereco_fk FOREIGN KEY ( id_enderco )
        REFERENCES endereco ( id );

ALTER TABLE empresa_telefone
    ADD CONSTRAINT empresa_telefone_empresa_fk FOREIGN KEY ( id_empresa )
        REFERENCES empresa ( id );

ALTER TABLE empresa_telefone
    ADD CONSTRAINT empresa_telefone_telefone_fk FOREIGN KEY ( telefone_id )
        REFERENCES telefone ( id );

ALTER TABLE empresa_usuario
    ADD CONSTRAINT empresa_usuario_empresa_fk FOREIGN KEY ( id_empresa )
        REFERENCES empresa ( id );

ALTER TABLE empresa_usuario
    ADD CONSTRAINT empresa_usuario_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id );

ALTER TABLE endereco
    ADD CONSTRAINT endereco_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado ( id );

ALTER TABLE endereco
    ADD CONSTRAINT endereco_logradouo_fk FOREIGN KEY ( id_logradouro )
        REFERENCES logradouro ( id );

ALTER TABLE endereco
    ADD CONSTRAINT endereco_municipio_fk FOREIGN KEY ( id_muncipo )
        REFERENCES municipio ( id );

ALTER TABLE log_acao
    ADD CONSTRAINT log_acao_usuario_fk FOREIGN KEY ( id_usurio )
        REFERENCES usuario ( id );

ALTER TABLE log_acesso
    ADD CONSTRAINT log_acesso_usuario_fk FOREIGN KEY ( id_usurio )
        REFERENCES usuario ( id );

ALTER TABLE movimentacao
    ADD CONSTRAINT movimentacao_bem_fk FOREIGN KEY ( id_bem )
        REFERENCES bem ( id );

ALTER TABLE movimentacao
    ADD CONSTRAINT movimentacao_empresa_entrada_fk FOREIGN KEY ( id_empresa_entrada )
        REFERENCES empresa ( id );

ALTER TABLE movimentacao
    ADD CONSTRAINT movimentacao_empresa_saida_fk FOREIGN KEY ( id_empresa_saida )
        REFERENCES empresa ( id );

ALTER TABLE movimentacao
    ADD CONSTRAINT movimentacao_setor_entrada_fk FOREIGN KEY ( id_setor_entrada )
        REFERENCES setor ( id );

ALTER TABLE movimentacao
    ADD CONSTRAINT movimentacao_setor_saida_fk FOREIGN KEY ( id_setor_saida )
        REFERENCES setor ( id );

ALTER TABLE movimentacao
    ADD CONSTRAINT movimentacao_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id );

ALTER TABLE municipio
    ADD CONSTRAINT municipio_estado_fk FOREIGN KEY ( id_estado )
        REFERENCES estado ( id );

ALTER TABLE papel_rotina
    ADD CONSTRAINT papel_rotina_papel_fk FOREIGN KEY ( id_papel )
        REFERENCES papel ( id );

ALTER TABLE papel_rotina
    ADD CONSTRAINT papel_rotina_rotina_fk FOREIGN KEY ( id_rotina )
        REFERENCES rotina ( id );

ALTER TABLE setor
    ADD CONSTRAINT setor_empresa_fk FOREIGN KEY ( id_empresa )
        REFERENCES empresa ( id );

ALTER TABLE usuario
    ADD CONSTRAINT usuario_endereco_fk FOREIGN KEY ( id_endereco )
        REFERENCES endereco ( id );

ALTER TABLE usuario_papel
    ADD CONSTRAINT usuario_papel_papel_fk FOREIGN KEY ( id_papel )
        REFERENCES papel ( id );

ALTER TABLE usuario_papel
    ADD CONSTRAINT usuario_papel_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id );

ALTER TABLE usuario_setor
    ADD CONSTRAINT usuario_setor_setor_fk FOREIGN KEY ( id_setor )
        REFERENCES setor ( id );

ALTER TABLE usuario_setor
    ADD CONSTRAINT usuario_setor_usuario_fk FOREIGN KEY ( id_usuaro )
        REFERENCES usuario ( id );

ALTER TABLE usuario_telefone
    ADD CONSTRAINT usuario_telefone_telefone_fk FOREIGN KEY ( id_telefone )
        REFERENCES telefone ( id );

ALTER TABLE usuario_telefone
    ADD CONSTRAINT usuario_telefone_usuario_fk FOREIGN KEY ( id_usuario )
        REFERENCES usuario ( id );
