# Generated by Django 4.2 on 2025-04-11 02:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Процессор ',
                'verbose_name_plural': '1.4 Процессор',
            },
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название цеха')),
                ('boss_fullName', models.CharField(max_length=255, verbose_name='Руководитель цеха')),
            ],
            options={
                'verbose_name': 'Цех ',
                'verbose_name_plural': 'Цех',
            },
        ),
        migrations.CreateModel(
            name='DiskType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип диска ',
                'verbose_name_plural': '2.5 Тип диска',
            },
        ),
        migrations.CreateModel(
            name='Frequency',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Частота процессора ',
                'verbose_name_plural': '1.6 Частота процессора',
            },
        ),
        migrations.CreateModel(
            name='Generation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Поколение процессора ',
                'verbose_name_plural': '1.5 Поколение процессора',
            },
        ),
        migrations.CreateModel(
            name='GPU',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Видеокарта ',
                'verbose_name_plural': '2 Видеокарта',
            },
        ),
        migrations.CreateModel(
            name='HDD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Диск  HDD ',
                'verbose_name_plural': '1.7 Диск  HDD',
            },
        ),
        migrations.CreateModel(
            name='MFO',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'МФУ ',
                'verbose_name_plural': '2.2 МФУ',
            },
        ),
        migrations.CreateModel(
            name='ModelWebCamera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Модель вебкамеры ',
                'verbose_name_plural': '2.4 Модель вебкамеры',
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Монитор ',
                'verbose_name_plural': '2.5 Монитор',
            },
        ),
        migrations.CreateModel(
            name='Motherboard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Производитель МП ',
                'verbose_name_plural': '1.2 Производитель МП',
            },
        ),
        migrations.CreateModel(
            name='MotherboardModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Модель МП ',
                'verbose_name_plural': '1.3 Модель МП',
            },
        ),
        migrations.CreateModel(
            name='OS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Операционная система ',
                'verbose_name_plural': '2.5 Операционная система',
            },
        ),
        migrations.CreateModel(
            name='Printer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Принтер ',
                'verbose_name_plural': '2.1 Принтер',
            },
        ),
        migrations.CreateModel(
            name='ProgramLicense',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_pdf', models.FileField(upload_to='', verbose_name='Лицензии PDF')),
                ('begin_date', models.DateField(verbose_name='Дата начала лицензии')),
                ('finish_date', models.DateField(verbose_name='Дата окончания лицензии')),
            ],
            options={
                'verbose_name': 'Программа лицензии ',
                'verbose_name_plural': 'Программа лицензии',
            },
        ),
        migrations.CreateModel(
            name='RAMSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Размер оперативной памяти ',
                'verbose_name_plural': '1.9 Размер оперативной памяти',
            },
        ),
        migrations.CreateModel(
            name='RAMType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип оперативки ',
                'verbose_name_plural': '2.5 Тип оперативки',
            },
        ),
        migrations.CreateModel(
            name='Scaner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Сканер ',
                'verbose_name_plural': '2.2 Сканер',
            },
        ),
        migrations.CreateModel(
            name='SSD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Диск  SSD ',
                'verbose_name_plural': '1.8 Диск  SSD',
            },
        ),
        migrations.CreateModel(
            name='TypeCompyuter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип орг.техники ',
                'verbose_name_plural': '1.1 Тип орг.техники',
            },
        ),
        migrations.CreateModel(
            name='TypeWebCamera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Тип вебкамера ',
                'verbose_name_plural': '2.3 Тип вебкамера',
            },
        ),
        migrations.CreateModel(
            name='WarehouseManager',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
            ],
            options={
                'verbose_name': 'Зав. склада ',
                'verbose_name_plural': '1.1 Зав. склада',
            },
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название отдела')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.department', verbose_name='Название цеха')),
            ],
            options={
                'verbose_name': 'Отдел ',
                'verbose_name_plural': 'Отдел',
            },
        ),
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('license_type', models.CharField(choices=[('license', 'Лицензированный'), ('no-license', 'Не лицензированный')], max_length=255, verbose_name='Cтатус лицензии')),
                ('type', models.CharField(choices=[('systemic', 'Системная'), ('additional', 'Дополнительные')], max_length=255, verbose_name='Тип программы')),
                ('title', models.CharField(max_length=255, verbose_name='Название программы')),
                ('version', models.CharField(max_length=255, verbose_name='Версия программы')),
                ('license_data', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.programlicense', verbose_name='Инфо лицензии')),
            ],
            options={
                'verbose_name': 'Программа ',
                'verbose_name_plural': 'Программа',
            },
        ),
        migrations.CreateModel(
            name='HistoricalCompyuter',
            fields=[
                ('id', models.BigIntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('seal_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер пломбы')),
                ('user', models.CharField(blank=True, max_length=255, null=True, verbose_name='Пользователь')),
                ('ipadresss', models.CharField(blank=True, max_length=255, null=True, verbose_name='IPv4 адрес')),
                ('mac_adress', models.CharField(blank=True, max_length=255, null=True, verbose_name='Физический(MAC) адрес')),
                ('qr_image', models.TextField(blank=True, default='qr_codes/default.png', max_length=100, null=True, verbose_name='QR-код')),
                ('bg_image', models.TextField(blank=True, default='back.jpg', max_length=100, null=True, verbose_name='QR-код')),
                ('internet', models.BooleanField(blank=True, default=False, null=True, verbose_name='Интернет')),
                ('joinDate', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Дате')),
                ('updatedAt', models.DateTimeField(blank=True, editable=False, null=True, verbose_name='Дата изменения')),
                ('slug', models.SlugField(blank=True)),
                ('isActive', models.BooleanField(default=True)),
                ('history_change_reason', models.TextField(null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField(db_index=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('CPU', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.cpu', verbose_name='Процессор')),
                ('GPU', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.gpu', verbose_name='Видеокарта')),
                ('HDD', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.hdd', verbose_name='Диск  HDD')),
                ('RAMSize', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.ramsize', verbose_name='Размер оперативной памяти')),
                ('RAM_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.ramtype', verbose_name='Тип оперативки')),
                ('SSD', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.ssd', verbose_name='Диск  SSD')),
                ('addedUser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
                ('departament', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.department', verbose_name='Цех')),
                ('disk_type', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.disktype', verbose_name='Тип диска')),
                ('frequency', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.frequency', verbose_name='Частота процессора')),
                ('generation', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.generation', verbose_name='Поколение процессора')),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
                ('motherboard', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.motherboard', verbose_name='Производитель МП')),
                ('motherboard_model', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.motherboardmodel', verbose_name='Модель МП')),
                ('type_compyuter', models.ForeignKey(blank=True, db_constraint=False, default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.typecompyuter', verbose_name='Тип орг.техники')),
                ('updatedUser', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to=settings.AUTH_USER_MODEL, verbose_name='Изменил')),
                ('warehouse_manager', models.ForeignKey(blank=True, db_constraint=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='+', to='Инвентаризация.warehousemanager', verbose_name='Зав. склада')),
            ],
            options={
                'verbose_name': 'historical Компьютеры ',
                'verbose_name_plural': 'historical Компьютеры',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': ('history_date', 'history_id'),
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Compyuter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seal_number', models.CharField(blank=True, max_length=255, null=True, verbose_name='Номер пломбы')),
                ('user', models.CharField(blank=True, max_length=255, null=True, verbose_name='Пользователь')),
                ('ipadresss', models.CharField(blank=True, max_length=255, null=True, verbose_name='IPv4 адрес')),
                ('mac_adress', models.CharField(blank=True, max_length=255, null=True, verbose_name='Физический(MAC) адрес')),
                ('qr_image', models.ImageField(blank=True, default='qr_codes/default.png', null=True, upload_to='qr_codes/', verbose_name='QR-код')),
                ('bg_image', models.ImageField(blank=True, default='back.jpg', null=True, upload_to='', verbose_name='QR-код')),
                ('internet', models.BooleanField(blank=True, default=False, null=True, verbose_name='Интернет')),
                ('joinDate', models.DateTimeField(auto_now=True, null=True, verbose_name='Дате')),
                ('updatedAt', models.DateTimeField(auto_now=True, null=True, verbose_name='Дата изменения')),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('isActive', models.BooleanField(default=True)),
                ('CPU', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.cpu', verbose_name='Процессор')),
                ('GPU', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.gpu', verbose_name='Видеокарта')),
                ('HDD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.hdd', verbose_name='Диск  HDD')),
                ('RAMSize', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.ramsize', verbose_name='Размер оперативной памяти')),
                ('RAM_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.ramtype', verbose_name='Тип оперативки')),
                ('SSD', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.ssd', verbose_name='Диск  SSD')),
                ('addedUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='Сотрудник')),
                ('departament', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.department', verbose_name='Цех')),
                ('disk_type', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.disktype', verbose_name='Тип диска')),
                ('frequency', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.frequency', verbose_name='Частота процессора')),
                ('generation', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.generation', verbose_name='Поколение процессора')),
                ('mfo', models.ManyToManyField(blank=True, null=True, related_name='mfo', to='Инвентаризация.mfo', verbose_name='МФУ')),
                ('model_webcam', models.ManyToManyField(blank=True, null=True, to='Инвентаризация.modelwebcamera', verbose_name='Модель вебкамеры')),
                ('motherboard', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.motherboard', verbose_name='Производитель МП')),
                ('motherboard_model', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.motherboardmodel', verbose_name='Модель МП')),
                ('printer', models.ManyToManyField(blank=True, null=True, related_name='printer', to='Инвентаризация.printer', verbose_name='Принтеры')),
                ('program', models.ManyToManyField(blank=True, null=True, to='Инвентаризация.program', verbose_name='Программы')),
                ('scaner', models.ManyToManyField(blank=True, null=True, related_name='scaner', to='Инвентаризация.scaner', verbose_name='Сканеры')),
                ('type_compyuter', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.typecompyuter', verbose_name='Тип орг.техники')),
                ('type_monitor', models.ManyToManyField(blank=True, null=True, related_name='typeMonitor', to='Инвентаризация.monitor', verbose_name='Тип Монитора')),
                ('type_webcamera', models.ManyToManyField(blank=True, null=True, related_name='typeCamera', to='Инвентаризация.typewebcamera', verbose_name='Тип вебкамера')),
                ('updatedUser', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='updated_computers', to=settings.AUTH_USER_MODEL, verbose_name='Изменил')),
                ('warehouse_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Инвентаризация.warehousemanager', verbose_name='Зав. склада')),
            ],
            options={
                'verbose_name': 'Компьютеры ',
                'verbose_name_plural': 'Компьютеры',
            },
        ),
    ]
