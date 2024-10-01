from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample in-memory product data
products = [
    {"id": 1, "name": "Apple", "price": 0.5, "quantity": 100},
    {"id": 2, "name": "Banana", "price": 0.3, "quantity": 150},
]

# Helper function to generate the next product ID
def get_next_product_id():
    if products:
        return max(product["id"] for product in products) + 1
    else:
        return 1

# Get all products
@app.route('/products', methods=['GET'])
def get_products():
    return jsonify(products)

# Get a specific product by ID
@app.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    if product:
        return jsonify(product)
    else:
        return jsonify({"message": "Product not found"}), 404

# Add a new product
@app.route('/products', methods=['POST'])
def add_product():
    new_product = request.json

    # Validate the incoming product data
    if not new_product.get('name') or not isinstance(new_product.get('price'), (int, float)) or not isinstance(new_product.get('quantity'), int):
        return jsonify({"message": "Invalid product data"}), 400

    new_product['id'] = get_next_product_id()
    products.append(new_product)
    return jsonify(new_product), 201

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
