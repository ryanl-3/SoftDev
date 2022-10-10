"""
Team M3HT: Shinji Kusakabe, Joseph Jeon, Ryan Lee
Softdev
k07 -- teardown
2022-10-03
time spent: 1 hr
"""

from flask import Flask

app = Flask(__name__) # Q0: Where have you seen similar syntax in other langs?

@app.route("/") # Q1: What points of reference do you have for meaning of '/'?
def hello_world():
    print(__name__) # Q2: Where will this print to? Q3: What will it print?
    return "No hablo queso!"  # Q4: Will this appear anywhere? How u know?

app.run()  # Q5: Where have you seen similar constructs in other languages?


'''
DISCO:
- "No hablo queso" prints on a website
QCC:
0. I have not seen this syntax before
1. Referencing files
2. In the terminal
3. name
4. No because it is returned not printed
5. Processing
...
INVESTIGATIVE APPROACH:
<Your concise summary of how
 you and your team set about
 "illuminating the cave of ignorance" here...>
 We combined our knowledge to attempt to answer the qccs
'''