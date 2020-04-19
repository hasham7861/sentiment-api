# sentiment-api
A simple sentiment api made in flask

## To run the app locally
1. Get into the flask environment `source virt/bin/activate`
2. Install all dep `pip install -r requirements.txt`
3. Running it on local server `python application.py` 

## Important Steps before deploying to ec2 instance:
1. Name your flask envirnoment virt
2. Make sure the main server code is in application.py
3. Freeze your dep `pip freeze`
4. Make sure your dep are up to date `pip freeze > requirements.txt`
5. Create a zip concluding of application.py vert/ requirements.txt
6. Upload the same zip file to Elastic Bean