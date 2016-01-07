#include "StdAfx.h"
#include "FutureTaskManager.h"
#include "ImageFinder.h"
#include "ScreenCapturer.h"
#include <sstream>
FutureTaskManager::FutureTaskManager(void) {
	keys.clear();
	keys.push_back(_T("bt"));
	keys.push_back(_T("yb"));
	keys.push_back(_T("mj"));
	keys.push_back(_T("sm"));

	// Images are sampled at (290 / 631, 160, 45, 22)
	for (unsigned int i = 0; i < keys.size(); i++) {
		std::wstringstream str;
		str << _T("futuretasks/") << keys[i] << _T(".bmp");

		this->images[keys[i]] = Image(str.str());
	}
}

FutureTaskManager::~FutureTaskManager(void)
{
}

FutureTaskManager& FutureTaskManager::get_instance() {
	static FutureTaskManager instance;
	return instance;
}

bool FutureTaskManager::find_and_click(const Image &screen, std::wstring key) {
	const Image& pattern = images[key];
	const Image screen_left(screen, 285, 100, 60, 300);
	const Image screen_right(screen, 625, 100, 60, 300);
	ImageFinder finder;
	ImageFinderResult left, right, result;
	left = finder.find_image(screen_left, pattern);
	right = finder.find_image(screen_right, pattern);
	bool isleft = false;
	if (left.distance < right.distance) {
		result = left;
		isleft = true;
	} else {
		result = right;
		isleft = false;
	}
	printf("FutureTask: %d %d %d\n", result.x, result.y, result.distance);
	if (result.distance < 70000) {
		int p = (isleft ? screen.get_pixel(result.x + 130 + 288, result.y + 100) : screen.get_pixel(result.x + 130 + 628, result.y + 100));
		int r = (p & 0xff0000) >> 16;
		int g = (p & 0xff00) >> 8;
		int b = (p & 0xff);
		if (abs(r - g) < 10 && abs(g - b) < 10) {
			printf("Completed task marked false\n");
			return false;
		}
		ScreenCapturer::get_instance().click(result.x + (isleft ? 500 : 840), result.y + 125);
		return true;
	}
	return false;
}

bool FutureTaskManager::get_task(std::wstring key) {
	printf("clicking on huodong\n");
	ScreenCapturer::get_instance().click(325, 35);
	Sleep(2000);
	ScreenCapturer::get_instance().click(325, 35);
	Sleep(2000);
	ScreenCapturer::get_instance().click(140, 166);
	Sleep(2000);
	for (int i = 0; i < 3; i++) {
		ScreenCapturer::get_instance().scroll(328, 164, 328, 410);
	}
	Sleep(2000);
	bool success = false;
	for (int i = 0; i < 3; i++) {
		std::auto_ptr<Image> screen = ScreenCapturer::get_instance().capture();
		success = find_and_click(*screen, key);
		if (!success) {
			ScreenCapturer::get_instance().scroll(328, 410, 328, 204);
			Sleep(2000);
		} else {
			break;
		}
	}
	
	if (!success) {
		printf("Closing huodong\n");
		ScreenCapturer::get_instance().click(887, 97);
		Sleep(3000);
	}
	return success;
}