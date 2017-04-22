# radio_recoder
FM4U 녹음용 파이썬 스크립트

### Edit crontab
```sh
$ crontab -e
```
For example (새벽 3시부터 3800초)
```sh
0 3 * * * python3 /home/jae/extern/Projects/radio_recoder/radio_recoder.py --record_secs 3800 --output_dir /home/jae/Dropbox/MBC_RADIO
```

### References
- http://younworld.tistory.com/entry/EBS-%EB%9D%BC%EB%94%94%EC%98%A4-%EC%9E%90%EB%8F%99-%EB%85%B9%EC%9D%8C
- https://wiki.changwoo.pe.kr/doku.php/project:unattendedradiorecorder
