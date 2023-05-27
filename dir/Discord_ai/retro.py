from requests import post

ai_1_name = 'ai_takl_1'
ai_1_url = 'https://discord.com/api/webhooks/1111633200968634418/YJx6I-x2awpnACFUQ2TaWUnCLmtXn5WmmBf7c5IgugMufdRWQdXsgu75qm_-pvI-jKo_'

def sent(cont):
    data = {
        'content': cont,
        'username': ai_1_name
    }
    post(ai_1_url, data=data)

sent("hello")