--
-- PostgreSQL database dump
--

-- Dumped from database version 14.4
-- Dumped by pg_dump version 14.4

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

ALTER TABLE IF EXISTS ONLY public.question DROP CONSTRAINT IF EXISTS question_member_member_id_fk;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS fk_tag_id;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS fk_question_id;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS fk_question_id;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS fk_question_id;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS fk_answer_id;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS comment_member_member_id_fk;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS answer_member_member_id_fk;
DROP INDEX IF EXISTS public.question_member_id_index;
DROP INDEX IF EXISTS public.member_user_name_uindex;
ALTER TABLE IF EXISTS ONLY public.tag DROP CONSTRAINT IF EXISTS pk_tag_id;
ALTER TABLE IF EXISTS ONLY public.question_tag DROP CONSTRAINT IF EXISTS pk_question_tag_id;
ALTER TABLE IF EXISTS ONLY public.question DROP CONSTRAINT IF EXISTS pk_question_id;
ALTER TABLE IF EXISTS ONLY public.comment DROP CONSTRAINT IF EXISTS pk_comment_id;
ALTER TABLE IF EXISTS ONLY public.answer DROP CONSTRAINT IF EXISTS pk_answer_id;
ALTER TABLE IF EXISTS ONLY public.member DROP CONSTRAINT IF EXISTS member_pk;
ALTER TABLE IF EXISTS public.tag ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.question ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.member ALTER COLUMN member_id DROP DEFAULT;
ALTER TABLE IF EXISTS public.comment ALTER COLUMN id DROP DEFAULT;
ALTER TABLE IF EXISTS public.answer ALTER COLUMN id DROP DEFAULT;
DROP SEQUENCE IF EXISTS public.tag_id_seq;
DROP TABLE IF EXISTS public.tag;
DROP TABLE IF EXISTS public.question_tag;
DROP SEQUENCE IF EXISTS public.question_id_seq;
DROP TABLE IF EXISTS public.question;
DROP SEQUENCE IF EXISTS public.member_member_id_seq;
DROP TABLE IF EXISTS public.member;
DROP SEQUENCE IF EXISTS public.comment_id_seq;
DROP TABLE IF EXISTS public.comment;
DROP SEQUENCE IF EXISTS public.answer_id_seq;
DROP TABLE IF EXISTS public.answer;
SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: answer; Type: TABLE; Schema: public; Owner: ania
--

CREATE TABLE public.answer (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    vote_number integer,
    question_id integer,
    message text,
    image text,
    member_id integer
);


ALTER TABLE public.answer OWNER TO macie;

--
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: ania
--

CREATE SEQUENCE public.answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answer_id_seq OWNER TO macie;

--
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ania
--

ALTER SEQUENCE public.answer_id_seq OWNED BY public.answer.id;


--
-- Name: comment; Type: TABLE; Schema: public; Owner: ania
--

CREATE TABLE public.comment (
    id integer NOT NULL,
    question_id integer,
    answer_id integer,
    message text,
    submission_time timestamp without time zone,
    edited_count integer,
    member_id integer
);


ALTER TABLE public.comment OWNER TO macie;

--
-- Name: comment_id_seq; Type: SEQUENCE; Schema: public; Owner: ania
--

CREATE SEQUENCE public.comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comment_id_seq OWNER TO macie;

--
-- Name: comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ania
--

ALTER SEQUENCE public.comment_id_seq OWNED BY public.comment.id;


--
-- Name: member; Type: TABLE; Schema: public; Owner: ania
--

CREATE TABLE public.member (
    member_id integer NOT NULL,
    user_name text NOT NULL,
    password text NOT NULL,
    registration_date timestamp without time zone DEFAULT now() NOT NULL
);


ALTER TABLE public.member OWNER TO macie;

--
-- Name: member_member_id_seq; Type: SEQUENCE; Schema: public; Owner: ania
--

CREATE SEQUENCE public.member_member_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.member_member_id_seq OWNER TO macie;

--
-- Name: member_member_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ania
--

ALTER SEQUENCE public.member_member_id_seq OWNED BY public.member.member_id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: ania
--

CREATE TABLE public.question (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    view_number integer,
    vote_number integer,
    title text,
    message text,
    image text,
    member_id integer
);


ALTER TABLE public.question OWNER TO macie;

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: ania
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_id_seq OWNER TO macie;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ania
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- Name: question_tag; Type: TABLE; Schema: public; Owner: ania
--

CREATE TABLE public.question_tag (
    question_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.question_tag OWNER TO macie;

--
-- Name: tag; Type: TABLE; Schema: public; Owner: ania
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    name text
);


ALTER TABLE public.tag OWNER TO macie;

--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: ania
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO macie;

--
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: ania
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.answer ALTER COLUMN id SET DEFAULT nextval('public.answer_id_seq'::regclass);


--
-- Name: comment id; Type: DEFAULT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.comment ALTER COLUMN id SET DEFAULT nextval('public.comment_id_seq'::regclass);


--
-- Name: member member_id; Type: DEFAULT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.member ALTER COLUMN member_id SET DEFAULT nextval('public.member_member_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: ania
--

COPY public.answer (id, submission_time, vote_number, question_id, message, image, member_id) FROM stdin;
1	2017-04-28 16:49:00	4	1	You need to use brackets: my_list = []	\N	\N
2	2017-04-25 14:42:00	35	1	Look it up in the Python docs	images/image2.jpg	\N
3	2022-07-06 09:38:00	3	0	You can either use [] to start a list or use list() function.		\N
5	2022-07-07 21:28:41	1	3	You can use ORDER BY query.		\N
\.


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: ania
--

COPY public.comment (id, question_id, answer_id, message, submission_time, edited_count, member_id) FROM stdin;
1	0	\N	Please clarify the question as it is too vague!	2017-05-01 05:49:00	\N	\N
2	\N	1	I think you could use my_list = list() as well.	2017-05-02 16:55:00	\N	\N
3	1	3	Lists are so useful in Python!	2022-07-07 17:55:50	0	\N
4	1	1	My Comment	2022-07-07 18:15:41.530106	0	\N
5	0	3	My Comment	2022-07-07 18:18:12.902073	0	\N
6	0	3	It's just perfect answer!	2022-07-07 18:21:36	0	\N
7	0	3	Have to delete my fake comment :)	2022-07-07 18:24:01	0	\N
\.


--
-- Data for Name: member; Type: TABLE DATA; Schema: public; Owner: ania
--

COPY public.member (member_id, user_name, password, registration_date) FROM stdin;
1	pussinboots	tobedone	2022-08-02 17:34:03.63429
2	robinhood	tobedone	2022-08-02 17:35:19.365956
\.


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: ania
--

COPY public.question (id, submission_time, view_number, vote_number, title, message, image, member_id) FROM stdin;
1	2017-04-29 09:19:00	15	9	Wordpress loading multiple jQuery Versions	I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();\r\n\r\nI could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.\r\n\r\nBUT in my theme i also using jquery via webpack so the loading order is now following:\r\n\r\njquery\r\nbooklet\r\napp.js (bundled file with webpack, including jquery)	images/image1.png	1
3	2022-07-06 23:29:32	0	1	How to sort in SQL	How to sort by specific column in SQL query?		2
2	2017-05-01 10:41:00	1364	57	Drawing canvas with an image picked with Cordova Camera Plugin	I'm getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I'm on IOS, it throws errors such as cross origin issue, or that I'm trying to use an unknown format.\r\n	\N	2
0	2017-04-28 08:29:00	29	7	How to make lists in Python?	I am totally new to this, any hints?	\N	1
\.


--
-- Data for Name: question_tag; Type: TABLE DATA; Schema: public; Owner: ania
--

COPY public.question_tag (question_id, tag_id) FROM stdin;
0	1
1	3
2	3
\.


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: ania
--

COPY public.tag (id, name) FROM stdin;
1	python
2	sql
3	css
\.


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ania
--

SELECT pg_catalog.setval('public.answer_id_seq', 5, true);


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ania
--

SELECT pg_catalog.setval('public.comment_id_seq', 7, true);


--
-- Name: member_member_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ania
--

SELECT pg_catalog.setval('public.member_member_id_seq', 2, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ania
--

SELECT pg_catalog.setval('public.question_id_seq', 3, true);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: ania
--

SELECT pg_catalog.setval('public.tag_id_seq', 3, true);


--
-- Name: member member_pk; Type: CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.member
    ADD CONSTRAINT member_pk PRIMARY KEY (member_id);


--
-- Name: answer pk_answer_id; Type: CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT pk_answer_id PRIMARY KEY (id);


--
-- Name: comment pk_comment_id; Type: CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT pk_comment_id PRIMARY KEY (id);


--
-- Name: question pk_question_id; Type: CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT pk_question_id PRIMARY KEY (id);


--
-- Name: question_tag pk_question_tag_id; Type: CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT pk_question_tag_id PRIMARY KEY (question_id, tag_id);


--
-- Name: tag pk_tag_id; Type: CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT pk_tag_id PRIMARY KEY (id);


--
-- Name: member_user_name_uindex; Type: INDEX; Schema: public; Owner: ania
--

CREATE UNIQUE INDEX member_user_name_uindex ON public.member USING btree (user_name);


--
-- Name: question_member_id_index; Type: INDEX; Schema: public; Owner: ania
--

CREATE INDEX question_member_id_index ON public.question USING btree (member_id);


--
-- Name: answer answer_member_member_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT answer_member_member_id_fk FOREIGN KEY (member_id) REFERENCES public.member(member_id);


--
-- Name: comment comment_member_member_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT comment_member_member_id_fk FOREIGN KEY (member_id) REFERENCES public.member(member_id);


--
-- Name: comment fk_answer_id; Type: FK CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_answer_id FOREIGN KEY (answer_id) REFERENCES public.answer(id);


--
-- Name: answer fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: comment fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag fk_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_tag_id FOREIGN KEY (tag_id) REFERENCES public.tag(id);


--
-- Name: question question_member_member_id_fk; Type: FK CONSTRAINT; Schema: public; Owner: ania
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT question_member_member_id_fk FOREIGN KEY (member_id) REFERENCES public.member(member_id);


--
-- PostgreSQL database dump complete
--

