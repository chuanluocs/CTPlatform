from flask import Flask, render_template, request, send_file, jsonify, make_response
from werkzeug.utils import secure_filename
import subprocess
from flask_cors import CORS
import os
import json
import secrets
import re
import xlwt
import pandas as pd
import io

app = Flask(__name__)
CORS(app)

app.config['UPLOAD_FOLDER'] = 'upload/'
app.config['DOWNLOAD_FOLDER'] = 'download/'
app.config['OUTPUT_FOLDER'] = 'output/'
app.config['INPUT_FOLDER'] = 'input/'
app.config['CTW_FOLDER'] = 'CTWedge/'

operators = [" AND ", " OR ", "not ", "=>", "<=>", "=", "!=", ">=", "<=", ">", "<", "(", ")", " "]
operators_0 = ["=>", "<=>"]
operators_1 = ["OR"]
operators_2 = ["AND"]
operators_3 = ["=", "!="]
operators_4 = [">=", "<=", ">", "<"]
operators_5 = ["not"]

def get_random_key():
    random_hex = secrets.token_hex(16)
    random_urlsafe = secrets.token_urlsafe(32)
    return random_urlsafe

def standardization(input):
    input = input.replace("==", "=")

    input = input.replace("||", " OR ")
    input = input.replace("|", " OR ")
    input = input.replace(" or ", " OR ")

    input = input.replace("&&", " AND ")
    input = input.replace("&", " AND ")
    input = input.replace(" and ", " AND ")

    input = input.replace("->", "=>")
    input = input.replace("<->", "<=>")

    input = input.replace("True", "true")
    input = input.replace("TRUE", "true")
    input = input.replace("False", "false")
    input = input.replace("FALSE", "false")
    return input

def Split(expression):
    # operators = ["AND", "OR", "not", "=>", "<=>", "=", "!=", ">=", "<=", ">", "<", "(", ")", " "]
    pattern = r'(' + '|'.join(re.escape(op) for op in operators) + r')'
    # print(pattern)
    tokens = re.split(pattern, expression)
    tokens = [token.strip() for token in tokens if token.strip()]

    operators_final = ["=", "!=", ">=", "<=", ">", "<"]
    arr = []
    length, i = len(tokens), 0
    while i < length:
        if i + 2 < length and (tokens[i + 1] in operators_final):
            arr.append('(')
            arr.append(tokens[i])
            arr.append(tokens[i + 1])
            arr.append(tokens[i + 2])
            arr.append(')')
            i += 3
        else:
            arr.append(tokens[i])
            i += 1
    return arr

def turn_Object(exp_array):
    # print(exp_array)
    length = len(exp_array)
    val = 0
    for i in range(length):
        op = exp_array[i]
        if exp_array[i] == "(":
            val += 1
            continue
        elif exp_array[i] == ")":
            val -= 1
            continue
        if val != 0:
            continue

        if exp_array[i] in operators_0:
            left = exp_array[0 : i]
            # print(i + 1, length - 1)
            right = exp_array[i + 1 : length]
            node1 = turn_Object(left)
            node2 = turn_Object(right)

            obj = {"expression" : " ".join(exp_array), "type" : exp_array[i]}
            obj["children"] = []
            if node1 != None:
                obj["children"].append(node1)
            if node2 != None:
                obj["children"].append(node2)
            obj["key"] = get_random_key()
            return obj
    
    for i in range(length):
        if exp_array[i] == "(":
            val += 1
            continue
        elif exp_array[i] == ")":
            val -= 1
            continue
        if val != 0:
            continue
        
        if exp_array[i] in operators_1:
            left = exp_array[0 : i]
            right = exp_array[i + 1 : length]
            node1 = turn_Object(left)
            node2 = turn_Object(right)
            obj = {"expression" : " ".join(exp_array), "type" : exp_array[i]}
            if node2 != None and node2["type"] in operators_1:
                obj["children"] = node2["children"]
                if node1 != None:
                    obj["children"].insert(0, node1)
            else:
                obj["children"] = []
                if node1 != None:
                    obj["children"].append(node1)
                if node2 != None:
                    obj["children"].append(node2)
            obj["key"] = get_random_key()
            return obj
    
    for i in range(length):
        if exp_array[i] == "(":
            val += 1
            continue
        elif exp_array[i] == ")":
            val -= 1
            continue
        if val != 0:
            continue
        
        if exp_array[i] in operators_2:
            left = exp_array[0 : i]
            right = exp_array[i + 1 : length]
            node1 = turn_Object(left)
            node2 = turn_Object(right)
            obj = {"expression" : " ".join(exp_array), "type" : exp_array[i]}
            if node2 != None and node2["type"] in operators_2:
                obj["children"] = node2["children"]
                if node1 != None:
                    obj["children"].insert(0, node1)
            else:
                obj["children"] = []
                if node1 != None:
                    obj["children"].append(node1)
                if node2 != None:
                    obj["children"].append(node2)
            obj["key"] = get_random_key()
            return obj
    
    for i in range(length):
        if exp_array[i] == "(":
            val += 1
            continue
        elif exp_array[i] == ")":
            val -= 1
            continue
        if val != 0:
            continue
        
        if exp_array[i] in operators_3:
            left = exp_array[0 : i]
            right = exp_array[i + 1 : length]
            node1 = turn_Object(left)
            node2 = turn_Object(right)

            obj = {"expression" : " ".join(exp_array), "type" : exp_array[i]}
            obj["children"] = []
            if node1 != None:
                obj["children"].append(node1)
            if node2 != None:
                obj["children"].append(node2)
            obj["key"] = get_random_key()
            return obj
    
    for i in range(length):
        if exp_array[i] == "(":
            val += 1
            continue
        elif exp_array[i] == ")":
            val -= 1
            continue
        if val != 0:
            continue
        
        if exp_array[i] in operators_4:
            left = exp_array[0 : i]
            right = exp_array[i + 1 : length]
            node1 = turn_Object(left)
            node2 = turn_Object(right)

            obj = {"expression" : " ".join(exp_array), "type" : exp_array[i]}
            obj["children"] = []
            if node1 != None:
                obj["children"].append(node1)
            if node2 != None:
                obj["children"].append(node2)
            obj["key"] = get_random_key()
            return obj
    
    if exp_array[0] == "not":
        node = turn_Object(exp_array[1 : length])
        obj = {"expression" : " ".join(exp_array), "type" : "not"}
        obj["children"] = []
        if node != None:
            obj["children"].append(node)
        obj["key"] = get_random_key()
        return obj

    if exp_array[0] == "(":
        return turn_Object(exp_array[1 : length - 1])
    
    obj = {"expression" : " ".join(exp_array), "type" : "final"}
    obj["children"] = []
    obj["key"] = get_random_key()
    return obj

def get_component(obj):
    operators_final = ["=", "!=", ">=", "<=", ">", "<"]
    pattern = r'(' + '|'.join(re.escape(op) for op in operators_final) + r')'
    if len(obj["children"]) == 0:
        tokens = re.split(pattern, obj["expression"])
        tokens = [token.strip() for token in tokens if token.strip()]
        # print(obj)
        # print(tokens)
        return [ tokens[0] ]
    component = []
    for ch in obj["children"]:
        arr = get_component(ch)
        for x in arr:
            if x not in component:
                component.append(x)
    component.sort()
    return component

def turn_exp(obj):
    if len(obj["children"]) == 0:
        return obj["expression"]
    elif obj["type"] == "not":
        return "not (" + turn_exp(obj["children"][0]) + ")"

    exp, length = "", len(obj["children"])
    for i in range(length):
        ch = obj["children"][i]
        if i > 0:
            exp += " " + obj["type"] + " "
        if ch["type"] == "final":
            exp += turn_exp(ch)
        else:
            exp += "(" + turn_exp(ch) + ")"
    return exp

def get_used_val(obj, need):
    used_val = {}
    if obj["type"] in operators_4 or obj["type"] in operators_3:
        left = obj["children"][0]
        right = obj["children"][1]

        try:
            int(right["expression"])
        except ValueError:
            return used_val
        
        if left["expression"] not in need:
            return used_val
        
        if left["type"] == "final" and right["type"] == "final":
            used_val[left["expression"]] = [ int(right["expression"]) ]
        if obj["type"] in operators_4:
            used_val[left["expression"]].append(int(right["expression"]) - 1)
            used_val[left["expression"]].append(int(right["expression"]) + 1)
        return used_val

    for ch in obj["children"]:
        used_val_ch = get_used_val(ch, need)
        for name in used_val_ch:
            if name in used_val:
                for val in used_val_ch[name]:
                    if val not in used_val[name]:
                        used_val[name].append(val)
            else:
                used_val[name] = used_val_ch[name]
    return used_val

def set_min_max(values, mn, mx):
    arr = []
    for val in values:
        if val >= mn and val <= mx and (val not in arr):
            arr.append(val)
    arr.sort()
    return arr

def change_obj(obj, opt, values):
    if obj["type"] in operators_3 or obj["type"] in operators_4:
        # operators_4 = [">=", "<=", ">", "<"]
        left = obj["children"][0]["expression"]
        right = obj["children"][1]["expression"]
        if left != opt:
            return
        # print(opt, values, right)
        idx = values.index(int(right))
        obj["children"][1]["expression"] = str(idx)
    
    for ch in obj["children"]:
        change_obj(ch, opt, values)
    return obj

@app.route('/api/uploader_get_json',methods = ['GET','POST'])
def uploader_get_json():
    if request.method == 'POST':
        f = request.files['file']
        # print(request.files)

        random_hex = secrets.token_hex(16)
        random_urlsafe = secrets.token_urlsafe(32)
        input_file_path = os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(random_urlsafe + f.filename))
        # print(input_file_path)
        f.save(input_file_path)

        options, constraints = [], []
        n, m = 0, 0
        state = ""
        name_to_type = {}
        with open(input_file_path, 'r') as f:
            for line in f.readlines():
                line = line.replace(";", "")
                arr = line.split()
                if len(arr) < 1:
                    continue
                
                # print(arr)
                if arr[0] == "Parameters:" or (len(arr) == 2 and arr[0] == "Parameters" and arr[1] == ":"):
                    state = "Parameters"
                    continue
                elif arr[0] == "Constraints:" or (len(arr) == 2 and arr[0] == "Constraints" and arr[1] == ":"):
                    state = "Constraints"
                    # print(name_to_type)
                    continue
                
                if state == "Parameters":
                    tokens = line.split(':')
                    arr = [token.strip() for token in tokens if token.strip()]
                    if len(arr) != 2:
                        continue
                    n += 1
                    opt = {"id":  n, "name": arr[0]}
                    if arr[1] == "Boolean":
                        opt["type"] = "Boolean"
                        opt["possible"] = ["True", "False"]
                        opt["possible_org"] = ["True", "False"]
                        opt["min_value"] = 0
                        opt["max_value"] = 0
                    
                    elif arr[1][0] == "{":
                        opt["type"] = "Category"
                        s = arr[1].replace("{", "").replace("}", "")
                        # tokens = s.split(',')
                        tokens = re.split(r"( |,)", s)
                        tokens = [token.strip() for token in tokens if token.strip()]
                        opt["possible"], opt["possible_org"] = [], []
                        cnt = 0
                        for token in tokens:
                            if token == ",":
                                continue
                            if cnt < 3:
                                opt["possible"].append(token.strip())
                            cnt += 1
                            opt["possible_org"].append(token.strip())
                        opt["min_value"] = 0
                        opt["max_value"] = 0
                    
                    elif arr[1][0] == "[":
                        opt["type"] = "Integer"
                        s = arr[1].replace("[", "").replace("]", "")
                        nums = s.split()
                        opt["possible"] = [ nums[0] + " ~" + nums[2] ]
                        opt["possible_org"] = [ nums[0] + " ~" + nums[2] ]
                        opt["min_value"] = int(nums[0])
                        opt["max_value"] = int(nums[2])

                    # opt["description"] = "This is a description"
                    opt["description"] = "Parameter " + str(len(options) + 1)
                    name_to_type[opt["name"]] = opt["type"]
                    options.append(opt)
                
                elif state == "Constraints":
                    exp = line.replace("#", " ").strip()
                    exp = standardization(exp)
                    exp_array = Split(exp)
                    obj = turn_Object(exp_array)
                    com = get_component(obj)
                    obj["component"] = []
                    for name in com:
                        if name in name_to_type:
                            obj["component"].append( { "name" : name, "type" : name_to_type[name] } )
                    
                    des = obj["expression"]
                    if len(des) > 50:
                        des = des[0 : 47] + "..."
                    obj["description"] = des

                    text = obj["expression"]
                    tmp = [text[i:i+60] for i in range(0, len(text), 60)]
                    # obj["expression"] = "\r\n".join(tmp)

                    constraints.append(obj)
                    m += 1
        feedback = {
            "options": options,
            "constraints": constraints
        }
        os.remove(input_file_path)
        # print(json.dumps(feedback))
        
        return json.dumps(feedback)

    else:
        return "QAQ"

@app.route('/api/get_testcases', methods = ['GET','POST'])
def get_testcases():
    data = request.get_json()  # 获取 POST 请求中的 JSON 数据
    options = data["options"]
    constraints = data["constraints"]
    # print(options)
    # print(constraints)

    large_integer, need, used_val = [], [], {}
    for op in options:
        if op["type"] == "Integer":
            min_value = int(op["min_value"])
            max_value = int(op["max_value"])
            if max_value - min_value > 20:
                large_integer.append(op)
                need.append(op["name"])
                used_val[op["name"]] = [ min_value, max_value ]
                if min_value * max_value < 0:
                    used_val[op["name"]].append(0)
    
    for con in constraints:
        used_val_tmp = get_used_val(con, need)
        for name in used_val_tmp:
            for val in used_val_tmp[name]:
                used_val[name].append(val)
    
    for name in used_val:
        for i in range(15):
            used_val[name].append(2**i)
            used_val[name].append(-(2**i))
    for op in large_integer:
        name = op["name"]
        min_value = int(op["min_value"])
        max_value = int(op["max_value"])
        used_val[name] = set_min_max(used_val[name], min_value, max_value)
    for con in constraints:
        for name in need:
            change_obj(con, name, used_val[name])

    random_hex = secrets.token_hex(16)
    random_urlsafe = secrets.token_urlsafe(32)
    ctw_path = os.path.join(app.config['CTW_FOLDER'], secure_filename(random_urlsafe + ".ctw"))
    # print(ctw_path)
    ctw_file = open(ctw_path, "w")

    random_hex = secrets.token_hex(16)
    random_urlsafe = secrets.token_urlsafe(32)
    ctw_file.write("Model Meow\n")
    
    ctw_file.write("Parameters:\n")
    for op in options:
        if op["type"] == "Boolean":
            ctw_file.write(op["name"] + " : " + op["type"] + "\n")
        elif op["type"] == "Category":
            ctw_file.write(op["name"] + " : {")
            nums = len(op["possible_org"])
            for i in range(nums):
                if i > 0:
                    ctw_file.write(", ")
                ctw_file.write(op["possible_org"][i])
            ctw_file.write("}\n")
        elif op["type"] == "Integer":
            ctw_file.write(op["name"] + " : [")
            if op["name"] not in need:
                ctw_file.write(str(op["min_value"]) + " .. " + str(op["max_value"]))
            else:
                ctw_file.write("0 .. " + str(len(used_val[op["name"]]) - 1))
            ctw_file.write("]\n")

    ctw_file.write("\nConstraints:\n")
    for con in constraints:
        # ctw_file.write("# " + con.replace("\n", "").replace("\r", "") + " #\n")
        exp = turn_exp(con)
        ctw_file.write("# " + exp + " #\n") 
    ctw_file.close()

    # input_cnf_path
    random_hex = secrets.token_hex(16)
    random_urlsafe = secrets.token_urlsafe(32)
    input_cnf_path = os.path.join(app.config['INPUT_FOLDER'], secure_filename(random_urlsafe + ".cnf"))
    # print(input_cnf_path)

    # parm_list_path
    random_hex = secrets.token_hex(16)
    random_urlsafe = secrets.token_urlsafe(32)
    parm_list_path = os.path.join(app.config['INPUT_FOLDER'], secure_filename(random_urlsafe + ".txt"))
    # print(parm_list_path)

    # ./parser ./BOOLC_1.ctw test.cnf test_list.txt > /dev/null 2>&1
    # command = "./CTWedge/parser " +  ctw_path + " " + input_cnf_path + " " + parm_list_path + " > /dev/null 2>&1"
    
    # command = "./CTWedge/parser " +  ctw_path + " " + input_cnf_path + " " + parm_list_path
    command = ["nohup", "./CTWedge/parser", ctw_path, input_cnf_path, parm_list_path]
    # print(command)
    # os.system(command)
    subprocess.run(command, check = True)

    random_hex = secrets.token_hex(16)
    random_urlsafe = secrets.token_urlsafe(32)
    output_file_path = os.path.join(app.config['OUTPUT_FOLDER'], secure_filename(random_urlsafe + ".txt"))
    # ./SamplingCA -input_cnf_path [INSTANCE_PATH] <optional_parameters> <optional_flags>
    command = ['nohup', './SamplingCA/SamplingCA', '-input_cnf_path', input_cnf_path, '-output_testcase_path', output_file_path]
    subprocess.run(command, check = True)

    option_names = []
    for op in options:
        option_names.append(op["name"])
    name_to_index = {}
    with open(input_cnf_path, 'r') as f:
        for line in f.readlines():
            arr = line.split()
            if len(arr) == 4 and arr[0] == "c" and arr[2] == "-->":
                name_to_index[arr[1]] = int(arr[3])

    # id: 1,
    # name: "Meow",
    # type: "Boolean",
    # description: "Meow Meow Meow",
    # value: "True",
    testcases = []
    with open(output_file_path, 'r') as f:
        for line in f.readlines():
            arr = list(map(int, line.split()))
            tc = []
            for x in options:
                opt = { "id" : x["id"] }
                opt["name"] = x["name"]
                opt["type"] = x["type"]
                opt["description"] = x["description"]

                if opt["type"] == "Boolean":
                    index = name_to_index[x["name"]]
                    if arr[index - 1] == 1:
                        opt["value"] = "True"
                    else:
                        opt["value"] = "False"

                elif opt["type"] == "Category":
                    for val in x["possible_org"]:
                        name = opt["name"] + "@" + val
                        index = name_to_index[name]
                        if arr[index - 1] == 1:
                            opt["value"] = val
                            break
                
                elif opt["type"] == "Integer":
                    mn, mx = x["min_value"], x["max_value"]
                    if opt["name"] in need:
                        mn, mx = 0, len(used_val[opt["name"]]) - 1
                    
                    for val in range(mn, mx + 1):
                        name = opt["name"] + "@" + str(val)
                        index = name_to_index[name]
                        if arr[index - 1] == 1:
                            if opt["name"] not in need:
                                opt["value"] = str(val)
                            else:
                                opt["value"] = str(used_val[opt["name"]][val])
                            break
                    # print(opt)

                tc.append(opt)
            testcases.append(tc)
    
    if os.path.exists(ctw_path):
        os.remove(ctw_path)
    if os.path.exists(input_cnf_path):
        os.remove(input_cnf_path)
    if os.path.exists(parm_list_path):
        os.remove(parm_list_path)
    if os.path.exists(output_file_path):
        os.remove(output_file_path)
    
    columns = []
    columns.append( { "title" : '编号', "width" : 130, "dataIndex" : 'index', "key" : 'index', "fixed" : 'left' } )
    
    # {
    #     title: 'Par0',
    #     dataIndex: 'Par0_value',
    #     key: '1',
    #     width: 100,
    # }
    nums = len(option_names)
    for i in range(nums):
        tmp_obj = {}
        tmp_obj["title"] = option_names[i]
        tmp_obj["dataIndex"] = option_names[i] + '_value'
        tmp_obj["key"] = str(i)
        tmp_obj["width"] = 100
        columns.append(tmp_obj)
    
    data = []
    tc_nums = len(testcases)
    for i in range(tc_nums):
        tc = testcases[i]
        tmp_obj = {}
        tmp_obj["key"] = str(i)
        tmp_obj["index"] = "TestCase " + str(i + 1)
        for opt in tc:
            tmp_obj[opt["name"] + "_value"] = opt["value"]
        data.append(tmp_obj)

    # feedback = json.dumps(testcases)
    feedback = {
        "columns": columns,
        "data": data
    }
    return json.dumps(feedback)

@app.route('/api/download_testcases', methods = ['GET', 'POST'])
def download_testcases():
    # data = request.get_json()  # 获取 POST 请求中的 JSON 数据
    # # print(data)
    # testcases = data["testcases"]
    # random_hex = secrets.token_hex(16)
    # random_urlsafe = secrets.token_urlsafe(32)
    # download_file_name = secure_filename(random_urlsafe + ".txt")
    # download_path = os.path.join(app.config['DOWNLOAD_FOLDER'], download_file_name)
    # download_file = open(download_path, "w")

    # # download_file.write(str(testcases))
    # length = len(testcases)
    # for i in range(length):
    #     tc = testcases[i]
    #     download_file.write("Test Case " + str(i) + ": ")
    #     for op in tc:
    #         download_file.write("(" + op["name"] + " : " + op["value"] + "), ")
    #     download_file.write("\n\n")

    # download_file.close()
    # return send_file(download_path, as_attachment=True, download_name = download_file_name)

    data = request.get_json()
    tc_columns = data["columns"]
    tc_data = data["data"]
    random_hex = secrets.token_hex(16)
    random_urlsafe = secrets.token_urlsafe(32)
    download_file_name = secure_filename(random_urlsafe + ".xls")
    download_path = os.path.join(app.config['DOWNLOAD_FOLDER'], download_file_name)

    workBook = xlwt.Workbook(encoding = 'utf-8')
    sheet = workBook.add_sheet("sheetName")
    head, xls_data = [], []

    keys = []
    for c in tc_columns:
        head.append(c["title"])
        keys.append(c["dataIndex"])
    
    for line in tc_data:
        tmp = []
        for key in keys:
            tmp.append(line[key])
        xls_data.append(tmp)

    for i in head:
	    sheet.write(0, head.index(i), i)
    length = len(xls_data)
    for i in range(length):
        line_len = len(xls_data[i])
        for j in range(line_len):
            sheet.write(i + 1, j, xls_data[i][j])
    workBook.save(download_path)
    return send_file(download_path, as_attachment = True, download_name = download_file_name, mimetype='application/vnd.ms-excel')

    # tc_columns = request.args.get('columns')
    # tc_data = request.args.get('data')
    # print("QAQ")
    # print(type(tc_columns))
    # print("QAQ")
    # print(tc_columns)

    # data = {'Name': ['Alice', 'Bob', 'Charlie'],
    #         'Age': [25, 30, 35]}
    # df = pd.DataFrame(data)

    # # Create an Excel writer
    # output = io.BytesIO()  # Create a BytesIO object to store the Excel file
    # writer = pd.ExcelWriter(output, engine='xlsxwriter')

    # # Convert the DataFrame to Excel format
    # df.to_excel(writer, sheet_name='Sheet1', index=False)

    # # Close the Excel writer and seek to the beginning of the BytesIO buffer
    # writer.close()
    # output.seek(0)

    # # Create a response with the XLS file
    # response = make_response(output.read())
    # response.headers['Content-Type'] = 'application/vnd.ms-excel'
    # response.headers['Content-Disposition'] = 'attachment; filename=data.xls'

    # return response


def get_standard_obj(obj):

    standard_obj = obj
    # print("\n")
    # print(obj["children"])
    # print(type(obj["children"]))
    # print(len(obj["children"]))
    # print("\n")
    if len(obj["children"]) == 0:
        if obj["type"] in operators:
            return [False, obj]
        standard_obj["type"] = "final"
    
    elif len(obj["children"]) == 1:
        if obj["type"] != "not":
            return [False, obj]

        tmp = get_standard_obj(obj["children"][0])
        if not tmp[0]:
            return [False, obj]
        child = tmp[1]
        standard_obj["children"][0] = child
        standard_obj["expression"] = "not (" + child["expression"] + ")"
    
    elif len(obj["children"]) == 2:
        tmp = get_standard_obj(obj["children"][0])
        if not tmp[0]:
            return [False, obj]
        child_left = tmp[1]

        tmp = get_standard_obj(obj["children"][1])
        if not tmp[0]:
            return [False, obj]
        child_right = tmp[1]

        standard_obj["children"][0] = child_left
        standard_obj["children"][1] = child_right
        standard_obj["expression"] = "( " + child_left["expression"] + " ) " 
        standard_obj["expression"] += obj["type"]
        standard_obj["expression"] += " ( " + child_right["expression"] + " )"

    else:
        if (obj["type"] != "OR") and (obj["type"] != "AND"):
            [ False, obj ]
        
        nums = len(obj["children"])
        standard_obj["expression"] = ""
        for i in range(nums):
            ch = obj["children"][i]
            tmp = get_standard_obj(ch)
            if not tmp[0]:
                return [False, obj]

            new_ch = tmp[1]
            standard_obj["children"][i] = new_ch

            if i > 0:
                standard_obj["expression"] += " " + obj["type"] + " "
            standard_obj["expression"] += "( " + new_ch["expression"] + " )"

    return [ True, standard_obj ]


@app.route('/api/get_constraint_obj', methods = ['GET', 'POST'])
def get_constraint_obj():
    data = request.get_json()  # 获取 POST 请求中的 JSON 数据
    obj = data["constraint"]
    options = data["options"]
    success, new_obj = get_standard_obj(obj)
    if not success:
        feedback = {
            "success": False,
            "new_constraint": {}
        }
        return json.dumps(feedback)
    
    name_to_type = {}
    for opt in options:
        name_to_type[opt["name"]] = opt["type"]
    
    com = get_component(obj)
    new_obj["component"] = []
    for name in com:
        if name in name_to_type:
            obj["component"].append( { "name" : name, "type" : name_to_type[name] } )
    
    # new_obj["description"] = "This is a description"
    des = new_obj["expression"]
    if len(des) > 50:
        des = des[0 : 47] + "..."
    new_obj["description"] = des

    feedback = {
        "success": True,
        "new_constraint": new_obj
    }
    # print(json.dumps(new_obj))
    return json.dumps(feedback)


@app.route('/api/download_model', methods = ['GET', 'POST'])
def download_model():
    data = request.get_json()
    options = data["options"]
    constraints = data["constraints"]

    random_hex = secrets.token_hex(16)
    random_urlsafe = secrets.token_urlsafe(32)
    download_file_name = secure_filename(random_urlsafe + ".txt")
    download_path = os.path.join(app.config['DOWNLOAD_FOLDER'], download_file_name)

    file = open(download_path, "w")
    file.write("Parameters:\n")
    for opt in options:
        file.write(opt["name"] + ": ")
        if opt["type"] == "Boolean":
            file.write("Boolean\n")
        elif opt["type"] == "Integer":
            file.write("[" + str(opt["min_value"]) + " .. " + str(opt["max_value"]) + "]\n")
        elif opt["type"] == "Category":
            file.write("{ ")
            for val in opt["possible_org"]:
                file.write(str(val) + " ")
            file.write("}\n")
    
    file.write("\n\nConstraints:\n")
    for con in constraints:
        file.write("# " + con["expression"] + " #\n")
    file.close()

    return send_file(download_path, as_attachment=True, download_name = download_file_name)


@app.route('/api/get_object', methods = ['GET', 'POST'])
def get_object():
    data = request.get_json()  # 获取 POST 请求中的 JSON 数据
    exp = data["expression"]

    exp = standardization(exp)
    exp_array = Split(exp)
    obj = turn_Object(exp_array)

    feedback = {
        "obj" : obj
    }
    return json.dumps(feedback)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
