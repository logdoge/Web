from django.shortcuts import render, Http404, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import Question, Choice
from django.template import loader
from django.core.urlresolvers import reverse
from django.views import generic

# Create your views here.
class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'
    def get_queryset(self):
        '''返回最近发布的5个问卷'''
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #发生choice未找到的异常时，重新返回表单页面，并返回错误提示
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'], )
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html',
                      {'question':question, 'error_message':"you didn't select a choice",

        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        #成功处理数据后，自动跳转到结果页面，防止连续多次提交
        return HttpResponseRedirect(reverse('polls:results', args=(question_id)))

