"""A procedure to setup local wanted files in CONP mode."""

import sys
import os.path as op
from datalad.distribution.dataset import require_dataset
from datalad.utils import create_tree

GROUP_NAME='conp'

ds = require_dataset(
    sys.argv[1],
    check_installed=True,
    purpose='setup CONP mode',
)

def set_group_wanted(subds, group_name=GROUP_NAME):
    subds.repo.set_preferred_content('group', group_name, remote='here')
    subds.repo.set_preferred_content('wanted', 'groupwanted', remote='here')

set_group_wanted(ds)
for submod in ds.repo.get_submodules():
    sub_ds = require_dataset(
        submod["path"],
        check_installed=True,
        purpose='setup CONP mode',
    )
    set_group_wanted(sub_ds)
