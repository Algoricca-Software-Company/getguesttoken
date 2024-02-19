import logging
import os
import time
import requests
import azure.functions as func


app = func.FunctionApp(http_auth_level=func.AuthLevel.FUNCTION)

@app.route(route="GetGuestToken")
def GetGuestToken(req: func.HttpRequest) -> func.HttpResponse:
    try:
        url = 'https://api.twitter.com/1.1/guest/activate.json'
        headers = {
            'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
            'x-twitter-client-language': 'pt',
            'sec-ch-ua-mobile': '?0',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
            'content-type': 'application/x-www-form-urlencoded',
            'Referer': 'https://twitter.com/',
            'x-client-transaction-id': '8JbG86GZL8oEZplPesvCbWiRjn0fH0VPFlf0tnIzaM6S7Uhbn1NKyp8Vx9j7Eq/7GWznlvHbm4V0+5Yaqbgc4YR5WvW58Q',
            'x-twitter-active-user': 'yes',
            'sec-ch-ua-platform': 'Windows',
        }
        status = None
        guest_token = None
        response = requests.post(url, headers=headers)
        status = response.status_code
        if status == 200:
            json_response = response.json()
            guest_token = json_response.get('guest_token')
            logging.info('Token de convidado obtido com sucesso.')
        else:
            logging.error(f'Status: {status}')
        return func.HttpResponse(f"{guest_token}", status_code=200)

    except Exception as e:
        logging.error(f'Erro ao obter token de convidado: {e}')
        return func.HttpResponse("Error occurred", status_code=400)
