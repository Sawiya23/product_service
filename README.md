# Grocery Shopping Microservices

This repository contains two Flask microservices for grocery shopping: `Product Service` and `Cart Service`.

## Services

### 1. Product Service

The Product Service is responsible for managing the list of available grocery products. It exposes the following endpoints:

- `/products` - Retrieve a list of all products.
- `/products/{product_id}` - Retrieve details of a specific product by ID.
- `curl -X POST -H "Content-Type: application/json" \ -d '{"name": "Orange", "price": 1.5, "quantity": 50}' \https://productservice.onrender.com/products` - Add a new product to the inventory.

**Product Service URL**:  
[Product Service on Render](https://product-service-izcg.onrender.com)
