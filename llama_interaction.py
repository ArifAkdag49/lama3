from data_loader import get_employee_data
from llama_model import generate_response

def interact_with_llama(employee_id):
    employee_data = get_employee_data(employee_id)
    if employee_data:
        prompt = f"Provide performance analysis for the following employee data: {employee_data}"
        response = generate_response(prompt)
        print(response)
    else:
        print("Employee not found.")

# Örnek kullanım
if __name__ == "__main__":
    interact_with_llama('1')
