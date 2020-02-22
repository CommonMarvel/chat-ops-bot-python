from utility.invoke import list_version_4_module, pull_source_version, roll_version_2_target


# TODO : need refactor

def action_block():
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "What do you want to do ❓"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "🗒 *Choose Module for List*"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select"
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🗒 noah-mobile"
                        },
                        "value": "list noah-mobile"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🗒 noah-admin"
                        },
                        "value": "list noah-admin"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🗒 xts-mobile"
                        },
                        "value": "list xts-mobile"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🗒 xts-admin"
                        },
                        "value": "list xts-admin"
                    }, {
                        "text": {
                            "type": "plain_text",
                            "text": "🗒 ly3kt-pay-api"
                        },
                        "value": "list ly3kt-pay-api"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🗒 ly3kt-game-api"
                        },
                        "value": "list ly3kt-game-api"
                    }
                ]
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "🕹 *Choose Module for Roll*"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select"
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🕹 noah-mobile"
                        },
                        "value": "roll noah-mobile"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🕹 noah-admin"
                        },
                        "value": "roll noah-admin"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🕹 xts-mobile"
                        },
                        "value": "roll xts-mobile"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🕹 xts-admin"
                        },
                        "value": "roll xts-admin"
                    }, {
                        "text": {
                            "type": "plain_text",
                            "text": "🕹 ly3kt-pay-api"
                        },
                        "value": "roll ly3kt-pay-api"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🕹 ly3kt-game-api"
                        },
                        "value": "roll ly3kt-game-api"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🕹 drawing-center"
                        },
                        "value": "roll drawing-center"
                    }
                ]
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": " "
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "❌ Cancel"
                },
                "value": "cancel"
            }
        }
    ]


def list_init_block(module_name):
    dev_ver = " "
    sit_ver = " "
    demo_ver = " "
    prod_ver = " "

    image_url = "http://www.pngmart.com/files/8/List-PNG-HD.png"

    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"✨ *{module_name}* ✨     (0/4)"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🔩 *Dev Env* 🔩\n    {dev_ver}\n\n⚔️ *Sit Env* ⚔️\n    {sit_ver}\n\n🔰 *Demo Env* 🔰\n    {demo_ver}\n\n💎 *Prod Env* 💎\n    {prod_ver}"
            },
            "accessory": {
                "type": "image",
                "image_url": image_url,
                "alt_text": module_name
            }
        }
    ]


def list_block(env_name, module_name, previous, count):
    versions = {
        "dev": " ",
        "sit": " ",
        "demo": " ",
        "prod": " "
    }

    version = list_version_4_module(env_name, module_name)
    versions[env_name] = version
    for key in previous.keys():
        versions[key] = previous[key]

    dev_ver = versions["dev"]
    sit_ver = versions["sit"]
    demo_ver = versions["demo"]
    prod_ver = versions["prod"]

    image_url = "http://www.pngmart.com/files/8/List-PNG-HD.png"

    return version, [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"✨ *{module_name}* ✨     ({count}/4)"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🔩 *Dev Env* 🔩\n    {dev_ver}\n\n⚔️ *Sit Env* ⚔️\n    {sit_ver}\n\n🔰 *Demo Env* 🔰\n    {demo_ver}\n\n💎 *Prod Env* 💎\n    {prod_ver}"
            },
            "accessory": {
                "type": "image",
                "image_url": image_url,
                "alt_text": module_name
            }
        }
    ]


def roll_init_block(module_name):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🚀 Rolling the version of ✨ *{module_name}* ✨ between two env !"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "📀 *Source Env*"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select"
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🔩 dev"
                        },
                        "value": f"roll {module_name} source dev"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "⚔️ sit"
                        },
                        "value": f"roll {module_name} source sit"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🔰 demo"
                        },
                        "value": f"roll {module_name} source demo"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "💎 prod"
                        },
                        "value": f"roll {module_name} source prod"
                    }
                ]
            }
        }
    ]


def roll_init_source_block(module_name, source_env, source_versions):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🚀 Rolling the version of ✨ *{module_name}* ✨ between two env !"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"📀 *Source Env*     ➡️     *{source_env}*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🔢 *Source Version* "
            }
        },
        {
            "type": "divider"
        }
    ]


def roll_source_block(module_name, source_env, source_versions):
    rtn = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🚀 Rolling the version of ✨ *{module_name}* ✨ between two env !"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"📀 *Source Env*     ➡️     *{source_env}*"
            }
        }
    ]

    options = []
    for version_dict in source_versions:
        version = version_dict["version"]
        time = version_dict["time"]

        options.append({
            "text": {
                "type": "plain_text",
                "text": f"{version},{time}"
            },
            "value": f"roll {module_name} source {source_env} {version}"
        })

    rtn.append(
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "🔢 *Source Version*"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select"
                },
                "options": options
            }
        })

    rtn.append({
        "type": "divider"
    })

    return rtn


def roll_target_block(module_name, source_env, source_version):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🚀 Rolling the version of ✨ *{module_name}* ✨ between two env !"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"📀 *Source Env*     ➡️     *{source_env}*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🔢 *Source Version*     ➡️     *{source_version}*"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "🖥 *Target Env*"
            },
            "accessory": {
                "type": "static_select",
                "placeholder": {
                    "type": "plain_text",
                    "text": "Select"
                },
                "options": [
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🔩 dev"
                        },
                        "value": f"roll {module_name} source {source_env} {source_version} target dev"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "⚔️ sit"
                        },
                        "value": f"roll {module_name} source {source_env} {source_version} target sit"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "🔰 demo"
                        },
                        "value": f"roll {module_name} source {source_env} {source_version} target demo"
                    },
                    {
                        "text": {
                            "type": "plain_text",
                            "text": "💎 prod"
                        },
                        "value": f"roll {module_name} source {source_env} {source_version} target prod"
                    }
                ]
            }
        },

    ]


def roll_init_processing_block(module_name, source_env, source_version, target_env, progress):
    if progress == "50":
        pull_source_version(module_name, source_env, source_version, target_env)

    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🚀 Rolling the version of ✨ *{module_name}* ✨ between two env !"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"📀 *Source Env*     ➡️     *{source_env}*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🔢 *Source Version*     ➡️     *{source_version}*"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🖥 *Target Env*     ➡️     *{target_env}*"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"... {progress}% ..."
            }
        }
    ]


def roll_processing_block(module_name, source_env, source_version, target_env):
    result = roll_version_2_target(module_name, source_version, target_env)

    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🚀 Rolling the version of ✨ *{module_name}* ✨ between two env !"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"📀 *Source Env*     ➡️     *{source_env}*"
            }
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🔢 *Source Version*     ➡️     *{source_version}*"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"🖥 *Target Env*     ➡️     *{target_env}*"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": result
            }
        }
    ]


def cancel_block(user_name):
    return [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"❌ *{user_name}* cancel the request"
            }
        }
    ]
