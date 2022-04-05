------
2_code
------

This folder contains the all the code to reproduce the analysis of the paper. 
Note that the global (CaMa-Flood and GTSM) model results are provided, but the local model setup is fully automated.
The code is saved in ipython notebook files and should be excecuted in the numbered order.

1_prepare
---------
NOTE: the notebooks in this folder can only be reproduced within the Deltares network. 
The exported & preprocessed data is however availabe from "../../1_data"
The paper contains references to the used datasets.
One should be able to pick-up from 2_experiment when using the published data.

- get_era5_waves.ipynb
- hydromt_data_export.ipynb
- preprocess_gtsm.ipynb

2_experiment
------------
- 21_setup_cmf_models.ipynb
21 prepares some files for the CaMa-Flood model of which the results are already provided in this repository but also 
translates some binary model files to GIS files for usage in 4_analyze_plot

- 22_setup_sfincs_models.ipynb
22 builds the SFINCS models for the sensitivity analysis and compound driver analysis for both historical events.
At the end of the script all models are executed by the SFINCS model kernel.

3_postprocess
-------------
All notebooks require 2_experiment to be finished.

- 31_process_eo_floodextent.ipynb
31 translates the original flood extent images to the model domain.

- 32_postprocess_simulations.ipynb
32 combines the max flood depth maps from all SFINCS scenarios and all CaMa-Flood scenarios.

4_analyze_plot
--------------
Step 41-42 require 2_experiment to be finished, Step 43-45 also require 3_postprocess to be finished.

- 41_plot_models.ipynb 
41 plots the model maps.

- 42_plot_forcing.ipynb
42 plots the forcing for both events.

- 43_floodextent_analysis.ipynb
43 computes several statistics (CSI, FR, HR) for both models based on the EO flood extent data.
Plots are made for the default scenarios. A table is produced for the sensitivity scenarios.

- 44_waterlevel_analysis.ipynb 
44 creates water level timeseries plots at several model output locations.

- 45_compound_analysis.ipynb
45 creates the compound driver plots.
