#include "StdAfx.h"
#include "BTTaskProcessor.h"
#include "ScreenCapturer.h"
#include "FutureTaskManager.h"
#include "TaskManager.h"
#include "ImageFinder.h"
#include "ItemUser.h"
#include <time.h>
#include <iostream>
BTTaskProcessor::BTTaskProcessor(void):
bt_(_T("buttons/bt.bmp")) // 490 350 50 50
{
}

BTTaskProcessor::~BTTaskProcessor(void)
{
}

void BTTaskProcessor::run() {
	
	while (true) {
		bool success = false;
		do {
			
			std::auto_ptr<Image> screen = ScreenCapturer::get_instance().capture();
			int ret = TaskManager::get_instance().find_and_click(*screen, _T("bt"));
			if (ret > 0) success = true;
			printf("Checking bt task: %d\n", ret);
			Sleep(3000);
			if (ret >= 0) break;
		} while (true);

		if (!success) {
			success = FutureTaskManager::get_instance().get_task(_T("bt"));
			if (success) {
				Sleep(30000);
				ScreenCapturer::get_instance().click(820, 530);
				printf("Got future task bt\n");
				Sleep(3000);
				continue;
			} else {
				break;
			}
		}

		int entry_time = (int) time(NULL);

		while (time(NULL) < 1200 + (int) time(NULL)) {
			std::auto_ptr<Image> screen = ScreenCapturer::get_instance().capture();
			if (TaskManager::get_instance().find_and_click(*screen, _T("bt")) == 0) {
				break;
			}
			Sleep(5000);
		}
		
	}
	// wabao
	// click zhengli
	ScreenCapturer::get_instance().click(918, 591);
	Sleep(3000);
	ScreenCapturer::get_instance().click(800, 600);
	Sleep(3000);

	Image region(*ScreenCapturer::get_instance().capture(),490, 195, 50, 365);
	ImageFinder finder;
	ImageFinderResult result = finder.find_image(region, bt_);
	std::cout << "get bt item location" << result.y << " " << result.distance << std::endl;
	if (result.distance < 30000) {
		ScreenCapturer::get_instance().click(490 + 25 + result.x, 195 + 25 + result.y);
		
		//ScreenCapturer.click(490 + result.x , 195 + result.y);
		Sleep(3000);
		ScreenCapturer::get_instance().click(370, 440);
		Sleep(3000);
		ItemUser itemuser;
		int tick = 20;
		while (tick > 0) {			
			if (itemuser.test_and_use_item(*ScreenCapturer::get_instance().capture())) {
				tick = 20;
			}
			tick--;
			std::cout << "wabao tick" << tick << std::endl;
			Sleep(5000);
		}
	}
}

void BTTaskProcessor::reset() {

}