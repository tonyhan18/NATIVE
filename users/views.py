from django.shortcuts import redirect, render,get_object_or_404
from .models import Users

def login(req):
    return render(req,'users/login.html')

def signup(req):
    if(req.method=='GET'):
        return render(req,'users/signup.html')
    elif(req.method=='POST'):
        username = req.POST.get('')

    return render(req,'users/signup.html')

def signup_verification(req):
    if(req.method == 'GET'):
        return redirect('/users/signup')
    elif(req.method=='POST'):
        userId = req.POST['uid']
        userPw = req.POST['upw']
        userNa = req.POST['una']
        userAd = req.POST['uad']
        userPh = req.POST['uph']

        try:
            userTemp = Users.objects.get(userId=userId)
        except:
            userTemp=None

        err={}
        if(userTemp and userTemp.userId == userId):
            err['err']='중복된 ID 입니다.'
            return render(req,'users/signup.html',err)
        else:
            users=Users(
                userId=userId,
                userPw=userPw,
                userName=userNa,
                userAddress=userAd,
                userPhone=userPh
            )
            users.save()
            return redirect('/users/signup/verify/success')
    return redirect('/users/signup')

def signup_success(req):
    return render(req,'users/signup_success.html')

def login_verification(req):
    #print(dir(req))
    if(req.method=='GET'):
        return redirect('/login')
    elif(req.method=='POST'):
        #유저 email이 제대로 들어오지 않아도 표현은 된다.
        userId = req.POST.get('uid', None)
        userPw = req.POST.get('upw', None)
        
        try:
            userObjId = Users.objects.get(userId=userId)
        except:
            userObjId=None
        if not userObjId or userId != userObjId.userId:
            return render(req,"users/login.html",{'errId':'아이디가 존재하지 않습니다.'})
        elif userPw != userObjId.userPw:
            return render(req,"users/login.html",{'errPw':'비밀번호가 틀렸습니다.'})
        else:
            req.session['user']=userObjId.userId
            return redirect('/')
    return redirect('/')