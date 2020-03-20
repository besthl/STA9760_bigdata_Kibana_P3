from sys import argv
from src.OPCV.getdata import Function
from os import environ
from math import ceil
import datetime

from elasticsearch import Elasticsearch


def create_and_update_index(index_name, doc_type):
    es = Elasticsearch()
    try:
        es.indices.create(index=index_name)
    except Exception:
        pass

    
    return es

def insert(docs, es):
    for doc in docs:
        doc['issue_date'] = datetime.datetime.strptime(
            doc['issue_date'],
            '%m/%d/%Y',
        )
        try:
            doc['amount_due'] = float(doc['amount_due'])
        except KeyError:
            pass
        try:
            doc['fine_amount'] = float(doc['fine_amount'])
        except KeyError:
            pass
        try:
            doc['interest_amount'] = float(doc['interest_amount'])
        except KeyError:
            pass
        try:
            doc['payment_amount'] = float(doc['payment_amount'])
        except KeyError:
            pass
        try:
            doc['penalty_amount'] = float(doc['penalty_amount'])
        except KeyError:
            pass
        try:
            doc['reduction_amount'] = float(doc['reduction_amount'])
        except KeyError:
            pass
        res = es.index(index='violation-parking-index', doc_type='vehicle', body=doc, )
        print('Inserting ....')
        #print(res['result'])    
        #print('\n')

if __name__ == "__main__":
    app_key = environ.get("APP_KEY")
    #es = create_and_update_index('violation-parking-index', 'vehicle')
    #print page_size and num_pages
    page_size_str = argv[1]
    page_size = int(page_size_str.split('=')[1])
    try:
        num_pages_str = argv[2]
        num_pages = int(num_pages_str.split('=')[1])
    except Exception:
        num_pages = None
    
    #print output
    try:
        output = argv[3]

    except Exception:
        output = None
    location = 'nc67-uf89'


    # if the output is es, send data to Elasticsearch 
    with Function(app_key) as function:
		
        es = create_and_update_index('violation-parking-index', 'vehicle')

        if num_pages == 0: 
            total_size = function.get_size(location)
            num_pages = ceil(total_size / page_size)
				
				# extract info
            docs = function.get_info(location, page_size)
            print('Extraction successful\n')
				
				# Load data
            insert(docs, es)
            print('Laoding successful')

				
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
				
				
				
	
