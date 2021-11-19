# Generated by Django 3.2.8 on 2021-11-19 17:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccountEmailaddress',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('email', models.CharField(max_length=254, unique=True)),
                ('verified', models.BooleanField()),
                ('primary', models.BooleanField()),
            ],
            options={
                'db_table': 'account_emailaddress',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AccountEmailconfirmation',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('created', models.DateTimeField()),
                ('sent', models.DateTimeField(blank=True, null=True)),
                ('key', models.CharField(max_length=64, unique=True)),
            ],
            options={
                'db_table': 'account_emailconfirmation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, unique=True)),
            ],
            options={
                'db_table': 'auth_group',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthGroupPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_group_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthPermission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('codename', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'auth_permission',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128)),
                ('last_login', models.DateTimeField(blank=True, null=True)),
                ('is_superuser', models.BooleanField()),
                ('username', models.CharField(max_length=150, unique=True)),
                ('first_name', models.CharField(max_length=150)),
                ('last_name', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=254)),
                ('is_staff', models.BooleanField()),
                ('is_active', models.BooleanField()),
                ('date_joined', models.DateTimeField()),
            ],
            options={
                'db_table': 'auth_user',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserGroups',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_groups',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='AuthUserUserPermissions',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
            ],
            options={
                'db_table': 'auth_user_user_permissions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoAdminLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('action_time', models.DateTimeField()),
                ('object_id', models.TextField(blank=True, null=True)),
                ('object_repr', models.CharField(max_length=200)),
                ('action_flag', models.SmallIntegerField()),
                ('change_message', models.TextField()),
            ],
            options={
                'db_table': 'django_admin_log',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoContentType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('app_label', models.CharField(max_length=100)),
                ('model', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'django_content_type',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoMigrations',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('app', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('applied', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_migrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSession',
            fields=[
                ('session_key', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('session_data', models.TextField()),
                ('expire_date', models.DateTimeField()),
            ],
            options={
                'db_table': 'django_session',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='DjangoSite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('domain', models.CharField(max_length=100, unique=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'django_site',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialaccount',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('provider', models.CharField(max_length=30)),
                ('uid', models.CharField(max_length=191)),
                ('last_login', models.DateTimeField()),
                ('date_joined', models.DateTimeField()),
                ('extra_data', models.TextField()),
            ],
            options={
                'db_table': 'socialaccount_socialaccount',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialapp',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('provider', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=40)),
                ('client_id', models.CharField(max_length=191)),
                ('secret', models.CharField(max_length=191)),
                ('key', models.CharField(max_length=191)),
            ],
            options={
                'db_table': 'socialaccount_socialapp',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialappSites',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('socialapp_id', models.BigIntegerField()),
            ],
            options={
                'db_table': 'socialaccount_socialapp_sites',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='SocialaccountSocialtoken',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('token', models.TextField()),
                ('token_secret', models.TextField()),
                ('expires_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'socialaccount_socialtoken',
                'managed': False,
            },
        ),
    ]
