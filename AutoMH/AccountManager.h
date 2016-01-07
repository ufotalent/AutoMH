#pragma once
#include "Image.h"
class AccountManager
{
private:
	Image login_button_;
	Image lt_button_;
public:
	AccountManager(void);
	~AccountManager(void);
	bool is_logged_in();
	void logout();
	void login(int id);
};
