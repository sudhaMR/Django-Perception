from django.shortcuts import render
from django.http import HttpResponse
from imgpage.forms import ImgForm

def index(request):

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'boldmessage': "I am bold font from the context"}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    return render(request, 'imgpage/add_category.html', context_dict)
    #return HttpResponse("Enter words the picture reminds you of!<br/> <a href='/imgpage/about'>About</a> ")

def about(request):
    return HttpResponse("About page<a href='/imgpage/add_category.html'>Index</a>")


def add_category(request):
    # A HTTP POST?
    if request.method == 'POST':
        #form = ImgForm()
        form = ImgForm(request.POST)

        # Have we been provided with a valid form?
        if form.is_valid():
            # Save the new category to the database.
            form.save(commit=True)

            # Now call the index() view.
            # The user will be shown the homepage.
            return index(request)
        else:
            # The supplied form contained errors - just print them to the terminal.
            print form.errors
    else:
        # If the request was not a POST, display the form to enter details.
        form = ImgForm()

    # Bad form (or form details), no form supplied...
    # Render the form with error messages (if any).
    return render(request, 'imgpage/add_category.html', {'form': form})
