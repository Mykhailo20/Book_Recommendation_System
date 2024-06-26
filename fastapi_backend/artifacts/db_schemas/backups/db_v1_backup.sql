PGDMP         )                |           Book_Recommendation_System    15.2    15.2                0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false                       0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false                       0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false                       1262    107788    Book_Recommendation_System    DATABASE     �   CREATE DATABASE "Book_Recommendation_System" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Ukrainian_Ukraine.1251';
 ,   DROP DATABASE "Book_Recommendation_System";
                mykhailo_lozinskyi    false            H           1247    107790 
   url_domain    DOMAIN     �   CREATE DOMAIN public.url_domain AS character varying(2048)
	CONSTRAINT url_domain_check CHECK (((VALUE)::text ~ '^https?://[^\s/$.?#].[^\s]*$'::text));
    DROP DOMAIN public.url_domain;
       public          postgres    false            �            1259    107792    book    TABLE     �   CREATE TABLE public.book (
    isbn character varying(10) NOT NULL,
    title character varying(300) NOT NULL,
    author character varying(255),
    publication_year integer,
    publisher character varying(255),
    image_url public.url_domain
);
    DROP TABLE public.book;
       public         heap    postgres    false    840            �            1259    107812    rating    TABLE     �   CREATE TABLE public.rating (
    isbn character varying(10) NOT NULL,
    user_id integer NOT NULL,
    rating integer,
    CONSTRAINT rating_rating_check CHECK (((rating >= 0) AND (rating <= 10)))
);
    DROP TABLE public.rating;
       public         heap    postgres    false            �            1259    107800    user    TABLE     �  CREATE TABLE public."user" (
    user_id integer NOT NULL,
    username character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(64) NOT NULL,
    CONSTRAINT user_email_check CHECK (((email)::text ~ '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$'::text)),
    CONSTRAINT user_username_check CHECK (((username)::text ~ '^[a-zA-Z0-9_]{2,}$'::text))
);
    DROP TABLE public."user";
       public         heap    postgres    false            �            1259    107799    user_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.user_user_id_seq;
       public          postgres    false    216                       0    0    user_user_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.user_user_id_seq OWNED BY public."user".user_id;
          public          postgres    false    215            q           2604    107803    user user_id    DEFAULT     n   ALTER TABLE ONLY public."user" ALTER COLUMN user_id SET DEFAULT nextval('public.user_user_id_seq'::regclass);
 =   ALTER TABLE public."user" ALTER COLUMN user_id DROP DEFAULT;
       public          postgres    false    215    216    216                      0    107792    book 
   TABLE DATA           [   COPY public.book (isbn, title, author, publication_year, publisher, image_url) FROM stdin;
    public          postgres    false    214   y                 0    107812    rating 
   TABLE DATA           7   COPY public.rating (isbn, user_id, rating) FROM stdin;
    public          postgres    false    217   �                 0    107800    user 
   TABLE DATA           D   COPY public."user" (user_id, username, email, password) FROM stdin;
    public          postgres    false    216   �                  0    0    user_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.user_user_id_seq', 1, false);
          public          postgres    false    215            v           2606    107798    book book_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (isbn);
 8   ALTER TABLE ONLY public.book DROP CONSTRAINT book_pkey;
       public            postgres    false    214            ~           2606    107817    rating rating_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_pkey PRIMARY KEY (isbn, user_id);
 <   ALTER TABLE ONLY public.rating DROP CONSTRAINT rating_pkey;
       public            postgres    false    217    217            x           2606    107811    user user_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_email_key;
       public            postgres    false    216            z           2606    107807    user user_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    216            |           2606    107809    user user_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_username_key;
       public            postgres    false    216                       2606    107818    rating rating_isbn_fkey    FK CONSTRAINT     t   ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_isbn_fkey FOREIGN KEY (isbn) REFERENCES public.book(isbn);
 A   ALTER TABLE ONLY public.rating DROP CONSTRAINT rating_isbn_fkey;
       public          postgres    false    3190    214    217            �           2606    107823    rating rating_user_id_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(user_id);
 D   ALTER TABLE ONLY public.rating DROP CONSTRAINT rating_user_id_fkey;
       public          postgres    false    3194    216    217                  x������ � �            x������ � �            x������ � �     