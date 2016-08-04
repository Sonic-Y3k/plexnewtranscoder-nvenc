Since the public available sources of the plex transcoder are based on ffmpeg 2.5 the nvidia encoder nvenc can be included.<br />

Installation:<br />
0. Clone the repository and make sure you have the nvidia-sdk and cuda installed<br />
1. tar xfv PlexNewTranscoder.tar.bz2 --bzip2<br />
2. cd ffmpeg-snapshot<br />
3. patch -p1 < ../plex_nvenc.patch<br />
4. configure for your needs (example in ArchLinux/PKGBUILD), don't forget to enable nvenc and to include relevant headers<br />
5. make<br />
6. find your "Plex Transcoder" binary of you Plex Media Center installation and replace it with the provided wrapper<br />
   e.g. (ArchLinux):<br />
    rm /opt/plexmediaserver/Ressources/Plex\ Transcoder<br />
    cp ./PlexTranscoderWrapper.py /opt/plexmediaserver/Ressources/Plex\ Transcoder<br />
    chmod +x /opt/plexmediaserver/Ressources/Plex\ Transcoder<br />
7. You are done.<br />
