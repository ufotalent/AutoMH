#include "StdAfx.h"
#include <cstdio>
#include "Image.h"
#include "Windows.h"

Image::Image(void)
{
	this->cx_ = this->cy_ = 0;	
}

Image::~Image(void)
{
}

Image::Image(int cx, int cy) {
	this->cx_ = cx;
	this->cy_ = cy;
	this->data_.resize(cy, std::vector<int>(cx));
}

Image::Image(const std::wstring filename) {
	FILE *fp;
	int width,height;
	if ((fp = _wfopen(filename.c_str(), _T("rb"))) == NULL) {
		throw std::runtime_error("image not found");
	}
	BITMAPFILEHEADER  bfHeader;
	BITMAPINFOHEADER  biHeader;
	fread(&bfHeader, sizeof(bfHeader), 1, fp);
	fread(&biHeader, sizeof(biHeader), 1, fp);
	fclose(fp);
	width = biHeader.biWidth;
	height = biHeader.biHeight;
	HBITMAP hbmp = (HBITMAP) LoadImage(NULL, filename.c_str(), IMAGE_BITMAP, width, height, LR_LOADFROMFILE);

	void *ptr = malloc(width * height * 4);
	GetBitmapBits(hbmp, width * height * 4, ptr);
	DeleteObject(hbmp);

	this->cx_ = width;
	this->cy_ = height;
	this->data_.resize(cy_, std::vector<int>(cx_));
	this->set_data(ptr);
	free(ptr);
}

Image::Image(const Image &image, int x, int y, int cx, int cy) {
	if (x + cx > image.cx_ || y + cy > image.cy_) {
		throw std::runtime_error("illegal reference");
	}
	this->cx_ = cx;
	this->cy_ = cy;
	this->data_.resize(cy, std::vector<int>(cx));
	for (int i = 0; i < cy; i++) {
		for (int j = 0; j < cx; j++) {
			this->data_[i][j] = image.data_[i + y][j + x];
		}
	}
}

int Image::get_pixel(int x, int y) const {
	return this->data_[y][x];
}

void Image::print() {
	printf("Size: %d %d\n", cx_, cy_);
	for (int i = 0; i < cy_; i++) {
		for (int j = 0; j < cx_; j++) {
			printf("(%d, %d, %d)", (data_[i][j] & 255), ((data_[i][j] >> 8) & 255), ((data_[i][j] >> 16) & 255));
		}
		printf("\n");
	}
}

void Image::set_data(void *ptr) {
	for (int y = 0; y < cy_; y++) {
		for (int x = 0; x < cx_; x++) {
			int *p=(int*)ptr + y * cx_ + x;
			data_[y][x] = *p;
		}
	}
}

int Image::cmp(const Image& rhs) {
	if (cx_ != rhs.cx_ || cy_ != rhs.cy_) {
		throw std::runtime_error("size mismatch");
	}
	int ret = 0;
	for (int y = 0; y < cy_; y++) {
		for (int x = 0; x < cx_; x++) {
			int b = data_[y][x] & 0xff;
			int g = (data_[y][x] & 0xff00) >> 8;
			int r = (data_[y][x] & 0xff0000) >> 16;
			int bb = rhs.data_[y][x] & 0xff;
			int gg = (rhs.data_[y][x] & 0xff00) >> 8;
			int rr = (rhs.data_[y][x] & 0xff0000) >> 16;
			ret += abs(r - rr) + abs(b - bb) + abs(g - gg);
		}
	}
	return ret;
}

