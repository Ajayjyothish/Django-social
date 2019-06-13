from django.shortcuts import render, get_object_or_404, redirect
from .form import BookForm, BookRawForm, PostForm
from .models import Book, Post
from django.contrib.auth.decorators import login_required
from django.views.generic import UpdateView


# Create your views here.

@login_required
def book_view(request, book_no, *args, **kwargs):
	obj = get_object_or_404(Book, pk=book_no)
	context = {
		'title': obj.title,
		'description': obj.description
	}

	return render(request, "products/details.html", context)


@login_required
def all_book_view(request, *args, **kwargs):
	queryset = Book.objects.all()
	context = {
		'object_list': queryset,

	}

	return render(request, "products/all-details.html", context)


# def form_view(request,*args, **kwargs):
#     form = BookForm(request.POST or None)
#     if form.is_valid():
#         form.save()
#         form= BookForm() 

#     obj = {
#         'form' : form
#     }

@login_required
def raw_form_view(request):
	form = BookForm()
	if request.method == "POST":
		form = BookForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.save()

			data = form.cleaned_data.get('title')
			form = BookForm()
			return render(request, "thanks.html", {
				'form': form,
				'title': data
			})

	obj = {
		'form': form
	}

	return render(request, "books-form.html", obj)


@login_required
def thank_view(request):
	return render(request, 'thanks.html', {})


def posts_view(request, *args, **kwargs):
	queryset = Post.objects.all()
	context = {
		'object_list': queryset,

	}

	return render(request, "posts.html", context)

@login_required
def post_form_view(request):
	if request.method == "POST":
		form = PostForm(request.POST)
		if form.is_valid():
			topic = form.save(commit=False)
			topic.save()
			data = form.cleaned_data.get('subject')
			form = PostForm()
			return redirect('posts')
	else:
		
		form = PostForm()

	return render(request, "posts_form.html", {
		'form': form,
		
	})


class PostUpdateView(UpdateView):
	model = Post
	fields = ('subject',)
	template_name = 'post_edit.html'
	pk_url_kwarg = 'post_pk'
	context_object_name = 'post'

	def form_valid(self, form):
		form.save()
		return redirect('posts')
