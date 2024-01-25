from.models import OrderDetails,Order ,Checkout

def get_detail(request):
    if  request.user.is_authenticated:
        if Order.objects.filter(user=request.user, is_finished=False).exists():
            order = Order.objects.get(user=request.user, is_finished=False)
            orderdetails = OrderDetails.objects.filter(order=order)
            total=0
            for sub in orderdetails:
                total += sub.cost * sub.quantity
            return {'orderdetails': orderdetails,
                    'total':total}
        else:
            return {}
    else:
        return {}


def order_payment(request):
    if request.user.is_authenticated:
        orders = Order.objects.all().filter(user=request.user)
        order_list = []
        for order in orders:
            orderdetails = OrderDetails.objects.filter(order=order)
            total=0
            for sub in orderdetails:
                total += sub.cost * sub.quantity
            payment = Checkout.objects.filter(order=order).first()
            delivery_date = payment.order_delivery_date if payment else None
            order_list.append({'order': order, 'total':total, 'delivery_date': delivery_date})
        return {'orders': order_list}
    else:
        return {}
