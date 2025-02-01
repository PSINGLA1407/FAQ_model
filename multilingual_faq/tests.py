import pytest
from myapp.models import MyModel

@pytest.mark.django_db
def test_my_model_creation():
    instance = MyModel.objects.create(field1='value1', field2='value2')
    assert instance.pk is not None
