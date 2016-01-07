#include "StdAfx.h"
#include "GoldPricer.h"
#include <limits>
#include <sstream>
GoldPricer::GoldPricer(void)
{
	for (int i = 1; i <= 9; i++) {
		std::wstringstream str;
		str << _T("numbers/") << i << _T(".bmp");
		
		numbers_[i].reset(new Image(str.str()));
	}
}

GoldPricer::~GoldPricer(void)
{
}

int GoldPricer::first_digit(const Image &image) {
	int minindex = -1;
	int mindis = std::numeric_limits<int>::max();

	Image region(image, 380, 244, 15, 20);
	for (int i = 1; i <= 9; i++) {
		int dis = region.cmp(*numbers_[i]);
		if (dis < mindis) {
			mindis = dis;
			minindex = i;
		}
	}
	return minindex;
}


// Find the rightmost non-background color position.
int GoldPricer::price_len(const Image &image) {
	int startx = 380;
	int starty = 250;
	int endx = 500;
	int r = 244;
	int g = 209;
	int b = 164;
	int templates[9] = {0};
	int maxx = startx;
	for (int x = startx; x < endx; x++) {
		int rgb = image.get_pixel(x, starty);
		int bb = rgb & 0xff;
		int gg = (rgb & 0xff00) >> 8;
		int rr = (rgb & 0xff0000) >> 16;
		int dis = abs(r - rr) + abs(b - bb) + abs(g - gg);
		if (dis > 50) {
			maxx = x;
		}
	}
	int width = maxx - startx;
	int minindex = 8;
	int min = std::numeric_limits<int>::max();
	for (int i = 1; i <= 7; i++) {
		int predicted = i * 14 + ((i - 1) / 3) * 8;
		if (abs(width - predicted) < min) {
			min = abs(width - predicted);
			minindex = i;
		}
	}
	return minindex;
	
}

bool GoldPricer::has_sale(const Image &image) {
	return true;
}