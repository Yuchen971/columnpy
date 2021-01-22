import operator
import sensorfun
py_compile.compile(os.environ['pyduino']+'/python/post_processing/sensorfun.py')
import sensorfun
reload(sensorfun)
py_compile.compile(os.environ['pyduino']+'/python/post_processing/figlib.py')
import figlib
reload(figlib)
lw=5
ms=8
mew=3
grid_width=2
y_fontsize=20


sp_sch={}
plot_interpolate=False
for line in open("schedule.ipt"):
    li=line.strip()
    if not li.startswith("#"):
        line_content=[x.strip() for x in li.split(',')]
        sch_name=line_content[2]
        sp_sch[sch_name]=pandas_scale.concat_data_roof(pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M'),
            pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M'),dt_s );
        sp_sch[sch_name].start_dt=pd.datetime.strptime(line_content[0],'%Y/%b/%d %H:%M')
        sp_sch[sch_name].end_dt=pd.datetime.strptime(line_content[1],'%Y/%b/%d %H:%M')

        sp_sch[sch_name].water_level   =float(line_content[3])
        sp_sch[sch_name].surface_area  =float(line_content[4])
        sp_sch[sch_name].soil_thickness=float(line_content[5])
        sp_sch[sch_name].por=float(line_content[6])
        sp_sch[sch_name].ub=float(line_content[7])
        sp_sch[sch_name].lb=float(line_content[8])

        sp_sch[sch_name].time_surface_emerge = pd.datetime.strptime(line_content[10],'%Y/%b/%d %H:%M')

        sp_sch[sch_name].merge_data(df=data.df, keys=['deltat_c_1']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['deltat_c_2']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['deltat_c_3']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['scale1']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['scale2']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['scale3']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['starttemp_c_1']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['starttemp_c_2']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['starttemp_c_3']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['vw_1']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['vw_2']   ,plot=plot_interpolate  ,coef=5e-10)
        sp_sch[sch_name].merge_data(df=data.df, keys=['vw_3']   ,plot=plot_interpolate  ,coef=5e-10)

        sp_sch[sch_name].df['cum_evap_scale1']=(sp_sch[sch_name].df['scale1'][0]-sp_sch[sch_name].df['scale1']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water
        sp_sch[sch_name].df['evap_rate_scale1']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_scale1'] ),np.nan)/dt_s
        
        sp_sch[sch_name].df['cum_evap_scale2']=(sp_sch[sch_name].df['scale2'][0]-sp_sch[sch_name].df['scale2']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water
        sp_sch[sch_name].df['evap_rate_scale2']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_scale2'] ),np.nan)/dt_s
        
        sp_sch[sch_name].df['cum_evap_scale3']=(sp_sch[sch_name].df['scale3'][0]-sp_sch[sch_name].df['scale3']
            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water
        sp_sch[sch_name].df['evap_rate_scale3']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_scale3'] ),np.nan)/dt_s

        sp_sch[sch_name].df['sat_scale1']=-((
            sp_sch[sch_name].df['cum_evap_scale1']-sp_sch[sch_name].df['cum_evap_scale1'].iloc[-1])
            )/sp_sch[sch_name].df['cum_evap_scale1'].iloc[-1]
        sp_sch[sch_name].df['sat_scale2']=-((
            sp_sch[sch_name].df['cum_evap_scale2']-sp_sch[sch_name].df['cum_evap_scale2'].iloc[-1])
            )/sp_sch[sch_name].df['cum_evap_scale2'].iloc[-1]
        sp_sch[sch_name].df['sat_scale3']=-((
            sp_sch[sch_name].df['cum_evap_scale3']-sp_sch[sch_name].df['cum_evap_scale3'].iloc[-1])
            )/sp_sch[sch_name].df['cum_evap_scale3'].iloc[-1]
        sp_sch[sch_name].df['suc_scale1']=constants.swcc_reverse_fredlund_xing_1994(vwc=sp_sch[sch_name].df.sat_scale1*sp_sch[sch_name].por,por=0.5,
            nf=0.9311,mf=0.1229,hr=238968.16,af=2.7090,psi_0=1e-0)
        sp_sch[sch_name].df['suc_scale2']=constants.swcc_reverse_fredlund_xing_1994(vwc=sp_sch[sch_name].df.sat_scale2*sp_sch[sch_name].por,por=0.5,
            nf=0.9311,mf=0.1229,hr=238968.16,af=2.7090,psi_0=1e-0)
        sp_sch[sch_name].df['suc_scale3']=constants.swcc_reverse_fredlund_xing_1994(vwc=sp_sch[sch_name].df.sat_scale3*sp_sch[sch_name].por,por=0.5,
            nf=0.9311,mf=0.1229,hr=238968.16,af=2.7090,psi_0=1e-0)
        sp_sch[sch_name].df['norm_t_1']= (sp_sch[sch_name].df['deltat_c_1']- sp_sch[sch_name].lb)/(sp_sch[sch_name].ub-sp_sch[sch_name].lb)
        sp_sch[sch_name].df['norm_t_2']= (sp_sch[sch_name].df['deltat_c_2']- sp_sch[sch_name].lb)/(sp_sch[sch_name].ub-sp_sch[sch_name].lb)
        sp_sch[sch_name].df['norm_t_3']= (sp_sch[sch_name].df['deltat_c_3']- sp_sch[sch_name].lb)/(sp_sch[sch_name].ub-sp_sch[sch_name].lb)
        #sp_sch[sch_name].df['suc_scale1']=np.log(


#sp_sch[sch_name].df.plot(x='time_days',y='cum_evap_scale1')
#sp_sch[sch_name].df.plot(x='time_days',y='evap_rate_scale1')
#
#sp_sch[sch_name].df.plot(x='time_days',y='cum_evap_scale2')
#sp_sch[sch_name].df.plot(x='time_days',y='evap_rate_scale1')
#
#
#
#sp_sch[sch_name].df.plot(x='time_days',y='cum_evap_scale3')
#
#        
#        sp_sch[sch_name].df['saltrh_2_suction']=-np.log(0.01*sp_sch[sch_name].df['saltrh_2_rh'])*constants.R*(constants.kelvin+sp_sch[sch_name].df['saltrh_2_t']
#           )/constants.g/constants.molecular_weight_water     
#        sp_sch[sch_name].df['saltrh_11_suction']=-np.log(0.01*sp_sch[sch_name].df['saltrh_11_rh'])*constants.R*(constants.kelvin+sp_sch[sch_name].df['saltrh_11_t']
#           )/constants.g/constants.molecular_weight_water     
#
#        sp_sch[sch_name].df['deltat_2896_heat']=sp_sch[sch_name].df['t_2896_peak']-sp_sch[sch_name].df['t_2896_begin']
#        sp_sch[sch_name].df['deltat_2896_cool']=sp_sch[sch_name].df['t_2896_peak']-sp_sch[sch_name].df['t_2896_end']
#        sp_sch[sch_name].df['deltat_19_heat']  =sp_sch[sch_name].df['t_19_peak']  -sp_sch[sch_name].df['t_19_begin']
#        sp_sch[sch_name].df['deltat_19_cool']  =sp_sch[sch_name].df['t_19_peak']  -sp_sch[sch_name].df['t_19_end']
#        sp_sch[sch_name].df['deltat_14_heat']  =sp_sch[sch_name].df['t_14_peak']  -sp_sch[sch_name].df['t_14_begin']
#        sp_sch[sch_name].df['deltat_14_cool']  =sp_sch[sch_name].df['t_14_peak']  -sp_sch[sch_name].df['t_14_end']
#        deltat_2896_low_2_high=sorted(sp_sch[sch_name].df['deltat_2896_heat'], key=float)
#        sp_sch[sch_name].min_deltat_2896=np.average(deltat_2896_low_2_high[:30])
#        sp_sch[sch_name].max_deltat_2896=np.average(deltat_2896_low_2_high[-30:])
#
#        deltat_19_low_2_high=sorted(sp_sch[sch_name].df['deltat_19_heat'], key=float)
#        sp_sch[sch_name].min_deltat_19=np.average(deltat_19_low_2_high[:10])
#        sp_sch[sch_name].max_deltat_19=np.average(deltat_19_low_2_high[-10:])
#
#        deltat_14_low_2_high=sorted(sp_sch[sch_name].df['deltat_14_heat'], key=float)
#        sp_sch[sch_name].min_deltat_14=np.average(deltat_14_low_2_high[:10])
#        sp_sch[sch_name].max_deltat_14=np.average(deltat_14_low_2_high[-10:])
#        
#        sp_sch[sch_name].df['norm_delta_t_2896_heat']=(sp_sch[sch_name].max_deltat_2896- sp_sch[sch_name].df['deltat_2896_heat'])/(
#            sp_sch[sch_name].max_deltat_2896-sp_sch[sch_name].min_deltat_2896)
#        sp_sch[sch_name].df['norm_delta_t_19_heat']=(sp_sch[sch_name].max_deltat_19- sp_sch[sch_name].df['deltat_19_heat'])/(
#            sp_sch[sch_name].max_deltat_19-sp_sch[sch_name].min_deltat_19)
#        sp_sch[sch_name].df['norm_delta_t_14_heat']=(sp_sch[sch_name].max_deltat_14- sp_sch[sch_name].df['deltat_14_heat'])/(
#            sp_sch[sch_name].max_deltat_14-sp_sch[sch_name].min_deltat_14)
#
#        sp_sch[sch_name].water_level   =float(line_content[3])
#        sp_sch[sch_name].surface_area  =float(line_content[4])
#        sp_sch[sch_name].soil_thickness=float(line_content[5])
#        sp_sch[sch_name].time_surface_emerge = pd.datetime.strptime(line_content[10],'%Y/%b/%d %H:%M')
#
#        sp_sch[sch_name].por=float(line_content[6])
#        sp_sch[sch_name].te_coef=float(line_content[8])
#        sp_sch[sch_name].tas606_coef=float(line_content[9])
#        min_index, min_value = min(enumerate( abs(data.df['date_time']-sp_sch[sch_name].start_dt)), key=operator.itemgetter(1))
#        sp_sch[sch_name].start_ind=min_index
#        min_index, min_value = min(enumerate( abs(data.df['date_time']-sp_sch[sch_name].end_dt)), key=operator.itemgetter(1))
#        sp_sch[sch_name].end_ind=min_index
#        #sp_sch[sch_name].df.=data.df[sp_sch[sch_name]['start_ind']:sp_sch[sch_name]['end_ind']]
#        ## reset index
#        sp_sch[sch_name].df=sp_sch[sch_name].df.reset_index(drop=True)
#        ## add new column
#        ## http://stackoverflow.com/questions/12555323/adding-new-column-to-existing-dataframe-in-python-pandas
#        sp_sch[sch_name].df=sp_sch[sch_name].df.assign(
#            time_days=[(sp_sch[sch_name].df['date_time'][x]-sp_sch[sch_name].df['date_time'][0]).total_seconds()/86400
#                    for x in range(len(sp_sch[sch_name].df['date_time']))])
#
#        min_index, min_value = min(enumerate( abs(sp_sch[sch_name].df['date_time']- sp_sch[sch_name].time_surface_emerge 
#            )), key=operator.itemgetter(1))
#        sp_sch[sch_name].idx_surface_emerge = min_index 
#
#        sp_sch[sch_name].df['cum_evap_te']=(sp_sch[sch_name].df['te'][0]-sp_sch[sch_name].df['te']
#            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water/sp_sch[sch_name].te_coef  
#        sp_sch[sch_name].df['evap_rate_te']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_te'] ),np.nan)/dt_s
#        sp_sch[sch_name].df['cum_evap_tas606']=(sp_sch[sch_name].df['tas606'][0]-sp_sch[sch_name].df['tas606']
#            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water/sp_sch[sch_name].tas606_coef  
#        sp_sch[sch_name].df['evap_rate_tas606']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_tas606'] ),np.nan)/dt_s
#
#        sp_sch[sch_name].df['cum_evap_commercial']=(sp_sch[sch_name].df['commercial'][0]-sp_sch[sch_name].df['commercial']
#            )*constants.g2kg/sp_sch[sch_name].surface_area/constants.rhow_pure_water
#        sp_sch[sch_name].df['evap_rate_commercial']=np.append(np.diff(sp_sch[sch_name].df['cum_evap_commercial'] ),np.nan)/dt_s
#        
#        # calculate saturaturation based on commercial balance
#        total_water_depth=sp_sch[sch_name].por*sp_sch[sch_name].soil_thickness
#
#        sp_sch[sch_name].df['sat_commercial'][sp_sch[sch_name].df['sat_commercial']>1]=1
#        sp_sch[sch_name].df['cum_evap_commercial'][sp_sch[sch_name].df['cum_evap_commercial']<0]=0
#        sp_sch[sch_name].df['cum_evap_te'][sp_sch[sch_name].df['cum_evap_te']<0]=0
#        sp_sch[sch_name].df['evap_rate_te'][sp_sch[sch_name].df['evap_rate_te']<0]=0
#        sp_sch[sch_name].df['suc_commercial']=constants.swcc_reverse_fredlund_xing_1994(vwc=sp_sch[sch_name].df.sat_commercial*sp_sch[sch_name].por,por=0.37)
#        sp_sch[sch_name].df['mo_7_suction']=sensorfun.dielectric_suction_fit(x=sp_sch[sch_name].df  ['mo_7'],x_offset=320,x_scale=25.0,y_scale=-20,y_offset=13.8,lamb=3.0)
#        sp_sch[sch_name].df['mo_8_suction']=sensorfun.dielectric_suction_fit(x=sp_sch[sch_name].df  ['mo_8'],x_offset=399,x_scale=15.0,y_scale=-20,y_offset=17.1,lamb=0.75)
#
#
#
#
#        if sch_name=='redmud_second':  # do only at the third
#            #x_inp=np.concatenate([np.array(sp_sch['redmud_first'].df['norm_delta_t_2896_heat']),np.array(sp_sch['redmud_second'].df['norm_delta_t_2896_heat'])])
#            #y_inp=np.log(np.concatenate([np.array(sp_sch['redmud_first'].df['suc_commercial']),np.array(sp_sch['redmud_second'].df['suc_commercial'])]))
#            x_inp=np.array(sp_sch['redmud_first'].df['norm_delta_t_2896_heat'])
#            y_inp=np.log(np.array(sp_sch['redmud_first'].df['suc_commercial']))
#            idx = np.isfinite(x_inp) & np.isfinite(y_inp)
#            
#            c=np.polyfit(x_inp[idx],y_inp[idx],1)
#            thermal_suction_2896_norm_temp=np.arange(0,1,0.02)
#            thermal_suction_2896_suction=np.exp(c[0]*thermal_suction_2896_norm_temp+c[1])
#        c=np.array([-11.70,15.96])  # best swcc
#        #c=np.array([-11.70,13.96])
#        #c=np.array([-13.50,14.96]) # best fitting
#        thermal_suction_2896_norm_temp=np.arange(0,1,0.02)
#        thermal_suction_2896_suction=np.exp(c[0]*thermal_suction_2896_norm_temp+c[1])
#        sp_sch[sch_name].df['suht_2896_suction']=np.exp(c[0]*sp_sch[sch_name].df['norm_delta_t_2896_heat']+c[1])
#        # getting the mo_9_wmc
#        #i=25 # this is the best as tested
#        #c=np.polyfit(sp_sch[sch_name].df ['mo_9'],sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'],i)
#        #y=0
#        #for ind,key in enumerate(c):
#        #    y+=key*sp_sch[sch_name].df ['mo_9']**(i-ind)
#        #sp_sch[sch_name].df['mo_9_vwc']=y
#
#   
#        #ii=20 # this is the best as tested
#        #cc=np.polyfit(sp_sch[sch_name].df ['mo_10'],sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'],ii)
#        #y=0
#        #for ind,key in enumerate(cc):
#        #    y+=key*sp_sch[sch_name].df ['mo_10']**(ii-ind)
#        #sp_sch[sch_name].df['mo_10_vwc']=y
#        #a=sp_sch[sch_name].df ['mo_9']
#        #b=sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial']
#        #aa=sp_sch[sch_name].df ['mo_10']
#        #i=15
#        #coef_poly=np.polyfit(sp_sch[sch_name].df ['mo_9'],sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'],i)
#        #y=0
#        #for ind,key in enumerate(coef_poly):
#        #    y+=key*a**(i-ind)
#
#   
#        #ii=15
#        #cc=np.polyfit(aa,b,ii)
#        #yy=0
#        #for ind,key in enumerate(cc):
#        #    yy+=key*aa**(ii-ind)
#        
##`import matplotlib.pylab as pylab
##`params = {'legend.fontsize': 'x-large',
##`          'figure.figsize': (10, 5),
##`         'axes.labelsize': 10,
##`         'axes.titlesize':'x-large',
##`         'xtick.labelsize':'20',
##`         'ytick.labelsize':'20'}
##`#         'axes.grid':'linewidth=grid_width,color = '0.5''}
##`#         'linewidth':lw,'markers.size':ms,'markers.edgewidth':mew}
##`pylab.rcParams.update(params)
#
#
##s script is used for calibrating load cells
#
##plot_fredlund_calibration=True
##plot_moisture_calibration=True
##plot_temphum_calibration=True
##plot_dielectric_suction_calibration=True
#
#plot_fredlund_calibration=False
#plot_fredlund_calibration_suction=False
#plot_moisture_calibration=False
#plot_temphum_calibration=False
#plot_dielectric_suction_calibration=False
#plot_volumetric_content_vs_suction=True
#
#
#
#if plot_fredlund_calibration_suction:
#    
#    fig=figlib.single_fig_initialise() 
#    
#    sch_name='redmud_first'
#    plt.semilogy(sp_sch[sch_name].df['norm_delta_t_2896_heat'] , sp_sch[sch_name].df ['suc_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Ther. suc. sensor C, red mud exp. 1') 
#
#    sch_name='redmud_second'
#    plt.semilogy(sp_sch[sch_name].df.norm_delta_t_2896_heat, sp_sch[sch_name].df ['suc_commercial'], 'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Ther. suc. sensor C, red mud exp. 2') 
#    
#    plt.semilogy(thermal_suction_2896_norm_temp,thermal_suction_2896_suction, 'c-',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='y = '+'%.2f' % c[0]+'x + '+'%.2f' % c[1]) 
#
#    
#    
#    plt.xlabel('NORMALIZED TEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
#    plt.ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
#    plt.legend(bbox_to_anchor=(.3, 0.98), loc=2, borderaxespad=0.,fontsize=12)
#    plt.grid(linewidth=grid_width,c = '0.5')
#    
#    plt.axhline(y=50,xmin=-1,xmax=2,c='0.2',linewidth=3,zorder=0)
#    plt.text(0.00, 70, 'Air entry pressure', fontsize=15)
#
#    
#    plt.show(block=False)
#    plt.close()
#    
#    fig.savefig('plot_fredlund_calibration_suction.png', format='png', dpi=300)
#    header = ["norm_delta_t_2847_heat", "norm_delta_t_2896_heat", "suc_commercial"]
#    sch_name='redmud_first'
#    sp_sch[sch_name].df.to_csv('plot_fredlund_calibration_suction_'+sch_name+'.csv', columns = header)
#    sch_name='redmud_second'
#    sp_sch[sch_name].df.to_csv('plot_fredlund_calibration_suction_'+sch_name+'.csv', columns = header)
#
#if plot_temphum_calibration:
#    fig = plt.figure(figsize=(10,10))
#    lw=5
#    ms=8
#    mew=3
#    grid_width=2
#    y_fontsize=20
#
#    ax = fig.add_subplot(111)
#
#    # you can change each line separately, like:
#    #ax.spines['right'].set_linewidth(0.5)
#    # to change all, just write:
#    
#    for axis in ['top','bottom','left','right']:
#      ax.spines[axis].set_linewidth(2) 
#    
#    sch_name='redmud_first'
#    plt.semilogx(sp_sch[sch_name].df  ['saltrh_2_suction'] ,sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Temp. Humi. A, experiment 1') 
#    plt.semilogx(sp_sch[sch_name].df  ['saltrh_11_suction'], sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Temp. Humi. B, experiment 1') 
#    sch_name='redmud_second'
#    #plt.semilogx(sp_sch[sch_name].df  ['saltrh_2_suction'] ,sp_sch[sch_name].df ['sat_commercial'], 'x' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Temp. Humi. A, experiment 2') 
#    #plt.semilogx(sp_sch[sch_name].df  ['saltrh_11_suction'] ,sp_sch[sch_name].df ['sat_commercial'], 'x' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Temp. Humi. B, experiment 2') 
#    plt.xlabel('SOIL SUCTION (m)', fontsize=y_fontsize, labelpad=10)
#    plt.ylabel('DEGREE OF SATURATION (-)', fontsize=y_fontsize, labelpad=10)
#    #plt.legend(bbox_to_anchor=(.5, 0.98), loc=2, borderaxespad=0.,fontsize=15)
#    #plt.grid(linewidth=grid_width,color = '0.5')
#    plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#
#    #plt.show(block=False)
#    
#    fig.savefig('plot_temperature_humidity_calibration.png', format='png', dpi=300)
#    plt.close()  # it is all caused by pywafo. 
#
#
#
#if plot_dielectric_suction_calibration:
#    fig=figlib.single_fig_initialise() 
#
#    fig.subplots_adjust(left=0.15, right=0.98, top=0.98, bottom=0.12)
#    
#    sch_name='redmud_first'
#
#    plt.semilogy(sp_sch[sch_name].df  ['mo_7'] ,sp_sch[sch_name].df ['suc_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Diel. suc. sen. A, red mud exp. 1') 
#    plt.semilogy(sp_sch[sch_name].df  ['mo_8'], sp_sch[sch_name].df ['suc_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. B, red mud exp. 1') 
#    plt.semilogy(sp_sch[sch_name].df  ['mo_7'], sp_sch[sch_name].df  ['mo_7_suction'] , 'k-',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. A, calibration curve',linewidth=lw) 
#    sch_name='redmud_second'
#    plt.semilogy(sp_sch[sch_name].df  ['mo_7'] ,sp_sch[sch_name].df ['suc_commercial'], 'x',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Diel. suc. sen. A, red mud exp. 2') 
#    plt.semilogy(sp_sch[sch_name].df  ['mo_8'], sp_sch[sch_name].df ['suc_commercial'], 'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. A, red mud exp. 2') 
#    plt.semilogy(sp_sch[sch_name].df  ['mo_8'], sp_sch[sch_name].df  ['mo_8_suction'] , '-',mfc='none' ,markeredgecolor='brown',color='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Diel. suc. sen. B, calibration curve',linewidth=lw) 
#    
#    plt.xlabel('RAW READING (m)', fontsize=y_fontsize, labelpad=10)
#    plt.ylabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
#    plt.legend(bbox_to_anchor=(.01, 0.98), loc=2, borderaxespad=0.,fontsize=12)
#    #plt.grid(linewidth=grid_width,color = '0.5')
#    plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    plt.axhline(y=1000,xmin=-1,xmax=2,c='0.2',linewidth=3,zorder=0)
#    plt.text(200, 1500, 'Air entry pressure\n10 bar', fontsize=15)
#
#    plt.ylim([1,1e7])
#    #plt.show(block=False)
#    
#    fig.savefig('plot_dielectric_suction_calibration.png', format='png', dpi=300)
#    plt.close()  # it is all caused by pywafo. 
#    
#    header = ["mo_7", "mo_8", "suc_commercial", "mo_7_suction","mo_7_suction"]
#    sch_name='redmud_first'
#    sp_sch[sch_name].df.to_csv('plot_dielectric_suction_calibration_'+sch_name+'.csv', columns = header)
#    sch_name='redmud_second'
#    sp_sch[sch_name].df.to_csv('plot_dielectric_suction_calibration_'+sch_name+'.csv', columns = header)
#
#
#if plot_volumetric_content_vs_suction:
#    
#    fig=figlib.single_fig_initialise() 
#    [vwc_fred_xing,suction_fred_xing_kpa]=constants.swcc_fredlund_xing_1994(plot=False,por=sp_sch['redmud_second'].por)
#
#    
#    sch_name='redmud_first'
#    plt.semilogx(suction_fred_xing_kpa, vwc_fred_xing, 'c-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='SWCC') 
#    #plt.semilogx(sp_sch[sch_name].df ['mo_7_suction'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric suction sensor A, experiment 1') 
#
#    #plt.semilogx(sp_sch[sch_name].df ['mo_8_suction'] , sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction sensor B, experiment 1') 
#    ##plt.semilogx(sp_sch[sch_name].df  ['suc_commercial'], sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'k-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',label='expontntial') 
#    plt.semilogx(sp_sch[sch_name].df ['mo_7_suction'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'DS A, red mud Expt 1') 
#    plt.semilogx(sp_sch[sch_name].df ['mo_8_suction'] , sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='red',markersize=ms,markeredgewidth=mew,fillstyle='full',label='DS B, red mud Expt 1') 
#    plt.semilogx(sp_sch[sch_name].df ['suht_2896_suction'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], '+',mfc='none' ,markeredgecolor='green',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'TS C, red mud Expt 1',ms=13,markevery=2) 
#    sch_name='redmud_second'
#    #plt.semilogx(sp_sch[sch_name].df   ['mo_7_suction'] ,sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric suction sensor A, experiment 2') 
#    #plt.semilogx(sp_sch[sch_name].df  ['mo_8_suction'], sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction sensor B, experiment 2') 
#
#    plt.semilogx(sp_sch[sch_name].df   ['mo_7_suction'] ,sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'DS A, red mud Expt 2') 
#    plt.semilogx(sp_sch[sch_name].df  ['mo_8_suction'], sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='pink',markersize=ms,markeredgewidth=mew,fillstyle='full',label='DS B, red mud Expt 2') 
#    plt.semilogx(sp_sch[sch_name].df ['suht_2896_suction'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], '+',mfc='none' ,markeredgecolor='orange',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'TS C, red mud Expt 2',ms=13,markevery=2) 
#
#
#    plt.ylabel('VOLUMETRIC WATER CONTENT\nFROM BALANCE', fontsize=y_fontsize, labelpad=10)
#    plt.xlabel('SUCTION (kPa)', fontsize=y_fontsize, labelpad=10)
#
#    #fig.set_axisbelow(True)
#    plt.legend(bbox_to_anchor=(.01, 0.3), loc=2, borderaxespad=0.,fontsize=12)
#    #plt.grid(linewidth=grid_width,color = '0.5')
#    plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#
#    plt.xlim([1,5e6])
#    plt.ylim([-0.01,0.58])
#    #plt.show(block=False)
#    
#    fig.savefig('plot_volumetric_content_vs_suction.png', format='png', dpi=300)
#    
#    plt.close()  # it is all caused by pywafo. 
#    np.savetxt("plot_volumetric_content_vs_suction.csv", [sp_sch[sch_name].df  ['mo_7_suction'],sp_sch[sch_name].df ['sat_commercial'],  sp_sch[sch_name].df  ['mo_8_suction'],sp_sch[sch_name].df ['sat_commercial']]
#    , delimiter=",")
#
#    header = ["mo_7_suction", "mo_8_suction", "suc_commercial", "mo_7_suction","mo_7_suction"]
#    sch_name='redmud_first'
#    sp_sch[sch_name].df.to_csv('plot_volumetric_content_vs_suction_'+sch_name+'.csv', columns = header)
#    sch_name='redmud_second'
#    sp_sch[sch_name].df.to_csv('plot_volumetric_content_vs_suction_'+sch_name+'.csv', columns = header)
#
#if plot_fredlund_calibration:
#
#    
#    lw=4
#    ms=8
#    mew=3
#    grid_width=2
#    y_fontsize=20
#    
#    fig = plt.figure(figsize=(12,12))
#    ax = fig.add_subplot(111)
#    for axis in ['top','bottom','left','right']:
#            ax.spines[axis].set_linewidth(2)
#
#    sch_name='redmud_first'
#    plt.plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['norm_delta_t_2896_heat']   ,'ro',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Red mud tailings experiment 1') 
#    sch_name='redmud_second'
#    plt.plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['norm_delta_t_2896_heat']   ,'kx',markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Red mud tailings experiment 2')
#    
#    plt.ylabel('NORMALISED TEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
#    plt.xlabel('DEGREE OF SATURATION (-)', fontsize=y_fontsize, labelpad=10)
#    plt.legend(bbox_to_anchor=(.4, 0.3), loc=2, borderaxespad=0.,fontsize=15)
#    plt.grid(linewidth=grid_width,color = '0.5')
#    plt.ylim(-0.1,1.1)
#    
#    
#    fig.savefig('normalised_temperature_single.png', format='png', dpi=300)
#    fig, ax = plt.subplots(3,sharex=True,figsize=(12,16))
#    plt.close()
#
#    
##    lw=4
##    ms=8
##    mew=3
##    grid_width=2
##    y_fontsize=20
##    
##    for i in ax:
##      for axis in ['top','bottom','left','right']:
##        i.spines[axis].set_linewidth(2)
##    
##    sch_name='redmud_first'
##    ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['norm_delta_t_2896_heat'] ,'ro',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 1') 
##    ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['norm_delta_t_19_heat']   ,'ro',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 1') 
##    ax[2].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['norm_delta_t_14_heat']   ,'ro',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction C, experiment 1') 
##    sch_name='redmud_second'
##    ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['norm_delta_t_2896_heat'] ,'kx',markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 2') 
##    ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['norm_delta_t_19_heat']   ,'kx',markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 2') 
##    ax[2].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['norm_delta_t_14_heat']   ,'kx',markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction C, experiment 2')
##    
##    ax[0].set_ylabel('NORMALISED\nTEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
##    ax[1].set_ylabel('NORMALISED\nTEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
##    ax[2].set_ylabel('NORMALISED\nTEMPERATURE (-)', fontsize=y_fontsize, labelpad=10)
##    ax[2].set_xlabel('DEGREE OF SATURATION (-)', fontsize=y_fontsize, labelpad=10)
##    ax[0].legend(bbox_to_anchor=(.5, 0.3), loc=2, borderaxespad=0.,fontsize=15)
##    ax[1].legend(bbox_to_anchor=(.5, 0.3), loc=2, borderaxespad=0.,fontsize=15)
##    ax[2].legend(bbox_to_anchor=(.5, 0.3), loc=2, borderaxespad=0.,fontsize=15)
##    ax[0].set_title('(A)',x=0.02,y=1.0)
##    ax[1].set_title('(B)',x=0.02,y=1.0)
##    ax[2].set_title('(C)',x=0.02,y=1.0)
##    ax[0].grid(linewidth=grid_width,color = '0.5')
##    ax[1].grid(linewidth=grid_width,color = '0.5')
##    ax[2].grid(linewidth=grid_width,color = '0.5')
##    ax[0].set_ylim(-0.1,1.1)
##    ax[1].set_ylim(-0.1,1.1)
##    ax[2].set_ylim(-0.1,1.1)
##    
##    #plt.show(block=False)
##    
##    fig.savefig('normalized_temperature.png', format='png', dpi=500)
#
##fig, ax = plt.subplots(3,sharex=True,figsize=(12,16))
##
##lw=4
##ms=3
##mew=1.5
##grid_width=2
##y_fontsize=20
##
##for i in ax:
##  for axis in ['top','bottom','left','right']:
##    i.spines[axis].set_linewidth(2)
##
##sch_name='redmud_first'
##ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['deltat_2896_heat'] ,'ro' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 1') 
##ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['deltat_19_heat'] ,'go' ,markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 1') 
##ax[2].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['deltat_14_heat'] ,'bo' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Moisture A, experiment 1') 
##sch_name='redmud_second'
##ax[0].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['deltat_2896_heat'] ,'rs',markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction A, experiment 2') 
##ax[1].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['deltat_19_heat'] ,'gs',markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric suction B, experiment 2') 
##ax[2].plot(sp_sch[sch_name].df ['sat_commercial'], sp_sch[sch_name].df  ['deltat_14_heat'] ,'bs',markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Moisture A, experiment 2')
##
##ax[0].set_ylabel('WEIGHT (G)', fontsize=y_fontsize, labelpad=10)
##ax[1].set_ylabel('RAW READING FROM \n DIELECTRIC SUCTION SENSORS ', fontsize=y_fontsize, labelpad=20)
##ax[2].set_xlabel('DEGREE OF SATURATION', fontsize=y_fontsize, labelpad=10)
##ax[0].legend(bbox_to_anchor=(.6, 0.98), loc=2, borderaxespad=0.,fontsize=15)
##ax[1].legend(bbox_to_anchor=(.02, 0.37), loc=2, borderaxespad=0.,fontsize=15)
##ax[0].set_title('(A)',x=0.02,y=1.0)
##ax[1].set_title('(B)',x=0.02,y=1.0)
##ax[0].grid(linewidth=grid_width,color = '0.5')
##ax[1].grid(linewidth=grid_width,color = '0.5')
##
##plt.show(block=False)
#
#
##
##
##
##
#if plot_moisture_calibration:
#    
#    fig=figlib.single_fig_initialise() 
#    
#    sch_name='redmud_first'
#
#    i=25 # this is the best as tested
#    c=np.polyfit(sp_sch[sch_name].df ['mo_9'],sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'],i)
#    y=0
#    for ind,key in enumerate(c):
#        y+=key*sp_sch[sch_name].df ['mo_9']**(i-ind)
#    sp_sch[sch_name].df['mo_9_vwc']=y
#    sch_name='redmud_second'
#    y=0
#    for ind,key in enumerate(c):
#        y+=key*sp_sch[sch_name].df ['mo_9']**(i-ind)
#    sp_sch[sch_name].df['mo_9_vwc']=y
#    sp_sch[sch_name].df['mo_9_vwc'][sp_sch[sch_name].df['mo_9_vwc']<0]=0
#    sp_sch[sch_name].df['mo_9_vwc'][sp_sch[sch_name].df['mo_9_vwc']>sp_sch[sch_name].por]=sp_sch[sch_name].por
# 
#
#
#    sch_name='redmud_first'
#    ii=20 # this is the best as tested
#    cc=np.polyfit(sp_sch[sch_name].df ['mo_10'],sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'],ii)
#    y=0
#    for ind,key in enumerate(cc):
#        y+=key*sp_sch[sch_name].df ['mo_10']**(ii-ind)
#    sp_sch[sch_name].df['mo_10_vwc']=y
#    sch_name='redmud_second'
#    y=0 
#    for ind,key in enumerate(cc):
#        y+=key*sp_sch[sch_name].df ['mo_10']**(ii-ind)
#    sp_sch[sch_name].df['mo_10_vwc']=y
#    sp_sch[sch_name].df['mo_10_vwc'][sp_sch[sch_name].df['mo_10_vwc']<0]=0
#    sp_sch[sch_name].df['mo_10_vwc'][sp_sch[sch_name].df['mo_10_vwc']>sp_sch[sch_name].por]=sp_sch[sch_name].por
#    
#    #a=sp_sch[sch_name].df ['mo_9']
#    #b=sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial']
#    #aa=sp_sch[sch_name].df ['mo_10']
#    #i=25 # this is the best as tested
#    #c=np.polyfit(a,b,i)
#    #y=0
#    #for ind,key in enumerate(c):
#    #    y+=key*a**(i-ind)
#   
#    #ii=20 # this is the best as tested
#    #cc=np.polyfit(aa,b,ii)
#    #yy=0
#    #for ind,key in enumerate(cc):
#    #    yy+=key*aa**(ii-ind)
#
#    #plt.plot(a,y, 'c-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
#    #plt.plot(aa,yy, 'k-',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
#    sch_name='redmud_first'
#
#    plt.plot(sp_sch[sch_name].df ['mo_9'], sp_sch[sch_name].df ['mo_9_vwc'] ,'-',color='k',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Dielectric moisture sensor A, cali. curve') 
#    plt.plot(sp_sch[sch_name].df ['mo_10'], sp_sch[sch_name].df ['mo_10_vwc'] ,'-',color='brown',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Dielectric moisture sensor B, cali. curve') 
#    plt.plot(sp_sch[sch_name].df ['mo_9'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\nred mud experiment 1') 
#    plt.plot(sp_sch[sch_name].df ['mo_10'] , sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric moisture sensor B,\nred mud experiment 1') 
#    
#
#    #plt.plot(sp_sch[sch_name].df ['mo_9'], sp_sch[sch_name].df ['mo_9_vwc'] ,'k-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
#    #plt.plot(sp_sch[sch_name].df ['mo_10'], sp_sch[sch_name].df ['mo_10_vwc'] ,'m-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
#    #plt.plot(sp_sch[sch_name].df ['mo_9'],   sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A, experiment 1') 
#    #plt.plot(sp_sch[sch_name].df ['mo_10'] , sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric moisture sensor B, experiment 1') 
#
#    sch_name='redmud_second'
#    plt.plot(sp_sch[sch_name].df  ['mo_9'] ,sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='k',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A,\nred mud experiment 2') 
#    plt.plot(sp_sch[sch_name].df  ['mo_10'], sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'x',mfc='none' ,markeredgecolor='brown',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric moisture sensor B,\nred mud experiment 2') 
#
#    #plt.plot(sp_sch[sch_name].df ['mo_9'], sp_sch[sch_name].df ['mo_9_vwc'] ,'r-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
#    #plt.plot(sp_sch[sch_name].df ['mo_10'], sp_sch[sch_name].df ['mo_10_vwc'] ,'b-',mfc='none' ,markeredgecolor='c',markersize=ms,markeredgewidth=mew,fillstyle='full',linewidth=lw,label='Fredlund SWCC device') 
#    #plt.plot(sp_sch[sch_name].df  ['mo_9'] ,sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label= 'Dielectric moisture sensor A, experiment 2') 
#    #plt.plot(sp_sch[sch_name].df  ['mo_10'], sp_sch[sch_name].por*sp_sch[sch_name].df ['sat_commercial'], 'o',mfc='none' ,markeredgecolor='b',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Dielectric moisture sensor B, experiment 2') 
#
#    
#    plt.ylabel('VOLUMETRIC WATER CONTENT\nFROM BALANCE', fontsize=y_fontsize, labelpad=10)
#    plt.xlabel('RAW READING FROM \n DIELECTRIC MOISTURE SENSORS ', fontsize=y_fontsize, labelpad=10)
#    plt.legend(bbox_to_anchor=(.33, 0.99), loc=2, borderaxespad=0.,fontsize=12)
#    plt.grid(True,which="both",ls=":",linewidth=grid_width,color = '0.5')
#    plt.ylim([-0.05,0.58])
#    
#    
#    fig.savefig('plot_moisture_calibration.png', format='png', dpi=300)
#    plt.close()  # it is all caused by pywafo. 
#    
#    
#    header = ["mo_9", "mo_10", "sat_commercial"]
#    sch_name='redmud_first'
#    sp_sch[sch_name].df.to_csv('plot_moisture_calibration_'+sch_name+'.csv', columns = header)
#    sch_name='redmud_second'
#    sp_sch[sch_name].df.to_csv('plot_moisture_calibration_'+sch_name+'.csv', columns = header)
#
##
###
### evaporation rate and potential evaporation, time as x axis
###xfmt = mdates.DateFormatter('%y-%m-%d %H:%M') %	for checking results
##xfmt = mdates.DateFormatter('%m/%d ')
##fig, ax = plt.subplots(2,sharex=False,figsize=(12,16))
##ax[0].plot((sp_sch['redmud_first'].df ['date_time']-sp_sch['redmud_first'].df ['date_time'][0])*constants.second2day, sp_sch['redmud_first'].df  ['cum_evap_te']*constants.m2mm,         'ro',markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Load cell') 
##ax[0].plot((sp_sch['redmud_second'].df['date_time']-sp_sch['redmud_first'].df ['date_time'][0])*constants.second2day, sp_sch['redmud_second'].df ['cum_evap_te']*constants.m2mm,         'ro',markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full') 
##ax[0].plot((sp_sch['redmud_first'].df ['date_time']-sp_sch['redmud_first'].df ['date_time'][0])*constants.second2day, sp_sch['redmud_first'].df  ['cum_evap_commercial']*constants.m2mm,'go',markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full' ,label='Commercial balance')
##ax[0].plot((sp_sch['redmud_second'].df['date_time']-sp_sch['redmud_first'].df ['date_time'][0])*constants.second2day, sp_sch['redmud_second'].df ['cum_evap_commercial']*constants.m2mm,'go',markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full' )
###ax[0].xaxis.set_major_formatter(xfmt)
##
##ax[1].plot((sp_sch['redmud_first'].df ['date_time']-sp_sch['redmud_first'].df ['date_time'][0])*constants.second2day, sp_sch['redmud_first'].df  ['evap_rate_te']*constants.ms2mmday,'ro',markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Load cell')           
##ax[1].plot((sp_sch['redmud_second'].df['date_time']-sp_sch['redmud_first'].df ['date_time'][0])*constants.second2day, sp_sch['redmud_second'].df ['evap_rate_te']*constants.ms2mmday,'ro',markeredgecolor='r',markersize=ms,markeredgewidth=mew,fillstyle='full')  
##ax[1].plot((sp_sch['redmud_first'].df ['date_time']-sp_sch['redmud_first'].df ['date_time'][0])*constants.second2day, sp_sch['redmud_first'].df  ['evap_rate_commercial']*constants.ms2mmday,'go',markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full',label='Commercial balance') 
##ax[1].plot((sp_sch['redmud_second'].df['date_time']-sp_sch['redmud_first'].df ['date_time'][0])*constants.second2day, sp_sch['redmud_second'].df ['evap_rate_commercial']*constants.ms2mmday,'go',markeredgecolor='g',markersize=ms,markeredgewidth=mew,fillstyle='full') 
##ax[0].set_ylabel('CUMULATIVE EVAPORATION (MM)', fontsize=y_fontsize, labelpad=10)
##ax[1].set_ylabel('EVAPORATION RATE', fontsize=y_fontsize, labelpad=20)
##ax[0].set_xlabel('TIME (DAYS)', fontsize=y_fontsize, labelpad=10)
##ax[1].set_xlabel('TIME (DAYS)', fontsize=y_fontsize, labelpad=10)
##ax[0].legend(bbox_to_anchor=(.6, 0.98), loc=2, borderaxespad=0.,fontsize=15)
##ax[1].legend(bbox_to_anchor=(.02, 0.37), loc=2, borderaxespad=0.,fontsize=15)
##ax[0].set_title('(A)',x=0.02,y=1.0)
##ax[1].set_title('(B)',x=0.02,y=1.0)
##ax[0].grid(linewidth=grid_width,color = '0.5')
##ax[1].grid(linewidth=grid_width,color = '0.5')
##plt.show(block=False)
##
##
### evaporation rate and potential evaporation, all start from zero
##fig, ax = plt.subplots(2,sharex=False)
##ax[0].plot(sp_sch['redmud_first'].df ['time_days'], sp_sch['redmud_first']. df ['cum_evap_te']*constants.m2mm,'r+',markevery=2) 
##ax[0].plot(sp_sch['redmud_second'].df['time_days'], sp_sch['redmud_second'].df ['cum_evap_te']*constants.m2mm,'g+',markevery=2) 
##ax[0].plot(sp_sch['redmud_first'].df['time_days'], sp_sch['redmud_first'].  df  ['cum_evap_commercial']*constants.m2mm,'rv',markevery=2) 
##ax[0].plot(sp_sch['redmud_second'].df['time_days'], sp_sch['redmud_second'].df ['cum_evap_commercial']*constants.m2mm,'gv',markevery=2) 
##
##ax[1].plot(sp_sch['redmud_first'].df ['time_days'], sp_sch['redmud_first'].df  ['evap_rate_te']*constants.ms2mmday,'r+',markevery=2) 
##ax[1].plot(sp_sch['redmud_second'].df['time_days'], sp_sch['redmud_second'].df ['evap_rate_te']*constants.ms2mmday,'g+',markevery=2) 
##ax[1].plot(sp_sch['redmud_first'].df ['time_days'], sp_sch['redmud_first'].df  ['evap_rate_commercial']*constants.ms2mmday,'rv',markevery=2) 
##ax[1].plot(sp_sch['redmud_second'].df['time_days'], sp_sch['redmud_second'].df ['evap_rate_commercial']*constants.ms2mmday,'gv',markevery=2) 
##plt.show(block=False)
