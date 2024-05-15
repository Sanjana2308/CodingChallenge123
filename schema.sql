create Database HexawareOrdersDB;
use HexawareOrdersDB;

-- Creating the Product table
CREATE TABLE Product (
    productId INT PRIMARY KEY,
    productName VARCHAR(255) NOT NULL,
    description VARCHAR(500) NOT NULL,
    price DECIMAL(10, 2),
    quantityInStock INT NOT NULL,
    type VARCHAR(50) CHECK (type IN ('Electronics', 'Clothing'))
);

-- Creating the Electronics table
CREATE TABLE Electronics (
    productId INT PRIMARY KEY,
    brand VARCHAR(255),
    warrantyPeriod INT,
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

-- Creating the Clothing table
CREATE TABLE Clothing (
    productId INT PRIMARY KEY,
    size VARCHAR(50),
    color VARCHAR(50),
    FOREIGN KEY (productId) REFERENCES Product(productId)
);

-- Creating the User table
CREATE TABLE Users(
    userId INT PRIMARY KEY,
    username VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    role VARCHAR(50) CHECK (role IN ('Admin', 'User'))
);