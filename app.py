from flask import Flask
from flask import request
from flask import render_template
from flask import jsonify
from jieba.analyse import  extract_tags
import jieba
import collections
import re
import matplotlib.font_manager as fm
import string
import utils

jieba.add_word("新冠", freq = 20000, tag = None)
jieba.add_word("加强针", freq = 20000, tag = None)
app = Flask(__name__)


@app.route('/') #注册路由
def hello_world():
    return render_template("main.html")

@app.route("/c1")
def get_c1_data():
    data = utils.get_c1_data()
    return jsonify({"confirm":data[0],"suspect":data[1],"heal":data[2],"dead":data[3]})

@app.route("/c2")
def get_c2_data():
    res = []
    for tup in utils.get_c2_data():
        # print(tup)
        res.append({"name":tup[0],"value":int(tup[1])})
    return jsonify({"data":res})

@app.route("/l1")
def get_l1_data():
    data = utils.get_l1_data()
    day,confirm,suspect,heal,dead = [],[],[],[],[]
    for a,b,c,d,e in data[7:]:
        day.append(a.strftime("%m-%d")) #a是datatime类型
        confirm.append(b)
        suspect.append(c)
        heal.append(d)
        dead.append(e)
    return jsonify({"day":day,"confirm": confirm, "suspect": suspect, "heal": heal, "dead": dead})

@app.route("/l2")
def get_l2_data():
    data = utils.get_l2_data()
    day, confirm_add, suspect_add = [], [], []
    for a, b, c in data[7:]:
        day.append(a.strftime("%m-%d"))  # a是datatime类型
        confirm_add.append(b)
        suspect_add.append(c)
    return jsonify({"day": day, "confirm_add": confirm_add, "suspect_add": suspect_add})

@app.route("/r1")
def get_r1_data():
    data = utils.get_r1_data()
    city = []
    confirm = []
    for k,v in data:
        city.append(k)
        confirm.append(int(v))
    return jsonify({"city": city, "confirm": confirm})


@app.route("/r2")
def get_r2_data():
    #jieba.load_userdict("word.txt")
    data = utils.get_r2_data() #格式 (('民警抗疫一线奋战16天牺牲1037364',), ('四川再派两批医疗队1537382',)
    d = []
    d1 = []
    d2 = []

    string = str(data)  # 字典转化成字符串
    #print(string)
    pattern = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|\"|\'|\'|\,|\，|\d+|')  # 定义正则表达式匹配模式
    string = re.sub(pattern, '', string)  # 将符合模式的字符去除
    mywordList = jieba.cut(string, cut_all=True)  # 分词
    remove_words = [u'的', u'，', u'和', u'是', u'随着', u'对于', u'对', u'等', u'能', u'都', u'。', u' ', u'、', u'中', u'在', u'了',
                    u'通常', u'如果', u'我们', u'需要',u'',u'月','日','例']  # 自定义去除词库
    for word in mywordList:  # 循环读出每个分词
        if word not in remove_words:  # 如果不在去除词库中
            d1.append(word)  # 分词追加到列表

    # 词频统计
    word_counts = collections.Counter(d1)  # 对分词做词频统计
    d2 = word_counts.most_common(40)  # 获取前40最高频的词

    for i in d2:
        j=i[0]
        v=str(i[1]*10099)
        d.append({"name":j,"value":v})
    #print(d)  # 输出检查[('', 38), ('疫情', 10), ('月', 10), ('日', 9), ('10', 9), ('新', 8), ( <class 'list'>
                        #[{'name': '新冠', 'value': ''}, {'name': '疫苗', 'value': ''}, {'name': '启动', 'value': ''},
##############################################33


    # for i in data:
    #     k = i[0].rstrip(string.digits)  # 移除热搜数字
    #     v = i[0][len(k):]  # 获取热搜数字
    #     ks = extract_tags(k)  # 使用jieba 提取关键字
    #     for j in ks:
    #         if not j.isdigit():
    #             d.append({"name": j, "value": v})
    # print(type(d))
    return jsonify({"kws": d})


@app.route("/time")
def get_time():
    return utils.get_time()

@app.route('/ajax',methods=["get","post"])
def hello_world4():
    name = request.values.get("name")
    score =  request.values.get("score")
    print(f"name:{name},score:{score}")
    return '10000'

if __name__ == '__main__':
    app.run()
    #get_r2_data()
