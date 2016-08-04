#!/usr/bin/python2
import subprocess
import sys
import re

def transcode_local(args):
    proc = subprocess.Popen(args)
    proc.wait()
    return proc.returncode

def parseParams(arguments):

    if "libx264" in arguments:
        removeParams = ['-crf', '-x264opts']
        replaceParams = [['libx264','nvenc'],['yuv420p','nv12'],['veryfast','default']]
    else:
        removeParams = []
        replaceParams = []

    newArgs = []
    nextArgJump=0
    for arg in arguments:
        if requireRemoveParam(arg,removeParams)==1:
            nextArgJump=1
        elif nextArgJump==0:
            newArgs.append(arg)
        else:
            nextArgJump=0

    newArgsModified = []
    for arg in newArgs:
        nextReplaceParamPosible = requireModifyParam(arg,replaceParams)
        if nextReplaceParamPosible is not None:
            newArgsModified.append(nextReplaceParamPosible)
            if nextReplaceParamPosible == "copy":
                #Internet explorer segment_format mpegts require mp4toannexb to work
                if "-segment_format" in arguments:
                    pos = arguments.index("-segment_format")
                    if arguments[pos+1] == "mpegts"  and "h264_mp4toannexb,h264_plex" not in arguments:
                        newArgsModified.append('-bsf:0')
                        newArgsModified.append('h264_mp4toannexb,h264_plex')

        else:
            newArgsModified.append(arg)
            
    if "aac" in newArgsModified:
        newArgsModified.insert(newArgsModified.index("aac")+1,'-strict')
        newArgsModified.insert(newArgsModified.index("aac")+2,'-2')
    
    if "nvenc" in newArgsModified:
        newArgsModified.insert(newArgsModified.index("nvenc")+1,'-profile:v')
        newArgsModified.insert(newArgsModified.index("nvenc")+2,'baseline')
        newArgsModified.insert(newArgsModified.index("nvenc")+3,'-tier:v')
        newArgsModified.insert(newArgsModified.index("nvenc")+4,'main')
        
    return newArgsModified

def requireRemoveParam(param,removableParams):
    for removableParam in removableParams:
        if removableParam[0] == '*':
            return param == removableParam.replace(removableParam[:1], '')
        elif param.find(removableParam) > -1:
            return 1
    return 0

def requireModifyParam(param,modifyParams):
    for modifyParam in modifyParams:
        if param.find(modifyParam[0]) > -1:
            return modifyParam[1]
    return None

try:
    #args = parseParams(["/opt/plexmediaserver/Resources/PT.orig"] + sys.argv[1:])
    args = parseParams(["/usr/bin/ffmpeg"] + sys.argv[1:])

    transcodeType="local"
    returnCode = 0

    returnCode = transcode_local(args)

    sys.exit(returnCode)
except Exception, e:
    print(e)
