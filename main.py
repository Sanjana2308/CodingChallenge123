from Entity import Product, Clothing, Electronics, Users

from Util.DBconn import DBConnection

from DAO import IOrderManagementRepository, OrderProcessor
class MainMenu(DBConnection):
    order_processor = OrderProcessor()
    def main(self):
        while True:
            print("""
                  1. Create product
                  2. Get all products
                  3. Create user
                  4. Get order by user
                  5. Create order
                  6. Cancel order
                  7. Exit
                  """)
            
            choice = int(input("Please choose from above options: "))

            if choice == 1:
                user_id = int(input("Enter user id: "))
                role = input("Enter user role: ")
                self.cursor.execute("SELECT * FROM Users WHERE userId = ? AND role = 'Admin'", (user_id))
                admin_user = self.cursor.fetchall()
                if admin_user:
                    productId = int(input("Enter product ID: "))
                    productName = input("Enter product name: ")
                    description = input("Enter product description: ")
                    price = float(input("Enter product price: "))
                    quantityInStock = int(input("Enter quantity in stock: "))
                    productType = input("Enter product type (Electronics/Clothing): ")
                    new_product = Product(productId, productName, description, price, quantityInStock, productType)
                    self.order_processor.createProduct
                else:
                    print("Error! ⚠️  Only admin users can create products!")
            
            elif choice == 2:
                self.order_processor.getAllProducts()

            elif choice == 3:
                user_id = input("Enter user Id: ")
                user_name = input("Enter user name: ")
                password = input("Enter user password: ")
                role = input("Enter user role: ")
                new_user = Users(user_id, user_name, password, role)
                self.order_processor.createUser(new_user)

            elif choice == 4:
                user_id = print("Enter user id: ")
                self.order_processor.getOrderByUser(user_id)


            elif choice == 5:
                userId = print("Print user Id: ")
                self.cursor.execute("SELECT * FROM Users WHERE userId = ?", (userId,))
                existing_user = self.cursor.fetchone()
                self.cursor.execute("SELECT * from Products")
                products = self.cursor.fetchall()
                if existing_user:
                    for product in products:
                        self.cursor.execute("SELECT * FROM Product WHERE productId = ?", (product.productId,))
                        existing_product = self.cursor.fetchone()
                        if existing_product:
                            self.order_processor.createOrder()
                else:
                    self.order_processor.create_user(user)
                    self.order_processor.create_order(user, products)


            elif choice == 6:
                continue
            elif choice == 7:
                
                break

if __name__ == "__main__":
    print("Welcome to orders app")
    main = MainMenu()
    main.main()


        


