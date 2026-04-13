import socket

import requests
from flask import Flask, render_template_string, request
from redis import Redis

app = Flask(__name__)

db = Redis(host="shop_db", port=6379, decode_responses=True)


def get_products_from_service():
    try:
        resp = requests.get("http://product_app:5000/", timeout=5)
        if resp.status_code == 200:
            data = resp.json().get("data", {})
            products = {}
            for sku, info in data.items():
                products[sku] = {
                    "name": info.get("name", ""),
                    "price": int(info.get("price", 0)),
                }
            return products
    except:
        pass
    return {}


def get_balance():
    try:
        resp = requests.get("http://money_app:5000/balance", timeout=5)
        if resp.status_code == 200:
            return resp.json().get("balance", 0)
    except:
        pass
    return 0


HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Microservice Shop</title>
    <style>
        * { box-sizing: border-box; margin: 0; padding: 0; }
        body {
            font-family: 'Courier New', Courier, monospace;
            background: #0a0a0a;
            min-height: 100vh;
            display: flex;
            align-items: center;
            justify-content: center;
            padding: 20px;
        }
        .terminal {
            background: rgba(20, 20, 20, 0.95);
            border: 1px solid #333;
            max-width: 520px;
            width: 100%;
            padding: 30px;
        }
        .terminal-header {
            border-bottom: 1px solid #333;
            padding-bottom: 15px;
            margin-bottom: 20px;
        }
        .terminal-title {
            color: #fff;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 2px;
        }
        .terminal-id {
            color: #666;
            font-size: 11px;
            margin-top: 5px;
        }
        .balance-display {
            background: #111;
            border: 1px solid #333;
            padding: 15px;
            margin-bottom: 25px;
            text-align: center;
        }
        .balance-label {
            color: #666;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .balance-amount {
            color: #fff;
            font-size: 32px;
            font-weight: bold;
            margin-top: 5px;
        }
        .section-title {
            color: #fff;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 10px;
            border-bottom: 1px solid #333;
            padding-bottom: 5px;
        }
        .product-list { margin-bottom: 20px; }
        .product-item {
            display: flex;
            justify-content: space-between;
            padding: 10px 0;
            border-bottom: 1px solid #222;
            color: #ccc;
        }
        .product-item:last-child { border-bottom: none; }
        .product-price { color: #fff; }
        select {
            width: 100%;
            padding: 12px;
            background: #111;
            color: #fff;
            border: 1px solid #333;
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
            margin: 15px 0;
            cursor: pointer;
        }
        select:focus { outline: none; border-color: #666; }
        button {
            width: 100%;
            padding: 12px;
            background: #fff;
            color: #000;
            border: none;
            font-family: 'Courier New', Courier, monospace;
            font-size: 14px;
            text-transform: uppercase;
            letter-spacing: 1px;
            cursor: pointer;
        }
        button:hover { background: #ccc; }
        .history { margin-top: 25px; }
        .history ul {
            list-style: none;
            background: #111;
            border: 1px solid #333;
            padding: 10px;
            max-height: 150px;
            overflow-y: auto;
        }
        .history li {
            padding: 6px 0;
            color: #888;
            font-size: 12px;
            border-bottom: 1px solid #222;
        }
        .history li:last-child { border-bottom: none; }
        .history .empty { color: #555; font-style: italic; text-align: center; }
        .msg {
            padding: 12px;
            margin-bottom: 20px;
            font-size: 12px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .success-msg { background: rgba(0, 255, 0, 0.1); color: #0f0; border: 1px solid #0f0; }
        .error-msg { background: rgba(255, 0, 0, 0.1); color: #f00; border: 1px solid #f00; }
        .link {
            display: block;
            text-align: center;
            margin-top: 20px;
            color: #666;
            text-decoration: none;
            font-size: 11px;
            text-transform: uppercase;
            letter-spacing: 1px;
        }
        .link:hover { color: #fff; }
        .info { font-size: 10px; color: #444; text-align: center; margin-top: 15px; text-transform: uppercase; letter-spacing: 1px; }
    </style>
</head>
<body>
    <div class="terminal">
        <div class="terminal-header">
            <div class="terminal-title">Checkout Service</div>
            <div class="terminal-id">{{ container_id }}</div>
        </div>

        {% if message %}
            <div class="msg {{ msg_class }}">{{ message }}</div>
        {% endif %}

        <div class="balance-display">
            <div class="balance-label">Balance</div>
            <div class="balance-amount">${{ balance }}</div>
        </div>

        <form method="POST" action="/order/submit">
            <div class="section-title">Products</div>
            <div class="product-list">
                {% for sku, info in products.items() %}
                <div class="product-item">
                    <span>{{ info.name }}</span>
                    <span class="product-price">${{ info.price }}</span>
                </div>
                {% endfor %}
            </div>
            <select name="sku">
                {% for sku, info in products.items() %}
                <option value="{{ sku }}">{{ info.name }} - ${{ info.price }}</option>
                {% endfor %}
            </select>
            <button type="submit">Place Order</button>
        </form>

        <div class="history">
            <div class="section-title">Order History</div>
            <ul>
                {% for log in logs %}
                    <li>{{ log }}</li>
                {% else %}
                    <li class="empty">No orders yet</li>
                {% endfor %}
            </ul>
        </div>

        <a class="link" href="/product/" target="_blank">View Inventory</a>
        <p class="info">shop_db (Shared Redis)</p>
    </div>
</body>
</html>
"""


@app.route("/")
def index():
    logs = db.lrange("order_history", 0, 9)
    container_id = socket.gethostname()
    balance = get_balance()
    products = get_products_from_service()
    return render_template_string(
        HTML_TEMPLATE,
        logs=logs,
        container_id=container_id,
        balance=balance,
        products=products,
        message=None,
        msg_class=None,
    )


@app.route("/submit", methods=["POST"])
def submit_order():
    sku = request.form["sku"]

    price_resp = requests.get(f"http://product_app:5000/price/{sku}", timeout=5)
    if price_resp.status_code != 200:
        return render_error("Product not found")

    price_data = price_resp.json()
    price = price_data.get("price", 0)
    product_name = price_data.get("name", "Unknown")

    deduct_resp = requests.post(
        "http://money_app:5000/deduct",
        json={"sku": sku, "amount": price},
        timeout=5,
    )
    deduct_data = deduct_resp.json()

    if not (deduct_resp.status_code == 200 and deduct_data.get("success")):
        return render_error(
            f"Payment Failed: {deduct_data.get('message', 'Insufficient balance')}"
        )

    stock_resp = requests.post(
        "http://product_app:5000/reduce_stock", json={"sku": sku}, timeout=5
    )
    stock_data = stock_resp.json()

    if stock_resp.status_code == 200 and stock_data.get("success"):
        order_id = db.incr("order_id_counter")
        new_balance = deduct_data.get("new_balance", 0)
        log_message = (
            f"#{order_id}: {product_name} (${price}) - Balance: ${new_balance}"
        )
        db.lpush("order_history", log_message)
        return render_success(
            f"Order #{order_id} Successful! {product_name} purchased for ${price}",
            new_balance,
        )
    else:
        db.incrby("shop_balance", price)
        return render_error(
            f"Order Failed: {stock_data.get('message', 'Out of stock')}"
        )


def render_success(message, balance):
    logs = db.lrange("order_history", 0, 9)
    products = get_products_from_service()
    return render_template_string(
        HTML_TEMPLATE,
        logs=logs,
        container_id=socket.gethostname(),
        balance=balance,
        products=products,
        message=message,
        msg_class="success-msg",
    )


def render_error(message):
    logs = db.lrange("order_history", 0, 9)
    products = get_products_from_service()
    return render_template_string(
        HTML_TEMPLATE,
        logs=logs,
        container_id=socket.gethostname(),
        balance=get_balance(),
        products=products,
        message=message,
        msg_class="error-msg",
    ), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
