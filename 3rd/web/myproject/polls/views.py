from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Question, Choice, User
import json
# Create your views here.

# def index(request):
#     question_list = Question.objects.all()
#     return render(request, 'index.html', {'q': question_list})


def index(request):
    question_list = Question.objects.all()
    datas = {}
    re = {} #return result, code status and so on
    if question_list:
        for q in question_list:
            datas[q.id] = q.question_text
        re['status'] = '200'
        re['message'] = 'success'
        re['data'] = datas
        r = json.dumps(re)
        return HttpResponse(r)
    else:
        re['status'] = '10021'
        re['message'] = 'null'
        re['data'] = datas
        r = json.dumps(re)
        return HttpResponse(r)

#显示某个问题下的选项
# def detail(request, question_id):
#     q = get_object_or_404(Question,pk=question_id)
#     return render(request, 'detail.html', {'question': q})

def detail(request, question_id):
    choices = Choice.objects.filter(question_id=question_id)
    datas = {}
    re = {}
    if choices:
        for q in choices:
            datas[q.id] = q.choice_text
        re['status'] = '200'
        re['message'] = 'success'
        re['data'] = datas
        r = json.dumps(re)
        return HttpResponse(r)
    else:
        re['status'] = '10021'
        re['message'] = 'null'
        re['data'] = datas
        r = json.dumps(re)
        return HttpResponse(r)

#vote
# def vote(request, question_id):
#     q = get_object_or_404(Question, pk=question_id)
#     choiceid = request.POST.get('choice')
#     print(choiceid)
#     selectchoice = q.choice_set.get(pk=choiceid)
#     print(selectchoice)
#     selectchoice.votes += 1
#     selectchoice.save()
#     return render(request, 'result.html', {'question': q})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    choice_id = request.POST.get('choice','')   # 比较关键的一点，就是获取choice 传过来的结果看是否有数据
    response_data = {}
    if choice_id == '':
        response_data['status'] = '10021'
        response_data['message'] = 'null'
        result = json.dumps(response_data)
        return HttpResponse(result)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice']) # 去找choice的选项是否能有对应的结果
    except (KeyError, Choice.DoesNotExist):
        response_data['status'] = '10022'
        response_data['message'] = 'The problem is the choice is not exist'
        result = json.dumps(response_data)
        return HttpResponse(result)
    else:
        selected_choice.votes += 1
        selected_choice.save()
        response_data['status'] = '200'
        response_data['message'] = 'success'
        result = json.dumps(response_data)
        return HttpResponse(result)

    # if request.data:
    #     data = request.data.decode('utf-8')
    #     for key in data.keys():
    #         choiceid = key
    #         selectchoice = data[key]
    #         selectchoice.votes += 1
    #         selectchoice.save()
    #
    # choices = Choice.objects.filter(question_id=question_id)
    #
    # datas = {}
    # re = {}
    # if choices:
    #     for q in choices:
    #         datas[q.choice_text] = q.votes
    #     re['status'] = '200'  #re means response
    #     re['message'] = 'success'
    #     re['data'] = datas
    #     r = json.dumps(re)
    # else:
    #     re['status'] = '10021'
    #     re['message'] = 'null'
    #     re['data'] = datas
    #     r = json.dumps(re)
    # return HttpResponse(r)

def login(request):
    username = request.POST.get('username','')
    password = request.POST.get('password','')
    user = User.objects.filter(user_name=username, pass_word=password)
    response_data = {}
    if list(user) == []:
        response_data['status'] = '10021'
        response_data['message'] = 'wrong username or password'

    else:
        response_data['status'] = '200'
        response_data['message'] = 'login success'

    result = json.dumps(response_data)
    return HttpResponse(result)



