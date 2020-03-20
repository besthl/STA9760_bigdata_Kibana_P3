# STA9760_bigdata Part 3 

![scrnshot](https://raw.githubusercontent.com/besthl/STA9760_bigdata_P3_Kibana/master/screenshot.PNG)
Start:

docker-compose up -d


This will start ElasticSearch and Kibana.

ElasticSearch: http://localhost:9200 Kibana: http://localhost:5601


Running python:


docker-compose run pyth python parking.py --page_size=12000 --num_pages=400


export curl output:

curl -X GET {localhost:9200/parking-violation-index} > output.txt


Shutting off:

docker-compose down
