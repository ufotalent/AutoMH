#pragma once
#include "Image.h"
#include "Pricer.h"
class GoldPricer : public Pricer
{
private:
	std::auto_ptr<Image> numbers_[10]; // 1 .. 9, 0 is NULL
public:
	GoldPricer(void);
	~GoldPricer(void);
	bool has_sale(const Image& image);
	int price_len(const Image& image);
	int first_digit(const Image& image);

};
