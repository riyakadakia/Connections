from flask import Flask, render_template, request, jsonify
import random

app = Flask(__name__)


@app.route('/')
def index():
  create_matrix()
  data = randomize_matrix()
  return render_template('front-end.html', data=data)


class Word:

  def __init__(self, word, group, button_clicked):
    self.word = word
    self.group = group
    self.clicked = button_clicked


def create_matrix():
  global matrix
  matrix = []
  word1 = Word("Global Warming", 1, False)
  word2 = Word("Pollution", 1, False)
  word3 = Word("Waste Disposal", 1, False)
  word4 = Word("Climate Change", 1, False)

  word5 = Word("Microsoft", 2, False)
  word6 = Word("Bank of America", 2, False)
  word7 = Word("IBM", 2, False)
  word8 = Word("Accenture", 2, False)

  word9 = Word("Walmart", 3, False)
  word10 = Word("Zara", 3, False)
  word11 = Word("IKEA", 3, False)
  word12 = Word("Starbucks", 3, False)

  word13 = Word("Cardboard", 4, False)
  word14 = Word("Plastic Bottles", 4, False)
  word15 = Word("Glass", 4, False)
  word16 = Word("Steel", 4, False)

  matrix.append(word1)
  matrix.append(word2)
  matrix.append(word3)
  matrix.append(word4)
  matrix.append(word5)
  matrix.append(word6)
  matrix.append(word7)
  matrix.append(word8)
  matrix.append(word9)
  matrix.append(word10)
  matrix.append(word11)
  matrix.append(word12)
  matrix.append(word13)
  matrix.append(word14)
  matrix.append(word15)
  matrix.append(word16)
  
  return 0


def randomize_matrix():
  random.shuffle(matrix)
  print("------------------------------")
  print(matrix[0].word)
  return matrix
  
@app.route('/button_clicked', methods=['POST'])
def button_clicked():
  # Handle the backend logic here
  # For example, you could print a message
  data = request.json
  value_received = data.get('value')
  if matrix[int(value_received)-1].clicked is True:
    matrix[int(value_received)-1].clicked = False
  else:
    matrix[int(value_received)-1].clicked = True
  print("value:")
  print(value_received)
  return jsonify({'message': value_received})

@app.route('/submitted', methods=['POST'])
def submitted():
  # Handle the backend logic here
  # For example, you could print a message\
  selected = []
  result=-1
  for x in range(16):
    if(matrix[x].clicked is True):
      selected.append(x)

  if len(selected) != 4:
    result=2
    return jsonify({'result': result, 'selected': selected})
  for x in range(len(selected)):
    matrix[selected[x]].clicked = False
    #"Please select 4 words"
  print('group numbers')
  print(matrix[selected[0]].group)
  print(matrix[selected[1]].group)
  print(matrix[selected[2]].group)
  print(matrix[selected[3]].group)
  if matrix[selected[0]].group == matrix[selected[1]].group \
  and matrix[selected[1]].group == matrix[selected[2]].group \
  and matrix[selected[2]].group == matrix[selected[3]].group:
    result=1
  else:
    result=0
  print('exiting submit loop result=')
  print(result)
  return jsonify({'result': result, 'selected': selected, 'group': matrix[selected[0]].group})
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000, debug=True)
