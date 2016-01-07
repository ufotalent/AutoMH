#pragma once
#include <memory>
#include "Image.h"
#include "Windows.h"
class ScreenCapturer
{
public:
	virtual ~ScreenCapturer(void);
	std::auto_ptr<Image> capture();
	void capture_to_clipboard(int x, int y, int cx, int cy);
	void fix_window();
	void click(int x, int y);
	void scroll(int fx, int fy, int tx, int ty);
	static ScreenCapturer& get_instance();
	
private:
	ScreenCapturer();
	ScreenCapturer(const ScreenCapturer&);
	HWND findOuterWindow();
	HWND findInnerWindow(HWND outerWindow);
	void* buffer_;
};

const static int OUTER_WINDOW_X = 962;
const static int OUTER_WINDOW_Y = 757;
const static int INNER_WINDOW_X = 960;
const static int INNER_WINDOW_Y = 720;
const static int BUFFER_SIZE = INNER_WINDOW_X * INNER_WINDOW_Y * 4;
