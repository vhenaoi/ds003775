import os
import glob
import numpy as np
import requests


subject_list = r'E:\Academico\Universidad\Posgrado\Tesis\Datos\BASESDEDATOS\SRM'
subjects = os.listdir(subject_list) 
json_remove = []
for sub in subjects:
    suffix = "sub"
    if sub.endswith(suffix,0,3) == True:
        ses = os.listdir(subject_list+'/'+sub)
        URL1 = "https://openneuro.org/crn/datasets/ds003775/snapshots/1.0.0/files/"+sub+":ses-t1:eeg:"+sub+"_ses-t1_task-resteyesc_eeg.edf"
        file = requests.get(URL1, stream = True)
        pathfile = subject_list+'/'+sub+'/'+'ses-t1/eeg/'+sub+'_ses-t1_task-resteyesc_eeg.edf'
        if os.path.exists(subject_list+'/'+sub+'/'+'ses-t2'): 
            URL2 = "https://openneuro.org/crn/datasets/ds003775/snapshots/1.0.0/files/"+sub+":ses-t2:eeg:"+sub+"_ses-t2_task-resteyesc_eeg.edf"
            file = requests.get(URL2, stream = True)  
            pathfile = subject_list+'/'+sub+'/'+'ses-t2/eeg/'+sub+'_ses-t2_task-resteyesc_eeg.edf' 
            with open(pathfile,"wb") as pdf:
                for chunk in file.iter_content(chunk_size=1024):            
                    if chunk:
                        pdf.write(chunk)
        else:
            pass
