# Software Architecture: Service-Based Architecture Style

# Assignment: Add a Money Service

## Background
The current system (https://github.com/lunarlunarll123/Service-Based) already includes:
- Product Service
- Order Service
- one shared database
- Nginx / API Gateway

Your task is to extend this service-based architecture by adding a new Money Service:
1. Each phone must have its own price. You set the price.
2. The initial total balance is 10000.
3. After each successful Place Order, the total balance must decrease.
4. Create a separate Money Service to manage the balance.
5. All services must continue to share one database.

What to Do:
- Update Order Service to support phone price.
- Create a new Money Service for:
    - initializing the balance
    - checking the current balance
    - deducting money after an order
- Update Order Service so that a successful order reduces the balance.
- Update docker-compose.yml to include the new service.
- Update Nginx routing if needed.
- Update the front-end page to show:
    - phone prices
    - current balance
    - updated balance after ordering

Rules
- Do not put money-related logic inside Product Service.
- Keep service responsibilities separate.
- Keep the current service-based architecture with one shared database.
- You can use AI to check the API usage and generate codes. It helps you to understand how to use AI in code generation. This rule only works on this project.
- You need to design a beautiful UI interaction.
