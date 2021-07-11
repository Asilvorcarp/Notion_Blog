from genericpath import isdir
import os
import zipfile
import datetime as dt
import urllib.parse as parse #for uni2ascii

root_path = "./" #待处理的目录路径
include_str = ".zip" #待搜索的名称
decode_type = 'utf-8' #md的编码格式
bool_delete_zip = True # 处理后是否删去zip

def get_pagename(md_name):
    #从输出的md文件读出真实文件名
    for i,c in enumerate(md_name[::-1]):
        if(c==' '):
            last=len(md_name)-i-1
            break
    return md_name[0:last]

def uni2ascii(uni):
    #unicode转为类似%23%21这样的浏览器传输格式
    return parse.quote(uni, encoding="UTF-8")

def add_to_top(file_name, top_lines):
    #追加top_lines到file的开头
    with open(file_name, 'r', encoding=decode_type) as f:
        lines = f.readlines()
    with open(file_name, 'w', encoding=decode_type) as n:
        n.writelines(top_lines + lines)

def findfiles(files_path, files_list):
    #查找文件代码 结果保存在files_list
    files = os.listdir(files_path)
    for s in files:
        s_path = os.path.join(files_path, s)
        if os.path.isdir(s_path):
            findfiles(s_path, files_list)
        elif os.path.isfile(s_path) and include_str in s:
            files_list.append(s_path)

'''
基本格式：zipfile.ZipFile(filename[,mode[,compression[,allowZip64]]])
mode：可选 r,w,a 代表不同的打开文件的方式；r 只读；w 重写；a 添加
compression：指出这个 zipfile 用什么压缩方法，默认是 ZIP_STORED，另一种选择是 ZIP_DEFLATED；
allowZip64：bool型变量，当设置为True时可以创建大于 2G 的 zip 文件，默认值 True；
'''
def extract_zip(zip_full_name,extract_folder):
    #解压指定zip到指定文件夹，返回所有文件的list
    zip_file = zipfile.ZipFile(zip_full_name)
    zip_list = zip_file.namelist() #得到压缩包里所有文件
    for f in zip_list:
        zip_file.extract(f, extract_folder) #循环解压文件到指定目录
    zip_file.close() #关闭文件，必须有，释放内存
    return zip_list

def get_longname_from_list(notion_ext_list):
    for s in notion_ext_list:
        if '.md' in s and not ('/' in s): #todo以后改成远路径之后换成/最小的那个文件 或者其实解压的第一个一般就是md
            l=len(s)
            return s[:l-3]

def change_names_of_folderandmd(oldname,newname):
    #rename folderAndMd
    if os.path.isdir(oldname):
        os.rename(oldname,newname)
    if os.path.isfile(oldname+'.md'):
        os.rename(oldname+'.md',newname+'.md')

def replace_str_infile(filename,oldstr,newstr):
    #替换文件中的字符串 # 目前仅支持在一行的准确替换
    newlines = []
    with open(filename, 'r', encoding=decode_type) as f:
        lines = f.readlines()
    for line in lines:
        line=line.replace(oldstr,newstr)
        newlines.append(line)
    with open(filename, 'w', encoding=decode_type) as n:
        n.writelines(newlines)

def get_top_lines(pagename):
    #title, date, typora
    top_lines = ['---\n']
    top_lines += ['title: '+pagename+'\n']
    now_time = dt.datetime.now().strftime('%F %T') #todo或许改进成可以自己设定时间
    top_lines += ['date: '+now_time+'\n']
    top_lines += ['typora-root-url: '+pagename+'\n']
    top_lines += ['---\n']
    return top_lines

def modify_md(pagename,longname):
    #处理md文件
    mdname=pagename+'.md'
    replace_str_infile(mdname,uni2ascii(longname)+'/','') #考虑到了转为浏览器传输格式
    top_lines=get_top_lines(pagename)
    add_to_top(mdname,top_lines)

def cope_with_one_zip(zip_full_name):
    #为blog处理一个notionZip
    ext_list=extract_zip(zip_full_name,root_path)
    longname=get_longname_from_list(ext_list)
    pagename=get_pagename(longname)
    change_names_of_folderandmd(longname,pagename)
    modify_md(pagename,longname)

def cope_with_all_zips(inpath):
    #处理指定路径下的所有zip
    zips = [] #定义保存结果的数组
    findfiles(inpath,zips)
    for zip in zips:
        cope_with_one_zip(zip)
        if bool_delete_zip:
            os.remove(zip)
        print('Done '+zip)


cope_with_all_zips(root_path)
