from flask import Flask, request, jsonify, render_template
import pandas as pd
import os
import logging

app = Flask(__name__)

# Loglama ayarları
logging.basicConfig(level=logging.INFO)

# CSV dosyasının yolu
EMPLOYEE_CSV = '/home/ubuntu/employees.csv'

# Ana sayfa route'u
@app.route('/')
def index():
    return render_template('index.html')

# Çalışan ekleme route'u
@app.route('/add_employee', methods=['POST'])
def add_employee():
    try:
        name = request.form['name']
        department = request.form['department']
        role = request.form['role']
        app.logger.info(f"Received data: name={name}, department={department}, role={role}")
        
        # CSV dosyasını okuyun
        if os.path.exists(EMPLOYEE_CSV):
            df = pd.read_csv(EMPLOYEE_CSV)
        else:
            df = pd.DataFrame(columns=['EmployeeID', 'Name', 'Department', 'Role', 'Email', 'Phone', 'HireDate', 'VacationDays', 'SickDays', 'PerformanceScore'])
        
        # Yeni EmployeeID'yi hesaplayın
        if not df.empty:
            new_employee_id = df['EmployeeID'].max() + 1
        else:
            new_employee_id = 1
        
        # Yeni çalışan verisini oluşturun
        new_employee = pd.DataFrame([{
            'EmployeeID': new_employee_id,
            'Name': name,
            'Department': department,
            'Role': role,
            'Email': '',  # Varsayılan boş değerler
            'Phone': '',
            'HireDate': '',
            'VacationDays': 0,
            'SickDays': 0,
            'PerformanceScore': 0
        }])
        
        # Yeni çalışanı DataFrame'e ekleyin
        df = pd.concat([df, new_employee], ignore_index=True)
        
        # CSV dosyasını güncelleyin
        df.to_csv(EMPLOYEE_CSV, index=False)
        
        return jsonify({"message": "Employee added successfully", "employee": new_employee.to_dict(orient='records')[0]})
    except Exception as e:
        app.logger.error(f"Error adding employee: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
