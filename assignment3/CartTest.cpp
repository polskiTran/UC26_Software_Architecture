#include <gtest/gtest.h>
#include "Item.h"
#include "Cart.h"
#include "ItemService.h"
#include <vector>

// mock ItemService so we can set the prices for our mock items
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
  	// mock items
    Item SDcard("1", "SDcard", 1);
    Item LEDlight("2", "LEDlight", 1);
    Item DashCam("3", "DashCam", 2);
    std::vector<Item> items = { SDcard, LEDlight, DashCam };

  	// put items to cart
    Cart cart;
    cart.setItems(items);

  	// setting the prices
    MockItemService mockService;
    cart.setItemService(&mockService);

  	// test the getCartTotalAmount
    double result = cart.getCartTotalAmount();
    EXPECT_EQ(result, 60);
}