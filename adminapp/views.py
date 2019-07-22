from adminapp.forms import ProductEditForm
from authapp.models import ShopUser
from mainapp.models import Product, ProductCategory, VisualModels

from django.shortcuts import HttpResponseRedirect, get_object_or_404, render
from django.contrib.auth.decorators import user_passes_test, login_required
from django.urls import reverse_lazy, reverse
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView


class VisualSite(ListView):
    model = VisualModels
    template_name = 'adminapp/visualisation.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(VisualSite, self).dispatch(*args, **kwargs)


class VisualSiteCreate(CreateView):
    model = VisualModels
    template_name = 'adminapp/visualisation_create.html'

    success_url = reverse_lazy('admin:visual_sites')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(VisualSiteCreate, self).dispatch(*args, **kwargs)


class VisualSiteUpdate(UpdateView):
    model = VisualModels
    template_name = 'adminapp/visualisation_update.html'
    success_url = reverse_lazy('admin:visual_sites')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(VisualSiteUpdate, self).dispatch(*args, **kwargs)


class VisualSiteDelete(DeleteView):
    model = VisualModels
    template_name = 'adminapp/visualisation_delete.html'

    success_url = reverse_lazy('admin:visual_sites')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()


class UsersList(ListView):
    model = ShopUser
    template_name = 'adminapp/users.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(UsersList, self).dispatch(*args, **kwargs)


class UserCreate(CreateView):
    model = ShopUser
    template_name = 'adminapp/user_create.html'

    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(UserCreate, self).dispatch(*args, **kwargs)


class UserUpdate(UpdateView):
    model = ShopUser
    template_name = 'adminapp/user_update.html'

    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(UserUpdate, self).dispatch(*args, **kwargs)


class UserDelete(DeleteView):
    model = ShopUser
    template_name = 'adminapp/user_delete.html'

    success_url = reverse_lazy('admin:users')

    @method_decorator(user_passes_test(lambda u: u.is_superuser)))
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())


class ProductCategoryList(ListView):
    model = ProductCategory
    template_name = 'adminapp/categories.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProductCategoryList, self).dispatch(*args, **kwargs)


class ProductCategoryCreate(CreateView):
    model = ProductCategory
    template_name = 'adminapp/category_create.html'

    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProductCategoryCreate, self).dispatch(*args, **kwargs)


class ProductCategoryUpdate(UpdateView):
    model = ProductCategory
    template_name = 'adminapp/category_update.html'
    success_url = reverse_lazy('admin:categories')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'категории/редактирование'

        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProductCategoryUpdate, self).dispatch(*args, **kwargs)


class ProductCategoryDelete(DeleteView):
    model = ProductCategory
    template_name = 'adminapp/category_delete.html'
    success_url = reverse_lazy('admin:categories')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())

@user_passes_test(lambda u: u.is_superuser)
def products(request, pk):
    title = 'админка/продукт'

    category = get_object_or_404(ProductCategory, pk=pk)
    products_list = Product.objects.filter(category__pk=pk).order_by('name')

    content = {
        'title': title,
        'category': category,
        'objects': products_list,
    }

    return render(request, 'adminapp/products.html', content)

@user_passes_test(lambda u: u.is_superuser)
def product_create(request, pk):
    title = 'продукт/создание'
    category = get_object_or_404(ProductCategory, pk=pk)

    if request.method == 'POST':
        product_form = ProductEditForm(request.POST, request.FILES)
        if product_form.is_valid():
            product_form.save()
            return HttpResponseRedirect(reverse('admin:products', args=[pk]))
    else:
        product_form = ProductEditForm(initial={'category': category})

    content = {'title': title,
               'update_form': product_form,
               'category': category,
               }

    return render(request, 'adminapp/product_create.html', content)


class ProductDetail(DetailView):
    model = Product
    template_name = 'adminapp/product_read.html'

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProductDetail, self).dispatch(*args, **kwargs)


class ProductUpdate(UpdateView):
    model = Product
    template_name = 'adminapp/product_read.html'

    success_url = reverse_lazy('admin:products')
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'продукт/редактирование'

        return context

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def dispatch(self, *args, **kwargs):
        return super(ProductUpdate, self).dispatch(*args, **kwargs)

class ProductDelete(DeleteView):
    model = Product
    template_name = 'adminapp/product_delete.html'

    success_url = reverse_lazy('admin:products')

    @method_decorator(user_passes_test(lambda u: u.is_superuser))
    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.is_active = False
        self.object.save()

        return HttpResponseRedirect(self.get_success_url())
