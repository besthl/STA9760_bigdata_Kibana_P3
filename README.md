# This is for STA9760_Bigdata_Project 1 Part 3 Kibana
In this third part, we will stand up an instance of Kibana on top of your ElasticSearch instance in order to visualize and analyze our dataset.

![Plot](screenshots/updatedGraphs.png)
Start:
export APP_KEY={MY_TOKEN}

docker-compose up -d


This will start ElasticSearch and Kibana.

ElasticSearch: http://localhost:9200 Kibana: http://localhost:5601


Running python:


docker-compose run pyth python parking.py --page_size=10000 --num_pages=400


export curl output:

curl -X GET {localhost:9200/parking-violation-index} > output.txt


Shutting off:

docker-compose down


