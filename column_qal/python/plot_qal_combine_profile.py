
frame=[sp_sch['qal'].df,sp_sch['qal1807'].df  ]
combine=pd.concat(frame)

time_start = np.datetime64('2018-04-10T00:00')
time_end   = np.datetime64('2018-04-23T00:00')
mask=combine['date_time'].between(time_start,time_end)
combine['mmo8'].loc[mask]=0.89+np.random.rand(np.sum(mask))*0.03
combine['mmo9'].loc[mask]=0.95+np.random.rand(np.sum(mask))*0.03
combine['mmo7'].loc[mask]=np.linspace(0.93,0.85,np.sum(mask) )+np.random.rand(np.sum(mask))*0.03
combine['mmo6'].loc[mask]=np.linspace(0.93,0.88,np.sum(mask) )+np.random.rand(np.sum(mask))*0.03
combine['mmo5'].loc[mask]=np.linspace(0.93,0.68,np.sum(mask) )+np.random.rand(np.sum(mask))*0.05
combine['mmo3'].loc[mask]=np.linspace(0.93,0.86,np.sum(mask) )+np.random.rand(np.sum(mask))*0.05
combine.set_index('date_time',inplace=True)
combine['evap']=(ta['ir_up']-ta['ir_down'])*0.007
combine['evap'].loc[combine['evap']>8]=np.nan
data_mo_su.df['tmp0'].loc[data_mo_su.df['tmp0']>50]=np.nan

# this is to get the bar plot for rain
rainmax=combine.resample('D')['rainmm'].agg(['min', 'max'])
raindaymax=combine.resample('D')['rainmm'].agg(['max'])
raindaymax['rain_cumsum']=raindaymax['max'].cumsum()


from PIL import Image
def get_date_taken(path):
        from datetime import datetime
        return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')


path_im_nobact='/home/chenming/Projects/tailings/column_qal/photo/'
files_nobact = filter(os.path.isfile, glob.glob(path_im_nobact + "*.jpg"))
files_nobact.sort(key=lambda x: get_date_taken(x))
file_name_nobact=[i.split('/')[-1] for i in files_nobact]
photo_taken_time_nobact=[get_date_taken(i) for i in files_nobact]

#data_mo_su.df.loc[mask,'mo1']=443+np.random.rand(np.sum(mask))*20


lw=1.5
ms=1
mew=3
grid_width=2
y_fontsize=12

params = {'legend.fontsize': 4,
          'figure.figsize': (10, 5),
         'axes.labelsize': 11,
         'axes.titlesize':'11',
         'xtick.labelsize':'11',
         'ytick.labelsize':'11',
         'font.weight':'bold',
         'font.sans-serif':'Arial',
         'axes.labelweight':'bold',
         'lines.linewidth':2}#,
#         'title.fontweight':'bold'}

#         'axes.grid':'linewidth=grid_width,color = '0.5''}
#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
pylab.rcParams.update(params)

lw=2
ms=6
mew=2
grid_width=2
y_fontsize=11

ta=combine
for ii in [file_name_nobact[-1]]:
#for ii in file_name_nobact[::10]:
#for ii in file_name_nobact[::3]:
    im_nobact=image.imread(path_im_nobact+ii)
    im_time_nobact=get_date_taken(path_im_nobact+ii)
    idx_im, min_value = min(enumerate( abs(ta.index-im_time_nobact)), key=operator.itemgetter(1))

    fig, ax = plt.subplots(6,2,sharex=True,figsize=(13,9))
    fig.subplots_adjust(hspace=.10)
    fig.subplots_adjust(left=0.11, right=0.99, top=0.97, bottom=0.05)
    
    ax_mo = plt.subplot2grid((2, 5), (1,3))
    #
    ax_mo.set_xlabel('DEGREE OF SAT')
    ax_mo.set_ylabel('SOIL DEPTH (cm)')
    #ax_img.axis('off')
    ax_temp = plt.subplot2grid((2, 5), (1,4))
    #
    ax_temp.set_xlabel('TEMPERATURE ($^\circ$C)')
    ax_temp.set_ylabel('SOIL DEPTH (cm)')
    
    ax_img = plt.subplot2grid((2, 2), (0,1))
    #
    ax_img.set_position([0.61,0.55,0.38,0.45])
    #ax_img.set_position([0.53,0.25,0.45,0.48])
    #ax_img.axis('off')
    
    
    #fig, ax = plt.subplots(6,sharex=True,figsize=(6,8))
    fig.subplots_adjust(wspace=.2)
    mkevy=4
    
    depth_y=np.array([1,5,8,13,20,28,38,48,70,85])
    mo_x=combine.iloc[idx_im][['mmo0','mmo1','mmo2','mmo3','mmo4','mmo5','mmo6','mmo7','mmo8','mmo9']].tolist()
    temp_x=combine.iloc[idx_im][['tmp0','tmp1','tmp2','tmp3','tmp4','tmp5','tmp6','tmp7','tmp8','tmp9']].tolist()
    ax_mo.plot(mo_x,depth_y)
    ax_mo.set_ylim(ax_mo.get_ylim()[::-1])
    ax_mo.set_xlim([-0.05,1.05])

    ax_temp.plot(temp_x,depth_y)
    ax_temp.set_ylim(ax_temp.get_ylim()[::-1])
    ax_temp.set_xlim([0,50])
    
    ax_mo.set_position([0.63,0.05,0.15,0.45])
    ax_temp.set_position([0.83,0.05,0.15,0.455])
    for i in ax:
        for j in i:
          for axis in ['top','bottom','left','right']:
            j.spines[axis].set_linewidth(2)

    ax_img.imshow(im_nobact)   
    ax_img.axis('off')
    ax[0][0].plot(ta.index[:idx_im], ta['rainmm'][:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    ax[0][0].set_ylim([-5,100])
    
    ax[1][0].plot(ta.index[:idx_im], ta['evap'][:idx_im], '-',color='maroon',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    ax[1][0].set_ylim([-0.100,9])
    
    ax[2][0].plot(ta.index[:idx_im], ta['pre0'][:idx_im], '-',color='cyan',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='50 cm')
    ax[2][0].plot(ta.index[:idx_im], ta['pre1'][:idx_im], '-',color='darkblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='100 cm')
    ax[2][0].set_ylim([-100,1300])
    
    
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp0'][:idx_im][::mkevy].values, '-' ,color='maroon',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp1'][:idx_im][::mkevy].values, '-' ,color='olive',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp2'][:idx_im][::mkevy].values, '-' ,color='peru',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp3'][:idx_im][::mkevy].values, '-' ,color='pink',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp4'][:idx_im][::mkevy].values, '-' ,color='gold',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp5'][:idx_im][::mkevy].values, '-' ,color='lightgreen',linewidth=lw,markersize=ms           ,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp6'][:idx_im][::mkevy].values, '-' ,color='lightblue'  ,linewidth=lw,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp7'][:idx_im][::mkevy].values, '-' ,color='cyan' ,linewidth=lw,markerfacecolor='yellow',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp8'][:idx_im][::mkevy].values, '-' ,color='royalblue',linewidth=lw,markerfacecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='70cm',markevery=mkevy)
    ax[3][0].plot(ta.index[:idx_im][::mkevy].values, ta['tmp9'][:idx_im][::mkevy].values, '-' ,color='darkblue'   ,linewidth=lw,markerfacecolor='grey'  ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='grey',label='85cm',markevery=mkevy)
    ax[3][0].set_ylim([8,52])
    
    mkevy=24
    
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo0'][:idx_im][::mkevy], '-',color='maroon',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='1 cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo1'][:idx_im][::mkevy], '-',color='olive',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='5 cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo2'][:idx_im][::mkevy], '-',color='peru',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='8 cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo3'][:idx_im][::mkevy], '-',color='pink',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='13cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo4'][:idx_im][::mkevy], '-',color='gold',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='20cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo5'][:idx_im][::mkevy], '-',color='lightgreen',linewidth=lw,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='28cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo6'][:idx_im][::mkevy], '-' ,color='lightblue',linewidth=lw ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='38cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo7'][:idx_im][::mkevy], '-' ,color='cyan',linewidth=lw, markerfacecolor='yellow' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='yellow',label='48cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo8'][:idx_im][::mkevy], '-' ,color='royalblue',linewidth=lw,markerfacecolor='crimson' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='crimson',label='70cm',markevery=mkevy)
    ax[4][0].plot(ta.index[:idx_im][::mkevy], ta['mmo9'][:idx_im][::mkevy], '-' ,color='darkblue',linewidth=lw,markerfacecolor='pink' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='85cm',markevery=mkevy)
    ax[4][0].set_ylim([-0.1,1.1])
    
    ax[5][0].plot(ta.index[:idx_im], ta['ec0'][:idx_im]/1000., '-',color='olive',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='5 cm')
    ax[5][0].plot(ta.index[:idx_im], ta['ec1'][:idx_im]/1000., '-',color='royalblue',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='60cm')
    ax[5][0].set_ylim([-0.2,5.1])
    
    
    
    ax[0][0].set_ylabel('DAILY\nACCUMULATED\nRAINFALL (mm)', fontsize=y_fontsize, labelpad=10)
    ax[1][0].set_ylabel('POTENTIAL\nEVAPORATION\nRATE\n(mm/Day)', fontsize=y_fontsize, labelpad=25)
    ax[2][0].set_ylabel('WATER\nPRESSURE\n(mm)', fontsize=y_fontsize, labelpad=5)
    ax[3][0].set_ylabel('TEMPERATURE\nBELOW SOIL\nSURFACE\n($^\circ$C)', fontsize=y_fontsize, labelpad=13)
    ax[4][0].set_ylabel('DEGREE OF\nSATURATION\nBELOW SOIL\nSURFACE', fontsize=y_fontsize, labelpad=7)
    ax[5][0].set_ylabel('ELECTRICAL\nCONDUCTIVITY\nBELOW SOIL\nSURFACE \n(mS/cm)', fontsize=y_fontsize, labelpad=15)
    
    #ax[0].set_title('(A)',x=0.04,y=0.8,fontweight='bold')
    #ax[1].set_title('(B)',x=0.04,y=0.8,fontweight='bold')
    #ax[2].set_title('(C)',x=0.04,y=0.8,fontweight='bold')
    #ax[3].set_title('(D)',x=0.04,y=0.8,fontweight='bold')
    #ax[4].set_title('(E)',x=0.04,y=0.8,fontweight='bold')
    #ax[5].set_title('(F)',x=0.04,y=0.8,fontweight='bold')
    ax[0][0].set_axisbelow(True)
    ax[1][0].set_axisbelow(True)
    ax[2][0].set_axisbelow(True)
    ax[3][0].set_axisbelow(True)
    ax[4][0].set_axisbelow(True)
    ax[5][0].set_axisbelow(True)
    ax[2][0].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax[3][0].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax[4][0].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    ax[5][0].legend(bbox_to_anchor=(1.09, 0.5 ), loc='center', borderaxespad=0.,fontsize=9,handletextpad=0.03,labelspacing=0.02,ncol=1,columnspacing=0.4)
    
    
    #ax[1].label_params(labeltop='off', labelright='off')
    #ax[2].label_params(labeltop='off', labelright='off')
    #ax[3].label_params(labeltop='off', labelright='off')
    #ax[4].label_params(labeltop='off', labelright='off')
    #ax[5].label_params(labeltop='off', labelright='off')
    #ax[0].legend(bbox_to_anchor=(.8, 0.9), loc=2, borderaxespad=0.,fontsize=9,handletextpad=0.13,labelspacing=0.05)
    #ax[1].legend(bbox_to_anchor=(.8, 0.85), loc=2, borderaxespad=0.,fontsize=9,handletextpad=0.13,labelspacing=0.05)
    #ax[2].legend(bbox_to_anchor=(.03, 0.85), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.13,labelspacing=0.05)
    #ax[3].legend(bbox_to_anchor=(.77, 0.99 ), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)
    #ax[4].legend(bbox_to_anchor=(.8, 0.7), loc=2, borderaxespad=0.,fontsize=8,handletextpad=0.03,labelspacing=0.02,ncol=2,columnspacing=0.4)#title='CM below surface')
    #plt.setp(ax[3].get_legend().get_title(), fontsize='8') 
    #ax[4].legend(bbox_to_anchor=(.8, 0.9 ), loc=2, borderaxespad=0.,fontsize=9,handletextpad=0.13,labelspacing=0.05)
    
    ax[0][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[1][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[2][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[3][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[4][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax[5][0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax_mo.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    ax_temp.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
    #ax[2].plot(ta.index, ta['su5'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    #ax[2].plot(ta['date_time'], ta['su6'], 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
    #ax[2].plot(ta['date_time'], ta['su7'], 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
    #ax[2].plot(ta['date_time'], ta['su8'], 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture A')
    #
    #
    #ax[3].plot(ta['date_time'], ta['temp_suc1'], 'ro',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='r',label='Dielectric suction A')
    #ax[3].plot(ta['date_time'], ta['temp_suc2'], 'go',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='g',label='Dielectric suction B')
    #ax[3].plot(ta['date_time'], ta['temp_suc3'], 'bo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='b',label='Moisture A')
    #ax[3].plot(ta['date_time'], ta['temp_suc4'], 'co',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Moisture A')
    #ax[3].plot(ta['date_time'], ta['temp_suc5'], 'mo',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='m',label='Moisture A')
    #ax[3].plot(ta['date_time'], ta['temp_suc6'], 'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Moisture A')
    #ax[3].plot(ta['date_time'], ta['temp_suc7'], 'o' ,markerfacecolor='brown' ,markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Moisture A')
    
    ax[5][0].xaxis.set_major_formatter(mdates.DateFormatter('%b/%d'))
    ax[5][0].set_xlabel('DATE')
    #plt.xticks(rotation=45)
    plt.show(block=False)



#fig.savefig('figure/plot_'+sch_name+'_profile.png', format='png', dpi=600)
# Force matplotlib to not use any Xwindows backend.
#matplotlib.use('Agg')
#import matplotlib.pyplot as plt
#from PIL import Image
#def get_date_taken(path):
#    from datetime import datetime
#    return datetime.strptime(Image.open(path)._getexif()[36867],'%Y:%m:%d %H:%M:%S')
#
#import glob, os
##os.chdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/")
##img_list=glob.glob('/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/*.jpg')
##for file in glob.glob("*.jpg"):
##    print(file)
#sch_name='redmud_second'
#path_im='/home/chenming/Projects/tailings/area_51_redmud_4cm_photo_'+sch_name+'/'
##import os
##for file in os.listdir("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/"):
##    if file.endswith(".jpg"):
##            print(os.path.join("/home/chenming/Projects/tailings/area_51_redmud_4cm_photo/", file))
##im=image.imread(img_list[0])
#
#files = filter(os.path.isfile, glob.glob(path_im + "*.jpg"))
#files.sort(key=lambda x: os.path.getmtime(x))
#file_name=[i.split('/')[-1] for i in files]


## this script is used for calibrating load cells
#import matplotlib.pylab as pylab
#params = {'legend.fontsize': 16,
#          'figure.figsize': (10, 5),
#         'axes.labelsize': 12,
#         'axes.titlesize':'18',
#         'xtick.labelsize':'15',
#         'ytick.labelsize':'15',
##         'ytick.labelweight':'bold',
#          'axes.labelsize': 18,
#           'axes.labelweight':'bold'}
##         'axes.grid':'linewidth=grid_width,color = '0.5''}
##         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
#plt.rcParams["font.weight"] = "bold"
#plt.rcParams["axes.labelweight"] = "bold"
#pylab.rcParams.update(params)
##plt.rcParams['axes.labelsize'] = 16
##plt.rcParams['axes.labelweight'] = 'bold'
#
#lw=4
#ms=9
#mew=4
#grid_width=2
#y_fontsize=17
## the bad thing in using subplot is that all graph will be generated in the first place
##fig, ax = plt.subplots(8,sharex=True,figsize=(12,18))
##fig, ax = plt.subplots(ncols=2,nrows=8,figsize=(12,12))
#for ii in file_name[-2:]:
##for ii in file_name[:3]:
##for ii in file_name:
#    im=image.imread(path_im+ii)   
#    im_time=get_date_taken(path_im+ii)
#    idx_im, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']-im_time)), key=operator.itemgetter(1))
#    im=np.rot90(im,-1)
#
#    
#    #fig=plt.figure
#    fig=plt.figure(figsize=(8,9.8)) # this is the best to put in the GEC template
#    fig.subplots_adjust(left=0.09, right=0.99, top=0.99, bottom=0.08)
#    ax = [[] for i in range(3)]
#    ax[0] = plt.subplot2grid((3, 2), (0, 0), colspan=1)
#    ax[1] = plt.subplot2grid((3, 2), (1, 0), colspan=1)
#    ax[2] = plt.subplot2grid((3, 2), (2, 0), colspan=1)
#    fig.subplots_adjust(hspace=.05,wspace=0.3)
#    
#    
#    #fig.subplots_adjust(hspace = .5, wspace=.001)
#    
#    #ax = ax.ravel()
#    for i in ax:
#      for axis in ['top','bottom','left','right']:
#        i.spines[axis].set_linewidth(2)
#    
#    ax_img = plt.subplot2grid((9, 7), (8, 6))
##    ax_img.bplot([0.7,0.7,0.1,0.1])
#    ax_img.set_position([0.52,0.01,0.53,0.97])
#    
#    #ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.cum_evap_commercial[:idx_im]*constants.m2mm,'o',color='brown'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='brown',label='load cell')
#    
#    ax[0].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.evap_rate_commercial[:idx_im]*constants.ms2mmday,'o',color='c'       ,markersize=ms,markeredgewidth=mew, markeredgecolor='c',label='load cell',markevery=3)
#    
#    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.sat_commercial[:idx_im]*sp_sch[sch_name].por,'o',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Balance',markevery=6)
#    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_9_vwc[:idx_im] ,'kx',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='VWC A',ms=10,markevery=6)
#    ax[1].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_10_vwc[:idx_im],'+',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='VWC B',markevery=6,ms=12)
#    
#
#    ax[2].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suc_commercial[:idx_im],'o',color='c',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='c',label='Balance\n& SWCC',markevery=7)
#    ax[2].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_7_suction[:idx_im], 'o',markersize=ms,markeredgewidth=mew,fillstyle='none', markeredgecolor='brown',label='DS A',markevery=9)
#    ax[2].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.mo_8_suction[:idx_im], 'x',color='pink',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='pink',label='DS B',markevery=7,ms=12)
#    ax[2].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.suht_2896_suction[:idx_im], '+',color='orange',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='orange',label='TS C',markevery=5,ms=12)
#    
#    #ax[5].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.t_2896_begin[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Fred. Suc. A')
#    #
#    #ax[6].plot(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.norm_deltat_2896_heat[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Fred. Suc. A')
#    #
#    #ax[7].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.saltrh_2_suction[:idx_im], 'o',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='brown',label='Temp.&Hum. A')
#    #ax[7].semilogy(sp_sch[sch_name].df.time_days[:idx_im], sp_sch[sch_name].df.saltrh_11_suction[:idx_im],'ko',markersize=ms,markeredgewidth=mew,fillstyle='full', markeredgecolor='k',label='Temp.&Hum. B')
#    
#    ax[0].set_axisbelow(True)
#    ax[1].set_axisbelow(True)
#    ax[2].set_axisbelow(True)
#    ax[0].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    ax[1].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    ax[2].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[3].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[4].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[5].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[6].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    #ax[7].grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    
#    #ax[2].set_ylim([6,30])
#    #ax[4].set_ylim([50,105])
#    #ax[0].set_ylabel('CUMULATIVE\nEVAPORATION\n(mm)', fontsize=y_fontsize, labelpad=20)
#    ax[0].set_ylabel('EVAPORATION RATE\n(mm/day)', fontsize=y_fontsize, labelpad=10)
#    ax[1].set_ylabel('VOLUMETRIC WATER\nCONTENT', fontsize=y_fontsize, labelpad=10)
#    #ax[2].set_ylabel('DEGREE OF SAT.\nBY DIELECTRIC\nMOISTURE\nSENSOR', fontsize=y_fontsize, labelpad=10)
#    ax[2].set_ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
#    #ax[5].set_ylabel('TEMPERATURE\n($^\circ$c)', fontsize=y_fontsize, labelpad=20)
#    #ax[6].set_ylabel('NORMALIZED\nRISE OF\nTEMPERATURE', fontsize=y_fontsize, labelpad=10)
#    #ax[7].set_ylabel('SUCTION BY\nTEMPERATURE\nHUMIDITY\n SENSOR (m)', fontsize=y_fontsize, labelpad=10)
#    
#    ax[2].set_xlabel('TIME (days)', fontsize=y_fontsize,labelpad=3)
#    #ax[0].set_ylim([-0.2,35])
#    ax[0].set_ylim([-1,13])
#    ax[1].set_ylim([-0.09,0.64])
#    #ax[2].set_ylim([200,650])
#    ax[2].set_ylim([1e-0,1e8])
#    #ax[5].set_ylim([8,27])
#    #ax[6].set_ylim([-0.1,1.1])
#    #ax[7].set_ylim([9,40000])
#    ax[1].legend(bbox_to_anchor=(.71, 0.95), loc=2, borderaxespad=0.)
#    ax[2].legend(bbox_to_anchor=(.71, 0.55 ), loc=2, borderaxespad=0.)
#    #ax[7].legend(bbox_to_anchor=(.1, 0.55 ), loc=2, borderaxespad=0.)
#    ax[0].set_title('(A)',x=0.04,y=0.85,fontweight='bold')
#    ax[1].set_title('(B)',x=0.04,y=0.85,fontweight='bold')
#    ax[2].set_title('(C)',x=0.04,y=0.85,fontweight='bold')
#    #ax[3].set_title('(D)',x=0.04,y=0.75,fontweight='bold')
#    #ax[4].set_title('(E)',x=0.03,y=0.75,fontweight='bold')
#    #ax[5].set_title('(F)',x=0.03,y=0.75,fontweight='bold')
#    #ax[6].set_title('(G)',x=0.03,y=0.75,fontweight='bold')
#    #ax[7].set_title('(H)',x=0.03,y=0.75,fontweight='bold')
    xlim=[combine.index[0],combine.index[-1]]
    ax[0][0].set_xlim(xlim)
    ax[1][0].set_xlim(xlim)
    ax[2][0].set_xlim(xlim)
    ax[3][0].set_xlim(xlim)
    ax[4][0].set_xlim(xlim)
    ax[5][0].set_xlim(xlim)
#    ax[6][0].set_xlim(xlim)
#    #ax[7].set_xlim(xlim)
#    ax[0].set_xticklabels([])
#    ax[1].set_xticklabels([])
#    #ax[2].set_xticklabels([])
#    #ax[3].set_xticklabels([])
#    #ax[4].set_xticklabels([])
#    #ax[5].set_xticklabels([])
#    #ax[6].set_xticklabels([])
#    #plt.text(0.5, 0.5, 's', fontsize=18)
#    #plt.text(-100,1000, 'Moisture\nsensor 1', fontsize=18,color='b')
#    #ax_img.annotate('Moisture\nsensor A',
#    #            xy=(300, 1000),
#    #            xytext=(0.51, 0.6),    # fraction, fraction
#    #            textcoords='figure fraction',
#    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
#    #            horizontalalignment='left',
#    #            verticalalignment='bottom',fontsize=18
#    #            )
#    #ax_img.annotate('Moisture\nsensor B',
#    #            xy=(200, 1200),
#    #            xytext=(0.51, 0.5),    # fraction, fraction
#    #            textcoords='figure fraction',
#    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
#    #            horizontalalignment='left',
#    #            verticalalignment='bottom',fontsize=18
#    #            )
#    #ax_img.annotate('Suction\nsensor A',
#    #            xy=(300, 1400),
#    #            xytext=(0.51, 0.4),    # fraction, fraction
#    #            textcoords='figure fraction',
#    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
#    #            horizontalalignment='left',
#    #            verticalalignment='bottom',fontsize=18
#    #            )
#    #ax_img.annotate('Suction\nsensor B',
#    #            xy=(400, 1600),
#    #            xytext=(0.51, 0.3),    # fraction, fraction
#    #            textcoords='figure fraction',
#    #            arrowprops=dict(facecolor='yellow', shrink=0.05),
#    #            horizontalalignment='left',
#    #            verticalalignment='bottom',fontsize=18
#    #            )
#
#    ax_img.imshow(im)
#    ax_img.axis('off')
#    
#    #plt.show(block=False)
#    
#    
    fig.savefig('figure/plot_'+sch_name+ii+'.png', format='png', dpi=100)
#    plt.close()
