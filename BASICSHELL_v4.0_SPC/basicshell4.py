#BASICSHELL 4.0 Chinese Edition
#Copyright© WRH
#Don't change this code
import time
import os

dirlog=True
notitle=False
nomultiuser=False
nobsui=False

print("Welcome to BASICSHELL")
print("Version 4.0")
print()
print("To specify advanced boot options, press Ctrl-C within three seconds")


try:
  time.sleep(3)
except KeyboardInterrupt:
  while True:
    if os.name=="nt":
      os.system("cls")
    else:
      os.system("clear")
    print("> Advanced boot options <\n")
    print("[1] Normal(Enter)")
    print("[2] Do not log in directly")
    print("[3] No title is set")
    print("[4] Multi-users are not allowed")
    print("[5] Disable BSUI")
    o=input()
    if o=="1" or o=="":
      break
    elif o=="2":
      dirlog=False
      break
    elif o=="3":
      notitle=True
      break
    elif o=="4":
      nomultiuser=True
      break
    elif o=="5":
      nobsui=True
      break
    else:
      input("Input Error")



if os.name=="nt":
   os.system("cls")
else:
   os.system("clear")


print("Loading BASICSHELL,please wait...")
print("Process:",end="",flush=True)



import os
import sys
import time
import platform
import struct
import socket

print(">",end="",flush=True)
def clear():#清屏
  if os.name=="nt":
    os.system("cls")
  else:
    os.system("clear")

def errno(code,cause):#报错
  clear()
  ui("BASICSHELL")
  print("出现问题,导致BASICSHELL意外退出")
  print("信息")
  print("停机码:",code,sep="")
  print("原因:",cause,sep="")
  print("解释器信息:",sys.exc_info(),sep="")
  print("请按回车退出")
  input()
  sys.exit()

print(">",end="",flush=True)    
    
#settings
    
#这里可以设置提示符
prompt="BASICSHELL -$"
print(">",end="",flush=True)
    
#这里可以设置二级提示符
prompt2="BASICSHELL 2nd -$"
print(">",end="",flush=True)
    
#这里可以设置默认的安全问题
question="1+1=？"
print(">",end="",flush=True)
    
#这里可以设置安全问题的答案
answer="2"
print(">",end="",flush=True)
    
#这里可以设置密码
s=""
print(">",end="",flush=True)
    
#这里可以设置是否允许有限设置
allow_restricted_functions=False
print(">",end="",flush=True)

#这里可以设置是否播放声音
sound=False
print(">",end="",flush=True)
    
#这里可以设置登录时是否进入BSUI
tobsui=True
print(">",end="",flush=True)




files={}#存储文件
print(">",end="",flush=True)
users={"system":""}#用户名
print(">",end="",flush=True)
current_user=""#当前用户
print(">",end="",flush=True)
admin=["system"]#管理员用户
print(">",end="",flush=True)
    
startsound=sound
print(">",end="",flush=True)
loginsound=sound
print(">",end="",flush=True)

while True:
  try:
    #program
    def wrhlogo():
      print("""
| | ||-\\| |
| | ||-/|-|
\\---/| \\| |
    """)

    def bsuilogo():
      print("""
/--WRH--\\  /------
|       |  |
|-------<  \\-----\\ |   | ---  |    |     /---\\
|        \\       | |   |  |   |    |     |   |
|        |       | |   |  |   \\----+-    |   |
\\--------/ ------/ \\---/ ---       |     |   |
                                   |  () \\---/
                                     4.0 中文版
""")

    def bsui():
      if nobsui:
        print("BSUI已经禁用")
        return -1
      while True:
        clear()
        bsuilogo()
        print("你好,",current_user,"!",sep="")
        print("欢迎您使用 BASICSHELL 4.0 BSUI!")
        print("为了最佳的显示效果,请将控制台窗口调大")
        print("主菜单:")
        print("1.CMD")
        print("2.PowerShell")
        print("3.BASICSHELL命令行")
        print("4.SHELLCMD")
        print("5.文件管理器")
        print("6.设置")
        print("7.用户管理器")
        print("8.锁定电脑")
        print("9.登录其它用户")
        print("10.退出BSUI")
        print("11.退出BASICSHELL")
        print("12.带提示退出BASICSHELL(Ctrl-C)")
        select=input()
        if select=="1":
          if os.name=="nt" or allow_restricted_functions:
            os.system("cmd")
          else:
            print("此功能只能在Windows下用")
        elif select=="2":
          if os.name=="nt" or allow_restricted_functions:
            os.system("powershell")
          else:
            print("此功能只能在Windows下用")
        elif select=="3":
          ui("BASICSHELL")
          print("请选择执行方式:")
          print("[1]终端")
          print("[2]单条命令")
          o=input()
          if o=="1":
            shell(True)
          elif o=="2":
            cmd=input("请输入命令行--->")
            do(cmd)
        elif select=="4":
          shellcmd()
        elif select=="5":
          filemgr()
        elif select=="6":
          settings()
        elif select=="7":
          if current_user in admin:
            usermgr()
          else:
            print("只能管理员使用")
        elif select=="8":
          if users[current_user]=="":
            ui("系统提示")
            print("当前用户未设置密码")
            print("你可以进入->设置->管理密码里面设置密码")
            print()
          else:
            password()
        elif select=="9":
          password()
        elif select=="10":
          break
        elif select=="11":
          sys.exit()
        elif select=="12":
          raise KeyboardInterrupt
        else:
          print("输入错误")
        input("请按回车键继续")
      clear()
        


    def eninfo():
      ui("环境信息")
      print("==操作系统信息")
      maxbit=sys.maxsize
      if maxbit>2**32:
        osbit="x64"
      else:
        osbit="x86"
      if struct.calcsize("P")==4:
        inbit="x86"
      else:
        inbit="x64"
      print("操作系统位数:       ",osbit,sep="\t")
      print("操作系统类型:       ",platform.system(),sep="\t")
      print("操作系统版本：       ",platform.platform(),sep="\t")
      print()
      print("==解释器信息")
      print("Python解释器版本:",sys.version,sep="\t")
      

      print("Python解释器位数:",inbit,sep="\t")
      print("Python解释器路径:",sys.executable,sep="\t")
      print("Python解释器目录:",os.path.dirname(sys.executable),sep="\t")
      print("Python解释器文件名:",os.path.basename(sys.executable),sep="\t")
      print()
      print("==电脑信息")
      print("用户名:           ",os.getenv(("USERNAME")),sep="\t")
      print("电脑名称:       ",socket.gethostname(),sep="\t")
      print("IP:             ",socket.gethostbyname(socket.gethostname()),sep="\t")
      input("请按回车继续")
      clear()
  
    def logo():
      print("""
/--WRH--\\   /----\\ /-----  --- /----- 
|       |   |    | |        |  |
|-------<   |----| \\-----\\  |  |                                         |    |     /---\\
|        \\  |    |       |  |  |        /-----  |    /---\\  |    |       |    |     |   |
|        |  |    |       |  |  |        \\----\\  |-\\  |---/  |    |       \\----+-    |   |
\\--------/  |    | ------/ --- \\-----   -----/  | |  \\----  \\--  \\--          |     |   |
                                                                              |  () \\---/
                                                                4.0  中文版
      """)
  
    def usermgr():
      global users
      global admin
      global current_user
      global nomultiuser
      while True:
        if nomultiuser:
          print("无法打开用户管理器,因为当前限制了多用户")
          return -1
        ui("用户管理器")
        print("当前现存的用户：")
        for a in users:
          print(a,end="")
          if a in admin:
            print("-管理员",end="")
          if a==current_user:
            print("-当前",end="")
          if a=="system":
            print("[系统用户]",end="")
          print()
  
        print("""
    请选择一个选项：
    1.创建用户
    2.删除用户
    3.赋予管理员权限
    4.撤销管理员权限
    其他 退出
        """)
        o=input()
        if o=="1":
          creatuser()
        elif o=="2":
          if len(users)==1:
            print("至少保留一个用户")
          else:
            delete_user=input("请输入要删除的用户--->")
            if delete_user=="system":
              print("system用户是必需的,不能删除")
            elif delete_user==current_user:
              print("要删除的用户是当前登录的用户，不能删除")
            else:
              if delete_user in users:
                sure=input("确定要删除吗？(Y/N)--->")
                if sure.lower()=="y":
                  del users[delete_user]
                  if delete_user in admin:
                    admin.remove(delete_user)
                  print("删除完成")
          input("请按回车键继续......")
        elif o=="3":
          _user=input("请输入用户名--->")
          if _user in users:
            if _user in admin:
              print("指定的用户已是管理员")
            else:
              admin.append(_user)
              print("赋予成功")
          else:
            print("找不到用户")
          input("请按回车键继续......")
        elif o=="4":
          if len(admin)==1:
            print("至少保留一个管理员")
          else:
            _user=input("请输入用户名--->")
            if _user in users:
              if _user=="system":
                print("system必须为管理员")
              else:
                if _user in admin:
                  admin.remove(_user)
                  print("撤销成功")
                else:
                  print("指定的用户不是管理员")
            else:
              print("找不到用户")
          input("请按回车键继续......")
            
        else:
          break
    def creatuser():
      global users
      ui("创建用户")
      print("欢迎使用创建用户向导")
      print("本向导将会帮助你创建一个新用户")
      print("\n注意,此操作只有管理员或system用户才能进行")
      print("\n若要继续,请按回车键继续")
      input()
      while True:
        ui("创建用户")
        newuser=input("请输入新用户的名字--->")
        if newuser!="":
          break
      while True:
        newuserpassword=input("请输入新用户的密码--->")
        if newuserpassword=="":
          break
        else:
          ui("创建用户")
          retype=input("请确认新用户的密码--->")
          if retype==newuserpassword:
            break
          else:
            print("密码不匹配")
      users[newuser]=newuserpassword
      ui("创建用户")
      print("你已成功地完成了创建用户向导")
      print("\n现在,你可以按回车键以退出此向导了")
      input()
  
  
    def edit(_retain=False,content=""):#文件编辑器
      str1=""
      a=[]
      print("输入OK完成编辑")
      print(content)
      while True:
        str1=input()
        if str1.lower()=="ok":
          break
        else:
          a.append(str1)
    
      result=""
      for b in a:
        result+=b+"\n"
      return result
  
    def filemgr():#文件管理器
      while True:
        cmd=input("Filemgr v1.2 "+prompt2).strip()
        if cmd=="exit":#退出程序
          break
        elif cmd.lower()=="create":#创建空文件
          filename=input("请输入新文件的名字--->")
          if filename!="":
            files[filename]=""
            doyouedit=input("创建成功,是否立即编辑？(Y/N)--->")
            if doyouedit.lower()=="y":
              files[filename]=edit()
          else:
            print("文件名不能为空")
  
  
        elif cmd.lower()=="delete":#删除文件
          filename=input("请输入文件名--->")
          for a in files:#检索文件
            if a==filename:
              del files[filename]#删除文件
              print("删除成功")
              break
          else:
            print("找不到文件")
        elif cmd.lower()=="edit":#编辑文件
          filename=input("请输入文件名--->")
          for a in files:#检索文件
            if a==filename:
              retain=input("要保留文件内容吗?(默认为不保留,Y=保留)")
              if retain.lower()=="y":
                files[filename]+=edit(content=files[filename])
              else:
                files[filename]=edit(True)#编辑文件
              print("编辑完成")
              break
          else:
            print("找不到文件")
        elif cmd.lower()=="view":
          filename=input("请输入文件名--->")
          for a in files:#检索文件
            if a==filename:
              print(files[filename])#显示文件内容
              break
          else:
            print("找不到文件")
        elif cmd.lower()=="ls":#检索文件
          print()
          for a in files:
            print(a)
          print("总共",len(files),"个文件",sep="")
        elif cmd.lower()=="help":
          print("""
    create 创建空文件
    delete 删除文件
    edit   编辑文件
    view   查看文件内容
    ls     检索文件
    search 查找文件
    rename 重命名文件
    about  关于FileMgr
    copy   创建文件副本
    help   显示此帮助
          """)
        elif cmd=="":#若命令为空，不执行
          pass
        elif cmd.lower()=="search":
          filename=input("请输入文件名--->")
          mode=input("请选择查找模式(1.全字模式,2.包括模式)--->")
          print("正在搜索......")
          matchfile=[]
          if mode=="1":
            for a in files:
              if filename==a:
                matchfile.append(a)
          elif mode=="2":
            for a in files:
              if filename in a:
                matchfile.append(a)
          print("总共找到",len(matchfile),"个文件",sep="")
          for a in matchfile:
            print(a)
        elif cmd.lower()=="rename":
          old_name=input("请输入文件名--->")
          if old_name in files:
            new_name=input("请输入文件的新名字--->")
            if new_name!="":
              temp=files[old_name]
              del files[old_name]
              files[new_name]=temp
            else:
              print("文件名不能为空")
          else:
            print("找不到文件")
        elif cmd.lower()=="about":
          logo()
          print("FileMgr v1.2 中文版")
          print("同BASICSHELL一起发行")
          print("版权归WRH所有")
          print("未经允许,不得拷贝此软件")
        elif cmd.lower()=="copy":
          filename=input("请输入文件的名字--->")
          if filename in files:
            copyname=input("请输入拷贝后的文件名--->")
            if copyname!="":
              files[copyname]=files[filename]
            else:
              print("文件名不能为空")
          else:
            print("找不到文件")

        else:
          print(cmd+"不是一个有效的命令")#报错
  
  
    def ui(title):#显示UI的标题
      clear()
      print(">",title,"<")
      print()
    
    def shellcmd():#SHELLCMD环境
      clear()
      print("""
    |———\\
    |   |
    |——<
    |   |
    |———/ASIC SHELLcmd v1.1
                            中文版
      """)
      while True:
        cmd=input("Shellcmd v1.1"+prompt2)
        if cmd=="exit":
          break
        elif cmd=="help":
          print("""
      在Shellcmd下，输入的每一行命令都是DOS/Unix/Linux命令
      输入exit退出，
      输入help显示此帮助。
        """)
        else:
          os.system(cmd)
      clear()
        
    def individualization():#个性化设置
      ui("个性化选项")
      print("""
      请输入数字选择选项：
      1.颜色个性化
      2.提示符自定义
      3.二级提示符自定义
      其他 退出
    """)
      str2=input()
      if str2=="1":#颜色个性化
        import os
        ui("控制台颜色设置")
        if os.name=="nt" or allow_restricted_functions:
          print("""
      请输入数字选择选项：
      1.黑底白字
      2.黑底绿字
      3.蓝底白字
      4.蓝底黄字
      5.自定义
    """)
          str2=input()
          if str2=="1":
            os.system("color 07")
          elif str2=="2":
            os.system("color 0a")
          elif str2=="3":
            os.system("color 1f")
          elif str2=="4":
            os.system("color 1e")
          elif str2=="5":
            ui("自定义颜色")
            print("""
      请根据这个规则表设置前景色和背景色
      0 黑色     8 灰色
      1 蓝色     9 淡蓝色
      2 绿色     A 淡绿色
      3 浅绿色   B 淡浅绿色
      4 红色     C 淡红色
      5 紫色     D 淡紫色
      6 黄色     E 淡黄色
      7 白色     F 亮白色
    """)
            foregroundcolor=input("请输入前景色--->")
            backgroundcolor=input("请输入背景色--->")
            color="color "+str(backgroundcolor)+str(foregroundcolor)
            os.system(color)
        else:
          print("这个功能只能在Windows系统上系统上使用，但是当前系统是",os.name,sep="")
      elif str2=="2":#设置提示符
        global prompt
        ui("设置提示符")
        prompt=input("输入提示符的样式--->")
      elif str2=="3":#设置二级提示符
        global prompt2
        ui("设置二级提示符")
        prompt2=input("输入二级提示符的样式--->")  
        
    def resetpassword(reset_user):#重置密码
      ui("重置密码")
      global users
      while True:
        psw5=input("请输入新密码--->")
        clear()
        retype2=input("请确认新密码--->")
        if retype2==psw5:
          users[reset_user]=psw5
          clear()
          break
        else:
          print("密码不匹配")
        
  
    
    def setquestion():#设置安全问题
      ui("设置安全问题")
      while True:
        global users
        global psw4
        global current_user
        psw4=input("请输入密码--->")
        if psw4==users[current_user]:
          break
        else:
          print("密码错误")
      global question
      global answer
      question=input("请输入安全问题--->")
      answer=input("请输入安全问题的答案--->")
    
    def soundsettings():
      global startsound
      global loginsound
      while True:
        ui("声音选项")
        print("1.启动声音 [",end="")
        if startsound==True:
          print("真]")
        else:
          print("假]")
        print("2.登录声音 [",end="")
        if loginsound==True:
          print("真]")
        else:
          print("假]")
        print("其他 退出")
        o=input()
        if o=="1":
          startsound=not startsound
        elif o=="2":
          loginsound=not loginsound
        else:
          break
      clear()

    def init():
      global users
      global prompt,prompt2,question,answer,s,allow_restricted_functions,sound,files,current_user,admin,startsound,loginsound,tobsui
      ui("初始化")
      print("欢迎使用初始化向导")
      print("本向导将会帮助你初始化BASICSHELL")
      print("\n注意:此操作只有system用户才能进行")
      print("\n若要继续,请输入yes(全部小写)后继续")
      sure=input()
      if sure=="yes":
        ui("初始化")
        if users["system"]=="":
          psw=""
        else:
          psw=input("请输入system用户的密码--->")
        if psw==users["system"]:
          ui("初始化")
          print("此操作将会更改以下内容:")
          print("--->删除所有用户")
          print("--->删除所有文件")
          print("--->还原所有设置")
          sure=input("确实要这样吗?(Y/N)--->")
          if sure.lower()=="y":
            ui("初始化")
            print("正在初始化......")
            prompt="BASICSHELL -$"
            prompt2="BASICSHELL 2nd -$"
            question="1+1=？"
            answer="2"
            s=""
            allow_restricted_functions=False
            sound=False
            files={}
            users={"system":""}
            current_user=""
            admin=["system"]    
            startsound=sound
            loginsound=sound
            tobsui=False
            ui("初始化")
            print("你已成功地完成了初始化向导")
            print("\n现在,你可以按回车键以退出此向导了")
            print("退出此向导后,BASICSHELL将重启")
            input()
            password()
          else:
            ui("初始化")
            print("你停止了初始化向导")
            print("\n按回车键以退出此向导")
            input()
        else:
          print("密码错误")
          input()
          ui("初始化")
          print("你停止了初始化向导")
          print("\n按回车键以退出此向导")
          input()
      else:
          ui("初始化")
          print("你停止了初始化向导")
          print("\n按回车键以退出此向导")
          input()






    def advanset():
      global allow_restricted_functions
      while True:
        ui("高级设置")
        print("1.允许不兼容的命令 [",end="")
 
        if allow_restricted_functions:
          print("真]")
        else:
          print("假]")
        print("2.初始化")
        o=input()
        if o=="1":
          if allow_restricted_functions==False:
            ui("警告")
            print("此选项会使命令不受平台限制,这样就可能会某些命令在其他平台上不可用")
            print("如果启用此选项,可能会损害你的系统")
            print("\n确定要继续吗?(Y/N)")
            sure=input()
            if sure.lower()=="y":
              allow_restricted_functions=True
          else:
            allow_restricted_functions=False
        elif o=="2":
          if current_user=="system":
            init()
          else:
            print("此操作只有system用户才能进行")
            input("请按下回车键继续")
        else:
          break
      clear()
            
      

    def settings():#设置
      global current_user
      ui("设置")
      print("""
      请输入数字选择选项：
      1.管理密码
      2.安全问题设置
      3.个性化
      4.用户管理
      5.声音管理
      6.高级
      7.BSUI设置
      其他 退出设置
    """)
      str1=input()
      if str1=="1":
        setpassword()
      elif str1=="2":
        setquestion()
      elif str1=="3":
        individualization()
      elif str1=="4":
        if current_user in admin:
          usermgr()
        else:
          print("此操作只有管理员才能进行")
      elif str1=="5":
        soundsettings()
      elif str1=="6":
        advanset()
      elif str1=="7":
        global tobsui
        while True:
          ui("BSUI设置")
          print("1.启动时自动进入BSUI [",end="")
          if tobsui:
            print("真]")
          else:
            print("假]")
          print("其他 退出")
          o=input()
          if o=="1":
            tobsui=not tobsui
          else:
            break

    
    def batch():#批量处理
      global batchs
      batch=""
      batchs=[]
      print("输入命令以实现批量执行，输入\"OK\"执行那些命令，输入\"del\"清除，输入\"exit\"退出")
      while not batch=="ok":
        batch=input(prompt2)
        if batch=="exit":
          batchs=[]
          break
        elif batch=="ok":
          break
        elif batch=="del":
          batchs=[]
        else:
          batchs.append(batch)
      for commands in batchs:
        do(commands.lower().strip())
    
  
    def setpassword():#密码设置界面
      global users
      global current_user
      ui("更改密码")
      print("欢迎使用更改密码向导")
      print("本向导将会帮助你更改密码")
      print("\n若要继续,请按回车键继续")
      input()
      while True:
        ui("更改密码")
        if users[current_user]=="":
          break
        oldpassword=input("请输入旧密码：")
        if oldpassword==users[current_user]:
          break
        else:
          print("密码错误")
          input("请按回车继续......")
      while True:
        ui("更改密码")
        newpassword=input("请输入新密码：")
        if newpassword=="":
          break
        ui("更改密码")
        retype=input("请确认新密码:")
        if newpassword==retype:
          break
        else:
          print("密码不匹配")
          input("请按回车继续......")
      users[current_user]=newpassword
      ui("更改密码")
      print("你已成功地完成了更改密码向导")
      print("\n现在,你可以按回车键以退出此向导了")
      input()
      clear()
  
        
    def calculator():#计算器
      try:
          a=int(input("输入一个数--->"))
      except ValueError:#输入保护机制
          print("输入内容不能为字符串")
          return 0
      try:
          ty=int(input("加法输入1，减法输入2，乘法输入3，除法输入4--->"))
      except ValueError:#输入保护机制
          print("输入内容不能为字符串")
          return 0
      try:
          b=int(input("输入另一个数--->"))
      except ValueError:
          print("输入内容不能为字符串")
          return 0
      if ty==1:
        print(a+b)
      elif ty==2:
        print(a-b)
      elif ty==3:
        print(a*b)
      elif ty==4:
        if b==0:
          print("除数不能为零")
        else:
          print(a/b)
    
    def tools():#小工具
      global current_user
      while True:
        com=input(current_user+"-Tools "+prompt2).lower().strip()
        if com=="time":#时间
          import time
          print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) )
        elif com=="exit":#退出
          print("正在退出......")
          break
        elif com=="titicks":#时间戳
          import time
          print(time.time())
        elif com=="calc":#简易计算器
          calculator()
        elif com=="acalc":#高级计算器
          print(eval(input("请输入算式--->")))
        elif com=="":#如果命令为空，不执行任何命令
          pass
        elif com=="timer":#计时器
          import time
          try:
              ti=int(input("输入时间--->"))
          except ValueError:#输入保护机制
              print("输入内容不能为字符串")
          else:
              print("\r",ti,"              ",sep="",end="")
              for time2 in range(ti-1,0,-1):
                time.sleep(1)
                print("\r",time2,"              ",sep="",end="")
              time.sleep(1)
              print("\r",0,"              ",sep="",end="")

              print()
        elif com=="help":#显示帮助
          print("""
      小工具
      time 时间
      exit 退出小工具
      titicks 时间戳
      calc 简易计算器
      acalc 高级计算器
      timer 计时器
      help 查看此帮助
        """)
    
    def do(c):#主要命令处理程序
      global users
      global current_user
      global nomultiuser
      if c=="tool"or c=="tools":#小工具
        tools()
      elif c=="":#若命令为空，不执行
        pass
      elif c=="about":#关于
        ui("关于BASICSHELL")
        wrhlogo()
        logo()   
        print("""         
      BASICSHELL 4.0 中文版
      版本 4.0
      版权归WRH所有
      未经允许,不得拷贝此软件
              
      注意:从2023年起,软件的制作者由WRH署名
        """)
        input("请按回车继续......")
        clear()
      elif c=="lock":#锁定
        global users
        global current_user
        if users[current_user]=="":
          print("lock:未设置密码")
        else:
          clear()
          print("已锁定")
          password()
      elif c=="help":#帮助
        print("""
        tool(s)    小工具
        about      关于Basic Shell
        lock       锁定
        help       查看帮助
        exit       退出程序
        exitprompt 带提示退出(Ctrl-C)
        batch      批量执行
        settings   系统设置
        cmd        跟Windows命令提示符交互
        powershell 跟Windows Powershell交互
        shell      运行DOS/Unix/Linux命令
        clear      清屏
        shellcmd   系统shell环境
        filemgr    文件管理器
        whoami     查看当前登录的用户
        admin      查看当前用户是否为管理员
        login      登录其他用户
        bsui       BASICSHELL 4.0 BSUI""",end="")
        if nomultiuser:
          print("[不可用]",end="")
        print("""
        usermgr    用户管理器(只能管理员使用)""",end="")
        if current_user not in admin or nomultiuser:
          print("[不可用]",end="")
        print("""
        ver        系统版本
        userinfo   用户信息""",end="")
        if nomultiuser:
          print("[不可用]",end="")
        print("""
        eninfo     环境信息
        """)
      elif c=="batch":#批量处理程序
        batch()
      elif c=="settings":#设置界面
        settings()
      elif c=="cmd":#与命令提示符交互
        import os
        if os.name=="nt" or allow_restricted_functions:#检测系统
          print("正在与Windows命令提示符交互......")
          os.system("cmd")
        else:
          print("这个功能只能在Windows系统上系统上使用，但是当前系统是",os.name,sep="")
      elif c=="powershell":
        import os
        if os.name=="nt" or allow_restricted_functions:#检测系统
          print("正在与Windows Powershell交互......")
          os.system("powershell")
        else:
          print("这个功能只能在Windows系统上系统上使用，但是当前系统是",os.name,sep="")
      elif c=="shell":#执行DOS/Unix/Linux命令
        import os
        os.system(input("请输入运行DOS/Unix/Linux命令--->"))
      elif c=="clear":#清屏
        clear()
      elif c=="shellcmd":#SHELLCMD环境
        shellcmd()
      elif c=="filemgr":
        filemgr()
      elif c=="whoami":
        print(current_user)
      elif c=="login":
        if nomultiuser==False:
          password()
        else:
          print("命令不可用,因为已经禁用了多用户")
      elif c=="admin":
        if current_user in admin:
          print("真")
        else:
          print("假")
      elif c=="usermgr":
        if current_user in admin:
          usermgr()
        else:
          print("此操作只有管理员才能进行")
      elif c=="ver":
        print("BASICSHELL v4.0 中文版")
      elif c=="userinfo":
        if nomultiuser==False:
          ui("用户信息")
          print("当前登录的用户:",current_user,sep="")
          print("是否为管理员:",end="")
          if current_user in admin:
            print("是")
          else:
            print("否")
          print("用户级别:",end="")
          if current_user=="system":
            print("系统用户")
          elif current_user in admin:
            print("管理员用户")
          else:
            print("普通用户")
          input("请按回车键继续......")
          clear()
        else:
          print("命令不可用,因为已经禁用了多用户")
      elif c=="exitprompt":
        raise KeyboardInterrupt
      elif c=="eninfo":
        eninfo()
      elif c=="bsui":
        bsui()
      else:#报错
        print(c+"不是一个有效的命令")
    
    def shell(a=False):#命令行部分
      clear()
      global tobsui
      if tobsui and not(nobsui) and not(a):
        bsui()
      global current_user
      global loginsound
      if loginsound:
        print("\a",end="")
      logo()
      if allow_restricted_functions:
        print("来自BASIC SHELL的通知：现已允许受限功能，将允许只能在Microsoft Windows下使用的功能，如果在除Windows外执行，则可能在这个系统上不可用。\n")
      print("--->输入help以查看帮助")
      while True:
        command=input(current_user+"-"+prompt).lower().strip()
        if command.lower()=="exit":#退出程序
          print("正在退出......")
          sys.exit()
        else:
          do(command.lower())
    
    def password():#登录界面
      clear()
      
      if users=={}:
        print("首次使用时必须创建用户")
        input("请按回车继续......")
        creatuser()
        admin.append(users[0])
      wrhlogo()
      logo()
      print("提示：输入密码时可以输入forget,用来重置密码。")
      print("如果要退出BASICSHELL,请按Ctrl-C(不是像以前一样输入exit)")
      while True:
        global current_user
        if len(users)!=1 or not(dirlog):
          print("现存用户：")
          for a in users:
            print(a,end="")
            if a in admin:
              print("[管理员]",end="")
            if a=="system":
              print("[系统用户]",end="")
            print()
          print()
        if len(users)==1 and dirlog:
          logon_user=list(users)[0]
        else:
          logon_user=input("用户名：")

        if logon_user in users:
          if users[logon_user]=="":
            current_user=logon_user
            clear()
            shell()
          else:
            logon_user_password=input("密码:")
            if users[logon_user]==logon_user_password:
              current_user=logon_user
              clear()
              shell()
            elif logon_user_password=="forget":
              global question
              global answer
              ui("回答安全问题")
              print("问:"+question)
              a=input("答:")
              if a==answer:
                resetpassword(logon_user)
              else:
                print("回答错误")
            else:
              print("密码不正确")
        else:
          print("用户不存在")
  
    print(">>>>>>>>>>>>>>>>>>>>>>>",end="",flush=True)
    if not notitle:
      os.system("cmd.exe /c title BASICSHELL")
    if startsound:
      print("\a",end="")


    clear()
    password()
  
  except KeyboardInterrupt:#以下是异常处理
      try:
        ui("退出BASICSHELL")
        print("你希望BASICSHELL做什么?")
        print("[Ctrl-C] 退出BASICSHELL")
        print("[Enter]  返回BASICSHELL")
        input()
      except KeyboardInterrupt:
        print("程序退出")
        sys.exit()
  except ZeroDivisionError:
      errno("0x000000A","The divisor cannot be zero")
  except ValueError:
      errno("0x0000010","Python:ValueError")
  except NameError:
      errno("0x0000011","Python:NameError")
  except TypeError:
      errno("0x0000012","Python:TypeError")
  except SyntaxError:
      errno("0xFFFFFFFF","Internal error")
  except EOFError:
      errno("0x0000021","End Of File(EOF)")
  except OSError:
      errno("0x0000022","Python:OSError")
  except SystemError:
      errno("0x0000022","Python:ValueError")
  except IndentationError:
      errno("0xFFFFFFFF","Internal error")
  except AttributeError:
      errno("0x0000013","Python:AttributeError")
  except IndexError:
      errno("0x0000014","Python:IndexError")
  except KeyError:
      errno("0x0000015","Python:KeyError")
  except TabError:
      errno("0x0000015","Python:TabError")
  except SystemExit:
      print("程序退出")
      sys.exit()