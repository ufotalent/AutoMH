#include "StdAfx.h"
#include "MJTaskProcessor.h"
#include "FutureTaskManager.h"
#include "ScreenCapturer.h"
MJTaskProcessor::MJTaskProcessor(void)
{
	jrzd_button = Image(_T("buttons/jrzd.bmp"));
}

MJTaskProcessor::~MJTaskProcessor(void)
{
}

void MJTaskProcessor::reset() {

}

void MJTaskProcessor::run() {
	bool success = FutureTaskManager::get_instance().get_task(_T("mj"));
	Sleep(30000);
	if (success == false) {
		return;
	}
	ScreenCapturer::get_instance().click(800, 450);
	Sleep(3000);
	ScreenCapturer::get_instance().click(209, 337);
	Sleep(3000);
	ScreenCapturer::get_instance().click(480, 320);
	Sleep(3000);
	ScreenCapturer::get_instance().click(510, 486);
	Sleep(3000);
	ScreenCapturer::get_instance().click(848, 252);
	Sleep(3000);
	do {
		ScreenCapturer::get_instance().click(840, 240);
		Sleep(2000);
		// 750, 445, 90, 25
		std::auto_ptr<Image> screen = ScreenCapturer::get_instance().capture();
		Image area(*screen, 750, 445, 90, 25);
		printf("checking jrzd_button");
		if (area.cmp(jrzd_button) < 120000) {
			break;
		}
		Sleep(30000);
	} while (true);

	ScreenCapturer::get_instance().click(43, 49);
	Sleep(3000);
	ScreenCapturer::get_instance().click(43, 49);
	Sleep(3000);
	ScreenCapturer::get_instance().click(474, 355);
	Sleep(3000);
}
