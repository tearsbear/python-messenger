from flask import Flask, request, Response
# from flask_ngrok import run_with_ngrok
from fbmessenger import elements, templates
from importlib_metadata import re
import requests, json, random, os
app = Flask(__name__)
# run_with_ngrok(app)

# verify token goes here
VERIFY_TOKEN = ''

# access token goes here
PAGE_ACCESS_TOKEN = ''

#Function to access the Sender API
def callSendAPI(user_id, user_message):

    print(user_message, '--getmessage')

    if user_message.lower() == 'website':
            response = {
                'recipient': {'id': user_id},
                'message': {
                    'attachment': {
                        'type': 'template',
                        'payload': {
                           'template_type': 'generic',
                           'elements':[{
                                'title':'Google',
                                'subtitle':'search engine',
                                'buttons': [
                                    {
                                    'type': 'web_url',
                                    'url': 'https://google.co.id',
                                    'title': 'Visit now'
                                    }                             
                                ]
                            }]
                        }
                    }
                }
            }
    elif user_message.lower() in ['hi', 'hello', 'halo', 'helo', 'hai', 'hey', 'hola']:
            response = {
                'recipient': {'id': user_id},
                'messaging_type': 'RESPONSE',
                'message': {
                    'text': 'Selamat datang di chatbot pintar. Silakan pilih:',
                    'quick_replies': [
                        {
                            'content_type': 'text',
                            'title': 'Kuliah',
                            'payload': 'Kuliah'
                        },{
                            'content_type': 'text',
                            'title': 'Kursus',
                            'payload': 'Kursus'
                        },{
                            'content_type': 'text',
                            'title': 'Kartu Prakerja',
                            'payload': 'Kartu Prakerja'
                        }
                    ]
                }
            }
    elif user_message.lower() == 'quicks':
            response = {
                'recipient': {'id': user_id},
                'messaging_type': 'RESPONSE',
                'message': {
                    'text': 'Selamat datang di chatbot pintar. Silakan pilih:',
                    'quick_replies': [
                        {
                            'content_type': 'text',
                            'title': 'Kuliah',
                            'payload': 'Kuliah'
                        },{
                            'content_type': 'text',
                            'title': 'Kursus',
                            'payload': 'Kursus'
                        },{
                            'content_type': 'text',
                            'title': 'Kartu Prakerja',
                            'payload': 'Kartu Prakerja'
                        }
                    ]
                }
            }
    elif user_message.lower() in ['iphone 13 mini ready?', 'iphone 13 mini ready ?', 'iPhone 13 mini ready?', 'iPhone 13 mini ready?', 'iphone 13 mini', 'iPhone 13 Mini']:
            response = {
                'recipient': {'id': user_id},
                'message': {
                    'attachment': {
                        'type': 'template',
                        'payload': {
                            'template_type': 'generic',
                            'elements':[{
                                'title':'iPhone 13 Mini',
                                'image_url':'https://images.tokopedia.net/img/cache/500-square/VqbcmM/2021/9/26/b19ac4ba-2101-4b7d-ac56-82d009f926dd.jpg',
                                'subtitle':'iPhone 13 Mini 512GB 256GB 128GB Resmi IBOX',
                                'buttons': [
                                    {
                                    'type': 'web_url',
                                    'url': 'https://www.tokopedia.com/tokomiracle-1/iphone-13-mini-512gb-256gb-128gb-5-4-dual-nano-single-resmi-ibox-midnight-128gb-single',
                                    'title': 'Buy now'
                                    }                            
                                ]
                            }]
                        }
                    }
                }
            }
    elif user_message.lower() in ['iphone', 'iphone?', 'iphone ?', 'iPhone', 'iPhone?', 'iPhone ?']:
            response = {
                'recipient': {'id': user_id},
                'message': {
                    'attachment': {
                        'type': 'template',
                        'payload': {
                            'template_type': 'generic',
                            'elements':[
                                {
                                    'title':'iPhone 13 Mini',
                                    'image_url':'https://images.tokopedia.net/img/cache/500-square/VqbcmM/2021/9/26/b19ac4ba-2101-4b7d-ac56-82d009f926dd.jpg',
                                    'subtitle':'iPhone 13 Mini 512GB 256GB 128GB Resmi IBOX',
                                    'buttons': [
                                        {
                                        'type': 'web_url',
                                        'url': 'https://www.tokopedia.com/tokomiracle-1/iphone-13-mini-512gb-256gb-128gb-5-4-dual-nano-single-resmi-ibox-midnight-128gb-single',
                                        'title': 'Buy now'
                                        }                            
                                    ]
                                },
                                {
                                    'title':'iPhone 13 Pro',
                                    'image_url':'https://images.tokopedia.net/img/cache/500-square/VqbcmM/2021/10/1/d6d9c33d-e7a7-4931-b158-58eaead60b1b.jpg',
                                    'subtitle':'iPhone 13 Pro 512GB 256GB 128GB Resmi IBOX',
                                    'buttons': [
                                        {
                                        'type': 'web_url',
                                        'url': 'https://www.tokopedia.com/apple-tree/iphone-13-pro-256gb-singlesim-nano-import-resmi',
                                        'title': 'Buy now'
                                        }                            
                                    ]
                                },
                                {
                                    'title':'iPhone 13 Pro Max Sierra Blue',
                                    'image_url':'https://images.tokopedia.net/img/cache/500-square/VqbcmM/2021/9/15/36ca8a0b-303b-44a2-b212-7463021a65cc.png',
                                    'subtitle':'iPhone 13 Pro Max Sierra Blue, 256GB Resmi IBOX',
                                    'buttons': [
                                        {
                                        'type': 'web_url',
                                        'url': 'https://www.tokopedia.com/apple-tree/iphone-13-pro-max-256gb-dualsim-nano-import-resmi',
                                        'title': 'Buy now'
                                        }                            
                                    ]
                                }
                            ]
                        }
                    }
                }
            }
    elif user_message.lower() == 'heart':
            response = {
                'recipient': {'id': user_id},
                'message': {
                    'attachment':{
                        'type':'like_heart'
                    }
                }
            }
    elif user_message.lower() == 'phone':
            response = {
                'recipient': {'id': user_id},
                'message': {
                    'attachment':{
                        'type':'template',
                        'payload':{
                            'template_type':'generic',
                            'text':'Need further assistance? Talk to a representative',
                            'buttons':[
                                {
                                    'type':'phone_number',
                                    'title':'Call Representative',
                                    'payload':'+628976203842'
                                }
                            ]
                        }
                    }
                }
            }
    elif user_message == 'Kuliah':
            response = {
                'recipient': {'id': user_id},
                'message': {
                    'attachment': {
                        'type': 'template',
                        'payload': {
                        'template_type': 'generic',
                        'elements':[{
                                'title':'Pintaria Kuliah',
                                'subtitle':'Pilihan Program Kuliah',
                                'buttons': [
                                    {
                                    'type': 'web_url',
                                    'url': 'https://pintaria.com/kuliah-online',
                                    'title': 'Visit now'
                                    }                             
                                ]
                            }]
                        }
                    }
                }                
            }
    elif user_message == 'Kursus':
            response = {
                'recipient': {'id': user_id},
                'message': {
                    'attachment': {
                        'type': 'template',
                        'payload': {
                        'template_type': 'generic',
                        'elements':[{
                                'title':'Pintaria Kursus',
                                'subtitle':'Pilihan Program Kursus',
                                'buttons': [
                                    {
                                    'type': 'web_url',
                                    'url': 'https://pintaria.com/semua-kursus',
                                    'title': 'Visit now'
                                    }                             
                                ]
                            }]
                        }
                    }
                }                
            }
    elif user_message == 'Kartu Prakerja':
            response = {
                'recipient': {'id': user_id},
                'message': {
                    'attachment': {
                        'type': 'template',
                        'payload': {
                        'template_type': 'generic',
                        'elements':[{
                                'title':'Pintaria Kartu Prakerja',
                                'subtitle':'Login/Register',
                                'buttons': [
                                    {
                                    'type': 'web_url',
                                    'url': 'https://pintaria.com/kartuprakerja',
                                    'title': 'Visit now'
                                    }                             
                                ]
                            }]
                        }
                    }
                }                
            }
    elif user_message.lower() == 'media':
            response = {
                'recipient': {'id': user_id},
                'message': {'text': 'This chatbot only accepts text messages'}
            }
    else:
            response = {
                'recipient': {'id': user_id},
                'message': {'text': 'Sorry, I am still learning!'}
            }

    headers = {'content-type': 'application/json'}

    url = 'https://graph.facebook.com/v12.0/me/messages?access_token={}'.format(PAGE_ACCESS_TOKEN)
    r = requests.post(url, json=response, headers=headers)
    print(r.text)


#Function for handling a message from MESSENGER
def handleMessage(senderPsid, receivedMessage):
    #check if received message contains text
    print('We entered the HANDLE MESSAGE FUNCTION')
    if 'text' in receivedMessage:
        print('TEXT does exist in the RECEIVER MESSAGE')

        response = receivedMessage['text']

        print(senderPsid, '--- id_user log')
        print(response, '--- text log')
        callSendAPI(senderPsid, response)
    else:
        response = 'media'
        print(response, '--- not text log')
        callSendAPI(senderPsid, response)

@app.route('/webhook', methods=["GET", "POST"])
def webhook_verify():
    if request.method == 'GET':
        #do something.....

        if 'hub.mode' in request.args:
            mode = request.args.get('hub.mode')
            print(mode)
        if 'hub.verify_token' in request.args:
            token = request.args.get('hub.verify_token')
            print(token)
        if 'hub.challenge' in request.args:
            challenge = request.args.get('hub.challenge')
            print(challenge)

        if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
            mode = request.args.get('hub.mode')
            token = request.args.get('hub.verify_token')

            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print('WEBHOOK VERIFIED')

                challenge = request.args.get('hub.challenge')

                return challenge, 200
            else:
                return 'ERROR', 403

        return 'SOMETHING', 200


    if request.method == 'POST':
        #do something.....
        
        if 'hub.mode' in request.args:
            mode = request.args.get('hub.mode')
            print(mode)
        if 'hub.verify_token' in request.args:
            token = request.args.get('hub.verify_token')
            print(token)
        if 'hub.challenge' in request.args:
            challenge = request.args.get('hub.challenge')
            print(challenge)

        if 'hub.mode' in request.args and 'hub.verify_token' in request.args:
            mode = request.args.get('hub.mode')
            token = request.args.get('hub.verify_token')

            if mode == 'subscribe' and token == VERIFY_TOKEN:
                print('WEBHOOK VERIFIED')

                challenge = request.args.get('hub.challenge')

                return challenge, 200
            else:
                return 'ERROR', 403



        #do something else
        data = request.data
        body = json.loads(data.decode('utf-8'))


        if 'object' in body and body['object'] == 'page':
            entries = body['entry']
            for entry in entries:
                webhookEvent = entry['messaging'][0]
                print(webhookEvent)

                senderPsid = webhookEvent['sender']['id']
                print('Sender PSID: {}'.format(senderPsid))

                if 'message' in webhookEvent:
                    handleMessage(senderPsid, webhookEvent['message'])

                return 'EVENT_RECEIVED', 200
        else:
            return 'ERROR', 404
    

@app.route('/webhook_dev', methods=['POST'])
def webhook_dev():
    # custom route for local development
    data = json.loads(request.data.decode('utf-8'))
    user_message = data['entry'][0]['messaging'][0]['message']['text']
    user_id = data['entry'][0]['messaging'][0]['sender']['id']
    response = {
        'recipient': {'id': user_id},
        'message': {'text': handle_message(user_id, user_message)}
    }
    return Response(
        response=json.dumps(response),
        status=200,
        mimetype='application/json'
    )

def handle_message(user_id, user_message):
    # DO SOMETHING with the user_message ... ¯\_(ツ)_/¯
    list_user_greetings = ['hi', 'hello', 'howdy', 'hey']
    list_user_farewell = ['bye', 'ciao', 'see you later', 'goodbye', 'good bye']
    list_user_thanks = ['thank you', 'thanks', 'cheers', 'grazie']
    list_user_ok = ['ok', 'okay', 'allright', 'right', 'all right']
    list_bot_greetings = ['Hey there', 'Howdy', 'Hiya', 'Hello']
    list_bot_farewell = ['Catch you later!', 'Good-bye now!', 'Bye bye!', 'See ya!']
    list_bot_thanks = ['You are welcome!', 'No worries!', 'Cheers', 'That is ok!']
    list_bot_ok = ['OK!', 'All right!']
    list_bot_fallback = ['Sorry, I did not get that! I am new.', 'Sorry, but I am new and still learning', 'Maybe one day I can answer that, I will learn!']
    bot_response = ''

    if user_message.lower() in list_user_greetings:
        bot_response = random.choice(list_bot_greetings)
    elif user_message.lower() in list_user_farewell:
        bot_response = random.choice(list_bot_farewell)
    elif user_message.lower() in list_user_thanks:
        bot_response = random.choice(list_bot_thanks)
    elif user_message.lower() in list_user_ok:
        bot_response = random.choice(list_bot_ok)        
    else:
        bot_response = random.choice(list_bot_fallback)

    # return "Hello "+user_id+" ! You just sent me : " + user_message
    return bot_response

@app.route('/privacy', methods=['GET'])
def privacy():
    # needed route if you need to make your bot public
    return "This facebook messenger bot's only purpose is to [...]. That's all. We don't use it in any other way."

@app.route('/', methods=['GET'])
def index():
    return "Hello there, I'm a facebook messenger bot."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
