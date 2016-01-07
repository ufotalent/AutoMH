#pragma once
#include <string>
#include <vector>
#include <map>
#include "Image.h"
class TaskManager
{
private:
	std::vector<std::wstring> keys;
	std::map<std::wstring, Image> images;
	std::vector<std::vector<bool>> get_yellow_bitmap(const Image& img);
	TaskManager(void);
	TaskManager(const TaskManager&);
	Image header;
	bool is_valid(const Image& screen);
public:
	~TaskManager(void);
	static TaskManager& get_instance();
	
	int find_and_click(const Image& screen, std::wstring key);
};
