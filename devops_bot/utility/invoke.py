import os
import re

from utility.config import gcp_project_meta_info


# TODO : need refactor

def list_version_4_module(env, module):
    meta_info = gcp_project_meta_info()

    credential_file = meta_info[env]["credential_file"]
    project_id = meta_info[env]["project_id"]
    cluster_name = meta_info[env][module]["cluster_name"]
    zone = meta_info[env][module]["zone"]
    namespace = meta_info[env][module]["namespace"]

    cmd = f"sh /docker/list-version-4-module.sh {credential_file} {project_id} {module} {cluster_name} {zone} {namespace}"
    # print(cmd)

    output_str = str(os.popen(cmd).read())

    rtn = output_str[output_str.index(f"asia.gcr.io/{project_id}/{module}"):].split("\n")[0]

    return rtn


def list_history_4_module(env, module):
    meta_info = gcp_project_meta_info()

    credential_file = meta_info[env]["credential_file"]
    project_id = meta_info[env]["project_id"]

    cmd = f"sh /docker/list-history-4-module.sh {credential_file} {project_id} {module}"
    # print(cmd)

    output_str_arr = str(os.popen(cmd).read()).split("\n")

    rtn = []
    for idx, line in enumerate(output_str_arr):
        if idx == 0:
            continue
        if idx > 3:
            break

        line_arr = re.split("\\s\\s+", line)

        rtn.append({
            "version": str(line_arr[1]).split(",")[0],
            "time": line_arr[len(line_arr) - 1]
        })

    return rtn


def pull_source_version(module, source_env, source_version, target_env):
    meta_info = gcp_project_meta_info()

    credential_file = meta_info[source_env]["credential_file"]
    source_project_id = meta_info[source_env]["project_id"]
    target_project_id = meta_info[target_env]["project_id"]

    cmd = f"sh /docker/pull-source-version.sh {credential_file} {source_project_id} {module} {source_version} {target_project_id}"
    # print(cmd)

    print(os.popen(cmd).read())


def roll_version_2_target(module, source_version, target_env):
    meta_info = gcp_project_meta_info()

    credential_file = meta_info[target_env]["credential_file"]
    target_project_id = meta_info[target_env]["project_id"]
    cluster_name = meta_info[target_env][module]["cluster_name"]
    zone = meta_info[target_env][module]["zone"]
    namespace = meta_info[target_env][module]["namespace"]

    cmd = f"sh /docker/roll-version-2-target.sh {credential_file} {target_project_id} {module} {source_version} {cluster_name} {zone} {namespace}"
    # print(cmd)

    output_str = str(os.popen(cmd).read())
    print(output_str)
    output_str_arr = output_str.split("\n")

    rtn = ""
    for idx, line in enumerate(output_str_arr):
        if idx < len(output_str_arr) - 3:
            continue

        rtn += f"{line}\n"

    return rtn


def check(type, account, password):
    os.popen(f"sh /docker/dump-param.sh {account} {password}")

    cmd = ""
    if type == '1':
        cmd = "newman run /docker/GoToWork.postman_collection.json -d /docker/param.csv"
    elif type == '2':
        cmd = "newman run /docker/GetOffWork.postman_collection.json -d /docker/param.csv"

    print(cmd)

    output_str = str(os.popen(cmd).read())
    print(output_str)
    output_str_arr = output_str.split("\n")

    rtn = ""
    for idx, line in enumerate(output_str_arr):
        if idx < len(output_str_arr) - 10:
            continue

        rtn += f"{line}\n"

    return rtn
