#ifndef ITEM_SERVICE_H
#define ITEM_SERVICE_H

#include "Item.h"

class ItemService {
    public:
        virtual ~ItemService() = default;
        virtual double getPrice(Item& item) = 0;
};
#endif // ITEM_SERVICE_H
