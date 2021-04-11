FIELD_MAPPERS = {
    '121': 'models.OneToOneField("{0}", on_delete=models.CASCADE)',
    'bool': 'models.BooleanField(default=True)',
    'char': 'models.CharField(max_length=50)',
    'date': 'models.DateField(default=timezone.now)',
    'datetime': 'models.DateTimeField(default=timezone.now)',
    'dt': 'models.DateTimeField(default=timezone.now)',
    'dict': 'models.ManyToManyField("{0}")',
    'email': 'models.EmailField(max_length=50)',
    'file': 'models.FileField()',
    'fk': 'models.ForeignKey("{0}", on_delete=models.CASCADE)',
    'float': 'models.FloatField(default=0)',
    'dec': 'models.DecimalField(default=0, max_digits=7, decimal_places=2)',
    'image': 'models.ImageField()',
    'img': 'models.ImageField()',
    'int': 'models.IntegerField(default=0)',
    'list': 'models.ForeignKey("{0}", on_delete=models.CASCADE)',
    'm2m': 'models.ManyToManyField("{0}")',
    'o2o': 'models.OneToOneField("{0}", on_delete=models.CASCADE)',
    'set': 'models.OneToOneField("{0}", on_delete=models.CASCADE)',
    'str': 'models.CharField(max_length=50)',
    'text': 'models.TextField()',
    'txt': 'models.TextField()',
}


MODEL_FIELD_TEMPLATE = """    {0} = {1}\n"""
