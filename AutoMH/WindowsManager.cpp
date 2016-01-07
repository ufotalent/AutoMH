#include "StdAfx.h"
#include "WindowsManager.h"
#include <sstream>

#define DEFINE_WINDOW(id, idx, idy) \
	keys.push_back(_T(#id)); \
	WindowInfo& id = windows[_T(#id)]; \
	id.id_x = idx; \
	id.id_y = idy; \
	id.key = _T(#id);
WindowsManager::WindowsManager(void) {

	DEFINE_WINDOW(gmcw, 430, 80);
	DEFINE_WINDOW(rwcwxz, 400, 155);
	DEFINE_WINDOW(rwwpxz, 707, 161);
	DEFINE_WINDOW(bt, 438, 80);
	DEFINE_WINDOW(sh, 438, 80);
	DEFINE_WINDOW(yd, 452, 78);
	DEFINE_WINDOW(bqp, 438, 80);
	/*
	keys.push_back(_T("gmcw"));
	WindowInfo& gmcw = windows[_T("gmcw")];
	gmcw.id_x = 430;
	gmcw.id_y = 80;
	gmcw.key = _T("gmcw");

	keys.push_back(_T("rwcwxz"));
	WindowInfo& rwcwxz = windows[_T("rwcwxz")];
	rwcwxz.id_x = 400;
	rwcwxz.id_y = 155;
	rwcwxz.key = _T("rwcwxz");

	// 707 161 150 25
	keys.push_back(_T("rwwpxz"));
	WindowInfo& rwwpxz = windows[_T("rwwpxz")];
	rwwpxz.id_x = 707;
	rwwpxz.id_y = 161;
	rwwpxz.key = _T("rwwpxz");
	
	// 438 80 80 20
	keys.push_back()*/

	for (unsigned int i = 0; i < keys.size(); i++) {
		std::wstringstream str;
		str << _T("windows/") << keys[i] << _T(".bmp");

		this->windows[keys[i]].id_img = Image(str.str());
	}
}

WindowsManager::~WindowsManager(void)
{
}

WindowsManager& WindowsManager::get_instance() {
	static WindowsManager instance;
	return instance;
}

std::wstring WindowsManager::tell_window(const Image &screen) {
	for (unsigned int i = 0; i < keys.size(); i++) {
		std::wstring key = keys[i];
		WindowInfo& info = windows[key];
		Image region(screen, info.id_x, info.id_y, info.id_img.getcx(), info.id_img.getcy());
		int dis = (region.cmp(info.id_img));
		
		if (dis < info.id_img.getcx() * info.id_img.getcy() * 10) {
			return key;
		}
	}
	return _T("");
}