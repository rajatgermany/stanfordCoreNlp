from stanfordcorenlp import StanfordCoreNLP
import json 

nlp = StanfordCoreNLP(r'./stanford-corenlp-full-2018-02-27')
props = {'annotators': 'coref, ssplit', 'pipelineLanguage': 'en'}

sentences = []
j = []
coref_data = []

def buildCoref (file_index):
    file_name = 'textData' + file_index + '.txt'
    coref_file_name = 'coref'+ file_index + '.json'

    with open(file_name, 'r') as file:
        answer = []
        for line in file:
            if 'start question' in line: 
                print('it hits here')
                index = 1
                j = []
                continue
        
            elif 'end question' in line:
                index = 0  
                coref_data.append({label: j, 'question': question})
                continue

            elif index == 1 :
                print('line', line)
                label = line.rstrip()
                index = 2
                continue
        
            elif index == 2:
                question = line
                question = question.rstrip()
                question = question + ' .'
                index = 0
                continue
        
        
            line = line.rstrip()       
            print('question', question)
            sentence = ' '.join([question, line])
            print('sentence', sentence)
            result =  nlp.annotate( sentence, properties=
                    {
                        'timeout': '10000000',
                        'annotators': 'coref',
                        'outputFormat': 'json'
                    })          

            result = json.loads(result)
        
            q = []
            for key, value in result['corefs'].items():
                print(value)
                u = []
                for i in value:
                    u.append({'text': i['text'], 'position': i['position']})
                q.append(u)
            
            j.append(q)
            

    with open(coref_file_name, 'w') as q:
        json.dump(coref_data,  q)
        



