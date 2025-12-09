"""
URL configuration for kollekvium project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def test_view(request):
    return HttpResponse("""
    <!DOCTYPE html>
    <html>
    <head>
        <title>Django Laboratoriya İşi №4</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 50px auto;
                padding: 20px;
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                color: white;
            }
            .container {
                background: rgba(255,255,255,0.1);
                padding: 30px;
                border-radius: 15px;
                backdrop-filter: blur(10px);
                text-align: center;
            }
            h1 {
                font-size: 2.5rem;
                margin-bottom: 20px;
                color: white;
            }
            .links {
                margin-top: 30px;
            }
            a {
                display: inline-block;
                margin: 10px;
                padding: 12px 25px;
                background: white;
                color: #667eea;
                text-decoration: none;
                border-radius: 25px;
                font-weight: bold;
            }
            .success {
                background: #4CAF50;
                color: white;
                padding: 10px;
                border-radius: 5px;
                margin: 20px 0;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🎉 Django Laboratoriya İşi №4</h1>
            <div class="success">Tapşırıq 4: Statik veb səhifə hazırlanması</div>
            
            <p>Django uğurla quraşdırıldı və işləyir!</p>
            <p><strong>Python 3.14 | Django 5.2.7</strong></p>
            
            <div class="links">
                <a href="/home/">🏠 Ana Səhifə (HTML Template)</a>
                <a href="/about/">📖 Haqqında Səhifəsi</a>
                <a href="/fastfood/">🍔 FastFood Sifariş</a>
                <a href="/admin/">⚙ Admin Panel</a>
            </div>
            
            <p style="margin-top: 30px; font-size: 0.9rem;">
                Bu səhifə Django HttpResponse ilə hazırlanmışdır
            </p>
        </div>
    </html>
    """)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', test_view, name='test'),
    path('', include('website.urls')),  # website tətbiqinin URL-ləri
]