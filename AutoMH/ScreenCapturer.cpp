#include "StdAfx.h"
#include "ScreenCapturer.h"
#include "Windows.h"

ScreenCapturer::ScreenCapturer(void)
{
	buffer_ = malloc(BUFFER_SIZE);
}

ScreenCapturer::~ScreenCapturer(void)
{
	free(buffer_);
}

ScreenCapturer& ScreenCapturer::get_instance() {
	static ScreenCapturer instance;
	return instance;
}

HWND ScreenCapturer::findOuterWindow() {
	HWND res = NULL;
	for (HWND hwnd = FindWindowEx(NULL, NULL, TEXT("CHWindow"), TEXT("")); hwnd != NULL; hwnd = FindWindowEx(NULL, hwnd, TEXT("CHWindow"), TEXT(""))) {
		if (::IsWindowVisible(hwnd)) {
			if (res != NULL) {
				throw std::runtime_error("cannot determine window");
			}
			res = hwnd;
		}
	}
	return res;	
}

HWND ScreenCapturer::findInnerWindow(HWND outerWindow) {
	return FindWindowEx(outerWindow, NULL, TEXT("CHWindow"), TEXT(""));
}

void ScreenCapturer::fix_window() {
	HWND outerWindow = findOuterWindow();
	HWND innerWindow = findInnerWindow(outerWindow);
	SetWindowPos(outerWindow, 0, 0, 0, OUTER_WINDOW_X, OUTER_WINDOW_Y, SWP_NOMOVE);
	printf("%lx %lx\n", outerWindow, innerWindow);
}

void ScreenCapturer::capture_to_clipboard(int x, int y, int cx, int cy) {
	HWND outerWindow = findOuterWindow();
	HWND hwnd = findInnerWindow(outerWindow);

	RECT rc;
	HDC hdcwindow = GetWindowDC(hwnd);
	GetWindowRect(hwnd, &rc);	

	if (rc.right - rc.left != INNER_WINDOW_X || rc.bottom - rc.top != INNER_WINDOW_Y) {
		throw std::runtime_error("wrong window size");
	}

    //create
    HDC hdcScreen = GetDC(NULL);
    HDC hdc = CreateCompatibleDC(hdcScreen);
    HBITMAP hbmp = CreateCompatibleBitmap(hdcScreen, 
        cx, cy);
    SelectObject(hdc, hbmp);
	
	BitBlt(hdc, 0, 0, cx, cy, hdcwindow, x, y, SRCCOPY);

    //copy to clipboard
    OpenClipboard(NULL);
    EmptyClipboard();
    SetClipboardData(CF_BITMAP, hbmp);
    CloseClipboard();

    //release
    DeleteDC(hdc);
    DeleteObject(hbmp);
    ReleaseDC(NULL, hdcScreen);
}

std::auto_ptr<Image> ScreenCapturer::capture() {
	HWND outerWindow = findOuterWindow();
	HWND hwnd = findInnerWindow(outerWindow);

	RECT rc;
	HDC hdcwindow = GetWindowDC(hwnd);
	GetWindowRect(hwnd, &rc);	

	if (rc.right - rc.left != INNER_WINDOW_X || rc.bottom - rc.top != INNER_WINDOW_Y) {
		throw std::runtime_error("wrong window size");
	}

    //create
    HDC hdcScreen = GetDC(NULL);
    HDC hdc = CreateCompatibleDC(hdcScreen);
    HBITMAP hbmp = CreateCompatibleBitmap(hdcScreen, 
        rc.right - rc.left, rc.bottom - rc.top);
    SelectObject(hdc, hbmp);
	
	BitBlt(hdc, 0, 0, rc.right - rc.left, rc.bottom - rc.top, hdcwindow, 0, 0, SRCCOPY);
	//BitBlt(hdc, 0, 0, 15, 20, hdcwindow, 380, 244, SRCCOPY);
	if (GetBitmapBits(hbmp, BUFFER_SIZE, buffer_) != BUFFER_SIZE) {
		throw std::runtime_error("failed to get bits");
	}

    //copy to clipboard
    /*OpenClipboard(NULL);
    EmptyClipboard();
    SetClipboardData(CF_BITMAP, hbmp);
    CloseClipboard();*/

    //release
    DeleteDC(hdc);
    DeleteObject(hbmp);
    ReleaseDC(NULL, hdcScreen);


	//printf("hwnd: %d\n", hwnd);
	Image *ret = new Image(INNER_WINDOW_X, INNER_WINDOW_Y);
	ret->set_data(buffer_);
	return std::auto_ptr<Image>(ret);
}

void ScreenCapturer::scroll(int fx, int fy, int tx, int ty) {
	fx = fx + rand() % 10 - 5;
	fy = fy + rand() % 10 - 5;
	tx = tx + rand() % 10 - 5;
	ty = ty + rand() % 10 - 5;
	RECT rc;
	GetWindowRect(this->findInnerWindow(findOuterWindow()), &rc);
	::SetCursorPos(fx + rc.left, fy + rc.top);
	::mouse_event(MOUSEEVENTF_LEFTDOWN, fx, fy, 0, 0);
	for (double step = 0; step < 1; step += 0.1) {
		int x = (step * tx + (1 - step) * fx);
		int y = (step * ty + (1 - step) * fy);
		::SetCursorPos(x + rc.left, y + rc.top);
		Sleep(rand() % 200);
	}
	::mouse_event(MOUSEEVENTF_LEFTUP, tx, ty, 0, 0);
}

void ScreenCapturer::click(int x, int y) {

	x = x + rand() % 5 - 2;
	y = y + rand() % 5 - 2;
	RECT rc;
	GetWindowRect(this->findInnerWindow(findOuterWindow()), &rc);
	::SetCursorPos(x + rc.left, y + rc.top);
	::mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0);
	Sleep(rand() % 300 + 200);
	::mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0);

	/*
	RECT rc;
	GetWindowRect(this->findInnerWindow(findOuterWindow()), &rc);
	POINT point;
	::GetCursorPos(&point);

	printf("%d %d %d %d\n", x, y, point.x, point.y);
	INPUT input;
    input.type=INPUT_MOUSE;
	//input.mi.dx=65535 * (x ) / GetSystemMetrics (SM_CXSCREEN);
	//input.mi.dy=65535 * (y ) / GetSystemMetrics (SM_CYSCREEN);
	input.mi.dx = 1;
	input.mi.dy = 1;
    input.mi.dwFlags=(MOUSEEVENTF_MOVE|MOUSEEVENTF_LEFTDOWN|MOUSEEVENTF_LEFTUP);
    input.mi.mouseData=0;
    input.mi.dwExtraInfo=NULL;
    input.mi.time=0;
    SendInput(1,&input,sizeof(INPUT));
	Sleep(500);
*/
	/*
	::GetCursorPos(&point);
	input.mi.dx=65535 * (x - point.x) / GetSystemMetrics (SM_CXSCREEN);
	input.mi.dy=65535 * (y - point.y) / GetSystemMetrics (SM_CYSCREEN);
	input.mi.dwFlags=(MOUSEEVENTF_LEFTUP);
	SendInput(1,&input,sizeof(INPUT));
	/*
	RECT rc;
	GetWindowRect(this->findInnerWindow(findOuterWindow()), &rc);
	::SetCursorPos(x + rc.left, y + rc.top);
	::Sleep(500);
	::mouse_event(MOUSEEVENTF_LEFTDOWN, x, y, 0, 0);
	::Sleep(500);
	::mouse_event(MOUSEEVENTF_LEFTUP, x, y, 0, 0);

	*/
	//mouse)e(this->findInnerWindow(this->findOuterWindow()), WM_LBUTTONDBLCLK, MK_LBUTTON, MAKELPARAM(x, y));
	
	/*
	PostMessage(this->findOuterWindow(), WM_LBUTTONDOWN, 0, MAKELPARAM(x, y));
	Sleep(100);
	PostMessage(this->findOuterWindow(), WM_LBUTTONUP, 0, MAKELPARAM(x, y));*/
}