CREATE TABLE answer
(
    id               SERIAL PRIMARY KEY,
    submission_time  TIMESTAMP DEFAULT LOCALTIMESTAMP NOT NULL,
    vote_number      INTEGER NOT NULL,
    question_id      INTEGER UNIQUE         NOT NULL,
    message_type     CHARACTER VARYING(255) NOT NULL,
    image_type       bytea 
);

CREATE TABLE question
(
    id               SERIAL PRIMARY KEY,
    submission_time  TIMESTAMP DEFAULT LOCALTIMESTAMP NOT NULL,
    view_number      INTEGER NOT NULL,
    vote_number      INTEGER NOT NULL,
    title            CHARACTER VARYING(255) NOT NULL,
    message_type     CHARACTER VARYING(255) NOT NULL,
    image_type       bytea
);