Since the public available sources of the plex transcoder are based on ffmpeg 2.5 the nvidia encoder nvenc can be included.

Installation:
0. Clone the repository and make sure you have the nvidia-sdk and cuda installed
1. tar xfv PlexNewTranscoder.tar.bz2 --bzip2
2. cd ffmpeg-snapshot
3. patch -p1 < ../plex_nvenc.patch
4. configure for your needs (example in ArchLinux/PKGBUILD), don't forget to enable nvenc and to include relevant headers
5. make
6. find your "Plex Transcoder" binary of you Plex Media Center installation and replace it with the provided wrapper
   e.g. (ArchLinux):
    rm /opt/plexmediaserver/Ressources/Plex\ Transcoder
    cp ./PlexTranscoderWrapper.py /opt/plexmediaserver/Ressources/Plex\ Transcoder
    chmod +x /opt/plexmediaserver/Ressources/Plex\ Transcoder
7. You are done.
