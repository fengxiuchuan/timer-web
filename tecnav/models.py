from django.db import models

# Create your models here.


# 标签类
class TLabel(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    #标签名称
    name = models.CharField(max_length=50,null=True)
    #标签描述
    desc = models.CharField(max_length=200,null=True)

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
    #原始文件名称
    file_name = models.CharField(max_length=100,null=True)
    #文件大小
    image_size = models.IntegerField(max_length=8,null=True)
    #文件保存路径
    image_path = models.CharField(max_length=100,null=True)
    #文件类型
    image_type = models.CharField(max_length=20,null=True)
    #保存的文件名称
    save_file_name = models.CharField(max_length=80,null=True)

    def __str__(self):
        return '%s %s' % (self.file_name,self.image_path)

    class Meta:
        app_label = 'tecnav'
        db_table = 'timer_image'

#图片关联
class TImageRel(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    #业务主键
    business_id = models.BigIntegerField(max_length=20,null=True)
    #业务类型
    business_type = models.CharField(max_length=20,null=True)
    #图片主键ID
    image_id = models.BigIntegerField(max_length=20,null=True)

    def __str__(self):
        return '%d %d %s' % (self.id,self.business_id,self.business_type)

    class Meta:
        app_label = 'tecnav'
        db_table = 'timer_image_rel'

#网站导航
class TSite(models.Model):
    id = models.AutoField(primary_key=True,unique=True,null=False)
    #网站链接
    site_url = models.CharField(max_length=200,null=True)
    #网站名称
    site_name = models.CharField(max_length=100,null=True)
    #网站描述
    site_desc = models.CharField(max_length=500,null=True)

    #重写__str__方法
    def __str__(self):
        return '%d %s %s' % (self.id,self.site_url,self.site_desc)

    class Meta:
        app_label = 'tecnav'
        db_table = 'timer_site'