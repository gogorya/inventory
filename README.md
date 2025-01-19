# Inventory Management System

This project is an Inventory Management System built using Django REST framework and MongoEngine. It allows you to manage suppliers, products, stock movements, and sale orders.

## Features

- Manage Suppliers
- Manage Products
- Track Stock Movements (In/Out)
- Create and Manage Sale Orders
- Check Current Stock for Each Product

## Installation

1. Create and activate a virtual environment:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

2. Install the required packages (make sure virtual venv is activated):

   ```bash
   pip install -r requirements.txt
   ```

3. Set up MongoDB:

   Ensure MongoDB is installed and running on your machine. Update the MongoDB connection settings in your Django settings file if necessary.

   ```
   host='your_mongoDB_host'
   ```

4. Run the development server:

   ```bash
   python manage.py runserver
   ```

## API Endpoints

### Suppliers

- `GET api/suppliers/` - List all suppliers
- `POST api/suppliers/` - Create a new supplier
- `GET api/suppliers/{id}/` - Retrieve a supplier
- `PATCH api/suppliers/{id}/` - Update a supplier
- `DELETE api/suppliers/{id}/` - Delete a supplier

### Products

- `GET api/products/` - List all products
- `POST api/products/` - Create a new product
- `GET api/products/{id}/` - Retrieve a product
- `PATCH api/products/{id}/` - Update a product
- `DELETE api/products/{id}/` - Delete a product

### Stock Movements

- `GET api/stockmovements/` - List all stock movements
- `POST api/stockmovements/` - Create a new stock movement
- `GET api/stockmovements/{id}/` - Retrieve a stock movement
- `PATCH api/stockmovements/{id}/` - Update a stock movement
- `DELETE api/stockmovements/{id}/` - Delete a stock movement

### Sale Orders

- `GET api/saleorders/` - List all sale orders
- `POST api/saleorders/` - Create a new sale order
- `GET api/saleorders/{id}/` - Retrieve a sale order
- `PATCH api/saleorders/{id}/` - Update a sale order
- `DELETE api/saleorders/{id}/` - Delete a sale order

### Product Stock

- `GET /product-stock/` - Get current stock for each product

## Models

### Supplier

- `name` - Name of the supplier
- `email` - Email of the supplier
- `phone` - Phone number of the supplier
- `address` - Address of the supplier

### Product

- `name` - Name of the product
- `description` - Description of the product
- `category` - Category of the product
- `price` - Price of the product
- `stock_quantity` - Stock quantity of the product
- `supplier` - Reference to the supplier

### Stock Movement

- `product` - Reference to the product
- `quantity` - Quantity of the stock movement
- `movement_type` - Type of the movement (In/Out)
- `movement_date` - Date of the movement
- `notes` - Additional notes

### Sale Order

- `product` - Reference to the product
- `quantity` - Quantity of the sale order
- `total_price` - Total price of the sale order
- `sale_date` - Date of the sale
- `status` - Status of the sale order (Pending/Completed/Cancelled)
