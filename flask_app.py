
# A very simple Flask Hello World app for you to get started with...

from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask!'

# Make the user give you the team email
# Keep them guessing till they get it right

print('Hello games day!')
teamemail = 'data-support@ed.ac.uk'
# print(teamemail)
print('Can you tell me the contact address for the Research Data Service?')
answer = ''
while answer != teamemail :
    answer = input()
    if ( answer == teamemail ):
        print('Yay! Well done.')
    else:
        print('Sorry, please try again. You can find the email address on the University website.')
