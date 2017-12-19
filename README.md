# radio_recoder
FM4U 녹음용 파이썬 스크립트

### Prerequisite
sudo apt install rtmpdump
sudo apt install ffmpeg

### Edit crontab
```sh
$ crontab -e
```
For example (새벽 0시부터 1800초, 새벽 1시부터 1800초)
```sh
0 0 * * * python3 ~/radio_recoder/radio_recoder.py --record_secs 1800 --output_dir ~/Dropbox/MBC_RADIO
0 1 * * * python3 ~/radio_recoder/radio_recoder.py --record_secs 1800 --output_dir ~/Dropbox/MBC_RADIO
```

### References
- http://younworld.tistory.com/entry/EBS-%EB%9D%BC%EB%94%94%EC%98%A4-%EC%9E%90%EB%8F%99-%EB%85%B9%EC%9D%8C
- https://wiki.changwoo.pe.kr/doku.php/project:unattendedradiorecorder
