
users = [8, 7, 1, 2]
res_duration = {}
equipment = {}
for i in users_details:
    res(user[i])+= res_duration
    equipment(user[i]) = equipment + equipment(user[i])


#pyspark

df2 = df.groupBy(User).agg(sum(duration)). 
     withColmun('Equipment', equipment)




RAG :

1. Ingestion -->  document AI search -> chunking -> embeding --> Weaviate 
2. Retrieval --> USer query--> Hbyrid (Semanti+keyword) --> LLM() --> Evalution 

1. Fastapi -> react -> ACA  


import Langchain.embedding 
import pyPDFLoader
import Lagnchains.chunking
from weaviatAPI imnport weviated
From AzureOpenAI import openAI 
import NLTK

API_token  = ""
API_URI =  "http"


get_api = callapi(API_token, api_uri)

doc = pypdf(API)

preprocesses = preprocess(doc)

chunking = Langchain.recursivetextsplitter(preprocessed)


weaviate.load(chunk)


----------

user = "" \"

users_embedding = openAI(model="text-embedding-3-mini")
       
data = weaviate.retreive(user_embedding)

#UserEmbedding+data 
context = "Act as Reseearcher"
response  = model.generate(model="gpt-4o-minin", USer+Retreived)



# ------------------------



















