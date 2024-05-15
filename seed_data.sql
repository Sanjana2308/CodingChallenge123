-- Inserting dummy data into the Product table
INSERT INTO Product (productId, productName, description, price, quantityInStock, type) VALUES
(1, 'Smartphone', 'A high-end smartphone with 128GB storage', 699.99, 50, 'Electronics'),
(2, 'Laptop', '15-inch laptop with 16GB RAM and 512GB SSD', 1199.99, 30, 'Electronics'),
(3, 'Headphones', 'Wireless over-ear headphones with noise cancellation', 199.99, 100, 'Electronics'),
(4, 'T-shirt', 'Cotton T-shirt with a cool print', 19.99, 200, 'Clothing'),
(5, 'Jeans', 'Slim fit denim jeans', 49.99, 150, 'Clothing'),
(6, 'Jacket', 'Waterproof jacket for outdoor activities', 89.99, 75, 'Clothing');


-- Inserting data into the Electronics table
INSERT INTO Electronics (productId, brand, warrantyPeriod)
VALUES 
(1, 'BrandA', 24),
(2, 'BrandB', 12),
(3, 'BrandC', 18);


-- Inserting data into the Clothing table
INSERT INTO Clothing (productId, size, color)
VALUES 
(4, 'M', 'Red'),
(5, 'L', 'Blue'),
(6, 'XL', 'Black');


-- Inserting data into the Users table
INSERT INTO Users (userId, username, password, role)
VALUES 
(1, 'admin1', 'password123', 'Admin'),
(2, 'user1', 'password456', 'User'),
(3, 'user2', 'password789', 'User'),
(4, 'admin2', 'password321', 'Admin'),
(5, 'user3', 'password654', 'User');

