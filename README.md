## Initializing Machine Learning Project
## Software and account Requirement
1. [Github Account](https://github.com/)
2. [Heroku Account](https://www.heroku.com/)
3. [VS code IDE](https://code.visualstudio.com/)
4. [GIT cli](https://git-scm.com/)

## Create a Virtual Environment
```
conda create -p venv python==3.7 -y

```
To Active the conda venv environment 
```
conda activate venv/
```
Or
```
source activate venv/

```
To download and install required package
```
pip install -r requirements.txt

```
To add file to git 
```
git add .
```
Or
```
git add filename
```
> Note : Ignore the file/folder  to git write the name of file/folder in .gitignore

To check the status 
```
git status
```
To create commit all changes by git
```
git commit -m "any message"

```
To check all version maintain by git
```
git log

```
To send changes to Github
```
git push origin main
```
To check remote url of Github repo
```
git remote -v
```

To set up CD/CI pipline in heroko 
1. heroko_email = khanabdulaziz532@gmail.com
2. heroko_API_KEY = <>
3. heroko_APP_NAME = abdul-machine-project

BUILD DOCKER IMAGE
```
docker build -t <image_name>:<tag_name> .
```
> Note : Docker image must be in lower case

```
python setup.py install
```
and this will install all the packages automatically 

To install ipykernel 
```
pip install ipykernel
```