
---Показать все базы данных---
show databases;

---Создание базы данных---
CREATE DATABASE pingvin;

---Удаление базы данных pingvin
DROP DATABASE pingvin;

---Выбираем базу данных---
USE pingvin;

---Создание Таблицы---
---VARCHAR Текстовый тип---
---FLOAT дробное число---
---INT целое число---
---BYTE 1 или 0---
---MEDIUMTEXT 64 6565 количество символов---
---TEXT 16 878 Количество макс. Символом---
---DOUBLE очень большое дробное число---
---LONGTEXT 4GB размер текста---
---BIGINT очень большое целое число---
---TEXT 16 878 Количество макс. Символов

CREATE TABLE users(
    name VARCHAR(250) NULL,
    login VARCHAR(100) NULL,
    password VARCHAR(300) NULL,
    address TEXT NULL DEFAULT NULL 
);

---Получение данных из таблицы---
SELECT name, login, password, address FROM users;

---Вставка данных в таблицу---
INSERT INTO users(name, login)
    VALUES('pingvin', 'kapycta');

---Создание Таблицы products---
CREATE TABLE products(
    name VARCHAR(250) NULL
);

---Создание Таблицы balance---
CREATE TABLE balance(
    bank_name VARCHAR(250) NULL,
    user_name VARCHAR(250) NULL,
    cash FLOAT NULL
);

---Добавляем данные на таблицу balance---
INSERT INTO balance(bank_name, users_name, cash)
    VALUES('Demir Bank', 'pingvin', 99999999999999.99);

---LAB - 1

CREATE TABLE country(
    names VARCHAR(250) NULL,
    valuta VARCHAR(100) NULL,
    population_count INT NULL
);

INSERT INTO country(names, valuta, population_count)
    VALUES('USA', '$' 200000000);

SELECT names, valuta FROM country

--- Меняем кодировку таблицы на utf8---
ALTER TABLE balance
    CHARACTER SET utf8mb4,
    COLLATE utf8mb4_general_ci;


--- Фильтрация получение данных ---
SELECT * FROM bank 
    WHERE bank.bank_name = 'Bakai Bank';

--- Изменение данных в таблице ---
UPDATE


INSERT INTO bank(bank_name, bank_balance, bank_info, client_count)
    VALUES('Emir_lox', 0, 'Aman_hacker', 0);


--- LAB 3 ---

CREATE TABLE films(
    name VARCHAR(250) NULL,
    status VARCHAR(250) NULL,
    actors TEXT, 
    money INT
)

INSERT INTO films(name, status, actors, money)
    VALUES('Форсаж', '93.43%', 'Вин Дизель, Пол Уокер, Люк Эванс, Тайриз Гибсон, Джордана Брюстер', 1236005118);


INSERT INTO films(name, year, status, actors, money)
    VALUES('Pingvin', 2021, 'GOOD', 'Aman-Pingvin', 1300459)