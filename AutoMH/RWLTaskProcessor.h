#pragma once
#include "Image.h"
#include "Pricer.h"
#include "GoldPricer.h"
#include "SHPricer.h"
#include "YDPricer.h"
class RWLTaskProcessor
{
private:
	enum RWLState {
		START,
		WAIT,
		GMCW,
		RWCWXZ,
		RWWPXZ,
		SHOPPING,
		STOP
	};
	enum WaitReason {
		WALKING,
		RESPOND,
		BATTLE,
		CHUANSHUO,
		ENTRY
	};
	RWLState state_;
	WaitReason wait_reason_;
	void dostart();
	void dowait();
	void dogmcw();
	void dorwcwxz();
	void dorwwpxz();
	void doshopping();

	bool chuanshuo_fail_;
	GoldPricer gold_pricer;
	SHPricer sh_pricer;
	YDPricer yd_pricer;
	Pricer* pricer;
	int shopping_threshold;
	int submit_x, submit_y;
	int prepare_x, prepare_y;

	bool user_triggered_;
	Image rwl_button, kszd_button;
public:
	RWLTaskProcessor(void);
	~RWLTaskProcessor(void);
	void run();
	void reset();
};
