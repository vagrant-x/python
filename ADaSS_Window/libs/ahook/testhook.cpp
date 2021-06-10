// testhook.cpp : 此文件包含 "main" 函数。程序执行将在此处开始并结束。
//

#include<stdio.h>
#include<Windows.h>
#define ZKINTERFACE __declspec(dllimport)
#define APICALL __stdcall
//Ahook.dll 接口

typedef  void (*pSetHook)();
typedef  void (*pUnHook)();
typedef int (*pSelectDev)(const char* vendor_id, const char* product_id, const char* ip, const char* busid);


//Fn
typedef int(__cdecl* PushMessage)(char* message);
typedef void(__cdecl* Log4Dll)(const char* logstr, const char* file, const char* function, int line);// 日志回掉函数
typedef  int (*pinitDriver)(PushMessage, Log4Dll);
typedef int (*pReadImage)(char* args, char* resmsg, char* errmsg, int readTimeout, int writeTimeout);
//Pin
typedef int (*WINAPI pGWQ_ReadPin)(int iPortNo, char extendPort, int iBaudRate, int iPinMode, int iVoiceType, int iTimeOut, char* Pin, int iPinSize);
int  Finger()
{
	HINSTANCE hDll;
	HANDLE hwnd = 0;
	hDll = LoadLibrary("./FingerVeinDLL_ZHY_x64.dll");//把依赖dll放到系统目录，或者是依赖dll的路径加到环境变量，后重启
	printf("lastcode=%d\n", GetLastError());
	if (hDll == NULL) {
		printf("加载失败\n");
		return -40;
	}
	pinitDriver init = (pinitDriver)GetProcAddress(hDll, "initDriver");
	if (init == NULL)
	{
		printf("加载init 函数失败，errocode=%d\n", GetLastError());
		return -1;
	}
	int ret = init(NULL, NULL);
	printf("ret=%d\n", ret);
	//调用指静脉
	pReadImage read = (pReadImage)GetProcAddress(hDll, "ReadImage");
	if (read == NULL)
	{
		printf("加载 ReadImage 函数失败，errocode=%d\n", GetLastError());
		return -1;
	}
	char* resmsg = (char*)malloc(4 * 1024 * 1024);
	char* errmsg = (char*)malloc(256);
	ret = read(NULL, resmsg, errmsg, 20, 20);
	printf("errmsg=%s\n", errmsg);
}
int Pin()
{
	HINSTANCE hDll;
	HANDLE hwnd = 0;
	hDll = LoadLibrary("./CENT_GWQ.dll");//把依赖dll放到系统目录，或者是依赖dll的路径加到环境变量，后重启
	printf("lastcode=%d\n", GetLastError());
	if (hDll == NULL) {
		printf("加载失败\n");
		return -40;
	}
	pGWQ_ReadPin init = (pGWQ_ReadPin)GetProcAddress(hDll, "GWQ_ReadPin");
	if (init == NULL)
	{
		printf("加载init 函数失败，errocode=%d\n", GetLastError());
		return -1;
	}
	char pin[256] = { 0 };
	int ret = init(0, NULL, 9600, 1, 1, 20, pin, 256);
	printf("ret=%d,pin=%s\n", ret, pin);

	return 0;
}
int main()
{
	HINSTANCE hDll;
	HANDLE hwnd = 0;
	hDll = LoadLibrary("C:\\zhongziyi\\agree\\测试\\c++\\工程测试\\Ahook\\Release\\Ahook.dll");//把依赖dll放到系统目录，或者是依赖dll的路径加到环境变量，后重启
	printf("lastcode=%d\n", GetLastError());
	if (hDll == NULL) {
		printf("加载失败\n");
		return -40;
	}
	printf("load sucessfully\n");
	pSelectDev select= (pSelectDev)GetProcAddress(hDll, "SelectDev");
	if (select == NULL)
	{
		printf("f\n");
	}
	pSetHook set = (pSetHook)GetProcAddress(hDll, "SetHook");
	pUnHook unset = (pUnHook)GetProcAddress(hDll, "UnHook");
	////选择替换
	set();

	select("2B46", "bc01", "10.8.1.101","1-3.4.1");
	Pin();

	////解除替换
	unset();
	return 0;
}

