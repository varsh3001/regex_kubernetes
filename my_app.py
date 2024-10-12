from flask import Flask,render_template,request,redirect,url_for

import re
#create a flask object
my_app=Flask(__name__)

#create a route for home page
@my_app.route('/',methods=["GET","POST"])
def index():
  matches=[]
  regex=''
  tst_string=''
  if request.method=='POST':
    regex=request.form.get('reg')
    tst_string=request.form.get('test_string')
    if tst_string and regex:
      try:
        pattern = re.compile(regex,re.IGNORECASE)
        ans = pattern.finditer(tst_string)
        for i in ans:
            matches.append(i.group())
      except re.error:
        matches.append("Invalid Regular Expression.")
  return render_template("home_page.html",matches=matches,regex=regex,tst_string=tst_string)



#create another route for email validation
@my_app.route('/email_validation',methods=['GET','POST'])
def email_func():
  validity=None
  res_mail=''
  if request.method=="POST":
    res_mail=request.form.get("email")
    if res_mail:
      pattern_mail=r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
      ans=re.search(pattern_mail,res_mail)
      if ans:
        validity=True
      else:
        validity=False
  return render_template('email_val.html',validity=validity,res_mail=res_mail)


  
#run the app
if __name__=='__main__':
  my_app.run(debug=True,host='0.0.0.0',port=5000)