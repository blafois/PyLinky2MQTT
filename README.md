# PyLinky2MQTT

## Tips

As I have multiple serial-TTL adapters connected to the same host, and to identify then easily (instead of ttyS0, ttyS1...), I use custom udev rules.

In `/etc/udev/rules.d`, create a custom rule file:

```
# LINKY
ACTION=="add", ATTRS{idVendor}=="0403", ATTRS{idProduct}=="6015", SYMLINK+="LINKY"
```

## Install as a systemd service

Copy `linky.service` fie to `/lib/systemd/system/linky.service`.

Then type `systemctl enable linky`

