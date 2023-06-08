# rest_api
set up the viertual environment and install the django and rest framework.
In settings.py file add your application in the installed apps. Also do add the "rest_framework" in the same.
For all the models migrated to the database and are being used in the views create serializer in the serializers.py in the application itself.
I have created two application both using same models and serializers. The major differnce is the views. 
In one I am using the generic api views and in the other I am using the tradtional style of creating the view.
