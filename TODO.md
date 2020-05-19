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

tox -r -v -e py37

## push to git and run ci

# Updating to new whisk version
