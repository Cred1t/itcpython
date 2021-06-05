
CREATE DATABASE itc_zaki_myblog;
USE itc_zaki_myblog;
-- ТАБЛИЦА ПОЛЬЗОВАТЕЛИ
-- ---------------------------------------
CREATE TABLE users(
 id INT NOT NULL AUTO_INCREMENT,
 name VARCHAR(200) NULL,
 login VARCHAR(200) NULL,
 password VARCHAR(300) NULL,
 is_admin BIT NULL,
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
-- ---------------------------------------
-- ТАБЛИЦА КАТЕГОРИЯ СТАТЬЕЙ
-- ---------------------------------------
CREATE TABLE post_category(
 id INT NOT NULL AUTO_INCREMENT,
 name VARCHAR(200) NULL,
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
-- ---------------------------------------
-- ТАБЛИЦА СТАТЬИ
-- ---------------------------------------
CREATE TABLE posts(
 id INT NOT NULL AUTO_INCREMENT,
 user_id INT NULL,
 title VARCHAR(200) NULL,
 content LONGTEXT NULL,
 short_content TEXT NULL,
 image_url TEXT NULL,
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
-- ---------------------------------------
-- ТАБЛИЦА МЕНЮ САЙТА
-- ---------------------------------------
CREATE TABLE menu(
 id INT NOT NULL AUTO_INCREMENT,
 menu_name VARCHAR(200) NULL,
 menu_url VARCHAR(200) NULL,
 PRIMARY KEY(id)
)
COLLATE='utf8mb4_general_ci'
ENGINE=InnoDB;
-- ---------------------------------------


INSERT INTO posts(user_id, title, content, short_content)
    VALUES(
        5, 
        'Основатель кампании Advencher.am', 
        'Осонователь и создатель всемирного мобильного OC Advencher Амантур Pingvin. Advencher представляет собой сифровым прорывом в истории человечества. Он знаменит тем что поддерживается на всех платформах и устройств. Advenxher пользуются обычные пользаватели, так и военные используют его в своих системах. Advencher стал мировым прорывом.', 
        'Самый богатый человек во всем в мире создатель и основатель кампании Advencher Амантур Pingvin'
    );


INSERT INTO posts(user_id, title, content, short_content)
    VALUES(
        5,
        'Германия стала единнственной сверхдержавой',
        'Германия стала единнственной сверхдержавой благодаря своей эканомике. 02.09.2047 числа Германия одержала победу в войне с свехрдержавами как: Россия, Америка и Китай. Благодаря этой победе Германия получила ресурсы и повысила экономику которая обеспечит величие Германской Империи на 1000лет.',
        'Германия стала всемирным производителем во всем мире'
    )



--- Добавляем новую колонку для таблицы posts
ALTER TABLE posts 
    ADD COLUMN post_category_id INT NULL;
----------------------------------------------
INSERT INTO posts(user_id, title, content, short_content, image_url)
    VALUES
        (
            1, 
            'Биткойн подоражал на 60 000$', 
            'Биткойн цифровая валюта для всех людей',
            'Биткойн всегда актуален',
            'bitcoin.png'
        ),
        (
            1, 
            'Садыр Жапаров', 
            'Садыр Жапаров Встретился с Путином',
            'Садыр Жапаров Встретился...',
            'politics.png'
        ),
        (
            1, 
            'Питон стал 1 языков прог-я мира', 
            'Питон стал самым популярным языков программирования на 2021 во всем мире',
            'Питон стал...',
            'python.png'
        ),
        (
            1, 
            'IT Инженеры начали хорошо зарабатывать', 
            'IT Инженеры начали зарабатывать 150 000$ в год',
            'IT Инженеры начали...',
            'engineer.png'
        ),
        (
            1, 
            'Экономика Кыргызстана растет', 
            'Кыргызстан стал лидером в Средней Азии по поставке Электрокаров',
            'Кыргызстан стал лидером...',
            'kyrgyzstan.png'
        );