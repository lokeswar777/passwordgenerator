from flask import Flask, render_template, request
import random
import itertools

app = Flask(__name__)

# Character arrays similar to the ones in your Python script
lows = [chr(x) for x in range(97, 123)]
highs = [chr(x) for x in range(65, 91)]
nums = [str(x) for x in range(0, 10)]
spl = [chr(x) for x in range(33, 48)]

def generate_password(n, l, c, s, n_n):
    l = [random.choice(lows) for _ in range(l)]
    c = [random.choice(highs) for _ in range(c)]
    s = [random.choice(spl) for _ in range(s)]
    nums_g = [random.choice(nums) for _ in range(n_n)]
    res = list(itertools.chain(l, c, s, nums_g))
    random.shuffle(res)
    return "".join(res)

@app.route('/', methods=['GET', 'POST'])
def index():
    password = ""
    if request.method == 'POST':
        min_length = int(request.form['minLength'])
        small_letters = int(request.form['smallLetters'])
        capitals = int(request.form['capitals'])
        special_chars = int(request.form['specialChars'])
        numbers = int(request.form['numbers'])

        if min_length >(small_letters + capitals + special_chars + numbers):
            password = "Error: Minimum length is less than the sum of all character types."
        else:
            password = generate_password(min_length, small_letters, capitals, special_chars, numbers)
    
    return render_template('home.html', password=password)

if __name__ == '__main__':
    app.run(debug=True)
