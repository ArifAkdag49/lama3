from flask import Flask, request, jsonify
import pandas as pd

app = Flask(__name__)

# Verileri yükleme
df = pd.read_csv('/home/ubuntu/training_data.csv')

# Verileri işleme fonksiyonu
def process_query(query):
    # Örnek sorgu işleme - Performans skorlarını gösterme
    if 'performance score' in query.lower():
        result = df[['text']].to_dict(orient='records')
        return result
    else:
        return "Query not recognized."

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query = data.get('query', '')
    response = process_query(query)
    return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
