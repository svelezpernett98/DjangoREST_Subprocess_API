from django.shortcuts import render
import os
import subprocess
import sys
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

@api_view(['POST'])
def startRPA(request):
    if request.method == 'POST':
        if request.data['token'] == "Aknjmasdfj3348raskfh38":
            
            py_filepath = 'C:\\Users\\svelez\\Desktop\\hola_mundo\\hola.py'

            args = '"%s" "%s" "%s"' % (sys.executable,                  # command
                                    py_filepath,                     # argv[0]
                                    os.path.basename(py_filepath))   # argv[1]

            proc = subprocess.run(args)
            print('subproceso finalizado')
            return Response(status=status.HTTP_202_ACCEPTED)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
    return Response({"message": ":s"})