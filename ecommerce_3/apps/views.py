from itertools import product
from multiprocessing import context
from re import template
import this
from django.shortcuts import render
from django.views.generic import TemplateView

from apps.models import Cart, CartProduct, Category, Product

# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['myname'] = "Babayew Eziz"
        context['product_list'] = Product.objects.all()
        context["product_list"] = Product.objects.all().order_by("-id")
        # context['allcategories'] = Category.objects.all()
        return context


class AllProductsView(TemplateView):
    template_name = "allproducts.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['allcategories'] = Category.objects.all()
        return context

class ProductDetailView(TemplateView):
    template_name = "productdetail.html"

    def get_context_data(self, **kwargs):
        context = super(). get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        product = Product.objects.get(slug=url_slug)
        product.view_count += 1
        product.save()
        context['product'] = product
        return context


class AddToCartView(TemplateView):
    template_name = "addtocart.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #get product id from requested url
        #talap edilýän url-dan önüm id-ini alyň
        product_id = self.kwargs['pro_id']
        

        #get product
        #önüm al
        product_obj = Product.objects.get(id=product_id)



        #check if cart exists
        #sebediň bardygyny ýa-da ýokdugyny barlaň
    
        cart_id = self.request.session.get("cart_id", None)
        if cart_id:
            cart_obj = Cart.objects.get(id=cart_id)
            this_product_in_cart = cart_obj.cartproduct_set.filter(
                product=product_obj)

            #item already exiists in cart
            #sebetde eýýäm bar

            if this_product_in_cart.exists():
                cartproduct = this_product_in_cart.last()
                cartproduct.quantity += 1
                cartproduct.subtotal += product_obj.selling_price
                cartproduct.save()
                cart_obj.total += product_obj.selling_price
                cart_obj.save()

            #new item is added in cart
            #sebede täze zat goşuldy
            else:
                cartproduct = CartProduct.objects.create(
                    cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
                cart_obj.total += product_obj.selling_price
                cart_obj.save()
            
        else:
            cart_obj = Cart.objects.create(total=0)
            self.request.session['cart_id'] = cart_obj.id
            cartproduct = CartProduct.objects.create(
                cart=cart_obj, product=product_obj, rate=product_obj.selling_price, quantity=1, subtotal=product_obj.selling_price)
            cart_obj.total += product_obj.selling_price
            cart_obj.save()

        #check if product already exists in cart.
        #sebetde önümiň bardygyny ýa-da ýokdugyny barlaň.

        return context


class AboutView(TemplateView):
    template_name = "about.html"


class ContactView(TemplateView):
    template_name = "contact.html"