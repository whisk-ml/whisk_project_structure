# Testing a whisk branch:

git checkout -b <whisk-branch>

## update requirements.txt with url to archive

https://github.com/whisk-ml/whisk/archive/whisk-branch.zip

## update setup.py:

install_requires=[
      'whisk==0.1.29'
  ],

'whisk @ https://github.com/whisk-ml/whisk/archive/whisk-branch.zip'

## .circleci/config.yml:

pip install -U https://github.com/whisk-ml/whisk/archive/whisk-branch.zip

## run tox with re-created env

pytest
tox -r -v -e py37

## push to git and run ci

# Updating to new whisk version

## update requirements.txt version

## update setup version

## update circleci version

pip uninstall -y whisk
pip install -r requirements.txt

pytest
tox -r -v -e py37

# Testing a full build

git checkout -b dir-under-module-name
rm -r *

From local whisk source:

rm ~/Desktop/whisk.log
whisk --log-file ~/Desktop/whisk.log create --force -o ~/projects/whisk_examples/ whisk_project_structure
