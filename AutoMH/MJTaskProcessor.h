#pragma once

#include "Image.h"
class MJTaskProcessor
{
private:
	Image jrzd_button;
public:
	MJTaskProcessor(void);
	~MJTaskProcessor(void);
	void run();
	void reset();
};
