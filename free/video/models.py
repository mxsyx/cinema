# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Anime(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=80)  # Field name made lowercase.
    introduction = models.TextField(db_column='INTRODUCTION', blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='DIRECTOR', max_length=60, blank=True, null=True)  # Field name made lowercase.
    actor = models.TextField(db_column='ACTOR', blank=True, null=True)  # Field name made lowercase.
    flag_time = models.CharField(db_column='FLAG_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    flag_area = models.CharField(db_column='FLAG_AREA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    flag_type = models.CharField(db_column='FLAG_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    url_img = models.TextField(db_column='URL_IMG', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateField(db_column='UPDATE_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'anime'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Begfilm(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15)  # Field name made lowercase.
    ttime = models.DateTimeField(db_column='TTIME')  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'begfilm'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Feedback(models.Model):
    id = models.AutoField(db_column='ID', primary_key=True)  # Field name made lowercase.
    ip = models.CharField(db_column='IP', max_length=15)  # Field name made lowercase.
    ttime = models.DateTimeField(db_column='TTIME')  # Field name made lowercase.
    url = models.CharField(db_column='URL', max_length=60)  # Field name made lowercase.
    content = models.TextField(db_column='CONTENT')  # Field name made lowercase.
    email = models.CharField(db_column='EMAIL', max_length=255)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'feedback'


class Movie(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=80)  # Field name made lowercase.
    introduction = models.TextField(db_column='INTRODUCTION', blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='DIRECTOR', max_length=60, blank=True, null=True)  # Field name made lowercase.
    actor = models.TextField(db_column='ACTOR', blank=True, null=True)  # Field name made lowercase.
    flag_time = models.CharField(db_column='FLAG_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    flag_area = models.CharField(db_column='FLAG_AREA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    flag_type = models.CharField(db_column='FLAG_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    url_img = models.TextField(db_column='URL_IMG', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateField(db_column='UPDATE_TIME')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'movie'


class Ranking(models.Model):
    vid = models.CharField(db_column='VID', primary_key=True, max_length=8)  # Field name made lowercase.
    rday = models.IntegerField(db_column='RDAY', blank=True, null=True)  # Field name made lowercase.
    rweek = models.IntegerField(db_column='RWEEK', blank=True, null=True)  # Field name made lowercase.
    rmonth = models.IntegerField(db_column='RMONTH', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ranking'


class Tvseries(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=80)  # Field name made lowercase.
    introduction = models.TextField(db_column='INTRODUCTION', blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='DIRECTOR', max_length=60, blank=True, null=True)  # Field name made lowercase.
    actor = models.TextField(db_column='ACTOR', blank=True, null=True)  # Field name made lowercase.
    flag_time = models.CharField(db_column='FLAG_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    flag_area = models.CharField(db_column='FLAG_AREA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    flag_type = models.CharField(db_column='FLAG_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    url_img = models.TextField(db_column='URL_IMG', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateField(db_column='UPDATE_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'tvseries'


class UAnime(models.Model):
    vid = models.IntegerField(db_column='VID', primary_key=True)  # Field name made lowercase.
    num = models.PositiveSmallIntegerField(db_column='NUM')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_anime'
        unique_together = (('vid', 'num'),)


class UTvseries(models.Model):
    vid = models.IntegerField(db_column='VID', primary_key=True)  # Field name made lowercase.
    num = models.PositiveSmallIntegerField(db_column='NUM')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_tvseries'
        unique_together = (('vid', 'num'),)


class UVariety(models.Model):
    vid = models.IntegerField(db_column='VID', primary_key=True)  # Field name made lowercase.
    num = models.PositiveSmallIntegerField(db_column='NUM')  # Field name made lowercase.
    url = models.TextField(db_column='URL', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'u_variety'
        unique_together = (('vid', 'num'),)


class Variety(models.Model):
    id = models.IntegerField(db_column='ID', primary_key=True)  # Field name made lowercase.
    name = models.CharField(db_column='NAME', unique=True, max_length=80)  # Field name made lowercase.
    introduction = models.TextField(db_column='INTRODUCTION', blank=True, null=True)  # Field name made lowercase.
    director = models.CharField(db_column='DIRECTOR', max_length=60, blank=True, null=True)  # Field name made lowercase.
    actor = models.TextField(db_column='ACTOR', blank=True, null=True)  # Field name made lowercase.
    flag_time = models.CharField(db_column='FLAG_TIME', max_length=4, blank=True, null=True)  # Field name made lowercase.
    flag_area = models.CharField(db_column='FLAG_AREA', max_length=8, blank=True, null=True)  # Field name made lowercase.
    flag_type = models.CharField(db_column='FLAG_TYPE', max_length=20, blank=True, null=True)  # Field name made lowercase.
    score = models.FloatField(db_column='SCORE', blank=True, null=True)  # Field name made lowercase.
    url_img = models.TextField(db_column='URL_IMG', blank=True, null=True)  # Field name made lowercase.
    update_time = models.DateField(db_column='UPDATE_TIME')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'variety'
