# Generated by Django 3.1.5 on 2024-07-16 15:44

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('globals', '0001_initial'),
        ('auth', '0012_alter_user_first_name_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Appraisal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('discipline', models.CharField(max_length=30, null=True)),
                ('knowledge_field', models.CharField(max_length=30, null=True)),
                ('research_interest', models.CharField(max_length=60, null=True)),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected'), ('outstanding', 'Outstanding'), ('excellant', 'Excellent'), ('very good', 'Very Good'), ('good', 'Good'), ('poor', 'Poor')], default='pending', max_length=20)),
                ('timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('other_research_element', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('publications', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('conferences_meeting_attended', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('conferences_meeting_organized', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('admin_assign', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('sevice_to_ins', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('extra_info', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('faculty_comments', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('start_date', models.DateField(blank=True, null=True)),
                ('end_date', models.DateField(blank=True, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='all_appraisals', to=settings.AUTH_USER_MODEL)),
                ('designation', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='desig', to='globals.designation')),
            ],
        ),
        migrations.CreateModel(
            name='Cpda_application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('approved', 'Approved'), ('rejected', 'Rejected'), ('adjustments_pending', 'Adjustments Pending'), ('finished', 'Finished')], max_length=20, null=True)),
                ('pf_number', models.CharField(default='1', max_length=50, null=True)),
                ('purpose', models.CharField(blank=True, default='', max_length=500)),
                ('requested_advance', models.IntegerField(blank=True)),
                ('request_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('adjustment_amount', models.IntegerField(blank=True, default='0', null=True)),
                ('bills_attached', models.IntegerField(blank=True, default='-1', null=True)),
                ('total_bills_amount', models.IntegerField(blank=True, default='0', null=True)),
                ('ppa_register_page_no', models.IntegerField(blank=True, default='-1', null=True)),
                ('adjustment_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Cpda Application',
            },
        ),
        migrations.CreateModel(
            name='CpdaBalance',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('cpda_balance', models.PositiveIntegerField(default=300000)),
            ],
        ),
        migrations.CreateModel(
            name='Ltc_application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('requested', 'Requested'), ('approved', 'Approved'), ('rejected', 'Rejected')], max_length=20, null=True)),
                ('pf_number', models.CharField(default='', max_length=50)),
                ('basic_pay', models.IntegerField(blank=True)),
                ('leave_start', models.DateField(null=True)),
                ('leave_end', models.DateField()),
                ('family_departure_date', models.DateField()),
                ('leave_nature', models.CharField(default='', max_length=50)),
                ('purpose', models.CharField(blank=True, default='', max_length=500)),
                ('is_hometown_or_elsewhere', models.CharField(choices=[('hometown', 'Home Town'), ('elsewhere', 'Elsewhere')], max_length=50)),
                ('phone_number', models.CharField(default='', max_length=13)),
                ('address_during_leave', models.CharField(blank=True, default='', max_length=500)),
                ('travel_mode', models.CharField(choices=[('rail', 'Rail'), ('road', 'Road')], max_length=50)),
                ('ltc_availed', models.CharField(blank=True, default='', max_length=100)),
                ('ltc_to_avail', models.CharField(blank=True, default='', max_length=200)),
                ('dependents', models.CharField(blank=True, default='', max_length=500)),
                ('requested_advance', models.IntegerField(blank=True)),
                ('request_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('review_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('applicant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Ltc Application',
            },
        ),
        migrations.CreateModel(
            name='Ltc_eligible_user',
            fields=[
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='auth.user')),
                ('date_of_joining', models.DateField(default='2005-04-01')),
                ('current_block_size', models.IntegerField(default=4)),
                ('total_ltc_allowed', models.IntegerField(default=2)),
                ('hometown_ltc_allowed', models.IntegerField(default=2)),
                ('elsewhere_ltc_allowed', models.IntegerField(default=1)),
                ('hometown_ltc_availed', models.IntegerField(default=0)),
                ('elsewhere_ltc_availed', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='ThesisResearchSupervision',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stud_name', models.CharField(max_length=30)),
                ('thesis_title', models.CharField(blank=True, max_length=30, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('semester', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants_supervised_stud', to='establishment.appraisal')),
                ('co_supervisors', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_supervisors', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SponsoredProjects',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('project_title', models.CharField(max_length=30)),
                ('sponsoring_agency', models.CharField(max_length=30)),
                ('funding', models.IntegerField()),
                ('duration', models.IntegerField()),
                ('status', models.CharField(max_length=30)),
                ('remarks', models.CharField(max_length=30)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_sponsored_projects', to='establishment.appraisal')),
                ('co_investigators', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='all_co_investigators', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='NewCoursesOffered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('course_num', models.IntegerField(blank=True, null=True)),
                ('ug_or_pg', models.CharField(blank=True, max_length=2, null=True)),
                ('tutorial_hrs_wk', models.FloatField(blank=True, null=True)),
                ('year', models.IntegerField(blank=True, null=True)),
                ('semester', models.IntegerField()),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicants_offered_new_courses', to='establishment.appraisal')),
            ],
        ),
        migrations.CreateModel(
            name='NewCourseMaterial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_name', models.CharField(max_length=30)),
                ('course_num', models.IntegerField(blank=True, null=True)),
                ('ug_or_pg', models.CharField(blank=True, max_length=2, null=True)),
                ('activity_type', models.CharField(blank=True, max_length=10, null=True)),
                ('availiability', models.CharField(blank=True, max_length=10, null=True)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_new_courses_material', to='establishment.appraisal')),
            ],
        ),
        migrations.CreateModel(
            name='Ltc_to_avail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('ltc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ltcToAvail', to='establishment.ltc_application')),
            ],
        ),
        migrations.CreateModel(
            name='Ltc_availed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('ltc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ltcAvailed', to='establishment.ltc_application')),
            ],
        ),
        migrations.CreateModel(
            name='Establishment_variables',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('est_admin', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Dependent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('age', models.IntegerField(blank=True, null=True)),
                ('depend', models.CharField(max_length=30)),
                ('ltc', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Dependent', to='establishment.ltc_application')),
            ],
        ),
        migrations.CreateModel(
            name='Cpda_bill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bill', models.FileField(blank=True, upload_to='')),
                ('application', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='establishment.cpda_application')),
            ],
            options={
                'db_table': 'Cpda Bills',
            },
        ),
        migrations.CreateModel(
            name='CoursesInstructed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('semester', models.IntegerField(blank=True, null=True)),
                ('course_name', models.CharField(max_length=30)),
                ('course_num', models.IntegerField(blank=True, null=True)),
                ('lecture_hrs_wk', models.FloatField(blank=True, null=True)),
                ('tutorial_hrs_wk', models.FloatField(blank=True, null=True)),
                ('lab_hrs_wk', models.FloatField(blank=True, null=True)),
                ('reg_students', models.IntegerField(blank=True, null=True)),
                ('co_instructor', models.CharField(blank=True, max_length=250, null=True)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applicant_courses', to='establishment.appraisal')),
            ],
        ),
        migrations.CreateModel(
            name='AppraisalRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('remark_hod', models.CharField(blank=True, max_length=50, null=True)),
                ('remark_director', models.CharField(blank=True, max_length=50, null=True)),
                ('status_hod', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected'), ('outstanding', 'Outstanding'), ('excellant', 'Excellent'), ('very good', 'Very Good'), ('good', 'Good'), ('poor', 'Poor')], default='pending', max_length=20)),
                ('status_director', models.CharField(choices=[('pending', 'Pending'), ('accepted', 'Accepted'), ('rejected', 'Rejected'), ('forwarded', 'Forwarded'), ('auto rejected', 'Auto Rejected'), ('outstanding', 'Outstanding'), ('excellant', 'Excellent'), ('very good', 'Very Good'), ('good', 'Good'), ('poor', 'Poor')], default='pending', max_length=20)),
                ('permission', models.CharField(blank=True, choices=[('intermediary', 'Intermediary Staff'), ('sanc_auth', 'Appraisal Sanctioning Authority'), ('sanc_off', 'Appraisal Sanctioning Officer')], default='sanc_auth', max_length=20, null=True)),
                ('request_timestamp', models.DateTimeField(auto_now=True, null=True)),
                ('appraisal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appraisal_tracking', to='establishment.appraisal')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='director', to=settings.AUTH_USER_MODEL)),
                ('hod', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='hod', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AppraisalAdministrators',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('authority', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sanc_authority_of_ap', to='globals.designation')),
                ('officer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='sanc_officer_of_ap', to='globals.designation')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='apprasial_admins', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Ltc_tracking',
            fields=[
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='tracking_info', serialize=False, to='establishment.ltc_application')),
                ('designations', models.CharField(blank=True, max_length=350, null=True)),
                ('remarks', models.CharField(blank=True, max_length=350, null=True)),
                ('review_status', models.CharField(choices=[('to_assign', 'To Assign'), ('under_review', 'Under Review'), ('reviewed', 'Reviewed')], max_length=20, null=True)),
                ('admin_remarks', models.CharField(blank=True, max_length=200, null=True)),
                ('reviewer_design', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='globals.designation')),
                ('reviewer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Ltc Tracking',
            },
        ),
        migrations.CreateModel(
            name='Cpda_tracking',
            fields=[
                ('application', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='tracking_info', serialize=False, to='establishment.cpda_application')),
                ('current_reviewer_id', models.IntegerField(blank=True, default=1)),
                ('remarks', models.CharField(blank=True, max_length=250, null=True)),
                ('remarks_rev1', models.CharField(blank=True, max_length=250, null=True)),
                ('remarks_rev2', models.CharField(blank=True, max_length=250, null=True)),
                ('remarks_rev3', models.CharField(blank=True, max_length=250, null=True)),
                ('review_status', models.CharField(choices=[('to_assign', 'To Assign'), ('under_review', 'Under Review'), ('reviewed', 'Reviewed')], max_length=20, null=True)),
                ('bill', models.FileField(blank=True, null=True, upload_to='')),
                ('reviewer_design', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desig1', to='globals.designation')),
                ('reviewer_design2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desig2', to='globals.designation')),
                ('reviewer_design3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='desig3', to='globals.designation')),
                ('reviewer_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer1', to=settings.AUTH_USER_MODEL)),
                ('reviewer_id2', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer2', to=settings.AUTH_USER_MODEL)),
                ('reviewer_id3', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reviewer3', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'Cpda Tracking',
            },
        ),
    ]
