#pragma once
#include "Image.h"
class BTTaskProcessor
{
private:
	Image bt_;
public:
	BTTaskProcessor(void);
	~BTTaskProcessor(void);
	void run();
	void reset();
};
