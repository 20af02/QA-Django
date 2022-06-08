from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt


import json, markdown2, bleach
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import redirect, render

from qa.models import *
from django.core import serializers

# Create your views here.


def index(request):
      context={}
      context['questions']=Questions.objects.all()
      return render(request, 'index.html', context)

def askquestion(request):
      if request.method=='POST':
            title=request.POST.get('question_title')
            question = request.POST.get('question_body')
            posted_by=request.POST.get('posted_by')

            question_obj=Questions(question_title=title, question_body=question, posted_by=posted_by)
            question_obj.save()
            return redirect(viewquestion, question_obj.question_id, question_obj.slug)
      return render(request, 'ask.html', {})

def viewquestion(request, question_id, qslug):
      context={}
      question_obj = Questions.objects.get(question_id=question_id, slug=qslug)

      question_obj_json = json.loads(serializers.serialize('json', [question_obj]))[0]['fields']
      question_obj_json['question_id']=question_obj.question_id
      question_obj_json['date_posted'] = question_obj.date_posted
      question_obj_json['question_body'] = markdown2.markdown(question_obj_json['question_body'])

      #TODO: figure out bleach for no js


      context['question']=question_obj
      answers_obj=Answers.objects.filter(question_id=question_id)
      for x in answers_obj:
            x.answer_body = markdown2.markdown(x.answer_body)
            context['answers'].append(x)
      
      return render(request, 'question.html', context)

@csrf_exempt
def answerquestion(request, question_id):
      if request.method=='POST':
            try:
                  json_=json.loads(request.body)
                  answer, posted_by, question_id=json_['answer_body'], json_['posted_by'], json_['qid']

                  answer_obj=Answers(question_id=Questions.objects.get(question_id=question_id), answer_body=answer, posted_by=posted_by)
                  answer_obj.save()
                  #JSON ??
                  #
                  #
                  #
                  #return JsonResponse({'Success':'Answer posted'})
                  return JsonResponse({'Success':'Answer posted'});
                  #return redirect(viewquestion, question_id, qslug)
            #return render(request, 'answerquestion.html', context)
            except Exception as e:
                  print(e)
                  return JsonResponse({'Error':'Answer not posted'})
