from flask import Flask, jsonify, request
from redis import Redis

app = Flask(__name__)

# Shared database
db = Redis(host="shop_db", port=6379, decode_responses=True)

INITIAL_BALANCE = 10000
BALANCE_KEY = "shop_balance"


def init_balance_if_needed():
    if not db.exists(BALANCE_KEY):
        db.set(BALANCE_KEY, INITIAL_BALANCE)


@app.route("/balance", methods=["GET"])
def get_balance():
    init_balance_if_needed()
    balance = int(db.get(BALANCE_KEY) or 0)
    return jsonify(
        {"success": True, "balance": balance, "initial_balance": INITIAL_BALANCE}
    )


@app.route("/deduct", methods=["POST"])
def deduct_balance():
    init_balance_if_needed()

    data = request.json
    sku = data.get("sku")
    amount = data.get("amount")

    if not sku or not amount:
        return jsonify({"success": False, "message": "Missing sku or amount"}), 400

    current_balance = int(db.get(BALANCE_KEY) or 0)
    amount = int(amount)

    if current_balance < amount:
        return jsonify(
            {
                "success": False,
                "message": f"Insufficient balance. Current: {current_balance}, Required: {amount}",
            }
        ), 400

    new_balance = db.decrby(BALANCE_KEY, amount)
    return jsonify(
        {
            "success": True,
            "message": "Deduction successful",
            "old_balance": current_balance,
            "new_balance": new_balance,
            "deducted": amount,
        }
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
