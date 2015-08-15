#coding:utf-8

import json
import requests

def translate(type,sentence):
    url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule&smartresult=ugc'
    data = {
        'type':type,
        'i':sentence,
        'doctype':'json',
        'xmlVersion':'1.8',
        'keyfrom':'fanyi.web',
        'ue':'UTF-8',
        'action':'FY_BY_CLICKBUTTON',
        'typoResult':'true'
    }
    content = requests.post(url,data).content
    mydict = json.loads(content)
    return mydict.get('translateResult')[0][0].get('tgt')

def change_type(order):
        if order == '_auto':
            type = 'AUTO'
            print u'已切换到自动检测模式'
        if order == '_zy':
            type = 'ZH_CN2EN'
            print u'已切换到中译英模式'
        if order == '_zr':
            type = 'ZH_CN2JA'
            print u'已切换到中译日模式'
        if order == '_zh':
            type = 'ZH_CN2KR'
            print u'已切换到中译韩模式'
        if order == '_zf':
            type = 'ZH_CN2FR'
            print u'已切换到中译法模式'
        if order == '_ze':
            type = 'ZH_CN2RU'
            print u'已切换到中译俄模式'
        if order == '_zx':
            type = 'ZH_CN2RU'
            print u'已切换到中译西模式'
        if order == '_yz':
            type = 'CN2EN_ZH'
            print u'已切换到英译中模式'
        if order == '_rz':
            type = 'CN2JA_ZH'
            print u'已切换到日译中模式'
        if order == '_hz':
            type = 'CN2KR_ZH'
            print u'已切换到韩译中模式'
        if order == '_fz':
            type = 'CN2FR_ZH'
            print u'已切换到法译中模式'
        if order == '_ez':
            type = 'CN2RU_ZH'
            print u'已切换到俄译中模式'
        if order == '_xz':
            type = 'CN2SP_ZH'
            print u'已切换到西译中模式'
        return type
if __name__ == '__main__':
    menu = u'【翻译模式切换指令】\n'\
           u'自动检测：_auto、中译英：_zy、中译日：_zr、中译韩：_zh、中译法：_zf、中译俄：_ze、中译西：_zx\n' \
           u'自动检测：_auto、英译中：_yz、日译中：_rz、韩译中：_hz、法译中：_fz、俄译中：_ez、西译中：_xz'
    print menu
    print u'请输入翻译模式(默认使用自动检测模式)：',
    type = raw_input()
    if type in ['_auto','_zy','_zr','_zh','_zf','_ze','_zx','_yz','_rz','_hz','_fz','_ez','_xz']:
            type = change_type(type)
    else:
        type = 'AUTO'
        print u'输入错误，默认使用自动检测模式。'
    while True:
        print u'【输入_quit退出,输入_menu显示切换指令,可随时输入指令以切换翻译模式】请输入需要进行翻译的句子：'
        sentence = raw_input().decode('GBK') #####此处要记得转换成GBK,否则乱码。
        if sentence == '_quit':
            print '程序已退出'
            break
        if sentence == '_menu':
            print menu
            continue
        if sentence == '':
            print '不能为空！请重新输入！'
            continue
        if sentence in ['_auto','_zy','_zr','_zh','_zf','_ze','_zx','_yz','_rz','_hz','_fz','_ez','_xz']:
            type = change_type(sentence)
        else:
            print translate(type,sentence)
