#include "StdAfx.h"
#include "AccountManager.h"
#include "ScreenCapturer.h"
#include <iostream>
AccountManager::AccountManager(void): 
login_button_(_T("buttons/login.bmp")),
lt_button_(_T("buttons/lt.bmp"))  // 425 245 40 40
{
	
}

AccountManager::~AccountManager(void)
{
}

bool AccountManager::is_logged_in() {
	ScreenCapturer& screen = ScreenCapturer::get_instance();
	std::auto_ptr<Image> img = screen.capture();
	Image button(*img, 400, 550, 100, 40);
	int dis = button.cmp(login_button_);
	std::wcout << "button distance" << dis << std::endl;
	if (dis < 40000) {
		return false;
	} else {
		return true;
	}
}

void AccountManager::logout() {
	// wait for the right bottom button to recover
	// Sleep(30000);
	ScreenCapturer& screen = ScreenCapturer::get_instance();
	screen.click(920, 674);
	Sleep(5000);
	screen.click(520, 674);
	Sleep(5000);
	screen.click(292, 545);
	Sleep(5000);
	screen.click(566, 404);
	Sleep(5000);
}

void AccountManager::login(int id) {
	ScreenCapturer& screen = ScreenCapturer::get_instance();
	screen.click(920, 48);
	Sleep(5000);
	screen.click(912, 38);
	Sleep(5000);
	screen.click(606, 292);
	Sleep(3000);

	int x = 528;
	int y = 334 + (376 - 338) * id;
	screen.click(x, y);
	Sleep(3000);
	screen.click(510,359);
	Sleep(10000);
	screen.click(484, 566);
	Sleep(30000);

	// initialize
	// choose first zhuzhan
	screen.click(920, 674);
	Sleep(2000);
	screen.click(837, 673);
	Sleep(5000);
	screen.click(522, 166);
	Sleep(2000);
	screen.click(894, 101);
	Sleep(5000);

	// click on guaji
	ScreenCapturer::get_instance().click(403, 35);
	Sleep(2000);
	ScreenCapturer::get_instance().click(403, 35);
	Sleep(2000);

	// get pingdinganbang
	ScreenCapturer::get_instance().click(117, 594);
	Sleep(3000);

	ScreenCapturer::get_instance().click(353, 522);
	Sleep(3000);

	Image skill(*ScreenCapturer::get_instance().capture(), 425, 245, 40, 40);
	int dis = skill.cmp(lt_button_);
	std::cout << "lt distance " << dis << std::endl;
	if (dis > 30000) {
		ScreenCapturer::get_instance().click(445, 265);
		Sleep(5000);
	} else {
		ScreenCapturer::get_instance().click(353, 522);
		Sleep(3000);
	}
	screen.click(894, 101);
	Sleep(5000);
}