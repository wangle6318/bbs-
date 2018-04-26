from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .forms import *
import json, re, random, time, os
from django.core.mail import send_mail
from django.contrib.auth.backends import ModelBackend
from django.http import StreamingHttpResponse


# Create your views here.

def getIndexContent():
    newc = Articles.objects.all()[:8]
    hotc = Articles.objects.order_by("-views")[:8]
    tag = Category.objects.order_by("created_time").all()
    f1 = CarouselImg.objects.get(id=1)
    f2 = CarouselImg.objects.get(id=2)
    f3 = CarouselImg.objects.get(id=3)
    f4 = CarouselImg.objects.get(id=4)
    newf = {"newc": newc, "hotc": hotc, "tags": tag, "f1": f1, "f2": f2, "f3": f3, "f4": f4}
    return newf


def homepage(request):
    newc = getIndexContent()
    return render(request, 'article/index.html', newc)


def user_login(request):
    reg_form = RegisterForm()
    code_form = IdenCodeForm()
    if request.method == "POST":
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            cd = login_form.cleaned_data
            user = authenticate(username=cd['user_name'], password=cd['password'])
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('../')
            else:
                err_msg = '1'
                return render(request, "article/register.html",
                              {"form": login_form, "err": err_msg,"regForm": reg_form, "codeForm": code_form})
        else:
            err_msg = '1'
            return render(request, "article/register.html",
                          {"form": login_form, "err": err_msg,"regForm": reg_form, "codeForm": code_form})
    if request.method == "GET":
        login_form = LoginForm()
        err_msg = '5'
        return render(request, "article/register.html",
                      {"form": login_form, "err":err_msg, "regForm": reg_form, "codeForm": code_form})


@login_required(login_url='register/login')
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('../')


def iden_code_data():
    lowercase = 'abcdefghijklmnopqrstuvwxyz'
    uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numcase = '0123456789'
    i = 0
    code_data = ''
    while i < 6:
        num = random.choice([0, 1, 2])
        if num == 0:
            code = random.choice(lowercase)
        elif num == 1:
            code = random.choice(uppercase)
        else:
            code = random.choice(numcase)
        code_data += code
        i += 1
    return code_data


def post_email(request):
    if request.method == "POST":
        username = request.POST.get('name')
        email_addr = request.POST.get('email')
        str = r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
        if re.match(str, email_addr) is None:
            status = '0'
            return HttpResponse(json.dumps({"status": status}))
        else:
            status = '2'
            code_data = iden_code_data()
            request.session[username] = code_data
            request.session.set_expiry(60 * 5)
            message = '\n\n师生互动社区注册验证码是：' + code_data + '\n有效时间5分钟，超时需重新获取验证码\n如非本人操作，请勿泄露！'
            send_mail('师生互动社区注册验证码', message, 'leowle@126.com', [email_addr], fail_silently=False)
            return HttpResponse(json.dumps({"status": status}))


def register(request):
    login_form = LoginForm()
    if request.method == "GET":
        reg_form = RegisterForm()
        code_form = IdenCodeForm()
        return render(request, "article/register.html",
                      {"regForm": reg_form, "codeForm": code_form,"form": login_form})
    elif request.method == "POST":
        reg_form = RegisterForm(request.POST)
        code_form = IdenCodeForm(request.POST)
        if reg_form.is_valid() * code_form.is_valid():
            cd = code_form.cleaned_data['iden_code']
            try:
                if cd == request.session[reg_form.cleaned_data['username']]:
                    del request.session[reg_form.cleaned_data['username']]
                    newuser = reg_form.save(commit=False)
                    newuser.set_password(reg_form.cleaned_data['password'])
                    newuser.save()
                    PersonalInfo.objects.create(user=newuser)
                    err_msg = '3'
                    return render(request, "article/register.html",
                                  {"regForm": reg_form, "codeForm": code_form, "err": err_msg,"form": login_form})
                else:
                    del request.session[reg_form.cleaned_data['username']]
                    err_msg = '2'
                    return render(request, "article/register.html",
                                  {"regForm": reg_form, "codeForm": code_form, "err": err_msg,"form": login_form})
            except Exception as e:
                print(e)
                err_msg = '4'
                return render(request, "article/register.html",
                              {"regForm": reg_form, "codeForm": code_form, "err": err_msg,"form": login_form})
        else:
            err_msg = '4'
            return render(request, "article/register.html",
                          {"regForm": reg_form, "codeForm": code_form, "err": err_msg,"form": login_form})


def post_email_login(request):
    if request.method == 'POST':
        username = request.POST.get('name')
        try:
            status = '1'
            email_addr= User.objects.get(username__exact=username).email
            code_data = iden_code_data()
            request.session[username] = code_data
            request.session.set_expiry(60 * 5)
            message = '\n\n师生互动社区登陆验证码是：' + code_data + '\n有效时间5分钟，超时需重新获取验证码\n如非本人操作，请勿泄露！'
            send_mail('师生互动社区注册验证码', message, 'leowle@126.com', [email_addr], fail_silently=False)
            return HttpResponse(json.dumps({"status": status}))
        except User.DoesNotExist:
            status = '0'
            return HttpResponse(json.dumps({"status": status}))


class EmailBackend(ModelBackend):
    def authenticate(self, request, username=None, cd=None, rcd=None, **kwargs):
        try:
            user = User.objects.get(username=username)
            if cd == rcd:
                return user
        except Exception as e:  #可以捕获除与程序退出sys.exit()相关之外的所有异常
            print(e)
            return None


def emailLogin(request):
    if request.method == 'GET':
        emaiLoForm = EmailLoginForm()
        return render(request, "article/emailfind.html", {"emaiLoForm": emaiLoForm})
    if request.method == 'POST':
        emaiLoForm = EmailLoginForm(request.POST)
        if emaiLoForm.is_valid():
            cd = emaiLoForm.cleaned_data['code']
            rcd = request.session[emaiLoForm.cleaned_data['user_name']]
            del request.session[emaiLoForm.cleaned_data['user_name']]
            user = authenticate(username=emaiLoForm.cleaned_data['user_name'], cd=cd, rcd=rcd)
            if user is not None and user.is_active:
                login(request, user)
                return HttpResponseRedirect('../')
            else:
                errmsg = '1'
                return render(request, "article/emailfind.html",
                              {"emaiLoForm": emaiLoForm, "err": errmsg})
        else:
            errmsg = '0'
            return render(request, "article/emailfind.html",
                          {"emaiLoForm": emaiLoForm, "err": errmsg})


def handle_upload_file(file):
    timenow = time.localtime(time.time())
    timenow = time.strftime("%Y-%m-%d",timenow)
    path='media/'+str(timenow) + "/"
                                      #上传文件的保存路径，可以自己指定任意的路径
    savepath = str(timenow)+"/"
    if not os.path.exists(path):
        os.makedirs(path)
    with open(path + file.name, 'wb+')as destination:
        for chunk in file.chunks():
            destination.write(chunk)
    return savepath+file.name


@login_required(login_url='register/login')
def publishArticle(request):
    if request.method == 'GET':
        pform = AriclesForm()
        return render(request, "article/newarticle.html", {"pform": pform})
    if request.method == 'POST':
        pform = AriclesForm(request.POST, request.FILES)
        if pform.is_valid():
            title = pform.cleaned_data['title']
            category = pform.cleaned_data['category']
            abstract = pform.cleaned_data['abstract']
            attachment = pform.cleaned_data['attachment']
            body = pform.cleaned_data['body']
            article = Articles()
            article.title = title
            article.author_id = request.user.id
            article.category = category
            article.abstract = abstract
            myfile = request.FILES.get("attachment", None)
            if myfile:
                attachment = handle_upload_file(myfile)
            article.attachment = attachment
            article.body = body
            article.save()
            return HttpResponseRedirect('../')
        else:
            return render(request, "article/newarticle.html", {"pform": pform})


def article(request,article_id):
    artcon = Articles.objects.get(id=article_id)
    artcon.views += 1
    artcon.save()
    comments = Comments.objects.filter(artid=article_id)
    reply = CommentsReply.objects.filter(art_id=article_id)
    path = str(artcon.attachment)
    filename = None
    fp = False
    if path:
        filename = path.split("/")[1]
        filetype = filename.split(".")[1]
        if filetype == 'pdf':
            fp = True
    is_collected = False
    if(artcon.collects.filter(id=request.user.id)):
        is_collected = True
    art = {
        "art": artcon,
        "is_collected": is_collected,
        "filename": filename,
        "ft": fp,
        "comments": comments,
        "reply": reply
    }
    return render(request, "article/showarticle.html", art)


def category(request,category_id):
    listobj = Articles.objects.filter(category_id=int(category_id))
    tag = Category.objects.order_by("created_time").all()
    return render(request, "article/showartlist.html", {"artlist": listobj, "tags": tag})


@login_required(login_url='register/login')
def collected(request):
    if request.method == 'POST':
        user_id = request.user.id
        article_id = int(request.POST.get('article'))
        article = Articles.objects.get(id=article_id)
        if (article.collects.filter(id=user_id)):
            article.collects.remove(request.user)
            status = '0'
        else:
            article.collects.add(request.user)
            status = '1'
        return HttpResponse(json.dumps({"status": status}))


@login_required(login_url='register/login')
def getmyarticle(request):
    listobj = Articles.objects.filter(author_id=request.user.id)
    return render(request, "article/myarticle.html", {"artlist": listobj})


@login_required(login_url='register/login')
def getmycollect(request):
    aid = User.objects.get(id=request.user.id)
    listobj = aid.articles_set.all()
    return render(request, "article/mycollect.html", {"artlist": listobj})


@login_required(login_url='register/login')
def myinfo(request):
    if request.method == 'GET':
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        username = user.username
        email = user.email
        userperson = PersonalInfo.objects.get(user_id=user)
        sex = userperson.sex
        born = userperson.born.strftime("%Y-%m-%d")
        intro = userperson.intro
        college = userperson.college
        data = {
            "username": username,
            "email": email,
            "sex": sex,
            "born": born,
            "intro": intro,
            "college": college
        }
        inForm = PersonalInfoForm(data)
        return render(request, "article/myinfo.html", {"info": inForm})
    if request.method == 'POST':
        inForm = PersonalInfoForm(request.POST)
        if inForm.is_valid():
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            userperson = PersonalInfo.objects.get(user_id=user)
            info = inForm.cleaned_data
            user.email = info['email']
            user.save()
            userperson.sex = info['sex']
            userperson.born = info['born']
            userperson.born = info['born']
            userperson.intro = info['intro']
            userperson.college = info['college']
            userperson.save()
        return render(request, "article/myinfo.html", {"info": inForm})


def readFile(filename,chunk_size=512):
    with open(filename,'rb') as f:
        while True:
            c=f.read(chunk_size)
            if c:
                yield c
            else:
                break


def downloadfile(request,article_id):
    filename = 'media/' + str(Articles.objects.get(id=article_id).attachment)
    thefilename = filename.split("/")[2]
    response = StreamingHttpResponse(readFile(filename))
    response['Content-Type'] = 'application/octet-stream'
    response['Content-Disposition'] = 'attachment;filename="{0}"'.format(thefilename)
    return response



def submit_comment(request):
    if request.method == 'POST':
        user_id = request.user.id
        article_id = int(request.POST.get('article'))
        artcon = Articles.objects.get(id=article_id)
        artcon.comments += 1
        artcon.save()
        content = request.POST.get('content')
        comments = Comments()
        comments.artid_id = article_id
        comments.author_id = user_id
        comments.content = content
        comments.save()
        status = '1'
        return HttpResponse(json.dumps({"status": status}))


def submit_reply(request):
    if request.method == 'POST':
        user_id = request.user.id
        article_id = int(request.POST.get('article'))
        artcon = Articles.objects.get(id=article_id)
        artcon.comments += 1
        artcon.save()
        comment_id = int(request.POST.get('comment'))
        author_to = int(request.POST.get('author_to'))
        content = request.POST.get('content')
        if(user_id == author_to):
            status = '0'
        else:
            status = '1'
            reply = CommentsReply()
            reply.content = content
            reply.art_id_id = article_id
            reply.author_id_id = user_id
            reply.author_to_id = author_to
            reply.comment_id = comment_id
            reply.save()
        return HttpResponse(json.dumps({"status": status}))


def search(request):
    words = request.POST['words']
    listobj = Articles.objects.filter(Q(title__icontains=words) | Q(abstract__icontains=words) | Q(body__icontains=words))
    return render(request, "article/search.html", {"artlist": listobj})


@login_required(login_url='register/login')
def resetpwd(request):
    if request.method == 'GET':
        user = User.objects.get(id=request.user.id)
        username = user.username
        data = {
            "username": username,
            "password": "",
            "cpassword": ""
        }
        resetForm = ResetPwdForm(data)
        return render(request, "article/resetpwd.html", {"rpwd": resetForm})
    elif request.method == 'POST':
        resetForm = ResetPwdForm(request.POST)
        if resetForm.is_valid():
            user = User.objects.get(id=request.user.id)
            username = resetForm.cleaned_data['username']
            pwd1 = resetForm.cleaned_data['password']
            pwd2 = resetForm.cleaned_data['cpassword']
            if(pwd1 == pwd2):
                user.set_password(pwd2)
                user.save()
                user = authenticate(username=username, password=pwd2)
                if user is not None and user.is_active:
                    login(request, user)
                    return HttpResponseRedirect('../')
            return render(request, "article/resetpwd.html", {"rpwd": resetForm})
        return render(request, "article/resetpwd.html", {"rpwd": resetForm})