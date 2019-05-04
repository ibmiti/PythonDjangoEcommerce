from django.http import HttpResponse
from django.shortcuts import render

def home_page(request):
    context = {
        "title":"Hello World!",
        "content":"Welcome to the homepage"
    }
    return render( request, "home_page.html", context)

def about_page(request):
    context = {
        "about":"about",
        "content":"Welcome to the Aboutpage"
    }
    return render(request, "about_page.html", context )

def contact_page(request):
    context = {
        "contact":"contact",
        "content":"welcome to the contactpage"
    }
    if request.method == "POST":
        print(request.POST)
    return render(request, "contact/view.html", context )


def home_page_old(request):
    html_= """
    <!DOCTYPE html>
    <html lang="en">
      <head>
        <meta charset="utf-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <!-- The above 3 meta tags *must* come first in the head; any other head content must come *after* these tags -->
        <title>Bootstrap 101 Template</title>

        <!-- Bootstrap -->
        <link href="css/bootstrap.min.css" rel="stylesheet">

        <!-- HTML5 shim and Respond.js for IE8 support of HTML5 elements and media queries -->
        <!-- WARNING: Respond.js doesn't work if you view the page via file:// -->
        <!--[if lt IE 9]>
          <script src="https://oss.maxcdn.com/html5shiv/3.7.3/html5shiv.min.js"></script>
          <script src="https://oss.maxcdn.com/respond/1.4.2/respond.min.js"></script>
        <![endif]-->
      </head>
      <body>
      <div class="container">
        <div class="row text-center">
            <div class="col-md-12 col-12">
              <h1>Hello, world!</h1>
          </div>
        </div>
      </div>


        <!-- jQuery (necessary for Bootstrap's JavaScript plugins) -->
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.12.4/jquery.min.js"></script>
        <!-- Include all compiled plugins (below), or include individual files as needed -->
        <script src="js/bootstrap.min.js"></script>
      </body>
    </html>
    """
    return HttpResponse("<h1>Hi world</h1>")
