import cv2
import sys
import os
import glob
# list of all classes
def gen_frame(path): 
    classes=('basketball','diving','horse_riding','soccer_juggling','swing','trampoline_jumping','walking','biking',
             'golf_swing','tennis_swing','volleyball_spiking');
    # get the parent directory where this program is stored
    dir=path
    print dir
    # concatenate the path to videos' folder
    save=os.path.join(dir,"frames")
    dir=os.path.join(dir,"frames")
    if not os.path.exists(save):
         os.mkdir(save)
    for category in classes:
    # category='basketball'
        rootdir=os.path.join(dir,category)
        print rootdir
         
        #     print subFolders,files
        print "Name of video file"
        for dirpath,dirname,files in os.walk(rootdir):
            # print "dirname",type(dirpath)
            x=dirpath.rfind("/")
            print dirpath[x+1:],dirpath
            print "files",files
            # if not os.path.exists(os.path.join(save,dirpath[x+1:],dirpath)):
            #     os.mkdir(os.path.join(save,dirpath[x+1:],dirpath))
            files=glob.glob(dirpath+"/*.mpg")
            print files
            if files:
                print 'h'
                for video_dir in files:
        #           capturing the location of video
                    print "dirpath",dirpath,"video",video_dir
                    # video_dir=os.path.join(dirpath,vid)
                    # print video_dir
                    x=video_dir.rfind(".")
                    new=video_dir[:x]   
                    if not os.path.isdir(new):
                        os.mkdir(new)

                    video = cv2.VideoCapture(video_dir)
                    if video.grab():
                        print "generating frames"
                        i=0
                        ret=True
                        while(ret):
                            try:
                                ret,frame=video.read()
                                if ret:
                                    pic=new+"/"+str(i)+".bmp"
                                    # print pic
                                    cv2.imwrite(pic,frame)
                                    i+=1
                            except (IOError,RuntimeError, TypeError, NameError):
                                print "skipping"
                    os.remove(video_dir)
                    # print i
                    # making frames of a video
    #             if video.grab()

if __name__=="__main__":
    # edit this path where the video is present
    gen_frame("/home/bashir/major_pro/dataset/store")
