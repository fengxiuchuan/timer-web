from django.db import models

# Create your models here.


# 标签类
class TLabel(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    name = models.CharField(max_length=50,)
    desc = models.CharField(max_length=200)

    def __str__(self):
        return 'mysql_tecnav %s ' % self.name

    class Meta:
        app_label = 'tecnav'
        db_table = 'timer_label'

#我的
class TPerson(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    p_name = models.CharField(max_length=50,null=True)
    p_phone = models.CharField(max_length=50,null=True)
    p_email = models.EmailField(max_length=100,null=True)
    p_sex = models.IntegerField(max_length=1,null=True)


    def __str__(self):
        return 'mysql_tecnav %s ' % self.name

    class Meta:
        app_label = 'tecnav'
        db_table = 'timer_person'

#我创建的
class TPersonSite(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    sitId = models.BigIntegerField(max_length=20)

    def __str__(self):
        return '%s %s' % (self.id,self.sitId)

    class Meta:
        app_label = 'tecnav'
        db_table = 'timer_person_site'


#图片
class TImage(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    file_name = models.CharField(max_length=100)
    image_size = models.IntegerField(max_length=8)
    image_path = models.CharField(max_length=100)
    image_type = models.CharField(max_length=20)
    save_file_name = models.CharField(max_length=80)

    def __str__(self):
        return '%s %s' % (self.file_name,self.image_path)

    class Meta:
        app_label = 'tecnav'
        db_table = 'timer_image'

#图片关联
class TImageRel(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    business_id = models.BigIntegerField(max_length=20)
    business_type = models.CharField(max_length=20)

    def __str__(self):
        return '%d %d %s' % (self.id,self.business_id,self.business_type)

    class Meta:
        app_label = 'tecnav'
        db_table = 'timer_image_rel'

#网站导航
class TSite(models.Model):
    id = models.AutoField(primary_key=True)
    site_url = models.CharField(max_length=200)
    site_desc = models.CharField(max_length=500)


    def __str__(self):
        return '%d %s %s' % (self.id,self.site_url,self.site_desc)

    class Meta:
        app_label = 'tecnav'
        db_table = 'timer_site'