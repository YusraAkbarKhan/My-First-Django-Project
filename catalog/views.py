from django.shortcuts import render ,redirect
from .models import Book
from .forms import CreatBook
from django.http import HttpResponse

# Create your views here.

def home(request):
    books = Book.objects.all()
    context = {'books': books}
    return render(request, 'home.html', context)


def upload(request):
    upload = CreatBook()
    if request.method == 'POST':
        upload = CreatBook(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('home')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'home'}}">reload</a>""")
    else:
        return render(request, 'upload_form.html', {'upload_form':upload})


def update_book(request, book_id):
    book_sel = Book.objects.get(id = book_id)
    book_form = CreatBook(request.POST, request.FILES, instance=book_sel)
    if book_form.is_valid():
        book_form.save()
        return redirect('home')
    return render(request, "upload_form.html", {'upload_form': book_form})


def delete_book(request, book_id):
    book_sel = Book.objects.get(id = book_id)
    book_sel.delete()
    return redirect('home')