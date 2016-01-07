#pragma once
#include "Image.h"
class YBTaskProcessor
{
private:
	Image header;
public:
	YBTaskProcessor(void);
	~YBTaskProcessor(void);
	void run();
	void reset();
};
