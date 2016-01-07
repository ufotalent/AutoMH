#pragma once
#include "Image.h"
class ItemUser
{
private:
	Image use_item_;
public:
	ItemUser(void);
	~ItemUser(void);
	bool test_and_use_item(const Image& img);
};
