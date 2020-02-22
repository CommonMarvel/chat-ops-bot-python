import _thread
import json
import os
import time

import slack
from flask import Flask, request, make_response

from utility.data import cancel_block, list_block, action_block, list_init_block, roll_init_block, \
    roll_source_block, roll_target_block, roll_processing_block, roll_init_processing_block, roll_init_source_block
from utility.invoke import list_history_4_module, check, roll_version_2_target

g_rtm_client = slack.RTMClient(token=os.environ["BOT_USER_OAUTH_ACCESS_TOKEN"])
g_slack_client = slack.WebClient(token=os.environ["BOT_USER_OAUTH_ACCESS_TOKEN"])


@slack.RTMClient.run_on(event="message")
def start(**payload):
    bot_id = os.environ["BOT_ID"]

    # print(payload)
    data = payload["data"]
    web_client = payload["web_client"]
    # rtm_client = payload["rtm_client"]

    text = str(data.get("text", []))
    # print(text)
    # @devops-bot action
    # @devops-bot exec ls
    # @devops-bot check 1 R014 account password

    if text.startswith(f"<@{bot_id}>"):
        if text.startswith(f"<@{bot_id}> action"):
            web_client.chat_postMessage(
                channel=data["channel"],
                blocks=action_block()
            )
        elif text.startswith(f"<@{bot_id}> exec"):
            cmd = text[text.index("exec") + 5:]

            rtn = os.popen(cmd).read()
            web_client.chat_postMessage(
                channel=data["channel"],
                text=rtn
            )
        elif text.startswith(f"<@{bot_id}> check"):
            text_arr = str(text).split(" ")
            print(text_arr)

            web_client.chat_postMessage(
                channel=data["channel"],
                text=check(text_arr[2], text_arr[3], text_arr[4])
            )
        else:
            pass


app = Flask(__name__)


@app.route("/rolling", methods=["POST"])
def rolling():
    data = request.json

    print(roll_version_2_target(data["moduleName"], data["version"], "dev"))

    return make_response("", 200)


@app.route("/interaction", methods=["POST"])
def interaction():
    payload = json.loads(request.form["payload"])
    # print(payload)

    action = payload["actions"][0]

    if action["type"] == "static_select":
        selected_option_value = str(action["selected_option"]["value"])

        # list action
        if selected_option_value.startswith("list"):
            previous = {}
            g_slack_client.chat_update(
                channel=payload["channel"]["id"],
                ts=payload["message"]["ts"],
                attachments=[],
                blocks=list_init_block(selected_option_value[5:])
            )

            dev, content = list_block("dev", selected_option_value[5:], previous, 1)
            previous["dev"] = dev
            g_slack_client.chat_update(
                channel=payload["channel"]["id"],
                ts=payload["message"]["ts"],
                attachments=[],
                blocks=content
            )
            time.sleep(7)
            sit, content = list_block("sit", selected_option_value[5:], previous, 2)
            previous["sit"] = sit
            g_slack_client.chat_update(
                channel=payload["channel"]["id"],
                ts=payload["message"]["ts"],
                attachments=[],
                blocks=content
            )
            time.sleep(7)
            demo, content = list_block("demo", selected_option_value[5:], previous, 3)
            previous["demo"] = demo
            g_slack_client.chat_update(
                channel=payload["channel"]["id"],
                ts=payload["message"]["ts"],
                attachments=[],
                blocks=content
            )
            time.sleep(7)
            prod, content = list_block("prod", selected_option_value[5:], previous, 4)
            previous["prod"] = prod
            g_slack_client.chat_update(
                channel=payload["channel"]["id"],
                ts=payload["message"]["ts"],
                attachments=[],
                blocks=content
            )
        # roll action
        elif selected_option_value.startswith("roll"):
            value_arr = selected_option_value.split(" ")
            # print(value_arr)

            # roll noah-mobile
            if len(value_arr) == 2:
                g_slack_client.chat_update(
                    channel=payload["channel"]["id"],
                    ts=payload["message"]["ts"],
                    attachments=[],
                    blocks=roll_init_block(value_arr[1])
                )
            # roll noah-mobile source dev
            elif len(value_arr) == 4:
                g_slack_client.chat_update(
                    channel=payload["channel"]["id"],
                    ts=payload["message"]["ts"],
                    attachments=[],
                    blocks=roll_init_source_block(value_arr[1], value_arr[3], [])
                )
                source_versions = list_history_4_module(value_arr[3], selected_option_value[5:])
                g_slack_client.chat_update(
                    channel=payload["channel"]["id"],
                    ts=payload["message"]["ts"],
                    attachments=[],
                    blocks=roll_source_block(value_arr[1], value_arr[3], source_versions)
                )
            # roll noah-mobile source dev 0.0.10
            elif len(value_arr) == 5:
                g_slack_client.chat_update(
                    channel=payload["channel"]["id"],
                    ts=payload["message"]["ts"],
                    attachments=[],
                    blocks=roll_target_block(value_arr[1], value_arr[3], value_arr[4])
                )
            # roll noah-mobile source dev 0.0.10 target sit
            elif len(value_arr) == 7:
                g_slack_client.chat_update(
                    channel=payload["channel"]["id"],
                    ts=payload["message"]["ts"],
                    attachments=[],
                    blocks=roll_init_processing_block(value_arr[1], value_arr[3], value_arr[4], value_arr[6], "30")
                )
                g_slack_client.chat_update(
                    channel=payload["channel"]["id"],
                    ts=payload["message"]["ts"],
                    attachments=[],
                    blocks=roll_init_processing_block(value_arr[1], value_arr[3], value_arr[4], value_arr[6], "50")
                )
                g_slack_client.chat_update(
                    channel=payload["channel"]["id"],
                    ts=payload["message"]["ts"],
                    attachments=[],
                    blocks=roll_processing_block(value_arr[1], value_arr[3], value_arr[4], value_arr[6])
                )
    # cancel action
    elif action["type"] == "button":
        g_slack_client.chat_update(
            channel=payload["channel"]["id"],
            ts=payload["message"]["ts"],
            attachments=[],
            blocks=cancel_block(payload["user"]["name"])
        )

    return make_response("", 200)


def flask_thread():
    app.run(host="0.0.0.0")


if __name__ == "__main__":
    _thread.start_new_thread(flask_thread, ())

    g_rtm_client.start()
