from flask import Flask, request, jsonify, render_template
from llama_model import generate_response
import pandas as pd
import os

app = Flask(__name__)

# EC2 üzerindeki verilerinize erişim sağlayacak fonksiyon
def get_all_data_from_ec2():
    # Tüm CSV dosyalarını okuyarak birleştirin
    directory = '/home/ubuntu'  # EC2 üzerindeki gerçek veri yolu
    all_data = []
    for filename in os.listdir(directory):
        if filename.endswith(".csv"):
            file_path = os.path.join(directory, filename)
            df = pd.read_csv(file_path)
            all_data.append(df)
    combined_df = pd.concat(all_data, ignore_index=True)
    return combined_df

# Verileri işleme fonksiyonu
def process_query(query):
    df = get_all_data_from_ec2()

    if 'performance score' in query.lower():
        result = df.to_dict(orient='records')
        return result
    elif 'department' in query.lower():
        department = query.split("department ")[-1]
        result = df[df['Department'].str.contains(department, case=False)].to_dict(orient='records')
        return result
    elif 'employee' in query.lower():
        employee_name = query.split("employee ")[-1]
        result = df[df['Name'].str.contains(employee_name, case=False)].to_dict(orient='records')
        return result
    else:
        # Genel sorular için modeli kullanma
        prompt = query
        response = generate_response(prompt)
        return response

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/query', methods=['POST'])
def query():
    try:
        data = request.json
        query = data.get('query', '')
        response = process_query(query)
        app.logger.info('Query: %s', query)
        app.logger.info('Response: %s', response)
        return jsonify(response)
    except Exception as e:
        app.logger.error('Error processing query: %s', e)
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
