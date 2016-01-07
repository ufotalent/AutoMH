#include "StdAfx.h"
#include "YBTaskProcessor.h"
#include "FutureTaskManager.h"
#include "ScreenCapturer.h"
YBTaskProcessor::YBTaskProcessor(void)
{
	//86, 100, 200, 20
	header = Image(_T("windows/yb.bmp"));
}

YBTaskProcessor::~YBTaskProcessor(void)
{
}

void YBTaskProcessor::reset() {

}

void YBTaskProcessor::run() {
	while (true) {
		bool success = FutureTaskManager::get_instance().get_task(_T("yb"));
		if (success) {
			Sleep(30000);
			printf("Click yb\n");
			ScreenCapturer::get_instance().click(792, 456);
			Sleep(3000);
			printf("Click confirm\n");
			ScreenCapturer::get_instance().click(565, 404);

			Sleep(3000);
			int cnt = 20;
			while (true) {
				std::auto_ptr<Image> screen = ScreenCapturer::get_instance().capture();
				if (Image(*screen, 86, 100, 200, 20).cmp(header) < 16000) {
					cnt = 20;
				}
				if (cnt-- == 0) {
					break;
				}
				printf("YB tick: %d\n", cnt);
				Sleep(5000);
			}
		} else {
			return;
		}
	}
}