# [Courtois NeuroMod - Raw data](https://www.cneuromod.ca/)

## Overview

The Courtois project on Neural Modelling (["Courtois NeuroMod"](https://www.cneuromod.ca/)) is a dense fMRI database that is being collected on 6 subjects since 2018.  Subjects are scanned regularly, up to several times a week, using the 3T Siemens PrismaFit scanner (64-channel head-neck coil, accelerated simultaneous multi-slice, gradient echo-planar imaging sequence) and both naturalistic and controlled stimuli from a broad range of cognitive domains. The aim of the Courtois Neuromod Project is to train artificial neural networks using extensive experimental data on individual human brain activity and behaviour.

## Participants

In an effort to accelerate discovery through Citizen Science, participants 01, 03, and 05 in the Courtois NeuroMod project have decided and consented to openly share their data with the scientific community to advance research at the interface of neuroscience and artificial intelligence.

Data for all 6 subjects in Courtois NeuroMod project are accessible through registered access and institutional data transfer agreement. For more information please visit our [homepage](https://www.cneuromod.ca/).

## Datasets

Datasets will be updated with each new CNeuroMod data release. This dataset contains the Courtois NeuroMod raw data but [preprocessed data derivatives](https://github.com/courtois-neuromod/cneuromod.processed) (including from the fMRIprep LTS pipeline) are also available for the same three participants in [this dataset](). ​Details on sequences, processing workflow, and datasets can be found in the [Courtois Neuromod documentation](http://docs.cneuromod.ca/).

## License

The CNeuroMod data and derivatives of these data provided by the CNeuroMod team (e.g., preprocessed data listed above) are shared under a [CC0 license](https://creativecommons.org/publicdomain/zero/1.0/legalcode) that is owned by the CNeuroMod team and the participants listed above. 

## Team and funding

The Courtois NeuroMod project is lead by a team based at the [Centre de Recherche de l’institut Universitaire de Gériatrie de Montréal](https://criugm.qc.ca/en/) (CRIUGM) and the University of Montreal. The project benefits from key collaborations with teams from around the world. For a full list of contributors please see [this page](https://docs.cneuromod.ca/en/latest/AUTHORS.html).

The project is made possible by a generous donation by the Courtois Foundation to [Pierre Bellec](https://simexp.github.io/lab-website/).

## How to cite

We kindly ask that all publications using CNeuroMod datasets include the following paragraph in their acknowledgement section:

The Courtois project on neural modelling was made possible by a generous donation from the Courtois foundation, administered by the Fondation Institut Gériatrie Montréal at CIUSSS du Centre-Sud-de-l’île-de-Montréal and  the University of Montreal. The Courtois NeuroMod team is based at “Centre de Recherche de l’Institut Universitaire de Gériatrie de Montréal”, with several other institutions involved. See the CNeuroMod documentation for an up-to-date list of contributors (https://docs.cneuromod.ca).

## Known issues

As this is an alpha release of this dataset, we ask that users keep a couple of points in mind:

1) Some of the data included in this dataset require a GitHub SSH key to download. Instructions on generating and using SSH keys for GitHub can be found on [this page of the GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).

2) In order to track provenance, some sub-directories in this dataset include links to other directories. Right now, the overall structure of these links does not permit recursive installation of the entire dataset using the `datalad install -r` command. **It is therefore recommended** that users install the dataset as described below (in the "Download Using DataLad" section of this page) and then enter directories of interest and execute `datalad get` to fetch specific files. Please [contact the CONP Portal team](https://portal.conp.ca/contact_us) concerning download failures or to sign up for notification of upcoming updates that we expect will resolve these problems.
