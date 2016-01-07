#pragma once
#include "Image.h"
#include "Pricer.h"
#include "GoldPricer.h"
#include "SHPricer.h"
#include "YDPricer.h"

class SMTaskProcessor
{
	enum SMState {
		START,
		WAIT,
		GMCW,
		RWCWXZ,
		RWWPXZ,
		SHOPPING,
		STOP
	} state_;
public:
	void dostart();
	void dowait();
	void dogmcw();
	void dorwcwxz();
	void dorwwpxz();
	void doshopping();
	GoldPricer gold_pricer;
	SHPricer sh_pricer;
	YDPricer yd_pricer;
	Pricer* pricer;
	int shopping_threshold;
	int submit_x, submit_y;
	int prepare_x, prepare_y;
	Image rw_sm;
	Image rw_expand;
	Image wysfln;
	Image smjrzd;
	SMTaskProcessor(void);
	~SMTaskProcessor(void);
	void run();
	void reset() {
		state_ = START;

	}
};
