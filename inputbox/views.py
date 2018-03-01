from inputbox.models import Article,Part
from inputbox.forms import User_Form
from django.views import generic
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.urlresolvers import reverse_lazy,reverse
from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth import authenticate,login,logout
from django.views.generic import View
#Hardcode sample getter
def get_sample():
    return Article.objects.filter(user__username='Sample_User')
#basic stuff
class IndexView(generic.ListView):
    template_name = 'inputbox/index.html'
    def get_queryset(self):
        if self.request.user.is_authenticated():
            return Article.objects.filter(user=self.request.user)
        else:
            return get_sample()
class DetailView(generic.DetailView):
    template_name = 'inputbox/article.html'
    def get_object(self):
        if self.request.user.is_authenticated():
            return get_object_or_404(Article,pk=self.kwargs['article_id'],user=self.request.user)
        else:
            return get_object_or_404(Article, pk=self.kwargs['article_id'])
#Operation about Article
class Article_Create_View(CreateView):
    fields = ['title','sample_cover']
    model = Article
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Article_Create_View, self).form_valid(form)
class Article_Edit_View(UpdateView):
    fields = ['title','sample_cover']
    model = Article
    def get_object(self):
        return get_object_or_404(Article,pk=self.kwargs['article_id'],user=self.request.user)
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(Article_Edit_View, self).form_valid(form)
    def get_success_url(self):
        return reverse('article:detail', args=(self.kwargs['article_id']))
class Article_Delete_View(DeleteView):
    model = Article
    success_url =  reverse_lazy("article:index")
#Operation about Part
class Part_Create_View(CreateView):
    model = Part
    fields = ['type','text']
    #rewrite form_valid() to get foreignKey
    def form_valid(self, form):
        form.instance.Article = get_object_or_404(Article, pk=self.kwargs['article_id'])
        return super(Part_Create_View, self).form_valid(form)
    def get_success_url(self):
        return reverse('article:detail', args=(self.kwargs['article_id']))
class Part_Edit_View(UpdateView):
    fields = ['type','text']
    def get_object(self):
        return get_object_or_404(Part,pk=self.kwargs['part_id'])
    def get_success_url(self):
        return reverse('article:detail', args=(self.kwargs['article_id']))
class Part_Delete_View(DeleteView):
    model = Part
    def get_object(self):
        return get_object_or_404(Part,pk=self.kwargs['part_id'])
    def get_success_url(self):
        return reverse('article:detail', args=(self.kwargs['article_id']))
#Operation about Auth
class User_Form_View(View):
    form_class = User_Form
    template_name = 'inputbox/registrate_form.html'
    #For new user
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name,{'form':form})
    #Regist to Database
    def post(self,request):
        form = self.form_class(request.POST)
        if form.is_valid():
             user = form.save(commit=False)
             username = form.cleaned_data['username']
             password = form.cleaned_data['password']
             user.set_password(password)
             user.save()
             user = authenticate(username=username,password=password)

             if user is not None:
                 if user.is_active:
                     login(request,user)
                     return redirect( 'article:index')
                     #if wanna call info about user just write user.username
        return render(request, self.template_name, {'form': form})
def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                #Query for a user goes here
                return render(request, 'inputbox/index.html',{'object_list':Article.objects.filter(user=request.user)})
            else:
                return render(request, 'inputbox/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'inputbox/login.html', {'error_message': 'Invalid login'})
    return render(request, 'inputbox/login.html')
def logout_user(request):
    logout(request)
    #give sample or ads in future
    return render(request, 'inputbox/index.html', {'object_list': get_sample()})

