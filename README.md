# arp-demo
Recipes training data samples upload


## Automatic recipe procesing (arp)

Automatic recipe processing is a microservice pipeline for processing and extracting recipes obtained from images or websites.
For the extraction of relevant recipe information (recipe name, ingredients, description...) Named Entity Recognition (NER) is used. 


### ARP NER Labeling & Training 

![ARP NER Labeling & Training](./docs/ARP_NER_Labeling.drawio.png "ARP in production vs. training")


### Setup

``` 
python -m venv venv/
source venv/bin/activate
pip install .
```

### Development

Start the FastAPI web server in development mode: `uvicorn main:app`

### Request

```json
[
  {
    "id": "image1.png",
    "text": "Käsekuchen\n\n3 Portionen...",
    "ocr": <Text object>   
  },
  ...
]
```

#### Curl

POST requests for uploading files can be done via the following:
`curl --location --request POST 'http://localhost:8080/uploadfiles' --form 'files=@"file1.txt"' --form 'files=@"file2.txt' ...`


#### Browser

Upload files via the UI at `http://localhost:8080/upload`.
