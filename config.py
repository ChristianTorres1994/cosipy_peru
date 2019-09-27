"""
 This is the COSIPY configuration (init) file.
 Please make your changes here.
"""

#-----------------------------------
# SIMULATION PERIOD 
#-----------------------------------
time_start = '2016-06-01T00:00'
time_end   = '2018-05-30T23:00'

#-----------------------------------
# FILENAMES AND PATHS 
#-----------------------------------
time_start_str=(time_start[0:10]).replace('-','')
time_end_str=(time_end[0:10]).replace('-','')

data_path = './data/'                       
input_netcdf= 'Peru_input.nc'
output_netcdf = 'Peru_'+time_start_str+'-'+time_end_str+'.nc'

#-----------------------------------
# STAKE DATA 
#-----------------------------------
stakes_loc_file = './data/input/Peru/loc_stakes.csv'        # path to stake location file
stakes_data_file = './data/input/Peru/data_stakes_peru.csv' # path to stake data file
eval_method = 'rmse'                                        # how to evaluate the simulations ('rmse')

#-----------------------------------
# PARALLELIZATION 
#-----------------------------------
slurm_use = True            # use SLURM
workers = None              # number of workers, if local cluster is used
local_port = 8786           # port for local cluster

#-----------------------------------
# WRITE FULL FIELDS 
#-----------------------------------    
full_field = False          # write full fields (2D data) to file 
    
#-----------------------------------
# RESTART 
#-----------------------------------
restart = False             # set to true if you want to start from restart file 

#-----------------------------------
# TOTAL PRECIPITATION  
#-----------------------------------
force_use_TP = False        # If total precipitation and snowfall in input data use total precipitation

#-----------------------------------
# SUBSET  (provide pixel values) 
#-----------------------------------
tile = False 
xstart = 18
xend = 20
ystart = 28
yend = 30

