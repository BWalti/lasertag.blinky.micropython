# USB Bridge to access ESP32 from IDE

To get deployment working withing DevContainer, follow this guide to share Windows USB device with WSL 2 and then mount that device into dev container:

- https://4sysops.com/archives/usbipd-win-access-and-share-usb-devices-in-hyper-v-vms-and-wsl/
- and on windows in an administrative prompt, run: `usbipd wsl attach --busid 3-2`
- adapt bus ID according to: `usbipd wsl list`
