# PlexNewTranscoder-nvenc

## Features
Since the public available sources of the plex transcoder are based on ffmpeg 2.5 the Nvidia encoder 'nvenc' can be included.<br>This means that you can use you descrete graphics card instead your cpu for transcoding jobs.

## Notes
 * This was made in ArchLinux you most probably have to change any paths depending on your distro
 * This is Linux only
 * Make sure you have the nvidia-sdk and cuda installed
 * The wrapper needs to be reinstalled after every plex update

## Installation

### ArchLinux
 1. Clone the repository and change into the ArchLinux directory
 2. Run makepkg
 3. Install builded package
 4. Rename 'Plex Transcoder' in '/opt/plexmediaserver/Ressources/' to something else
 5. Copy the wrapper as 'Plex Transcoder' into '/opt/plexmediaserver/Ressources/'
 6. Run 'chmod +x /opt/plexmediaserver/Ressources/Plex\ Transcoder'
 7. Congratulations you'r done.

### Other
 1. Clone the repository and make sure you have the nvidia-sdk and cuda installed
 2. Untar the PlexNewTranscoder with 'tar xfv PlexNewTranscoder.tar.bz2 --bzip2'
 3. Change directory into ffmpeg-snapshot
 4. Patch ffmpeg with 'patch -p1 < ../plex_nvenc.patch'
 5. Configure for your needs (example in ArchLinux/PKGBUILD)
 6. Run 'make'
 7. Find your "Plex Transcoder" binary of you Plex Media Center installation and replace it with the provided wrapper
 8. Chmod +x your Plex Transcoder wrapper
 9. Congratulations you'r done
