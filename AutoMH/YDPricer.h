#pragma once
#include "Pricer.h"
class YDPricer : public Pricer
{
public:
	YDPricer(void);
	~YDPricer(void);
	virtual bool has_sale(const Image& image) {
		return true;
	}

	virtual int price_len(const Image& image) {
		return 1;
	}

	virtual int first_digit(const Image& image) {
		return 0;
	}
};
