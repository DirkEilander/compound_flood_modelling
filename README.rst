------------------------
compound flood modelling
------------------------

This repository contains all scripts and necessary data to reproduce the local SFINCS model simulations and analysis performed for:

Eilander, D., Couasnon, A., Muis, S., Ikeuchi, H., Dullaart, J., Yamazaki, D., Winsemius, H. C., & Ward, P. J. (submitted). 
A globally-applicable framework for compound flood hazard modeling. Natural Hazards and Earth System Sciences Discussions.

Getting started
---------------

1. Clone or download the repository and unzip all zip files in the "1_data" and "3_model/CMF" folders.
2. Install a conda environment based on the environment.yml file within this repository, see code below.
3. Then, follow the notebooks contained in the 2_code folder.

.. code-block:: console
  
  conda env create -f environment.yml


Repository outline
------------------

::

  > 1_data
    > 1_static
    > 2_forcing
    > 3_eo_rapid
    > 4_observations
  > 2_code
    > 1_prepare (not required / only executable from with the Deltares network)
    > 2_experiment
    > 3_postprocess
    > 4_analysis 
  > 3_models
    > SFINCS (created by scripts in 2_code/2_experiment)
    > CMF
  > 4_results (empty; results from 2_code/4_analysis)
