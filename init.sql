CREATE DATABASE IF NOT EXISTS edades_db;

USE edades_db;

CREATE TABLE IF NOT EXISTS personas (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nombre VARCHAR(100) NOT NULL,
    edad INT NOT NULL
);

INSERT INTO personas (nombre, edad) VALUES
('Ana',5),('Luis',8),('Pedro',10),('Marta',12),('Carlos',11),
('Laura',6),('Sofia',9),('Diego',7),('Valeria',4),('Mateo',3),

('Juan',13),('Camila',14),('Daniel',15),('Sara',16),('David',17),
('Valentina',14),('Andres',16),('Paula',15),('Sebastian',13),('Natalia',17),

('Miguel',18),('Fernando',22),('Jorge',25),('Alejandra',30),('Patricia',35),
('Ricardo',40),('Sandra',45),('Felipe',50),('Andrea',28),('Claudia',33),

('Roberto',60),('Carmen',55),('Hector',42),('Juliana',27),('Angela',38),
('Esteban',29),('Cristian',24),('Monica',31),('Rosa',48),('Gloria',53),

('Mario',20),('Lucia',19),('Oscar',23),('Diana',26),('Gabriel',34),
('Erika',37),('Ivan',41),('Tatiana',44),('Rafael',52),('Lina',21);