
-- создание базы данных для блога --
-- TABLE users
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

INSERT INTO users(name, login, password, is_admin)
    VALUES
        ('Zalkar', 'zalkar', '123', 0),
        ('Meerim', 'meka', '123456', 0),
        ('Aiganysh', 'aika', '123456', 0),
        ('Bekbolot', 'beka', '9601', 0),
        ('Pingvin', 'Hacker', '4513', 1),
        ('Emir', 'ema', '5354', 0),
        ('Bekzat', 'bekzat', '4502', 0),
        ('Iskender', 'iskender', '5656', 0);

--- Удаление записей
DELETE FROM users WHERE id IN(10, 12, 14);
DELETE FROM users WHERE login = 'aika';
DELETE FROM users WHERE id = 9;
DELETE FROM users WHERE id BETWEEN 13 AND 19;

-- Обновление записей
UPDATE users
    SET
        name = 'Pingvin',
        login = 'hacker',
        password = 'HACKING'
    WHERE id = 5;



UPDATE users
    SET
        name = 'Pingvin',
        login = 'hacker',
        password = '8513'
    WHERE id BETWEEN 20 AND 24;


-- 

INSERT INTO customers(customerNumber, customerName, country)
    VALUES
        (9995, 'Pingvin', 'Germany'); 