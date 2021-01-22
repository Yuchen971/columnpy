# applymap is the case to apply for all .
prof['grange_d_electrochem_o2']['data'].df= prof['grange_d_electrochem_o2']['data'].df.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None)
prof['grange_d_type_moisture_suction']['data'].df=prof['grange_d_type_moisture_suction']['data'].df.drop(columns=['temp'])
#prof['grange_d_type_moisture_suction']['data'].df= prof['grange_d_type_moisture_suction']['data'].df.applymap(lambda x: 0 ) if x.isdigit() is False else None)
prof['grange_d_type_moisture_suction']['data'].df= prof['grange_d_type_moisture_suction']['data'].df.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None)


prof['grange_a_electrochem_o2']['data'].df['dox3'].loc [   prof['grange_a_electrochem_o2']['data'].df['dox3'] <=10.0] =np.nan

time_start=np.datetime64('2018-05-12 21:50:53.445')
time_end=np.datetime64('2018-06-07 21:50:53.445')
prof['grange_a_electrochem_o2']['data'].df['wox2'].loc[time_start:time_end] =np.nan

time_start=np.datetime64('2018-07-18 21:50:53.445')
#time_end=np.datetime64('2018-06-07 21:50:53.445')
prof['grange_a_electrochem_o2']['data'].df['wox2'].loc[time_start:] =np.nan

sp=prof['grange_a_electrochem_o2']['data'].df
alpha_0=1.0
sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(300.0**alpha_0-1.0**alpha_0)*21.
#sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)
sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.

sp['wox0_c'] = (sp.wox0**alpha_0  -1.0**alpha_0)/(511.0**alpha_0-1.0**alpha_0)*13.
sp['wox1_c'] = (sp.wox1**alpha_0  -1.0**alpha_0)/(232.0**alpha_0-1.0**alpha_0)*13.
sp['wox2_c'] = (sp.wox2**alpha_0  -1.0**alpha_0)/(200.0**alpha_0-1.0**alpha_0)*13.
sp['wox3_c'] = (sp.wox3**alpha_0  -1.0**alpha_0)/(188.0**alpha_0-1.0**alpha_0)*13.
sp['wox4_c'] = (sp.wox4**alpha_0  -1.0**alpha_0)/(530.0**alpha_0-1.0**alpha_0)*13.
sp['wox7_c'] = (sp.wox7**alpha_0  -1.0**alpha_0)/(430.0**alpha_0-1.0**alpha_0)*13.

prof['grange_a_moisture_suction']['data'].df['mo7'].loc [   prof['grange_a_moisture_suction']['data'].df['mo7'] <=10] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo6'].loc [   prof['grange_a_moisture_suction']['data'].df['mo6'] <=10] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo5'].loc [   prof['grange_a_moisture_suction']['data'].df['mo5'] <=10] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo4'].loc [   prof['grange_a_moisture_suction']['data'].df['mo4'] <=10] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo3'].loc [   prof['grange_a_moisture_suction']['data'].df['mo3'] <=10] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo2'].loc [   prof['grange_a_moisture_suction']['data'].df['mo2'] <=10] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo1'].loc [   prof['grange_a_moisture_suction']['data'].df['mo1'] <=10] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo0'].loc [   prof['grange_a_moisture_suction']['data'].df['mo0'] <=10] =np.nan

prof['grange_a_moisture_suction']['data'].df['mo7'].loc [   prof['grange_a_moisture_suction']['data'].df['mo7'] >=600] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo6'].loc [   prof['grange_a_moisture_suction']['data'].df['mo6'] >=600] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo5'].loc [   prof['grange_a_moisture_suction']['data'].df['mo5'] >=600] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo4'].loc [   prof['grange_a_moisture_suction']['data'].df['mo4'] >=600] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo3'].loc [   prof['grange_a_moisture_suction']['data'].df['mo3'] >=600] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo2'].loc [   prof['grange_a_moisture_suction']['data'].df['mo2'] >=600] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo1'].loc [   prof['grange_a_moisture_suction']['data'].df['mo1'] >=600] =np.nan
prof['grange_a_moisture_suction']['data'].df['mo0'].loc [   prof['grange_a_moisture_suction']['data'].df['mo0'] >=600] =np.nan

prof['grange_d_type_moisture_suction']['data'].df['mo7'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo7'] <=10] =np.nan
prof['grange_d_type_moisture_suction']['data'].df['mo6'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo6'] <=10] =np.nan
prof['grange_d_type_moisture_suction']['data'].df['mo5'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo5'] <=10] =np.nan
prof['grange_d_type_moisture_suction']['data'].df['mo4'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo4'] <=10] =np.nan
prof['grange_d_type_moisture_suction']['data'].df['mo3'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo3'] <=10] =np.nan
prof['grange_d_type_moisture_suction']['data'].df['mo2'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo2'] <=10] =np.nan
prof['grange_d_type_moisture_suction']['data'].df['mo1'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo1'] <=10] =np.nan
prof['grange_d_type_moisture_suction']['data'].df['mo0'].loc [   prof['grange_d_type_moisture_suction']['data'].df['mo0'] <=10] =np.nan

prof['grange_5_mo_su']['data'].df=prof['grange_5_mo_su']['data'].df[pd.Timestamp('2018-2-06 21:50:53.445'):]
prof['grange_5_mo_su']['data'].df['mo7'].loc [   prof['grange_5_mo_su']['data'].df['mo7'] <=10] =np.nan
prof['grange_5_mo_su']['data'].df['mo6'].loc [   prof['grange_5_mo_su']['data'].df['mo6'] <=10] =np.nan
prof['grange_5_mo_su']['data'].df['mo5'].loc [   prof['grange_5_mo_su']['data'].df['mo5'] <=10] =np.nan
prof['grange_5_mo_su']['data'].df['mo4'].loc [   prof['grange_5_mo_su']['data'].df['mo4'] <=10] =np.nan
prof['grange_5_mo_su']['data'].df['mo3'].loc [   prof['grange_5_mo_su']['data'].df['mo3'] <=10] =np.nan
prof['grange_5_mo_su']['data'].df['mo2'].loc [   prof['grange_5_mo_su']['data'].df['mo2'] <=10] =np.nan
prof['grange_5_mo_su']['data'].df['mo1'].loc [   prof['grange_5_mo_su']['data'].df['mo1'] <=10] =np.nan
prof['grange_5_mo_su']['data'].df['mo0'].loc [   prof['grange_5_mo_su']['data'].df['mo0'] <=10] =np.nan

prof['grange_3_mo_su']['data'].df=prof['grange_3_mo_su']['data'].df[pd.Timestamp('2018-2-06 21:50:53.445'):]
prof['grange_4_mo_su']['data'].df=prof['grange_4_mo_su']['data'].df[pd.Timestamp('2018-2-06 21:50:53.445'):]

time_start=np.datetime64('2018-09-15 21:50:53.445')
#time_end=np.datetime64('2018-08-03 21:50:53.445')
prof['grange_3_luo2_dry']['data'].df['dlut2'].loc[time_start:] =np.nan

time_start=np.datetime64('2018-12-08 21:50:53.445')
#time_end=np.datetime64('2018-08-03 21:50:53.445')
prof['grange_4_luo2_dry']['data'].df['dlut4'].loc[time_start:] =np.nan


time_start=np.datetime64('2018-08-25 21:50:53.445')
#time_end=np.datetime64('2018-08-03 21:50:53.445')
prof['grange_4_mo_su']['data'].df['dluo7'].loc[time_start:] =np.nan

prof['grange_b_electrochem_o2']['data'].df['dox0'].loc [   prof['grange_b_electrochem_o2']['data'].df['dox0'] <=10] =np.nan
prof['grange_b_electrochem_o2']['data'].df['dox5'].loc [   prof['grange_b_electrochem_o2']['data'].df['dox5'] <=10] =np.nan
prof['grange_b_electrochem_o2']['data'].df['dox7'].loc [   prof['grange_b_electrochem_o2']['data'].df['dox7'] <=10] =np.nan

time_start=np.datetime64('2018-08-01 21:50:53.445')
time_end=np.datetime64('2018-08-12 21:50:53.445')
prof['grange_d_electrochem_o2']['data'].df['wox0'].loc[time_start:time_end] =np.nan


time_start=np.datetime64('2018-08-09 21:50:53.445')
#time_end=np.datetime64('2018-09-05 21:50:53.445')
#time_start=pd.to_datetime('2018-08-09 21:50:53.445')
#time_end=pd.to_datetime('2018-09-05 21:50:53.445')
#prof['grange_b_electrochem_o2']['data'].df['timestamp']=prof['grange_b_electrochem_o2']['data'].df.index
prof['grange_b_electrochem_o2']['data'].df['dox7'].loc[time_start:] =np.nan
#prof['grange_b_electrochem_o2']['data'].df['dox7'].loc[time_start:time_end] =np.nan

time_start=np.datetime64('2018-01-31 21:50:53.445')
#time_end=np.datetime64('2018-08-12 21:50:53.445')
prof['grange_b_electrochem_o2']['data'].df['wox3'].loc[time_start:] =np.nan

sp=prof['grange_b_electrochem_o2']['data'].df
sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*19.
sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(420.0**alpha_0-1.0**alpha_0)*19.
#sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*19.
#sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['dox5_c'] = (sp.dox5**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*19.
sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*19.
sp['dox7_c'] = (sp.dox7**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*19.

sp['wox0_c'] = (sp.wox0**alpha_0  -1.0**alpha_0)/(485.0**alpha_0-1.0**alpha_0)*20.
sp['wox1_c'] = (sp.wox1**alpha_0  -1.0**alpha_0)/(3.0**alpha_0-1.0**alpha_0)*20.
#sp['wox2_c'] = (sp.wox2**alpha_0  -1.0**alpha_0)/(.0**alpha_0-1.0**alpha_0)*21.
sp['wox3_c'] = (sp.wox3**alpha_0  -1.0**alpha_0)/(510.0**alpha_0-1.0**alpha_0)*20.
#sp['wox4_c'] = (sp.wox4**alpha_0  -1.0**alpha_0)/(.0**alpha_0-1.0**alpha_0)*21.
#sp['dox5_c'] = (sp.dox5**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
#sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
sp['wox7_c'] = (sp.wox7**alpha_0  -1.0**alpha_0)/(470.0**alpha_0-1.0**alpha_0)*20.

time_start=np.datetime64('2018-07-31 21:50:53.445')
#time_end=np.datetime64('2018-08-03 21:50:53.445')
prof['grange_d_electrochem_o2']['data'].df['dox3'].loc[time_start:] =np.nan

sp=prof['grange_d_electrochem_o2']['data'].df
#  https://stackoverflow.com/questions/22847304/exception-handling-in-pandas-apply-function
# below does not update the result
#sp['dox0'].apply(lambda x: float(x.strip('"') ) if type(x) is str else None) 
# this is the best
#sp['dox0']= sp['dox0'].apply(lambda x: float(x.strip('"') ) if type(x) is str else None) 
#sp= sp.applymap(lambda x: float(x.strip('"') ) if type(x) is str else None) 

#sp.assign('dox0'=lambda x: float(x.strip('"') ) if type(x) is str else None)

#only after this time is used as before that, the data was shown as string
#sp=prof['grange_d_electrochem_o2']['data'].df[pd.Timestamp('2017-12-13 21:50:53.445'):]
#2017-12-13 21:29
#sp.ix[sp.index.indexer_between_time(pd.timestamp('2017-12-13 14:03:00') ,pd.timestamp('2017-12-13 21:03:00')) ] ,  datetime.datetime(2017,12,13,21,30))]
#sp.ix[ sp[:pd.Timestamp('2018-1-13 14:50:53.445')] ]
#sp=sp[pd.Timestamp('2017-12-13 21:50:53.445'):]
sp['dox0_c'] = (sp.dox0**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*18.
sp['dox1_c'] = (sp.dox1**alpha_0  -1.0**alpha_0)/(420.0**alpha_0-1.0**alpha_0)*18.
sp['dox2_c'] = (sp.dox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*18.
sp['dox3_c'] = (sp.dox3**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*18.
sp['dox4_c'] = (sp.dox4**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*18.
#sp['dox5_c'] = (sp.dox5**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
sp['dox6_c'] = (sp.dox6**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*18.
#sp['dox7_c'] = (sp.dox7**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.

sp['wox0_c'] = (sp.wox0**alpha_0  -1.0**alpha_0)/(4.0**alpha_0-1.0**alpha_0)*21.
sp['wox1_c'] = (sp.wox1**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['wox2_c'] = (sp.wox2**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
sp['wox3_c'] = (sp.wox3**alpha_0  -1.0**alpha_0)/(4.0**alpha_0-1.0**alpha_0)*21.
sp['wox4_c'] = (sp.wox4**alpha_0  -1.0**alpha_0)/(510.0**alpha_0-1.0**alpha_0)*21.
#sp['dox5_c'] = (sp.dox5**alpha_0  -1.0**alpha_0)/(450.0**alpha_0-1.0**alpha_0)*21.
sp['wox6_c'] = (sp.wox6**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.
#sp['dox7_c'] = (sp.dox7**alpha_0  -1.0**alpha_0)/(550.0**alpha_0-1.0**alpha_0)*21.

prof['grange_b_luo2']['data'].df['dluo2'].loc [   prof['grange_b_luo2']['data'].df['dluo2'] <=0.0] =np.nan
prof['grange_b_luo2']['data'].df['dluo4'].loc [   prof['grange_b_luo2']['data'].df['dluo4'] <=0.0] =np.nan


prof['grange_3_luo2_dry']['data'].df['dluo0'].loc[ prof['grange_3_luo2_dry']['data'].df['dluo0']<=0 ] =np.nan
prof['grange_4_luo2_dry']['data'].df['dluo4'].loc[ prof['grange_4_luo2_dry']['data'].df['dluo4']<=10 ] =np.nan

prof['grange_5_luo2_dry']['data'].df['dluo6'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo6']<=5 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo5'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo5']<=5 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo4'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo4']<=5 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo3'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo3']<=5 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo2'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo2']<=5 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo1'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo1']<=5 ] =np.nan
prof['grange_5_luo2_dry']['data'].df['dluo0'].loc[ prof['grange_5_luo2_dry']['data'].df['dluo0']<=5 ] =np.nan

prof['grange_3_mo_su']['data'].df['dluo7'].loc[prof['grange_3_mo_su']['data'].df['dluo7']<=0.0] =np.nan
prof['grange_3_mo_su']['data'].df['tmp7'].loc[prof['grange_3_mo_su']['data'].df['tmp7']<=0.1] =np.nan
prof['grange_4_mo_su']['data'].df['tmp7'].loc[prof['grange_4_mo_su']['data'].df['tmp7']<=0.1] =np.nan
prof['grange_5_mo_su']['data'].df['tmp7'].loc[prof['grange_5_mo_su']['data'].df['tmp7']<=0.1] =np.nan


prof['grange_d_electrochem_o2']['data'].df['dtp4'].loc[ prof['grange_d_electrochem_o2']['data'].df['dtp4'] <=0 ] =np.nan

#time_start=np.datetime64('2018-12-05 21:50:53.445')
#time_end=np.datetime64('2018-08-03 21:50:53.445')
#prof['grange_5_luo2_wet']['data'].df['wluo5'].loc[time_start:time_end] =np.nan

prof['grange_5_luo2_wet']['data'].df['wluo0'].loc[ prof['grange_5_luo2_wet']['data'].df['wluo0']<=0.1 ] =np.nan
prof['grange_5_luo2_wet']['data'].df['wluo1'].loc[ prof['grange_5_luo2_wet']['data'].df['wluo1']<=0.1 ] =np.nan
prof['grange_5_luo2_wet']['data'].df['wluo2'].loc[ prof['grange_5_luo2_wet']['data'].df['wluo2']<=0.1 ] =np.nan
prof['grange_5_luo2_wet']['data'].df['wluo3'].loc[ prof['grange_5_luo2_wet']['data'].df['wluo3']<=0.1 ] =np.nan
prof['grange_5_luo2_wet']['data'].df['wluo4'].loc[ prof['grange_5_luo2_wet']['data'].df['wluo4']<=0.1 ] =np.nan
prof['grange_5_luo2_wet']['data'].df['wluo5'].loc[ prof['grange_5_luo2_wet']['data'].df['wluo5']<=0.1 ] =np.nan
prof['grange_5_luo2_wet']['data'].df['wluo4'].loc[ prof['grange_5_luo2_wet']['data'].df['wluo4']>=5 ] =np.nan
prof['grange_5_luo2_wet']['data'].df['wluo6'].loc[ prof['grange_5_luo2_wet']['data'].df['wluo6']<=0.1 ] =np.nan

prof['grange_3_luo2_wet']['data'].df['wluo0'].loc[ prof['grange_3_luo2_wet']['data'].df['wluo0']<=0.1 ] =np.nan
prof['grange_3_luo2_wet']['data'].df['wluo1'].loc[ prof['grange_3_luo2_wet']['data'].df['wluo1']<=0.1 ] =np.nan
prof['grange_3_luo2_wet']['data'].df['wluo2'].loc[ prof['grange_3_luo2_wet']['data'].df['wluo2']<=0.1 ] =np.nan
prof['grange_3_luo2_wet']['data'].df['wluo3'].loc[ prof['grange_3_luo2_wet']['data'].df['wluo3']<=0.1 ] =np.nan
prof['grange_3_luo2_wet']['data'].df['wluo4'].loc[ prof['grange_3_luo2_wet']['data'].df['wluo4']<=0.1 ] =np.nan
prof['grange_3_luo2_wet']['data'].df['wluo5'].loc[ prof['grange_3_luo2_wet']['data'].df['wluo5']<=0.1 ] =np.nan
prof['grange_3_luo2_wet']['data'].df['wluo6'].loc[ prof['grange_3_luo2_wet']['data'].df['wluo6']<=0.1 ] =np.nan

prof['grange_4_luo2_wet']['data'].df['wluo0'].loc[ prof['grange_4_luo2_wet']['data'].df['wluo0']<=0.1 ] =np.nan
prof['grange_4_luo2_wet']['data'].df['wluo1'].loc[ prof['grange_4_luo2_wet']['data'].df['wluo1']<=0.1 ] =np.nan
prof['grange_4_luo2_wet']['data'].df['wluo2'].loc[ prof['grange_4_luo2_wet']['data'].df['wluo2']<=0.1 ] =np.nan
prof['grange_4_luo2_wet']['data'].df['wluo3'].loc[ prof['grange_4_luo2_wet']['data'].df['wluo3']<=0.1 ] =np.nan
prof['grange_4_luo2_wet']['data'].df['wluo4'].loc[ prof['grange_4_luo2_wet']['data'].df['wluo4']<=0.1 ] =np.nan
prof['grange_4_luo2_wet']['data'].df['wluo5'].loc[ prof['grange_4_luo2_wet']['data'].df['wluo5']<=0.1 ] =np.nan
prof['grange_4_luo2_wet']['data'].df['wluo6'].loc[ prof['grange_4_luo2_wet']['data'].df['wluo6']<=0.1 ] =np.nan


prof['grange_5_mo_su']['data'].df['dluo7'].loc[ prof['grange_5_mo_su']['data'].df['dluo7']<=10 ] =np.nan
prof['grange_5_mo_su']['data'].df['wluo7'].loc[ prof['grange_5_mo_su']['data'].df['wluo7']<=0.1 ] =np.nan
prof['grange_3_mo_su']['data'].df['wluo7'].loc[ prof['grange_3_mo_su']['data'].df['wluo7']<=0.1 ] =np.nan
prof['grange_4_mo_su']['data'].df['wluo7'].loc[ prof['grange_4_mo_su']['data'].df['wluo7']<=0.1 ] =np.nan

prof['grange_5_mo_su']['data'].df['tmp7'].loc[ prof['grange_5_mo_su']['data'].df['tmp7']<=0.1 ] =np.nan
prof['grange_3_mo_su']['data'].df['tmp7'].loc[ prof['grange_3_mo_su']['data'].df['tmp7']<=0.1 ] =np.nan
prof['grange_4_mo_su']['data'].df['tmp7'].loc[ prof['grange_4_mo_su']['data'].df['tmp7']<=0.1 ] =np.nan



time_start=np.datetime64('2018-12-24 21:50:53.445')
prof['grange_4_mo_su']['data'].df['mo7'].loc[time_start:] =np.nan
#time_end=np.datetime64('2018-08-05 21:50:53.445')

time_start=np.datetime64('2018-10-01 21:50:53.445')
prof['grange_3_luo2_wet']['data'].df['wluo3'].loc[time_start:] =np.nan

alpha_mo=-5.0
porosity = 0.3

sp=prof['grange_a_moisture_suction']['data'].df
sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity

sp=prof['grange_b_moisture_suction']['data'].df
sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)*porosity
sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)*porosity
sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)*porosity
sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)*porosity
sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)*porosity
sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)*porosity
sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)*porosity
sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-330.**alpha_mo)*porosity

sp=prof['grange_d_type_moisture_suction']['data'].df
sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity
sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-350.**alpha_mo)*porosity


sp=prof['grange_3_mo_su']['data'].df
sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity

sp=prof['grange_4_mo_su']['data'].df
sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity

sp=prof['grange_5_mo_su']['data'].df
sp['mo0_c'] = -(sp.mo0**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo1_c'] = -(sp.mo1**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo2_c'] = -(sp.mo2**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo3_c'] = -(sp.mo3**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo4_c'] = -(sp.mo4**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo5_c'] = -(sp.mo5**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo6_c'] = -(sp.mo6**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity
sp['mo7_c'] = -(sp.mo7**alpha_mo  -550.**alpha_mo)/(550.0**alpha_mo-297.**alpha_mo)*porosity

