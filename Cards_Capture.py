import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    # Define the file path
    file_path = os.path.expanduser("~/Desktop/QandQJava/QandAjava.txt")

    # Define the output file path
    output_file_path = os.path.expanduser("~/Desktop/output.txt")

    # open the file
    with open(file_path) as f:
        content = f.readlines()

    # initialize the dictionary
    qa_dict = {}

    # loop through the lines of the file and extract the questions and answers
    for i, line in enumerate(content):
        if line.startswith('=== Question: "'):
            question = line.replace('=== Question: "', '').rstrip('"\n')
            answer = content[i + 1].replace('Answer: "', '').rstrip('"\n')
            qa_dict[question] = answer

    # open the output file in write mode








    with open(output_file_path, "w") as f:
        # write the dictionary to the output file
        for key, value in qa_dict.items():
            f.write(key + "\n")
            f.write(value + "\n")
            f.write("===============================\n")

    data = qa_dict
    return render_template('Front_End_Module.html', data=data)

if __name__ == '__main__':
    app.run(debug=True)