
import os
import re
from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from song import *


app = Flask(__name__)

# 必須放上自己的Channel Access Token
line_bot_api = LineBotApi(
    'hlZ/Dges1b87yy/CAvwv6dpmo0m2yrJN1H/E4rRRSf9szrJlvS/p1QMyuxkeJo8pvJu1HZx59Nqh6X7qVTq+1897jQcRG2Z6w0Q1sLpwcY/UBBHP4dnqYqnFMfOijD33bHZd5ca4XrnC/j8f6Zm77AdB04t89/1O/w1cDnyilFU=')
# 必須放上自己的Channel Secret
handler = WebhookHandler('0e7e6087725a1dd0a133f2a79e383bd4')

line_bot_api.push_message(
    'U9a1b23f0f62669c12d05cb8a9933f07c', TextSendMessage(text='你可以開始了'))

# 監聽所有來自 /callback 的 Post Request


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'

# 訊息傳遞區塊
##### 基本上程式編輯都在這個function #####


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = text = event.message.text
    if re.match('靠杯', message):
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage('牛逼啊!老鐵'))
    elif re.match('推歌', message):
        getsong()
        replysong = getsong()
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage(str(replysong)))
    elif re.match('推餐廳', message):
        line_bot_api.reply_message(
            event.reply_token, TextSendMessage('功能開發中，請等待小水豚發威'))


# 主程式
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
