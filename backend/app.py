import os
import pickle

from markupsafe import escape
from . import constants
from flask import Flask, send_from_directory, request, jsonify

from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings

from huggingface_hub import login
login("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")


app = Flask(__name__)

@app.after_request
def after_request(response):
  response.headers.add('Access-Control-Allow-Origin', '*')
  response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
  response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
  return response

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')


@app.route('/prompt', methods=['POST'])
def generate_prompt():
  req = request.json
  question = req['question']
  
  document_data = find_documents(question)
  abstracts = get_abstracts(document_data)
  
  prompt = create_prompt(question, abstracts)
  
  return jsonify({'prompt' : prompt})
  
  
@app.route('/documents', methods=['GET'])
def get_docs():
  question = "What factors controls the ability of palladium cathods to attain high loading levels?"
  document_data = find_documents(question)
  abstracts = get_abstracts(document_data)
  
  prompt = create_prompt(question, abstracts)
  return jsonify({'prompt' : prompt})

# @app.route("/data", methods=['POST'])
# def data():
#     server = constants.app_constant['cpp_server']
#     url = server + "/completion"
    
#     prompt_text = request.json['prompt']
#     print(prompt_text)
#     data =  {
#         "prompt": prompt_text,
#         "n_predict": 1024,
#         "stream": True
#     }
#     headers = {'Content-type': 'application/json'}
#     response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)
    
#     def stream():
#         for chunk in response.iter_content(chunk_size=10):
#             print(chunk)
#             yield chunk

#     return stream()


def find_documents(question):

  persist_directory = constants.app_constant['persist_directory']
  embedding_model = constants.app_constant['embedding_model']
  dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', persist_directory))
  embeddings = HuggingFaceEmbeddings(model_name=embedding_model)
  vector_db = Chroma(persist_directory=dir, embedding_function=embeddings)
  result_docs = vector_db.similarity_search(question, k=10)

  docs = []
  doc_count = 0
  for doc in result_docs:
    obj = {
      'page_content' : doc.page_content,
      'metadata': doc.metadata
    }
    docs.append(obj)
    doc_count += 1
  
  data = {
    'doc_count': doc_count,
    'documents': docs
  }
  
  return data

def get_abstracts(document_data):
  candidates = {}
  for doc in document_data['documents']:
      md = (doc['metadata'])
      candidates[md['doc_id']] = 1
  
  dir = os.path.abspath(os.path.join(os.path.dirname( __file__ ), '..', 'src', 'abstracts.pkl'))
  with open(dir, 'rb') as file:
    abstracts = pickle.load(file)
  
  candidate_abstracts = ""
  for id in candidates:
    candidate_abstracts += f"\n doc{id}.pdf: {abstracts[id - 1][0:300]};"
  
  return candidate_abstracts


def create_prompt(question, abstracts):
  prompt = f""" [INST] You are a recommendation system which recommends papers based on search. Given below are the following.
    1. The prompt from user 
    2. The candidate papers and its incomplete abstract seperated by semicolon.
    Give recommendation of top 3 papers and insights about these candidates for future research.
    User prompt: {question} 
    Candidates: {abstracts} 
    [/INST]
    """
  return prompt