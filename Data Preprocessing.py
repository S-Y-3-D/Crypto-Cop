#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np

df1 = pd.read_csv(r"E:\Personal\University\7th Semester\FYP\Dataset\final-anormal-data-set.csv\abnormals.csv",engine='python');
df1['target']=1;

df1.drop(['cpu_guest','cpu_guest_nice','cpu_irq','cpu_softirq','diskio_sda1_disk_name','diskio_sda1_key','diskio_sda1_time_since_update','diskio_sda_disk_name'
       ,'diskio_sda_key','diskio_sda_time_since_update','diskio_sda_write_bytes','fs_/_device_name',
       'fs_/_fs_type','fs_/_key','fs_/_mnt_point','fs_/_size','load_min1','load_min15','load_min5',
       'mem_cached','mem_percent','memswap_free','memswap_percent','memswap_sin','memswap_sout','memswap_total',
       'network_lo_cumulative_cx','network_lo_cumulative_rx','network_lo_cumulative_tx','network_lo_cx',
       'network_lo_interface_name','network_lo_key','network_lo_rx','network_lo_time_since_update','network_lo_tx',
       'percpu_0_cpu_number','percpu_0_guest','percpu_0_guest_nice','percpu_0_idle',
       'percpu_0_key','percpu_0_nice','percpu_0_steal','percpu_0_total','percpu_0_user','processcount_sleeping',
        'system_hostname','system_hr_name','system_linux_distro','system_os_name','system_os_version','percpu_0_irq','mem_free','system_platform','timestamp'],axis=1, inplace=True);
df1.info()


# In[2]:


df2 = pd.read_csv(r"E:\Personal\University\7th Semester\FYP\Dataset\final-normal-data-set.csv\Normal.csv",engine='python');
df2['target']=0;
df2.drop(['cpu_guest','cpu_guest_nice','cpu_irq','cpu_softirq','diskio_sda1_disk_name','diskio_sda1_key','diskio_sda1_time_since_update','diskio_sda_disk_name'
       ,'diskio_sda_key','diskio_sda_time_since_update','diskio_sda_write_bytes','fs_/_device_name',
       'fs_/_fs_type','fs_/_key','fs_/_mnt_point','fs_/_size','load_min1','load_min15','load_min5',
       'mem_cached','mem_percent','memswap_free','memswap_percent','memswap_sin','memswap_sout','memswap_total',
       'network_lo_cumulative_cx','network_lo_cumulative_rx','network_lo_cumulative_tx','network_lo_cx',
       'network_lo_interface_name','network_lo_key','network_lo_rx','network_lo_time_since_update','network_lo_tx',
       'percpu_0_cpu_number','percpu_0_guest','percpu_0_guest_nice','percpu_0_idle',
       'percpu_0_key','percpu_0_nice','percpu_0_steal','percpu_0_total','percpu_0_user','processcount_sleeping',
        'system_hostname','system_hr_name','system_linux_distro','system_os_name','system_os_version','percpu_0_irq','mem_free','system_platform','timestamp'],axis=1, inplace=True);
df2.head(5)


# In[43]:


frames = [df1, df2]
result = pd.concat(frames)
result.info()


# In[3]:



frames = [df1, df2]

result = pd.concat(frames)


# In[7]:


result.to_csv('cryptojacking.csv',index=False);


# In[ ]:




