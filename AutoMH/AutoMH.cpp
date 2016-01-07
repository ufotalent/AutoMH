// AutoMH.cpp : 定义控制台应用程序的入口点。
//

#include "stdafx.h"
#include "ScreenCapturer.h"
#include "GoldPricer.h"
#include "TaskManager.h"
#include "RWLTaskProcessor.h"
#include "BTTaskProcessor.h"
#include "YBTaskProcessor.h"
#include "MJTaskProcessor.h"
#include "SMTaskProcessor.h"
#include "AccountManager.h"
#include <set>
#include <string>
#include <iostream>
int _tmain(int argc, _TCHAR* argv[])
{
	std::set<std::wstring> cmd_set;
	std::vector<int> accounts;
	for (int i = 1; i < argc; i++) {
		std::wstring cmd = argv[i];
		
		if (cmd.length() > 6 && cmd.substr(0, 7) == _T("account")) {
			std::wstring num = cmd.substr(7);
			accounts.push_back(_tstoi(num.c_str()));
			std::wcout << accounts.back() << std::endl;
		}
		cmd_set.insert(cmd);
	}
	ScreenCapturer& capturer = ScreenCapturer::get_instance();
	GoldPricer pricer;
	int a, b, c, d;
	AccountManager account_manager;
	while (scanf("%d%d%d%d", &a, &b, &c, &d) != EOF) {
		do {
			RWLTaskProcessor rwlprocessor;
			BTTaskProcessor btprocessor;
			YBTaskProcessor ybprocessor;
			MJTaskProcessor mjprocessor;
			SMTaskProcessor smprocessor;
			std::auto_ptr<Image> img = capturer.capture();
			capturer.capture_to_clipboard(a, b, c, d);
			if (!account_manager.is_logged_in()) {
				if (accounts.size() == 0) {
					continue;
				}
				account_manager.login(accounts[0]);
				accounts.erase(accounts.begin());
			}
			
			if (cmd_set.count(_T("sm"))) {
				smprocessor.reset();
				smprocessor.run();

			}
			if (cmd_set.count(_T("bt"))) {
				btprocessor.reset();
				btprocessor.run();
			}

			if (cmd_set.count(_T("mj"))) {
				mjprocessor.reset();
				mjprocessor.run();
			}

			if (cmd_set.count(_T("yb"))) {
				ybprocessor.reset();
				ybprocessor.run();
			}


			if (cmd_set.count(_T("rwl"))) {
				rwlprocessor.reset();
				rwlprocessor.run();
			}
			if (!accounts.empty()) {
				account_manager.logout();
			}
		} while (!accounts.empty());
		/*
		for (int x = 200; x < 500; x += 10) {
			capturer.click(x, 500);
			//Sleep(10000);
		}*/
	}
	return 0;
}

