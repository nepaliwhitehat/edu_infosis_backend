# from django.shortcuts import render
# #from django.contrib.auth.models import StdRegister
# from app1.models import User, Student,Teacher,Class, ClassStudent,Parents,Accountant,Section,SectionStudent,\
# Syllabus,Subject,Routine,SubjectMarks,SubMarkType,Barcode,Attendance,Payment,Exam,Book,MyPhoto
# from rest_framework import viewsets
# from rest_framework.response import Response
# from rest_framework.decorators import action
# from rest_framework.parsers import FormParser, MultiPartParser
# import random
# from app1.modules.barcode import Code128##For Barcode
# from rest_framework import status

# from app1.serializers import StudentSerializer,TeacherSerializer, \
# ClassSerializer,ClassStudentSerializer,ParentSerializer,AccountantSerializer,SectionSerializer,\
# SectionStudentSerializer,SyllabusSerializer,SubjectSerializer,RoutineSerializer,SubjectMarksSerializer,\
# BarcodeSerializer,AttendanceSerializer,PaymentSerializer,StudentUpdateSerializer,TeacherUpdateSerializer,\
# ParentUpdateSerializer,AccountantUpdatserializer,ClassUpdateSerializer,ExamSerializer,BookSerializer,\
# BookUpdateSerializer,MyPhotoSerializer,UserPostSerializer

# class StudentViewset(viewsets.ModelViewSet):
#     queryset = Student.objects.all()
#     serializer_class = StudentSerializer

#     http_methods = ['get', 'post','put','delete']


#     def create(self, request):
#         serializer=StudentSerializer(data=request.data)
#         serializer.is_valid()
#         row = serializer.data
#         user = row['user']
#         full_name = user['full_name']
#         first_name = full_name.split(' ')[0]

#         #email = first_name + '@schoolX.com'


#         # _e = User.objects.filter(email=email)
#         # if _e:
#         #     email = first_name + str(+count) + '@schoolX.com'
#         emailpattern =  '{}(\d*)@schoolx.com'.format(first_name)
#         count = User.objects.filter(email__iregex=emailpattern).count()
#         email = '{}{}@schoolx.com'.format(first_name, str(count) if count > 0 else "")

        
#         user,created = User.objects.get_or_create(email= email, 
#             defaults={'full_name':row['user']['full_name'],'addresss':row['user']['addresss'],'username':email})
#         student = Student.objects.create(user_id=user.id)

#         return Response({'email':email})

#     def update(self,request,*args,**kwargs):
#         instance=self.get_object()
#         serializer=StudentUpdateSerializer(data=request.data)

#         serializer.is_valid(raise_exception=True)

#         data = serializer.data

#         user = data.get('user', False)
#         if user:
#             if user.get('full_name',False):
#                 instance.user.full_name=user.get('full_name')
#             if user.get('addresss',False):
#                 instance.user.addresss=user.get('addresss')
#             if user.get('phoneno',False):
#                 instance.user.phoneno=user.get('phoneno')
#             if user.get('email',False):
#                 instance.user.email=user.get('email')
#             instance.user.save()

      
#         if data.get('father_name', False):
#             instance.father_name = data.get('father_name')

#         if data.get('mother_name', False):
#             instance.mother_name = data.get('mother_name')
        
#         instance.save()
#         return Response(serializer.data)

#     def destroy(self, request, *args,**kwargs):
#         print("hello")
#         instance = self.get_object()
#         self.perform_destroy(instance)
#         return Response(status=status.HTTP_204_NO_CONTENT)
#     def perform_destroy(self,instance):
#         instance.delete()
   

#     # def update(self, request, *args, **kwargs):
#     #     instance = self.get_object()
#     #     serializer = StudentUpdateSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)
#     #     instance.father_name = request.data.get("father_name")
#     #     instance.save()
#     #     return Response(serializer.data)


# class TeacherViewset(viewsets.ModelViewSet):
#     queryset = Teacher.objects.all()
#     serializer_class = TeacherSerializer

#     def create(self,request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data
#         email=username=row['user']['email']
#         # if user['password'] != user['re_password']:
#         #     return Response({'message':'pw not matched'})


#         user, created = User.objects.get_or_create(email=email, 
#             defaults={'full_name':row['user']['full_name'],'addresss':row['user']['addresss'],
#             'phoneno':row['user']['phoneno'],
#             'gender':row['user']['gender'] ,'username':username})
#         if created == False:
#             return Response({'message':'sorry the Teacher is already exist'})
            
#         teacher=Teacher.objects.create(user_id=user.id)
#         return Response(row)




#     def update(self,request,*args,**kwargs):
#         instance=self.get_object()
#         serializer=TeacherUpdateSerializer(data=request.data)
#         serializer.is_valid()
#         data=serializer.data

#         user = data.get('user', False)
#         if user:
#             if user.get('full_name',False):
#                 instance.user.full_name=user.get('full_name')
#             if user.get('addresss',False):
#                 instance.user.addresss=user.get('addresss')
#             if user.get('phoneno',False):
#                 instance.user.phoneno=user.get('phoneno')
#             if user.get('email',False):
#                 instance.user.email=user.get('email')
#             instance.user.save()

#         if data.get('qualification',False):
#             instance.qualification=data.get('qualification')
#         instance.save()
#         return Response(serializer.data)

# class ClassViewset(viewsets.ModelViewSet):
#     queryset=Class.objects.all()
#     serializer_class=ClassSerializer

#     # @action(methods=['post'], detail=True)
#     # def set_students(self, request, id=None):
#     #     serializer=ClassStudentSerializer(data=request.data)
#     #     serializer.is_valid(raise_exception=True)

#     #     row=serializer.data

#     #     student_ids = row['students']
#     #     for sid in student_ids:
#     #         ClassStudent.objects.get_or_create(student_id=sid, Class_id=id)

#     #     return Response(row)
#     def update(self,request,*args,**kwargs):
#         instance=self.get_object()
#         serializer=ClassUpdateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data=serializer.data
#         if data.get('name',False):
#             instance.name=data.get('name')
#         if data.get('max_capacity',False):
#             instance.max_capacity=data.get('max_capacity')
#         if data.get('description',False):
#             instance.description=data.get('description')

#         instance.save()
#         return Response(serializer.data)


# class ClassStudentViewset(viewsets.ModelViewSet):
#     queryset=ClassStudent.objects.all()
#     serializer_class=ClassStudentSerializer

#     def create(self, request, class_pk):

#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data

#         student_ids = row['students']
#         for id in student_ids:
#             ClassStudent.objects.get_or_create(student_id=id, _class_id=self.kwargs['class_pk'])
            
#         return Response(id)

#     def list(self,request, class_pk):

#         students = ClassStudent.objects.filter(_class_id=class_pk)
#         output = []
#         for student in students:
#             output.append (
#                     {'id':student.id

#                     }
#                 )
#         return Response(output)




# class ParentViewset(viewsets.ModelViewSet):
#     queryset = Parents.objects.all()
#     serializer_class = ParentSerializer

#     def create(self,request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data
#         #to verify password
#         user=row['user']
#         if user['password'] != user['re_password']:
#             return Response({'message':'pw not matched'})


#         email=username=row['user']['email']

#         user, created = User.objects.get_or_create(email=email,
#             defaults={'full_name':row['user']['full_name'],'addresss':row['user']['addresss'],
#             'phoneno':row['user']['phoneno'],'password':row['user']['password'] ,'re_password':row['user']['re_password'],
#             'gender':row['user']['gender'] ,'username':username})
#         if created == False:
#             return Response({'message':'sorry the Parents is already exist'})
            
#         parent=Parents.objects.create(user_id=user.id)
#         return Response(row)

#     def update(self,request,*args,**kwargs):
#         instance=self.get_object()
#         serializer=ParentUpdateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data=serializer.data

#         user = data.get('user', False)
#         if user:
#             if user.get('full_name',False):
#                 instance.user.full_name=user.get('full_name')
#             if user.get('addresss',False):
#                 instance.user.addresss=user.get('addresss')
#             if user.get('phoneno',False):
#                 instance.user.phoneno=user.get('phoneno')
#             if user.get('email',False):
#                 instance.user.email=user.get('email')
#             if user.get('password',False):
#                 instance.user.password=user.get(password)
#             if user.get('re_password',False):
#                 instance.user.re_password=user.get(re_password)
#             instance.user.save()
            
#         return Response(serializer.data)
# ### For Accountant

# class AccountantViewset(viewsets.ModelViewSet):
#     queryset = Accountant.objects.all()
#     serializer_class = AccountantSerializer

#     def get(self, request):
#         queryset = Accountant.objects.all()
#         serializer_class = AccountantSerializer
#         serializer=self.get_serializer(data=request.data)
#         return Response(serializer.data)


#     def create(self,request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data
        
#         email=username=row['user']['email']

#         user, created = User.objects.get_or_create(email=email, 
#             defaults={'full_name':row['user']['full_name'],'addresss':row['user']['addresss'],
#             'phoneno':row['user']['phoneno'],
#             'gender':row['user']['gender'] ,'username':username})

#         if created == False:
#             return Response({'message':'sorry the Parents is already exist'})
            
#         parent=Accountant.objects.create(user_id=user.id)
#         return Response(row)
#     def update(self,request,*args,**kwargs):
#         instance=self.get_object()
#         serializer=AccountantUpdatserializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data=serializer.data
#         user=data.get('user',False)
#         if user:
#             if user.get('full_name',False):
#                 instance.user.full_name=user.get('full_name')
#             if user.get('addresss',False):
#                 instance.user.addresss=user.get('addresss')
#             if user.get('phoneno',False):
#                 instance.user.phoneno=user.get('phoneno')
#             if user.get('email',False):
#                 instance.user.email=user.get('email')
#             if user.get('password',False):
#                 instance.user.password=user.get('password')
#             if user.get('re_password',False):
#                 instance.user.re_password=user.get('re_password')
#             instance.user.save()

#         return Response(serializer.data)


# class ClassSectionViewset(viewsets.ModelViewSet):
#     queryset=Section.objects.all()
#     serializer_class=SectionSerializer

#     def create(self,request, class_pk):
#         serializer=self.get_serializer(data=request.data)
#         #print(serializer)
#         serializer.is_valid(raise_exception=True)
#         row=serializer.data
#         #print(row)
#         section_name=row['section_name']
       
#         ## to check class id
#         try:

#             Class.objects.get(id=class_pk)

#         except Exception as ex:
#             return Response({'message':'sorry'+ str(ex)})
#         else:
#             Section.objects.get_or_create(_class_id=class_pk,section_name=section_name,
#             defaults={'section_description':row['section_description']})
           
#         return Response({'message':'created'})
#     #def update(self,requet,*args)


# class SectionViewset(viewsets.ModelViewSet):

#     queryset=Section.objects.all()
#     serializer_class=SectionSerializer

#     def create(self,request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data
#         Section.objects.get_or_create(_class_id=row['class_id'], section_name=row['section_name'],defaults={
#             'section_description':row['section_description']})
#         return Response(row)

# class SectionStudentViewset(viewsets.ModelViewSet):
#     queryset = SectionStudent.objects.all()
#     serializer_class = SectionStudentSerializer

#     def create(self,request,section_pk):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data
#         SectionStudent.objects.get_or_create(sec_id=section_pk,student_id=row['student_id'])

#         return Response(row)

# class SyllabusViewset(viewsets.ModelViewSet):
#     queryset = Syllabus.objects.all()
#     serializer_class = SyllabusSerializer

#     def create(self,request,class_pk):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data
#         Syllabus.objects.get_or_create(_class_id=class_pk,defaults={'title':row['title'],'description':row['description']})

#         return Response(row)


# class SubjectViewset(viewsets.ModelViewSet):
#     queryset=Subject.objects.all()
#     serializer_class=SubjectSerializer

#     def create(self,request,class_pk):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid()

#         row=serializer.data
#         Subject.objects.get_or_create(_class_id=class_pk,subject_name=row['subject_name'], defaults={'description':row['description']})

#         return Response(row)




# class RoutineViewset(viewsets.ModelViewSet):
#     queryset=Routine.objects.all()
#     serializer_class=RoutineSerializer

#     def create(self,request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data
#         try:
#             _Section=Section.objects.get(id=row['section_id'])
#             _Teacher=Teacher.objects.get(id=row['teacher_id'])
#             _Subject=Subject.objects.get(id=row['subject_id'])
#         except:
#             return Response({'message':'sorry id doesnot exist'})
#         else:
#             Routine.objects.get_or_create(section_id=row['section_id'],subject_id=row['subject_id'],teacher_id=row['teacher_id'],
#             defaults={'time_start':row['time_start'],'time_end':row['time_end']})
#         return Response({'message':'created'})

# class SubjectMarkViewset(viewsets.ModelViewSet):
#     queryset=Routine.objects.all()
#     serializer_class=SubjectMarksSerializer

#     def create(self,request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data
#         try:
#             SubMarkType=SubMarkType.objects.get(id=row['SubMarkType_id'])

#         except:
#             return Response({'message':'sorry'})
#         else:
#             SubjectMarks.objects.get_or_create(_type_id=row['SubMarkType_id'],defaults={obtained_marks:row['obtained_marks'],marks_type:row['marks_type']})
#         return Response({'Created Successfully'})


# ######Barcode#####
# class BarcodeViewset(viewsets.ModelViewSet):
#     queryset=Barcode.objects.all()
#     serializer_class=BarcodeSerializer
#     def create(self,request):
#         upload_dir = 'app1/storage/barcodes/'
#         try:
#             os.makedirs(upload_dir)
#         except:
#             pass

#         n = random.random()

#         code = 'SMS-%s'%str(n)

#         bar = Code128()
#         bar.getImage(code,100,"png", path=upload_dir)

#         b, c = Barcode.objects.get_or_create(bar_code=code, defaults={'file':upload_dir+code+'.png'})

#         return b
# # parser_classes = (FormParser, MultiPartParser)


# class AttendanceViewset(viewsets.ModelViewSet):
#     queryset=Attendance.objects.all()
#     serializer_class=AttendanceSerializer
   
#     def create(self,request,section_pk):
#         #print(request.POST)
#         #print(request.FILES)
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid()

#         #files = request.FILES

#         # row=request.POST 
#         row=serializer.data
#         try:
#             _Section=Section.objects.get(id=row['section_id'])
#             _Student=Student.objects.get(id=row['student_id'])
#         except:
#             return Response("Sorry Sec id And Student id not found")
#         else:
#             Attendance.objects.get_or_create(sec_id=row['section_id'],student_id=row['student_id'],defaults={
#                 'status':row['status']
#                 })
#             #'file':files['file'
#             return Response("Present")

#     # def list(self, request, section_pk):
#     #     data=request.get
#     #     return Response([{'id':'testingingeisngie'}])

# class PaymentViewset(viewsets.ModelViewSet):
#     queryset=Payment.objects.all()
#     serializer_class=PaymentSerializer

#     def create(self,request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         row=serializer.data
        
#         Payment.objects.get_or_create(student_id=row['student_id'],defaults={
#             'pay_amount':row['pay_amount'],'description':row['description'],
#             })
#         return Response("created")


# class ExamViewset(viewsets.ModelViewSet):
#     queryset=Exam.objects.all()
#     serializer_class=ExamSerializer

#     def create(self,request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         row=serializer.data
#         Exam.objects.get_or_create(name=row['name'],defaults={'date':row['date'],'description':row['description']})
#         return Response(serializer.data)

# class BookViewset(viewsets.ModelViewSet):
#     queryset=Book.objects.all()
#     serializer_class=BookSerializer

#     def create(self,request):
#         serializer=self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         row=serializer.data
#         Book.objects.get_or_create(isbn_no=row['isbn_no'],defaults={'name':row['name'],
#             'publisher':row['publisher'],'edition':row['edition'],'author':row['author']})
#         return Response(serializer.data)

#     def update(self,request,*args,**kwargs):
#         instance=self.get_object()
#         serializer=BookUpdateSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         data=serializer.data

#         if data.get('name',False):
#             instance.name=data.get('name')
#         if data.get('author',False):
#             instance.author=data.get('author')
#         if data.get('description',False):
#             instance.description=data.get('description')
#         instance.save()
#         return Response(serializer.data)

# class MyPhotoViewset(viewsets.ModelViewSet):
#     queryset=MyPhoto.objects.all()
#     serializer_class=MyPhotoSerializer
#     parser_classes = (FormParser, MultiPartParser)

#     def create(self,request):
#         files=request.FILES
#         print(files)
#         MyPhoto.objects.get_or_create(image=files['image'])
#         return Response("created")