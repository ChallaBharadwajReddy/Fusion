# Generated by Django 3.1.5 on 2024-07-16 15:44

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Curriculum',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('version', models.DecimalField(decimal_places=1, default=1.0, max_digits=5, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.DecimalValidator(decimal_places=1, max_digits=5)])),
                ('working_curriculum', models.BooleanField(default=True)),
                ('no_of_semester', models.PositiveIntegerField(default=1)),
                ('min_credit', models.PositiveIntegerField(default=0)),
                ('latest_version', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Programme',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(choices=[('UG', 'Undergraduate'), ('PG', 'Postgraduate'), ('PHD', 'Doctor of Philosophy')], max_length=3)),
                ('name', models.CharField(max_length=70, unique=True)),
                ('programme_begin_year', models.PositiveIntegerField(default=2024)),
            ],
        ),
        migrations.CreateModel(
            name='Semester',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester_no', models.PositiveIntegerField()),
                ('instigate_semester', models.BooleanField(default=False, null=True)),
                ('start_semester', models.DateField(blank=True, null=True)),
                ('end_semester', models.DateField(blank=True, null=True)),
                ('semester_info', models.TextField(blank=True, null=True)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme_curriculum.curriculum')),
            ],
            options={
                'unique_together': {('curriculum', 'semester_no')},
            },
        ),
        migrations.CreateModel(
            name='Discipline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('acronym', models.CharField(default='', max_length=10)),
                ('programmes', models.ManyToManyField(blank=True, to='programme_curriculum.Programme')),
            ],
        ),
        migrations.AddField(
            model_name='curriculum',
            name='programme',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme_curriculum.programme'),
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('version', models.DecimalField(decimal_places=1, default=1.0, max_digits=5, validators=[django.core.validators.MinValueValidator(1.0), django.core.validators.DecimalValidator(decimal_places=1, max_digits=5)])),
                ('credit', models.PositiveIntegerField(default=0)),
                ('lecture_hours', models.PositiveIntegerField(null=True)),
                ('tutorial_hours', models.PositiveIntegerField(null=True)),
                ('pratical_hours', models.PositiveIntegerField(null=True)),
                ('discussion_hours', models.PositiveIntegerField(null=True)),
                ('project_hours', models.PositiveIntegerField(null=True)),
                ('pre_requisits', models.TextField(blank=True, null=True)),
                ('syllabus', models.TextField()),
                ('percent_quiz_1', models.PositiveIntegerField(default=10)),
                ('percent_midsem', models.PositiveIntegerField(default=20)),
                ('percent_quiz_2', models.PositiveIntegerField(default=10)),
                ('percent_endsem', models.PositiveIntegerField(default=30)),
                ('percent_project', models.PositiveIntegerField(default=15)),
                ('percent_lab_evaluation', models.PositiveIntegerField(default=10)),
                ('percent_course_attendance', models.PositiveIntegerField(default=5)),
                ('ref_books', models.TextField()),
                ('working_course', models.BooleanField(default=True)),
                ('latest_version', models.BooleanField(default=True)),
                ('disciplines', models.ManyToManyField(blank=True, to='programme_curriculum.Discipline')),
                ('pre_requisit_courses', models.ManyToManyField(blank=True, related_name='_course_pre_requisit_courses_+', to='programme_curriculum.Course')),
            ],
            options={
                'unique_together': {('code', 'version')},
            },
        ),
        migrations.CreateModel(
            name='Batch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('B.Tech', 'B.Tech'), ('M.Tech', 'M.Tech'), ('B.Des', 'B.Des'), ('M.Des', 'M.Des'), ('Phd', 'Phd')], max_length=50)),
                ('year', models.PositiveIntegerField(default=2024)),
                ('running_batch', models.BooleanField(default=True)),
                ('curriculum', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='programme_curriculum.curriculum')),
                ('discipline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme_curriculum.discipline')),
            ],
            options={
                'unique_together': {('name', 'discipline', 'year')},
            },
        ),
        migrations.CreateModel(
            name='Proposal_Tracking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_id', models.CharField(max_length=100)),
                ('current_id', models.CharField(max_length=100)),
                ('current_design', models.CharField(max_length=100)),
                ('receive_date', models.DateTimeField(auto_now_add=True)),
                ('forward_date', models.DateTimeField(auto_now_add=True)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('is_added', models.BooleanField(default=False)),
                ('is_submitted', models.BooleanField(default=False)),
                ('is_rejected', models.BooleanField(default=False)),
                ('sender_archive', models.BooleanField(default=False)),
                ('receiver_archive', models.BooleanField(default=False)),
                ('disciplines', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme_curriculum.discipline')),
                ('receive_design', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.designation')),
                ('receive_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('file_id', 'current_id', 'current_design', 'disciplines')},
            },
        ),
        migrations.CreateModel(
            name='NewProposalFile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uploader', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=100)),
                ('credit', models.PositiveIntegerField(default=3)),
                ('lecture_hours', models.PositiveIntegerField(default=3, null=True)),
                ('tutorial_hours', models.PositiveIntegerField(default=0, null=True)),
                ('pratical_hours', models.PositiveIntegerField(default=0, null=True)),
                ('discussion_hours', models.PositiveIntegerField(default=0, null=True)),
                ('project_hours', models.PositiveIntegerField(default=0, null=True)),
                ('pre_requisits', models.TextField(blank=True, null=True)),
                ('syllabus', models.TextField()),
                ('percent_quiz_1', models.PositiveIntegerField(default=10)),
                ('percent_midsem', models.PositiveIntegerField(default=20)),
                ('percent_quiz_2', models.PositiveIntegerField(default=10)),
                ('percent_endsem', models.PositiveIntegerField(default=30)),
                ('percent_project', models.PositiveIntegerField(default=15)),
                ('percent_lab_evaluation', models.PositiveIntegerField(default=10)),
                ('percent_course_attendance', models.PositiveIntegerField(default=5)),
                ('ref_books', models.TextField()),
                ('subject', models.CharField(max_length=100, null=True)),
                ('description', models.CharField(max_length=400, null=True)),
                ('upload_date', models.DateTimeField(auto_now_add=True)),
                ('is_read', models.BooleanField(default=False)),
                ('is_update', models.BooleanField(default=False)),
                ('is_archive', models.BooleanField(default=False)),
                ('pre_requisit_courses', models.ManyToManyField(blank=True, to='programme_curriculum.Course')),
            ],
            options={
                'unique_together': {('code', 'uploader', 'name')},
            },
        ),
        migrations.AlterUniqueTogether(
            name='curriculum',
            unique_together={('name', 'version')},
        ),
        migrations.CreateModel(
            name='CourseSlot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(choices=[('Professional Core', 'Professional Core'), ('Professional Elective', 'Professional Elective'), ('Professional Lab', 'Professional Lab'), ('Engineering Science', 'Engineering Science'), ('Natural Science', 'Natural Science'), ('Humanities', 'Humanities'), ('Design', 'Design'), ('Manufacturing', 'Manufacturing'), ('Management Science', 'Management Science'), ('Open Elective', 'Open Elective'), ('Swayam', 'Swayam'), ('Project', 'Project'), ('Optional', 'Optional'), ('Others', 'Others')], max_length=70)),
                ('course_slot_info', models.TextField(null=True)),
                ('duration', models.PositiveIntegerField(default=1)),
                ('min_registration_limit', models.PositiveIntegerField(default=0)),
                ('max_registration_limit', models.PositiveIntegerField(default=1000)),
                ('courses', models.ManyToManyField(blank=True, to='programme_curriculum.Course')),
                ('semester', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme_curriculum.semester')),
            ],
            options={
                'unique_together': {('semester', 'name', 'type')},
            },
        ),
        migrations.CreateModel(
            name='CourseInstructor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('batch_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='programme_curriculum.batch')),
                ('course_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='programme_curriculum.course')),
                ('instructor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='globals.extrainfo')),
            ],
            options={
                'unique_together': {('course_id', 'instructor_id', 'batch_id')},
            },
        ),
    ]
