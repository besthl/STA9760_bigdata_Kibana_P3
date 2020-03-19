from sys import argv
from src.OPCV.getdata import Function
from os import environ
from math import ceil
from elasticsearch import Elasticsearch
from sodapy import Socrata

def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass
    return es

def insert(docs, es):
    for doc in docs:
        res = es.index(index='violation-parking-index', doc_type='vehicle', body=doc, )
        #print('Inserting ....')
        print(res['result'])    
        #print('\n')

if __name__ == "__main__":
    app_key = 'gOC80zDpmRj2bjooeYI5HMKVO'    

    es = create_and_update_index('violation-parking-index', 'vehicle')
    #print page_size and num_pages
    page_size_str = argv[1]
    page_size = int(page_size_str.split('=')[1])
    try:
        num_pages_str = argv[2]
        num_pages = int(num_pages_str.split('=')[1])
    except Exception:
        num_pages = None  
   
    
    es = Elasticsearch()
    location = 'nc67-uf89'


    # if the output is es, send data to Elasticsearch 
    with Function(app_key) as function:
        #es = create_and_update_index('violation-parking-index', 'vehicle')
        if num_pages is None: 
            	
			# extract info
            docs = function.get_info(location, page_size)
            print('Extraction successful\n')
				
				# Load data
            insert(docs, es)
            print('Laoding successful\n')

				
        else:
            total_size = function.get_size(location)
            # print(f"total_size={total_size}")	
            docs = function.get_info(location, page_size)
            insert(docs, es)
            for i in range(num_pages):    
                docs = function.get_info(location, page_size, offset=i*num_pages)
                print(docs)	
                print('Extraction successful\n')
			    # Load data
                insert(docs, es)
                print('Laoding successful\n')

            print (f'num_pages = {num_pages}')
            print (f'page_size = {page_size}')
            print('Loading to ES')
            h = input("Press 'Enter' to continue...")				
				
			