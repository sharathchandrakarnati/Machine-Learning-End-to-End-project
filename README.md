# Machine-Learning-End-to-End-project
### My end to end machine learning end to end project

 ### Software and Account Requriments:
--------------
 1 .[github account]
 2.[heroku account]
 3.[vs code IDE]
 4.[GIT CLI]



Create conda environment 
```

conda create -p venv python==3.10.6 -y
```
Or 

To add files to git 
```
git add.
```

To add single file 
```
git add<file name>
```


> Note: TO ignore file or folder from git we can write name of file /folder in .gitignore file
``` 

To check git status 
```

git status 
```

To check all versions maintained by git 
```
git log
```

To create version/commit all changes 
```
git commit -m "messages
```


To send version /Changes 
```
git push origin main
```
To check url
```
git remote -v
```





To set CI/CD PIPELINE IN HEROKU WE NEED 3 INFORMATION 
1. Heroku_email = sharathchandrakarnati5@gmail.com
2. Heroku_Api_Key = f7ec100a-f0d4-4084-a26b-59a7acab791d
3. Heroku_App_name = app name


 Bulid Docker Image 
'''
docker bulid -t<image_name>:<tagname> .
'''

> Note : Image name of docker must be lowercase 

to list docker image
```
docker images 
```
Run docker image 
```
docker run -p 5000:5000 -e port =5000 44f5936b7ecd


'''
python setup.py install 
'''


install ipykernel 

'''
pip install ipykernel
'''