# post-api
Saves a timestamp into a database.

There are two options to chose from;  
Option_1 launches the application without Kibana for better performance  
on computers with limited resources.

Option_2 launches the application with Kibana, it takes longer to load but  
the database can be accessed using a web browser.

Please note, it might take some time for tha application to be ready  
after having issued the 'vagrant up' command.  

Once vagrant is finished it will take a little while longer for Elasticsearch  
to be ready and significantly more for kibana to be responding.  

However, once the 'api' container is reported to be running it can be  
accessed in a browser or by curl using the following url:  
http://localhost:1080/app  
or curl -XGET http://localhost:1080/app  
Example response: '{"timestamp": "26-08-2018 20:20:11"}'

A post request issued by curl should result in a document with the current  
timestamp in the index called 'eventlog'.

Example post request:
curl -XPOST http://localhost:1080/app  

The response should be the same as a GET request.

To see the documents stored in the datebase you can use kibana (once it's ready) when using option_2   
on the following address:  
http://localhost:8080

Alternatively the following curl command will list all documents stored in the relevant index:  
curl -XGET 'http://localhost:9200/eventlog/_search?pretty=true&q=*'  

When promped for the index pattern, enter 'eventlog'.  
The timestamp documents can then be seen under the discovery tab.
