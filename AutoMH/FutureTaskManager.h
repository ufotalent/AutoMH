#pragma once
#include <string>
#include <vector>
#include <map>
#include "Image.h"
class FutureTaskManager
{
	std::vector<std::wstring> keys;
	std::map<std::wstring, Image> images;
	FutureTaskManager(void);
	
	bool find_and_click(const Image& screen, std::wstring key);
public:
	~FutureTaskManager(void);
	static FutureTaskManager& get_instance();
	bool get_task(std::wstring key);
};
