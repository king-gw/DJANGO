from Home.models import shoppingcar


def shopcard(request):
    uid = request.session.get('uid',0)
    data = []
    total = 0
    if uid != 0:
        data = shoppingcar.objects.filter(user_id = uid)
        for goods in data:
            total += goods.goods.price
    return {'shoppingcar':data,'car_total':total}
