#pragma once
#include <string>
#include <vector>
#include <map>
#include "Image.h"
struct WindowInfo {
	Image id_img;
	int id_x;
	int id_y;
	std::wstring key;
};

class WindowsManager
{
private:
	std::vector<std::wstring> keys;
	std::map<std::wstring, WindowInfo> windows;
	
	WindowsManager(void);
	
	WindowsManager(const WindowsManager&);
public:
	~WindowsManager(void);
	static WindowsManager& get_instance();
	std::wstring tell_window(const Image& screen);
};
