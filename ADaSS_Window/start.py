from ui import window
from device import gwq
from tools import filetools

if __name__ == '__main__':
    # window = window.AWindow()
    # window.mainloop()

    g1 =gwq.DeviceGWQ()
    # g1.GWQ_StartKeyboard()
    g1.AHook_GWQ_StartKeyboard()

