#include "StdAfx.h"
#include "SMTaskProcessor.h"
#include <iostream>
#include <cassert>
#include <ctime>
#include "ScreenCapturer.h"
#include "ImageFinder.h"
#include "TaskManager.h"
#include "WindowsManager.h"
#include "ItemUser.h"
#include "FutureTaskManager.h"
// rw_expand : 235 170 20 20
// rw_sm : 120 235 100 30
// wysfln : 725 500 140 25
// smjrzd : 750 500 90 25
SMTaskProcessor::SMTaskProcessor(void):rw_sm(_T("buttons/rw_sm.bmp")), 
rw_expand(_T("buttons/rw_expand.bmp")), 
wysfln(_T("buttons/wysfln.bmp")),
smjrzd(_T("buttons/smjrzd.bmp"))
{
	state_ = START;
}

SMTaskProcessor::~SMTaskProcessor(void)
{
}

void SMTaskProcessor::run() {
	while (true) {

		switch (state_) {
			case START: printf("status: START\n"); dostart(); break;
			case WAIT: printf("status: WAIT\n"); dowait(); break;
			case GMCW: printf("status: GMCW\n"); dogmcw(); break;
			case RWCWXZ: printf("status: RWCWXZ\n"); dorwcwxz(); break;
			case RWWPXZ: printf("status: RWWPXZ\n"); dorwwpxz(); break;
			case SHOPPING: printf("status: SHOPPING\n"); doshopping(); break;
			case STOP: printf("status: STOP\n"); return;
		}
		Sleep(5000);
	}

}
void SMTaskProcessor::dostart() {
	//ScreenCapturer::get_instance().click(300 + rand() % 200, 200 + rand() % 200);
	bool has_task = false;
	
	std::auto_ptr<Image> img = ScreenCapturer::get_instance().capture();
	int ret = TaskManager::get_instance().find_and_click(*img, _T("sm"));
	if (ret < 0) {
		state_ = WAIT;
		return;
	}
	has_task = (ret > 0);
	
	Sleep(3000);
	if (has_task) {
		state_ = WAIT;
	} else {
		// get from future task
		bool success = FutureTaskManager::get_instance().get_task(_T("sm"));
		if (!success) {
			state_ = STOP;
		} else {
			Sleep(30000);
			state_ = START;
			// get task
			ScreenCapturer::get_instance().click(788, 512);
			Sleep(2000);
		}
	}
}
void SMTaskProcessor::dogmcw() {
	ScreenCapturer::get_instance().click(807, 597);
	state_ = WAIT;
	return;
}

void SMTaskProcessor::dorwcwxz() {
	ScreenCapturer::get_instance().click(650, 550);
	state_ = START;
	return;
}

void SMTaskProcessor::dorwwpxz() {
	ScreenCapturer::get_instance().click(775, 546);
	state_ = START;
	return;
}

void SMTaskProcessor::doshopping() {
	std::auto_ptr<Image> img = ScreenCapturer::get_instance().capture();
	

	int f = pricer->first_digit(*img);
	int l = pricer->price_len(*img) - 1;
	while (l--) f = f * 10;
	if (f < this->shopping_threshold) {
		ScreenCapturer::get_instance().click(this->prepare_x, this->prepare_y);
		Sleep(2000);
		ScreenCapturer::get_instance().click(this->submit_x, this->submit_y);
		Sleep(2000);
		this->state_ = WAIT;
		return;
	} else {
		ScreenCapturer::get_instance().click(870, 100);
		Sleep(2000);
		// abandon task
		ScreenCapturer::get_instance().click(804, 114);
		Sleep(2000);
		img = ScreenCapturer::get_instance().capture();
		Image exp(*img, 235, 170, 20, 20);
		int expand_dis = exp.cmp(rw_expand);
		std::cout << "expand" << expand_dis << std::endl;
		if (expand_dis < 3000) {
			ScreenCapturer::get_instance().click(235, 170);
		}
		img = ScreenCapturer::get_instance().capture();
		Image area(*img, 120, 235, 100, 400);
		assert(rw_sm.getcx() == 100);
		assert(rw_sm.getcy() == 30);
		ImageFinder finder;
		ImageFinderResult result = finder.find_image(area, rw_sm);
		std::cout << "finding rw_sm:" << result.x << " " << result.y << " " << result.distance << std::endl;
		ScreenCapturer::get_instance().click(120 + result.x, 235 + result.y);
		Sleep(2000);
		ScreenCapturer::get_instance().click(396, 590);
		Sleep(2000);
		ScreenCapturer::get_instance().click(573, 407);
		Sleep(2000);
		// close 
		ScreenCapturer::get_instance().click(870, 100);
		Sleep(2000);
		state_ = START;
	}
	
	return;
}

void SMTaskProcessor::dowait() {
	int entry_time = (int) time(NULL);
	int wait_time = 30;
	ItemUser itemuser;
	while (time(NULL) < entry_time + wait_time) {
		std::auto_ptr<Image> img = ScreenCapturer::get_instance().capture();
		if (itemuser.test_and_use_item(*img)) {
			Sleep(5000);
			state_ = START;
			return;
		}


		std::wstring window = WindowsManager::get_instance().tell_window(*img);
		if (window == _T("gmcw")) {
			state_ = GMCW;
			return;
		}

		if (window == _T("rwcwxz")) {
			state_ = RWCWXZ;
			return;
		}

		if (window == _T("rwwpxz")) {
			state_ = RWWPXZ;
			return;
		}

		if (window == _T("bt")) {
			this->pricer = &this->gold_pricer;
			this->shopping_threshold = 799;
			this->submit_x = 780;
			this->submit_y = 600;
			this->prepare_x = 420;
			this->prepare_y = 240;
			state_ = SHOPPING;
			return;
		}

		if (window == _T("sh")) {
			this->pricer = &this->sh_pricer;
			this->shopping_threshold = 0x3fffffff;
			this->submit_x = 740;
			this->submit_y = 600;
			this->prepare_x = 640;
			this->prepare_y = 360;
			state_ = SHOPPING;
			return;
		}

		if (window == _T("yd") || window == _T("bqp")) {
			this->pricer = &this->yd_pricer;
			this->shopping_threshold = 500;
			this->submit_x = 760;
			this->submit_y = 545;
			this->prepare_x = 765;
			this->prepare_y = 255;
			state_ = SHOPPING;
			return;
		}

		Image wysfln_(*img, 725, 500, 140, 25);
		int dis = wysfln_.cmp(wysfln);
		std::cout << "wysfln:" << dis << std::endl;
		if (dis < 200000) {
			ScreenCapturer::get_instance().click(800, 510);
			Sleep(60000);
			state_ = START;
			return;
		}

		Image jrzd_(*img, 750, 500, 90, 25);
		dis = smjrzd.cmp(jrzd_);
		if (dis < 120000) {
			ScreenCapturer::get_instance().click(800, 510);
			Sleep(60000);
			state_ = START;
			return;
		}
		Sleep(5000);
	}
	state_ = START;
}