def animate(line1, line2, timeStep=0.01,filename='animasi', folder='images') :
    # line1 & 2 -> x,y,name
    
    def save_frame(lineOne, lineTwo,limx, limy, number, absolutePath,time_Step=0.01, picturename='frame', extension='png'):
        #print(len(lineOne[0]),len(lineOne[1]),lineOne[-1])
        #print(len(lineTwo[0]),len(lineTwo[1]),lineTwo[-1])
        fig = plt.figure()
        ax =  plt.subplot(111)
        ax.plot(lineOne[0], lineOne[1], color="green", label=lineOne[-1])
        ax.plot(lineTwo[0], lineTwo[1], color="orange", label=lineTwo[-1])
        ax.plot([0],[0], color="blue", label='time : {0:.2f}s'.format(number * time_Step))
        
        #print(max_x, max_y)
        plt.xlim(limx[0]-3,limx[-1]+3)
        plt.ylim(limy[0],limy[-1]+8)
        plt.xlabel('X', fontsize=18)
        plt.ylabel('Y', fontsize=16)
        ax.legend(loc="upper left")
        #plt.show()
        file_name = '{0}_{1}.{2}'.format(picturename, number, extension)
        abs_filepath = absolutePath + '\\' + file_name
        fig.savefig(abs_filepath)
        #x = input('Press Enter .. .')
        #fig.close()
        plt.close('all')
        
        return abs_filepath
    
    
    ##############
    absPath = os.getcwd()+'\\'+folder
    if not os.path.exists(absPath) :
        try :
            os.mkdir(absPath)
        except TypeError :
            print('Already Exist')
    
    
    
    limx = [min([min(line1[0]), min(line2[0])]), max([max(line1[0]), max(line2[0])])]   
    limy = [min([min(line1[1]), min(line2[1])]), max([max(line1[1]), max(line2[1])])]
    #print (limx, limy)
    total_frame = len(line1[1])
    #x = input('Press Enter .. .')
    #print(total_frame)
    frame_list = []
    
    for num in range(1, total_frame) :
        if num > len(line1[1]) :
            lim_lineOne = len(line1[1])
        else :
            lim_lineOne = num
                                         
        if num > len(line2[1]) :
            lim_lineTwo = len(line2[1])
        else :
            lim_lineTwo = num                                                     
        frame_list.append(save_frame([line1[0][:lim_lineOne], line1[1][:lim_lineOne], line1[-1]],
                                     [line2[0][:lim_lineTwo], line2[1][:lim_lineTwo], line2[-1]],
                                     limx, limy,
                                     num-1, absPath
                                    ))
        #print('{} of {} done '.format(num+1, total_frame ))
        
        
    ## ulangi frame terakhir 50x
    for i in range(0,50):
        frame_list.append(frame_list[-1])
    
    
    ### part to animate using cv2
    # https://stackoverflow.com/questions/44947505/how-to-make-a-movie-out-of-images-in-python
    video_name = filename+'.mp4'

    frame = cv2.imread(frame_list[0])
    height, width, layers = frame.shape

    video = cv2.VideoWriter(video_name, 0, 100, (width,height))

    for image in frame_list:
        video.write(cv2.imread(image))

    cv2.destroyAllWindows()
    video.release()
    
    
    
    
    ####
    
    #x = input('Press Enter to delete temp file ...')
    for pat in frame_list :
        if os.path.isfile(pat) :
            os.remove(pat)       
    os.rmdir(absPath)
    
    print('Done file : {}'.format(video_name))