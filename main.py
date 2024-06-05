# pip install transformers torch      /////  torch-159 mb ... transformers - 10 mb ...  mkl-2021.4.0-py2.py3-none-win_amd64.whl - 228 mb ..


from llama_interaction import interact_with_llama

if __name__ == "__main__":
    employee_id = input("Enter Employee ID: ")
    interact_with_llama(employee_id)
