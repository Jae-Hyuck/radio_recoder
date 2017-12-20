import json
from urllib.request import urlopen
import subprocess
import datetime
import argparse
import os
import os.path as osp


def recording(FLAGS):

    rtmp_addr = json.loads(
        urlopen('http://miniplay.imbc.com/WebLiveURL.ashx?channel=mfm&agent=&protocol=RTMP')
        .read().decode('utf-8')[1:-2])['AACLiveURL']

    os.makedirs(FLAGS.output_dir, exist_ok=True)
    start_time = datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    flv_file = osp.join('/tmp', 'FM4U_' + start_time + '.flv')
    aac_file = osp.join(FLAGS.output_dir, 'FM4U_' + start_time + '.aac')

    rtmpdump = ['rtmpdump', '-r', rtmp_addr, '-B', str(FLAGS.record_secs), '-o', flv_file]
    ffmpeg = ['ffmpeg', '-i', flv_file, '-vn', '-acodec', 'copy', aac_file]
    rm = ['rm', flv_file]

    p = subprocess.Popen(rtmpdump)
    p.wait()
    p = subprocess.Popen(ffmpeg)
    p.wait()
    p = subprocess.Popen(rm)
    p.wait()
    if FLAGS.dropbox_uploader:
        dropbox = [osp.expanduser(FLAGS.dropbox_uploader), 'upload', aac_file, '/']
        p = subprocess.Popen(dropbox)
        p.wait()


if __name__ == "__main__":
    ############
    # Argparse #
    ############
    parser = argparse.ArgumentParser()

    # required arguments
    parser.add_argument('--record_secs', type=int, required=True)
    parser.add_argument('--output_dir', type=str, required=True)
    parser.add_argument('--dropbox_uploader', type=str, default=None)

    FLAGS = parser.parse_args()

    recording(FLAGS)
