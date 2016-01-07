#include "StdAfx.h"
#include <time.h>
#include <iostream>
#include "RWLTaskProcessor.h"
#include "ScreenCapturer.h"
#include "TaskManager.h"
#include "Image.h"
#include "WindowsManager.h"
#include "ImageFinder.h"

RWLTaskProcessor::RWLTaskProcessor(void) {
	this->state_ = START;
	// 730, 385, 70, 35
	rwl_button = Image(_T("buttons/rwl.bmp"));

	// 750. 388, 90, 25
	kszd_button = Image(_T("buttons/kszd.bmp"));

	

}

RWLTaskProcessor::~RWLTaskProcessor(void) {
}

void RWLTaskProcessor::reset() {
	state_ = START;
	user_triggered_ = true;
	chuanshuo_fail_ = false;
}

void RWLTaskProcessor::run() {
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

void RWLTaskProcessor::dowait() {
	int entry_time = (int) time(NULL);
	int wait_time = 0;
	if (wait_reason_ == BATTLE) {
		wait_time = 300;
	} else if (wait_reason_ == CHUANSHUO){
		wait_time = 1200;
	} else if (wait_reason_ == WALKING) {
		wait_time = 120;
	} else {
		wait_time = 60;
	}
	while (time(NULL) < entry_time + wait_time) {
		std::auto_ptr<Image> img = ScreenCapturer::get_instance().capture();
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
			this->shopping_threshold = 300;
			this->submit_x = 780;
			this->submit_y = 600;
			this->prepare_x = 420;
			this->prepare_y = 240;
			state_ = SHOPPING;
			return;
		}

		if (window == _T("sh")) {
			this->pricer = &this->sh_pricer;
			this->shopping_threshold = 300;
			this->submit_x = 740;
			this->submit_y = 600;
			this->prepare_x = 640;
			this->prepare_y = 360;
			state_ = SHOPPING;
			return;
		}

		if (window == _T("yd")) {
			this->pricer = &this->yd_pricer;
			this->shopping_threshold = 500;
			this->submit_x = 760;
			this->submit_y = 545;
			this->prepare_x = 765;
			this->prepare_y = 255;
			state_ = SHOPPING;
			return;
		}

		if (window == _T("")) {
			ImageFinder finder;
			{
				int dis = Image(*img, 750, 388, 90, 25).cmp(kszd_button);
				if (dis < 120000) {
					ScreenCapturer::get_instance().click(750, 388);
					return;
				}
			}
			{
				//Image button_area = Image(*img, 730, 385, 120, 150);
				Image button_area = Image(*img, 720, 210, 90, 330);
				ImageFinderResult find_result = finder.find_image(button_area, rwl_button);
				printf("rwl_button: %d %d %d\n",find_result.x, find_result.y, find_result.distance);
				if (find_result.distance < 130000 ) {
					ScreenCapturer::get_instance().click(find_result.x + 720 + rwl_button.getcx() / 2, find_result.y + 210 + rwl_button.getcy() / 2);
					return;
				}
			}
			
		}
		Sleep(5000);
	}
	if (wait_reason_ == CHUANSHUO) {
		this->chuanshuo_fail_ = true;
	}
	state_ = START;
}

void RWLTaskProcessor::dostart() {
	bool has_task = false;
	do {		
		std::auto_ptr<Image> img = ScreenCapturer::get_instance().capture();
		int ret = TaskManager::get_instance().find_and_click(*img, _T("rwl"));
		has_task = (ret > 0);
		
		printf("Checking RWL task: %d\n", ret);
		if (user_triggered_ || ret >= 0) break;
		Sleep(3000);
	} while (true);

	if (has_task) {
		wait_reason_ = WALKING;
		state_ = WAIT;
		return;
	}

	if (!user_triggered_ ) {
		state_ = STOP;
	} else {
		user_triggered_ = false;
		state_ = WAIT;
		wait_reason_ = ENTRY;
	}
	return;
}

void RWLTaskProcessor::dogmcw() {
	ScreenCapturer::get_instance().click(807, 597);
	wait_reason_ = WALKING;
	state_ = WAIT;
	return;
}

void RWLTaskProcessor::dorwcwxz() {
	ScreenCapturer::get_instance().click(650, 550);
	wait_reason_ = WALKING;
	state_ = WAIT;
	return;
}

void RWLTaskProcessor::dorwwpxz() {
	ScreenCapturer::get_instance().click(775, 546);
	wait_reason_ = WALKING;
	state_ = WAIT;
	return;
}

void RWLTaskProcessor::doshopping() {
	std::auto_ptr<Image> img = ScreenCapturer::get_instance().capture();
	this->wait_reason_ = CHUANSHUO;
	this->state_ = WAIT;
	if (pricer->has_sale(*img) || chuanshuo_fail_) {
		int f = pricer->first_digit(*img);
		int l = pricer->price_len(*img) - 1;
		while (l--) f = f * 10;
		if (f < this->shopping_threshold || chuanshuo_fail_) {
			ScreenCapturer::get_instance().click(this->prepare_x, this->prepare_y);
			Sleep(2000);
			ScreenCapturer::get_instance().click(this->submit_x, this->submit_y);
			this->wait_reason_ = WALKING;
			chuanshuo_fail_ = false;
			return;
		}
	}
	
	
	ScreenCapturer::get_instance().click(870, 100);
	Sleep(2000);
	ScreenCapturer::get_instance().click(403, 37);
	Sleep(2000);
	ScreenCapturer::get_instance().click(403, 37);
	Sleep(2000);
	ScreenCapturer::get_instance().click(360, 360);
	chuanshuo_fail_ = false;
	return;
}