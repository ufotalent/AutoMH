#include "StdAfx.h"
#include "ItemUser.h"
#include "ScreenCapturer.h"
#include <iostream>
// 770 585 65 30
ItemUser::ItemUser(void):use_item_(_T("buttons/use_item.bmp"))
{
}

ItemUser::~ItemUser(void)
{
}

bool ItemUser::test_and_use_item(const Image& img) {
	Image area(img, 770, 585, 65, 30);
	int dis = area.cmp(use_item_);
	std::cout << "use_item dis:" << dis << std::endl;
	if (dis < 25000) {
		ScreenCapturer::get_instance().click(800, 600);
		return true;
	}
	return false;
}
