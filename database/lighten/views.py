from django.shortcuts import render, get_object_or_404, HttpResponseRedirect
from django.http import HttpResponse
import json
from lighten.models import Lighten, User 

def findusr(username):
	p = User.objects.filter(username=username)
#	p = User.objects.raw("select * from lighten_user where username = '%s'",[username])
	if p.count() == 0:
		return False
	else:
		return True

def verified(username, password):
	p = User.objects .filter(username = username, password = password)
	# p = User.objects.raw("select * from lighten_user where username = '%s' and password = '%s'",[username],[password])
	if p.count() == 0:
		return False
	else:
		return True

def regist(request):
	result = {'result':'success'}
	try:
		if request.method == 'POST':
			username = request.POST.get('username')
			password = request.POST.get('password')
			if not findusr(username):
				User.objects.create(username = username, password = password)
				result['result'] = 'new user'
			else:
				if not verified(username,password):
					result['result'] = 'password wrong'
	except Exception:
		result['result'] = 'database wrong'
	response = HttpResponse(json.dumps(result))
	response["Access-Control-Allow-Origin"] = "*" #添加header，access-control-allow-origin
	request.session["username"] = username
	print(str(request.session.keys()))
	return response

def add_furniture(request):
	result = {'result':'success'}
	#print(str(request.session.keys()))
	#if request.session.get("username", None) == None:
#		response = HttpResponse(json.dumps({'result': "fail"}))
#		response["Access-Control-Allow-Origin"] = "*" #添加header，access-control-allow-origin
#		return response
#	username = request.session["username"]
	username = "zcj"
	try:
		if request.method == 'POST':
			direction1 = float(request.POST.get('direction1'))
			direction2 = float(request.POST.get('direction2'))
			direction3 = float(request.POST.get('direction3'))
			furniture_id = request.POST.get('id')
			furniture_type = request.POST.get('type')
			furniture_on = request.POST.get('ins_open')
			furniture_off = request.POST.get('ins_close')
			print("AAA")
			if findusr(username):
				print("true")
				Lighten.objects.create(username = username, direction1 = direction1, direction2 = direction2, \
				direction3 = direction3, furniture_id = furniture_id, furniture_type = furniture_type, furniture_on = furniture_on, \
				furniture_off = furniture_off)
			else:
				result['result'] = 'user not found'
	except Exception:
		print(Exception)
		result['result'] = 'database wrong'
	response = HttpResponse(json.dumps(result))
	response["Access-Control-Allow-Origin"] = "*" #添加header，access-control-allow-origin
	return response

def delete_all(request):
	result = {'result':'success'}
	try:
		if request.method == 'POST':
			Lighten.objects.raw("delete * from lighten_lighten where username = '%s'",[request.POST.username])
	except Exception:
		result['result'] = 'database wrong'
	response = HttpResponse(json.dumps(result))
	response["Access-Control-Allow-Origin"] = "*" #添加header，access-control-allow-origin
	return response

def get_furniture(request):
	try:
		if request.method == 'GET':
			#req = json.loads(request.raw_post_data)
			#username = request.GET['username']
			username = "zcj"
			i = 0
			furniture = {
				"result": "",
				"directions": []
			}
			# furniture_set = Lighten.objects.raw("select * from lighten_lighten where username = '%s'",[username])
			furniture_set = Lighten.objects.filter(username=username)
			print(furniture_set)
			if furniture_set.count() == 0:
				furniture['result'] = 'norecord'
				response = HttpResponse(json.dumps(furniture))
				response["Access-Control-Allow-Origin"] = "*" #添加header，access-control-allow-origin
				return response
			else:
				for p in furniture_set:
					print(str(p))
					furniture["directions"].append([p.direction1, p.direction2, p.direction3])
#					furniture[i]['direction1'] = p.direction1
#					furniture[i]['direction2'] = p.direction2
#					furniture[i]['direction3'] = p.direction3
#					print(str(furniture))
#					i+=1				
			response = HttpResponse(json.dumps(furniture))
			response["Access-Control-Allow-Origin"] = "*" #添加header，access-control-allow-origin
			return response
	except Exception:
		furniture['result'] = 'failed' 
		response = HttpResponse(json.dumps(furniture))
		response["Access-Control-Allow-Origin"] = "*" #添加header，access-control-allow-origin
		return response
				