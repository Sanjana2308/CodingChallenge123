from Util.DBconn import DBConnection

from DAO.order_management import IOrderManagementRepository

from Exception.my_exceptions import UserNotFound

class OrderProcessor(IOrderManagementRepository, DBConnection):
    def createOrder(self, user, products):
        # Insert order details into the Orders table
        for product in products: 
            if product: 
                self.cursor.execute("INSERT INTO Orders (userId, productId) VALUES (?, ?)", (user.userId, product.productId))
            else:
                print(f"Error: Product with ID {product.productId} not found.")
            

    def cancelOrder(self, userId, orderId):
        try: 
            self.cursor.execute("SELECT * FROM Orders WHERE userId = ? AND orderId = ?", (userId, orderId))
            existing_order = self.cursor.fetchone()
            if existing_order:
                self.cursor.execute("DELETE FROM Orders WHERE userId = ? AND orderId = ?", (userId, orderId))

            else:
                print("Error: Order not found.")
        except Exception as e:
            print(e)

    def createProduct(self, user, product):
        try:
            self.cursor.execute("INSERT INTO Product (productId, productName, description, price, quantityInStock, type) VALUES (?, ?, ?, ?, ?, ?)", 
                        (product.productId, product.productName, product.description, product.price, product.quantityInStock, product.type))
            if product.type == 'Electronics':
                self.cursor.execute("INSERT INTO Electronics (productId, brand, warrantyPeriod) VALUES (?, ?, ?)", 
                        (product.productId, product.brand, product.warrantyPeriod))
            elif product.type == 'Clothing':
                self.cursor.execute("INSERT INTO Clothing (productId, size, color) VALUES (?, ?, ?)", 
                            (product.productId, product.size, product.color))
        except Exception as e:
            raise UserNotFound("User not found.",e)


    def createUser(self, user):
        try:
            self.cursor.execute(
                "INSERT INTO Users (userId, username, password, role) VALUES (?, ?, ?, ?)",
                (user.user_id, user.user_name, user.password, user.role), 
            )
            print("User added successfully!🥳")

        except Exception as e:
            print(e)


    def getAllProducts(self):
        try:
            self.cursor.execute("select * from Product")
            products = self.cursor.fetchall()
            for product in products:
                print(product)
        except Exception as e:
            print(e)



    def getOrderByUser(self, user):
        try: 
            self.cursor.execute("SELECT * FROM Orders WHERE userId = ?", (user))
            orders =  self.cursor.fetchall()
            for order in orders:
                print(order)
        except Exception as e:
            print(e)
    
 