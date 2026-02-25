#ifndef CART_H
#define CART_H
#include "Item.h"
#include "ItemService.h"
#include <vector>

class Cart {
    private:
        std::vector<Item> items;
        ItemService* itemService;
    public:
        Cart() : itemService(nullptr) {}

        void setItemService(ItemService* service) { itemService = service; }
        void setItems(std::vector<Item>& items) { this->items = items; }

        double getCartTotalAmount() {
            double totalAmount = 0.0;
            for ( auto& item : items) {
                if (itemService) {
                    totalAmount += itemService->getPrice(item) * item.getQuantity();
                }
            }
            return totalAmount;
        }
};

#endif // CART_H
