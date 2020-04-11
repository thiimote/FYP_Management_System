from account.models import StudentGroup, Dean, Hod, Supervisor
from project.models import School, Department, Groups, Project, GroupProgress
from users.models import CustomerUser
from .forms import AddGroupForm, AddGroupProgressForm, CreateDepartment
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import CreateView, UpdateView, DeleteView,DetailView


@login_required
def school(request):
    schools = School.objects.all()
    context = {
        'schools': schools
    }
    return render(request, 'coordinator/school.html', context=context)


@login_required
def departmentPage(request, pk=None):
    schools = get_object_or_404(School, pk=pk)
    departments = Department.objects.filter(school_id=pk)
    depart_count = departments.count()
    deans = Dean.objects.filter(school_id=pk)
    custom = CustomerUser.objects.filter(school=pk)
    hods = Hod.objects.all()

    context = {

        'schools': schools,
        'departments': departments,
        'deans': deans,
        'custom': custom,
        'hods': hods,
        'depart_count': depart_count,
    }

    return render(request, 'dean/department.html', context=context)


@login_required
def department_details(request, pk):
    departments = Department.objects.get(pk=pk)
    groups = Groups.objects.filter(department_id=departments)
    supervisors = Supervisor.objects.all()
    projects = Project.objects.all()
    customs = CustomerUser.objects.filter(department=departments)
    students = StudentGroup.objects.filter(department_name=departments)

    context = {
        'departments': departments,
        'projects': projects,
        'supervisors': supervisors,
        'groups': groups,
        'customs': customs,
        'students': students,
        }
    return render(request, 'hod/department_detail.html', context=context )


class StudentDetailView(LoginRequiredMixin, DetailView):
    model = StudentGroup


class StudentDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = StudentGroup
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        # if self.request.user == post.author:
        #     return True
        return True


class GroupProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        # if self.request.user == post.author:
        #     return True
        return True


class GroupProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    fields = ['group_id', 'project_title', 'project_description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class GroupProjectDetailView(LoginRequiredMixin, DetailView):
    model = Project


class GroupProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    fields = ['project_title', 'project_description']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # if self.request.user == post.author:
        #     return True
        return True


class StudentCreateView(LoginRequiredMixin, CreateView):
    model = StudentGroup
    fields = ['department_name', 'student_name', 'group_id']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class StudentUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = StudentGroup
    fields = ['department_name', 'student_name', 'group_id']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post = self.get_object()
        # if self.request.user == post.author:
        #     return True
        return True


@login_required
def dean_department_detail(request, pk):
    departments = Department.objects.get(pk=pk)
    groups = Groups.objects.filter(department_id=departments)
    supervisors = Supervisor.objects.all()
    projects = Project.objects.all()
    customs = CustomerUser.objects.filter(department=departments)
    students = StudentGroup.objects.filter(department_name=departments)

    context = {
        'departments': departments,
        'projects': projects,
        'supervisors': supervisors,
        'groups': groups,
        'custom': customs,
        'students': students,
        }
    return render(request, 'dean/department_detail.html', context=context )


@login_required
def singleGroup(request, pk):
    groups = Groups.objects.get(pk=pk)
    projects = Project.objects.filter(group_id=groups)
    supervisors = Supervisor.objects.filter(group_id=groups)
    member = StudentGroup.objects.filter(group_id=groups)
    progress = GroupProgress.objects.filter(group_id=groups)
    context = {
        'projects': projects,
        'supervisors': supervisors,
        'groups': groups,
        'member': member,
        'progress': progress,
        }

    return render(request, 'group/group.html', context=context )


@login_required
def groupProgress(request):
    if request.method == 'POST':
        form = AddGroupProgressForm(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, ' your account has been Updated!')
            return redirect('home')

    else:
        form = AddGroupProgressForm()

    context = {
        'form': form
    }
    return render(request, 'group/progress.html', context)


@login_required
def group_detail(request, pk):
    users = User.objects.get(pk=pk)
    hods = Hod.objects.filter(hod_name=users)
    custom = CustomerUser.objects.filter(username=users)
    students = StudentGroup.objects.all()
    deans = Dean.objects.filter(dean_name=users)
    teachers = Supervisor.objects.filter(supervisor_name=users)
    projects = Project.objects.all()
    progress = GroupProgress.objects.all()

    context = {
        'users': users,
        'students': students,
        'custom': custom,
        'deans': deans,
        'hods': hods,
        'teachers': teachers,
        'progress': progress,
        'projects': projects,
    }
    return render(request, 'supervisor/group_detail.html', context=context)


@login_required
def hodGroupDetail(request, pk):
    groups = Groups.objects.get(pk=pk)
    projects = Project.objects.filter(group_id=groups)
    supervisors = Supervisor.objects.filter(group_id=groups)
    students_group = StudentGroup.objects.filter(group_id=groups)
    customs = CustomerUser.objects.all()
    hods = Hod.objects.all()
    context = {
        'projects': projects,
        'supervisors': supervisors,
        'groups': groups,
        'customs': customs,
        'hods': hods,
        'students_group': students_group,
        }
    return render(request, 'hod/hod_group.html', context=context )


@login_required
def create_group(request):
    form = AddGroupForm(request.POST)
    if request.method == 'POST':
        try:
            if form.is_valid():
                group = form.save(commit=False)
                group.save()
                messages.success(request, 'group was created successfully')
        except Exception as e:
            form = AddGroupForm()
            messages.warning(request, 'Sorry, group not created, try again.Error : {}'.format(e))

    return render(request, 'hod/addgroup.html', {'form': form})


@login_required
def hodSupervisorDetail(request, pk):
    customs_user = CustomerUser.objects.get(pk=pk)
    groups = Groups.objects.all()
    students = StudentGroup.objects.all()
    supervisors = Supervisor.objects.all()

    context = {
            'groups': groups,
            'supervisors': supervisors,
            'students': students,
            'customs_user': customs_user,
            }
    return render(request, 'hod/supervisor.html', context=context)


@login_required
def create_department(request):
    form = CreateDepartment(request.POST)
    if request.method == 'POST':
        try:
            if form.is_valid():
                group = form.save(commit=False)
                group.save()
                messages.success(request, 'Department was created successfully')
        except Exception as e:
            form = AddGroupForm()
            messages.warning(request, 'Sorry, Department not created, try again.Error : {}'.format(e))

    return render(request, 'hod/create_department.html', {'form': form})

