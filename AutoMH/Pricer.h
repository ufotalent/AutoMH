#pragma once
#include "Image.h"
class Pricer
{
public:
	Pricer(void);
	~Pricer(void);
	virtual bool has_sale(const Image& image) = 0;
	virtual int price_len(const Image& image) = 0;
	virtual int first_digit(const Image& image) = 0;
};
