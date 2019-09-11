from django.http import JsonResponse

# Create your views here.
from rest_framework.views import APIView

from .serializer import UserSerializer
from .models import AppUser


class AppUserView(APIView):

    def login(self,request):
        name = request.data.get('name', None)
        password = request.data.get('password', None)

        if not all((name, password)):
            return JsonResponse({
                'code': 100,
                'msg': '用户名或口令不能为空'
            })

        else:
            qs = AppUser.objects.filter(name=name)
            if qs.exists():
                # 获取登录的用户信息
                login_user = qs.first()
                if login_user.auth_key == password:
                    info = UserSerializer(login_user, many=False).data
                    return JsonResponse({
                        'code': 200,
                        'data': {
                            'id': login_user.id,
                            'phone': login_user.phone
                        }
                    })

                return JsonResponse({
                    'code': 102,
                    'msg': '用户名或口令不正确，请重试或联系管理员'
                })

            else:
                return JsonResponse({
                    'code': 101,
                    'msg': '查无此用户, 可能未激活'
                })

    def regist(self, request):
        pass

    def get(self,request):
        # 读取用户信息（读取详情）
        id = request.GET.get('id', None)
        if not id:
            return JsonResponse({
                'code': 100,
                'msg': '必须提供id参数'
            })
        try:
            login_user = AppUser.objects.get(pk=id)
            return JsonResponse({
                'code': 200,
                'data': UserSerializer(login_user).data
            })
        except:
            return JsonResponse({
                'code': 101,
                'msg': '查无此用户'
            })

    def post(self, request):
        # 用户登录或注册

        action = request.GET.get('action')
        if action == 'login':
            return self.login(request)
        elif action == 'regist':
            return self.regist(request)
        else:
            return JsonResponse({
                'msg': '请求无效， 请确定是否提供action参数'
            })

    def put(self, request):
        # 修改用户信息（头像、口令、激活）
        pass

    def delete(self, request):
        # 注销用户
        pass