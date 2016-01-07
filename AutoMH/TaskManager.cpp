#include "StdAfx.h"
#include "TaskManager.h"
#include "ScreenCapturer.h"
#include <sstream>

TaskManager& TaskManager::get_instance() {
	static TaskManager instance;
	return instance;
}

TaskManager::TaskManager(void) : header(_T("tasks/header.bmp")) {
	keys.clear();
	keys.push_back(_T("rwl"));
	keys.push_back(_T("sm"));
	keys.push_back(_T("bt"));


	// Images are sampled at y:760 x:155 for sm
	for (unsigned int i = 0; i < keys.size(); i++) {
		std::wstringstream str;
		str << _T("tasks/") << keys[i] << _T(".bmp");

		this->images[keys[i]] = Image(str.str());
	}
}

TaskManager::~TaskManager(void)
{
}

std::vector<std::vector<bool> > TaskManager::get_yellow_bitmap(const Image& img) {
	std::vector<std::vector<bool> > ret(img.getcy(), std::vector<bool>(img.getcx(), false));
	for (int y = 0; y < img.getcy(); y++) {
		for (int x = 0; x < img.getcx(); x++) {
			int rgb = img.get_pixel(x, y);
			int b = rgb & 0xff;
			int g = (rgb & 0xff00) >> 8;
			int r = (rgb & 0xff0000) >> 16;
			if (r > 200 && g > 200 && b < 100) {
				ret[y][x] = true;
			}
		}
	}
	return ret;
}

static void print(const std::vector<std::vector<bool> >& data) {
	for (int i = 0; i < data.size(); i++) {
		for (int j = 0; j < data[0].size(); j++) {
			if (data[i][j]) {
				printf("*");
			} else {
				printf(".");
			}
		}
		printf("\n");
	}
}

// 1 for found, 0 for unfound, -1 for invalid
int TaskManager::find_and_click(const Image& screen, std::wstring key) {
	if (!is_valid(screen)) {
		return -1;
	}
	const Image& img = images[key];
	std::vector<std::vector<bool> > pat = get_yellow_bitmap(img);
	int t = 1; 
	int st = 0;
	while (t--) {
		int foundy = -1;
		int dx = 760;
		for (int dy = 150; dy < 405; dy++) {
			const Image region(screen, dx, dy, img.getcx(), img.getcy());
			std::vector<std::vector<bool> > src = get_yellow_bitmap(region);
			int cnt = 0;
			int tot = 0;
			
			for (int y = 0; y < img.getcy(); y++) {
				for (int x = 0; x < img.getcx(); x++) {
					tot += src[y][x] | pat[y][x];
					cnt += src[y][x] & pat[y][x];
				}
			}
			double ratio = cnt * 1.0 / tot;
			/*
			if (dy == 248) {
				
				printf("----\n");
				print(src);
				printf("----\n");
				print(pat);
			}*/
			
			//printf("%d: %lf\n", dy, ratio);
			if (ratio >= 0.30) {
				foundy = dy;
			}
		}
		if (foundy != -1) {
			ScreenCapturer::get_instance().click(dx, foundy);
			Sleep(1000);
			ScreenCapturer::get_instance().click(dx, foundy);
			Sleep(1000);
			return 1;
		}
		if (t != 0) {
			ScreenCapturer::get_instance().scroll(854, 366, 854, 179);
			Sleep(2000);
		}
	};

	return 0;
}

bool TaskManager::is_valid(const Image& screen) {
	// 765, 105
	return Image(screen, 765, 105, 19, 19).cmp(header) < 8000;
}