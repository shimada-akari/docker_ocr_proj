from django.shortcuts import render
from django.views import generic
from .forms import ImgForm
from .models import ImageModel
from ocrproj.settings import MEDIA_ROOT
import os
import shutil
import pyocr
from PIL import Image

class OcrView(generic.FormView):
    template_name = "ocrapp/ocr.html"
    form_class = ImgForm

    def post(self, request, *args, **kwargs):
        shutil.rmtree(MEDIA_ROOT)
        os.mkdir(MEDIA_ROOT)
        form = ImgForm(request.POST, request.FILES)
        if form.is_valid():
            imgmodel = ImageModel()
            imgmodel.img = request.FILES["img"]
            imgmodel.save()
            img = Image.open(request.FILES["img"])
            

            tools = pyocr.get_available_tools()
            tool = tools[0]
            builder = pyocr.builders.TextBuilder(tesseract_layout=6)
            result = tool.image_to_string(img, lang="eng", builder=builder)
            # result = "\n" + result
            print(result)
            context = {
                "result" : result,
                "image" : imgmodel.img
            }

            return render(request, self.template_name, context)

        else:
            context = {}
            return render(request, self.template_name, context)