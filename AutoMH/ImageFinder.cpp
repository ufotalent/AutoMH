#include "StdAfx.h"
#include "ImageFinder.h"
#include <limits>
ImageFinder::ImageFinder(void)
{
}

ImageFinder::~ImageFinder(void)
{
}

ImageFinderResult ImageFinder::find_image(const Image &src, const Image &target) {
	ImageFinderResult result;
	result.x = result.y = 0;
	result.distance = std::numeric_limits<int>::max();
	for (int dx = 0; dx <= src.getcx() - target.getcx(); dx++) {
		for (int dy = 0; dy <= src.getcy() - target.getcy(); dy++) {
			int dis = Image(src, dx, dy, target.getcx(), target.getcy()).cmp(target);
			
			if (dis < result.distance) {
				//printf("%d %d: %d\n", dx, dy, dis);
				result.distance = dis;
				result.x = dx;
				result.y = dy;
			}
		}
	}
	return result;
}