#include <gtest/gtest.h>
#include "Item.h"
#include "Cart.h"
#include "ItemService.h"
#include <vector>

// mock item service for prices
class MockItemService : public ItemService {
public:
    double getPrice(Item& item) override {
        if (item.getName() == "SDcard") return 10.0;
        if (item.getName() == "LEDlight") return 10.0;
        if (item.getName() == "DashCam") return 20.0;
        return 0.0;
    }
};

TEST(CartTotalAmountTest, GetCartTotalAmount) {
    // make mock item
    Item SDcard("1", "SDcard", 1);
    Item LEDlight("2", "LEDlight", 1);
    Item DashCam("3", "DashCam", 2);

    std::vector<Item> items = { SDcard, LEDlight, DashCam };

    // add item to cart
    Cart cart;
    cart.setItems(items);
    MockItemService mockService;
    cart.setItemService(&mockService);

    double result = cart.getCartTotalAmount();

    EXPECT_EQ(result, 60);
}
