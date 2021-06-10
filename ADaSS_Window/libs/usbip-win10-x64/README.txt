			USBIP win10x64使用说明
1、安装测试证书
./usbip_test.pfx (password: usbip)
安装两次，分别选择：
	"Trusted Root Certification Authority" in "Local Computer"
	"Trusted Publishers" in "Local Computer"

2、开始测试模式
bcdedit -set TESTSIGNING OFF
重启

3、安装驱动
usbip.exe uninstall
usbip.exe install -w

4、使用
usbip.exe list -r 10.8.1.101 -l
usbip.exe attach -r 10.8.1.101 -b 1-3.7 



