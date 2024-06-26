PGDMP     1    3    
            |            Book_Recommendation_System_Clear    15.2    15.2     %           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            &           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            '           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            (           1262    108129     Book_Recommendation_System_Clear    DATABASE     �   CREATE DATABASE "Book_Recommendation_System_Clear" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Ukrainian_Ukraine.1251';
 2   DROP DATABASE "Book_Recommendation_System_Clear";
                mykhailo_lozinskyi    false            I           1247    108131 
   url_domain    DOMAIN     �   CREATE DOMAIN public.url_domain AS character varying(2048)
	CONSTRAINT url_domain_check CHECK (((VALUE)::text ~ '^https?://[^\s/$.?#].[^\s]*$'::text));
    DROP DOMAIN public.url_domain;
       public          postgres    false            �            1255    108185 $   update_updated_at_trigger_function()    FUNCTION     �   CREATE FUNCTION public.update_updated_at_trigger_function() RETURNS trigger
    LANGUAGE plpgsql
    AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$;
 ;   DROP FUNCTION public.update_updated_at_trigger_function();
       public          postgres    false            �            1259    108133    book    TABLE     y  CREATE TABLE public.book (
    isbn character varying(10) NOT NULL,
    title character varying(300) NOT NULL,
    author character varying(255),
    publication_year integer,
    publisher character varying(255),
    image_url public.url_domain,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT book_created_at_check CHECK ((created_at >= '2024-01-01 00:00:00'::timestamp without time zone)),
    CONSTRAINT book_updated_at_check CHECK ((updated_at >= '2024-01-01 00:00:00'::timestamp without time zone))
);
    DROP TABLE public.book;
       public         heap    postgres    false    841            �            1259    108138    rating    TABLE     M  CREATE TABLE public.rating (
    isbn character varying(10) NOT NULL,
    user_id integer NOT NULL,
    rating integer,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT rating_created_at_check CHECK ((created_at >= '2024-01-01 00:00:00'::timestamp without time zone)),
    CONSTRAINT rating_rating_check CHECK (((rating >= 0) AND (rating <= 10))),
    CONSTRAINT rating_updated_at_check CHECK ((updated_at >= '2024-01-01 00:00:00'::timestamp without time zone))
);
    DROP TABLE public.rating;
       public         heap    postgres    false            �            1259    108142    user    TABLE       CREATE TABLE public."user" (
    user_id integer NOT NULL,
    username character varying(100) NOT NULL,
    email character varying(100) NOT NULL,
    password character varying(64) NOT NULL,
    created_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    updated_at timestamp without time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    CONSTRAINT user_created_at_check CHECK ((created_at >= '2024-01-01 00:00:00'::timestamp without time zone)),
    CONSTRAINT user_email_check CHECK (((email)::text ~ '^[A-Za-z0-9._%-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,4}$'::text)),
    CONSTRAINT user_updated_at_check CHECK ((updated_at >= '2024-01-01 00:00:00'::timestamp without time zone)),
    CONSTRAINT user_username_check CHECK (((username)::text ~ '^[a-zA-Z0-9_]{2,}$'::text))
);
    DROP TABLE public."user";
       public         heap    postgres    false            �            1259    108147    user_user_id_seq    SEQUENCE     �   CREATE SEQUENCE public.user_user_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 '   DROP SEQUENCE public.user_user_id_seq;
       public          postgres    false    216            )           0    0    user_user_id_seq    SEQUENCE OWNED BY     G   ALTER SEQUENCE public.user_user_id_seq OWNED BY public."user".user_id;
          public          postgres    false    217            v           2604    108148    user user_id    DEFAULT     n   ALTER TABLE ONLY public."user" ALTER COLUMN user_id SET DEFAULT nextval('public.user_user_id_seq'::regclass);
 =   ALTER TABLE public."user" ALTER COLUMN user_id DROP DEFAULT;
       public          postgres    false    217    216                      0    108133    book 
   TABLE DATA           s   COPY public.book (isbn, title, author, publication_year, publisher, image_url, created_at, updated_at) FROM stdin;
    public          postgres    false    214   _$                  0    108138    rating 
   TABLE DATA           O   COPY public.rating (isbn, user_id, rating, created_at, updated_at) FROM stdin;
    public          postgres    false    215   |$       !          0    108142    user 
   TABLE DATA           \   COPY public."user" (user_id, username, email, password, created_at, updated_at) FROM stdin;
    public          postgres    false    216   �$       *           0    0    user_user_id_seq    SEQUENCE SET     ?   SELECT pg_catalog.setval('public.user_user_id_seq', 1, false);
          public          postgres    false    217            �           2606    108150    book book_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.book
    ADD CONSTRAINT book_pkey PRIMARY KEY (isbn);
 8   ALTER TABLE ONLY public.book DROP CONSTRAINT book_pkey;
       public            postgres    false    214            �           2606    108152    rating rating_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_pkey PRIMARY KEY (isbn, user_id);
 <   ALTER TABLE ONLY public.rating DROP CONSTRAINT rating_pkey;
       public            postgres    false    215    215            �           2606    108154    user user_email_key 
   CONSTRAINT     Q   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_email_key UNIQUE (email);
 ?   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_email_key;
       public            postgres    false    216            �           2606    108156    user user_pkey 
   CONSTRAINT     S   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_pkey PRIMARY KEY (user_id);
 :   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_pkey;
       public            postgres    false    216            �           2606    108158    user user_username_key 
   CONSTRAINT     W   ALTER TABLE ONLY public."user"
    ADD CONSTRAINT user_username_key UNIQUE (username);
 B   ALTER TABLE ONLY public."user" DROP CONSTRAINT user_username_key;
       public            postgres    false    216            �           2620    108186     book set_book_updated_at_trigger    TRIGGER     �   CREATE TRIGGER set_book_updated_at_trigger BEFORE UPDATE ON public.book FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_trigger_function();
 9   DROP TRIGGER set_book_updated_at_trigger ON public.book;
       public          postgres    false    218    214            �           2620    108187 $   rating set_rating_updated_at_trigger    TRIGGER     �   CREATE TRIGGER set_rating_updated_at_trigger BEFORE UPDATE ON public.rating FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_trigger_function();
 =   DROP TRIGGER set_rating_updated_at_trigger ON public.rating;
       public          postgres    false    218    215            �           2620    108188     user set_user_updated_at_trigger    TRIGGER     �   CREATE TRIGGER set_user_updated_at_trigger BEFORE UPDATE ON public."user" FOR EACH ROW EXECUTE FUNCTION public.update_updated_at_trigger_function();
 ;   DROP TRIGGER set_user_updated_at_trigger ON public."user";
       public          postgres    false    216    218            �           2606    108159    rating rating_isbn_fkey    FK CONSTRAINT     t   ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_isbn_fkey FOREIGN KEY (isbn) REFERENCES public.book(isbn);
 A   ALTER TABLE ONLY public.rating DROP CONSTRAINT rating_isbn_fkey;
       public          postgres    false    215    3203    214            �           2606    108164    rating rating_user_id_fkey    FK CONSTRAINT        ALTER TABLE ONLY public.rating
    ADD CONSTRAINT rating_user_id_fkey FOREIGN KEY (user_id) REFERENCES public."user"(user_id);
 D   ALTER TABLE ONLY public.rating DROP CONSTRAINT rating_user_id_fkey;
       public          postgres    false    216    215    3209                  x������ � �             x������ � �      !      x������ � �     