# Generated by Django 3.1.3 on 2021-03-09 17:50

from django.db import migrations, models
import django.db.models.deletion
import django_resized.forms


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_id', models.CharField(max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Food',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, verbose_name='名称')),
                ('commented', models.IntegerField(default=0, verbose_name='评价人数')),
                ('photo', django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[600, 600], upload_to='foods', verbose_name='菜品图片')),
                ('stars', models.BigIntegerField(default=0, verbose_name='总星数')),
            ],
        ),
        migrations.CreateModel(
            name='FoodForMeal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total', models.IntegerField(verbose_name='总份数')),
                ('wanted', models.IntegerField(default=0, verbose_name='想要人数')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.food', verbose_name='菜品')),
            ],
        ),
        migrations.CreateModel(
            name='FoodForStudent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('food_for_meal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.foodformeal', verbose_name='点的菜')),
            ],
        ),
        migrations.CreateModel(
            name='Meal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='日期')),
                ('index', models.PositiveSmallIntegerField(verbose_name='当日索引')),
                ('description', models.CharField(max_length=4, verbose_name='描述')),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_id', models.CharField(max_length=6, verbose_name='学号')),
                ('name', models.CharField(max_length=16, verbose_name='姓名')),
                ('password', models.CharField(max_length=32, verbose_name='密码—md5加密')),
                ('asked_meal', models.ManyToManyField(blank=True, through='canteen.FoodForStudent', to='canteen.FoodForMeal', verbose_name='已点的餐')),
                ('last_order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.meal', verbose_name='上次点餐的Meal')),
                ('stu_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.class', verbose_name='班级')),
            ],
        ),
        migrations.AddField(
            model_name='foodforstudent',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.student', verbose_name='学生'),
        ),
        migrations.AddField(
            model_name='foodformeal',
            name='meal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.meal', verbose_name='餐'),
        ),
        migrations.AddField(
            model_name='food',
            name='meal',
            field=models.ManyToManyField(through='canteen.FoodForMeal', to='canteen.Meal', verbose_name='关联餐'),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(verbose_name='发表日期')),
                ('stars', models.PositiveSmallIntegerField(verbose_name='打分')),
                ('content', models.CharField(max_length=1024, verbose_name='评论内容')),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.food', verbose_name='所评食物')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='canteen.student', verbose_name='评价学生')),
            ],
        ),
    ]
