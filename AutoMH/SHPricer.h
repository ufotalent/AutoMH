#pragma once
#include "Pricer.h"
class SHPricer : public Pricer
{
public:
	SHPricer(void);
	~SHPricer(void);
	virtual bool has_sale(const Image& image) {
		return true;
	}

	virtual int price_len(const Image& image) {
		return 7;
	}

	virtual int first_digit(const Image& image) {
		return 9;
	}
};
