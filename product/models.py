from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.urls import reverse


# Create your models here.

# Function Name Upload
def product_img_upload(instance,filename):
    imgname , imgextension = filename.split(".")
    return "product/%s/%s.%s"%(instance.item_no,instance.item_no,imgextension)

def category_img_upload(instance,filename):
    imgname , imgextension = filename.split(".")
    return "category/%s/%s.%s"%(instance.class_m_name,instance.class_m_name,imgextension)

def brand_img_upload(instance,filename):
    imgname , imgextension = filename.split(".")
    return "brand/%s/%s.%s"%(instance.camp_name,instance.camp_name,imgextension)

class ComStClassMaster(models.Model):
    class_m_no = models.AutoField(primary_key=True)
    class_m_name = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("Category Main Name"))
    class_m_descraption = models.TextField(max_length=1000, blank=True, null=True,verbose_name=_("Category Descraption"))
    class_m_img = models.ImageField(upload_to=category_img_upload,blank=True, null=True,verbose_name=_("Category Photo"))

    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs ):
        self.slug = slugify(self.class_m_name)
        return super(ComStClassMaster,self).save(*args,**kwargs)

    def __str__(self):
        return self.class_m_name
    class Meta:
        db_table = 'com_st_class_master'
        verbose_name = 'Main Category'
        verbose_name_plural = 'Main Categories'
        ordering = ['class_m_no']

class ComStClassDetails(models.Model):
    class_d_no = models.AutoField(primary_key=True)
    class_m_no = models.ForeignKey('ComStClassMaster',on_delete=models.CASCADE,verbose_name=_("Category Main Name"))
    class_d_name = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("Category Sub Name"))
    class_d_descraption = models.TextField(max_length=1000, blank=True, null=True,verbose_name=_("Category Sub Descraption"))

    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs ):
        self.slug = slugify(self.class_d_name)
        return super(ComStClassDetails,self).save(*args,**kwargs)

    def __str__(self):
        return str(self.class_d_name)
    class Meta:
        db_table = 'com_st_class_details'
        verbose_name = 'Sub Category'
        verbose_name_plural = 'Sub Categories'

    def get_categroy_url(self):
        return reverse("product:catgeroies", kwargs={"slug":self.slug})

class ComStCampProduced(models.Model):
    camp_id = models.AutoField(primary_key=True)
    camp_name = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("Brand Name"))
    camp_comp = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("Brand Company Name"))
    camp_alias = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("Brand Alias Name"))
    camp_logo = models.ImageField(upload_to=brand_img_upload,blank=True, null=True,verbose_name=_("Brand Photo"))
    camp_swift_code = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("Brand Swift Code"))
    camp_email = models.EmailField(max_length=254, blank=True, null=True,verbose_name=_("Brand Email"))
    camp_tel_one = models.CharField(max_length=25, blank=True, null=True,verbose_name=_("Brand Phone (1)"))
    camp_tel_two = models.CharField(max_length=25, blank=True, null=True,verbose_name=_("Brand Phone (2)"))
    camp_fax_no = models.CharField(max_length=25, blank=True, null=True,verbose_name=_("Brand Fax"))
    camp_mob_one = models.CharField(max_length=25, blank=True, null=True,verbose_name=_("Brand Moblie (1)"))
    camp_mob_two = models.CharField(max_length=25, blank=True, null=True,verbose_name=_("Brand Moblie (2)"))
    camp_address_one = models.CharField(max_length=300, blank=True, null=True,verbose_name=_("Brand Address (1)"))
    camp_address_two = models.CharField(max_length=300, blank=True, null=True,verbose_name=_("Brand Address (2)"))
    camp_web = models.CharField(max_length=200, blank=True, null=True,verbose_name=_("Brand WebSite"))
    camp_contact = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("Brand Contact"))

    slug=models.SlugField(blank=True,null=True)

    def save(self,*args,**kwargs ):
        self.slug = slugify(self.camp_name)
        return super(ComStCampProduced,self).save(*args,**kwargs)

    def __str__(self):
        return self.camp_name

    class Meta:
        db_table = 'com_st_camp_produced'
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['camp_id']


class ComStUnits(models.Model):
    unit_no = models.AutoField(primary_key=True)
    unit_name = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("Unit Name"))
    unit_parameters = models.IntegerField(blank=True, null=True,verbose_name=_("Unit Parameter"))
    def __str__(self):
        return self.unit_name
    class Meta:
        db_table = 'com_st_units'
        verbose_name = 'Unit'
        verbose_name_plural = 'Units'

class ComStItemColors(models.Model):
    item_c_no = models.AutoField(primary_key=True)
    item_c_name = models.CharField(max_length=50, blank=True, null=True,verbose_name=_("Color Name"))
    def __str__(self):
        return self.item_c_name
    class Meta:
        db_table = 'com_st_item_colors'
        verbose_name = 'Color'
        verbose_name_plural = 'Colors'

class ComStProducts(models.Model):

    GUARANTEE = [
        ('yes','yes'),
        ('no','no'),
    ]
    GUARANTEE_TYPE = [
        ('month','month'),
        ('year','year'),
    ]
    PRODUCT_TYPE = [
        ('new','new'),
        ('used','used'),
    ]
    item_no = models.AutoField(primary_key=True)
    camp_id = models.ForeignKey('ComStCampProduced', on_delete=models.CASCADE,verbose_name=_("Brand Name"))
    item_full_name = models.CharField(max_length=150, blank=True, null=True,verbose_name=_("Product Name"))
    item_alias = models.CharField(max_length=20, blank=True, null=True,verbose_name=_("Product Alias"))
    item_desc = models.TextField(max_length=1000, blank=True, null=True,verbose_name=_("Product Descraption"))
    item_code = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("Product Code"))
    item_type_no = models.CharField(max_length=25, blank=True, null=True,choices=PRODUCT_TYPE,verbose_name=_("Product Type"))
    class_d_no = models.ForeignKey('ComStClassDetails', on_delete=models.CASCADE, db_column='class_d_no',verbose_name=_("Product Category Sub"))
    unit_no = models.ForeignKey('ComStUnits', on_delete=models.CASCADE, db_column='unit_no',verbose_name=_("Product Unit"))
    item_c_no = models.ForeignKey('ComStItemColors', on_delete=models.CASCADE, db_column='item_c_no', blank=True, null=True,verbose_name=_("Product Color"))
    item_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True,verbose_name=_("Product Price"))
    have_serial = models.CharField(max_length=100, blank=True, null=True,verbose_name=_("Product Serial"))
    last_update = models.DateTimeField(auto_now_add=True)
    saling_price = models.DecimalField(max_digits=11, decimal_places=2, blank=True, null=True,verbose_name=_("Product Price Saling"))
    item_image = models.ImageField(upload_to=product_img_upload,null=True,blank=True,verbose_name=_("Product Photo"))
    have_guarantee = models.CharField(max_length=100, blank=True, null=True,choices=GUARANTEE,verbose_name=_("Product Warranty"))
    guarantee_type = models.CharField(max_length=100, blank=True, null=True,choices=GUARANTEE_TYPE,verbose_name=_("Product Warranty Date"))
    published_at_item = models.DateTimeField(auto_now=True)
    item_comment = models.TextField(max_length=1000, blank=True, null=True,verbose_name=_("Product Comment"))
    have_barcode = models.CharField(max_length=100, blank=True, null=True,choices=GUARANTEE,verbose_name=_("Product Barcode"))
    item_stok =  models.IntegerField(blank=True, null=True,verbose_name=_("Product Stok"))
    
    slug = models.SlugField(blank=True,null=True)

    class Meta:
        db_table = 'com_st_products'
        verbose_name = 'Product'
        verbose_name_plural = 'Products'
        ordering = ['item_no']

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.item_full_name)
        return super(ComStProducts,self).save(*args, **kwargs)

    def __str__(self):
        return str(self.item_full_name)


    def get_absolute_url(self):
        return reverse("product:product_single", kwargs={"slug":self.slug})


    



class ComStItemImage(models.Model):
    item_image_no = models.AutoField(primary_key=True)
    item_no = models.ForeignKey('ComStProducts',  on_delete=models.CASCADE, db_column='item_no', blank=True, null=True,verbose_name=_("Product"))
    item_image_s = models.ImageField(upload_to=product_img_upload,null=True,blank=True,verbose_name=_("Product Photos"))
    def __str__(self):
        return str(self.item_no)

    class Meta:
        db_table = 'com_st_item_image'
        verbose_name = 'Product Photo'
        verbose_name_plural = 'Product Photos'

class ComStAlternative_Pro(models.Model):
    item_no = models.ForeignKey('ComStProducts',  on_delete=models.CASCADE, db_column='item_no',related_name='item_alternative_no',verbose_name=_("Product"))
    item_alternative = models.ManyToManyField(ComStProducts,related_name='item_alternative',verbose_name=_("Product Alternative"))
    def __str__(self):
        return str(self.item_no)

    class Meta:
        db_table = 'com_st_alternative_pro'
        verbose_name = 'Product Alternative'
        verbose_name_plural = 'Product Alternatives'

class ComStAccessories_pro(models.Model):
    item_no = models.ForeignKey('ComStProducts',  on_delete=models.CASCADE, db_column='item_no',related_name='item_accessories_no',verbose_name=_("Product"))
    item_alternative = models.ManyToManyField(ComStProducts,related_name='item_accessories',verbose_name=_("Product Accessories"))
    def __str__(self):
        return str(self.item_no)
    class Meta:
        db_table = 'com_st_accessories_pro'
        verbose_name = 'Product Accessory'
        verbose_name_plural = 'Product Accessories'

