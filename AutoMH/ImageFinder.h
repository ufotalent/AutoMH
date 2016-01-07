#pragma once
#include <algorithm>
#include "Image.h"
struct ImageFinderResult {
	int x;
	int y;
	int distance;
};
class ImageFinder
{
public:
	ImageFinder(void);
	~ImageFinder(void);
	ImageFinderResult find_image(const Image& src, const Image& target);
};
