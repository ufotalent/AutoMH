#pragma once
#include <vector>

class Image
{
private:
	int cx_;
	int cy_;
	std::vector<std::vector<int>> data_;
public:
	Image(int cx, int cy);
	Image(const Image& image, int x, int y, int cx, int cy);
	Image(const std::wstring filename);
	Image(void);
	~Image(void);
	
	void set_data(void*);
	void print();
	int cmp(const Image& image);
	int getcx() const { return cx_; }
	int getcy() const { return cy_; }
	int get_pixel(int x, int y) const;
};
