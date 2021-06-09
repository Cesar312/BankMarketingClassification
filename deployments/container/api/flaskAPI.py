from flask import Flask, request
from flasgger import Swagger
import pickle5 as pickle
import pandas as pd
from sklearn.preprocessing import StandardScaler

# load model from PKL file 
model_file = '../SVC-model/model.pkl'

with open(model_file,'rb') as file:
  prediction_model = pickle.load(file)

app = Flask(__name__)

# enable this app for swagger and it will auto generate UI
swagger = Swagger(app)


@app.route('/svc_model_file', methods=['POST'])
def detection_file():
    # BELOW docstring lines are required to support swagger documentation
    """ Endpoint returning Banking Marketing Classification prediction
    ---
    parameters:
        - name: input_file
          in: formData
          type: file
          required: true
    """
    columns = ['duration',
     'pdays',
     'previous',
     'emp.var.rate',
     'euribor3m',
     'nr.employed']
     
    data_df = pd.read_csv(request.files["input_file"])
    data_df = data_df[columns]
    print('~~~~~~~~~~ DataFrame for Prediction: ~~~~~~~~~~\n\n', data_df)
    print('\n')
    
    ss = StandardScaler()
    data_ss = ss.fit_transform(data_df)

    # predictions = []
    predictions = prediction_model.predict(data_ss)

    results = []
    
    for i in predictions:
        if i == 1:
            results.append('Yes')
        else:
            results.append('No')

    print(f'Prediction: {results}')
    print('\n')
    
    # print(f'Prediction: {result}')
    # print('\n')
    # return result
    
    return str(results)

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
