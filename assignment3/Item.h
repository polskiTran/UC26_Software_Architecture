#ifndef ITEM_H
#define ITEM_H
#include <string>

class Item {

    private:
        std::string itemId;
        std::string name;
        int quantity;
    public:
        Item(const std::string& itemId, const std::string& name, int quantity): itemId(itemId), name(name), quantity(quantity) {}
        std::string getItemId() const { return itemId; }
        void setItemId(const std::string& itemId) { this->itemId = itemId; }
        std::string getName() const { return name; }
        void setName(const std::string& name) { this->name = name; }
        int getQuantity() const { return quantity; }
        void setQuantity(int quantity) { this->quantity = quantity; }
        bool operator==(const Item& other) const {
            return itemId == other.itemId && name == other.name && quantity == other.quantity;
        }
};
#endif // ITEM_H
