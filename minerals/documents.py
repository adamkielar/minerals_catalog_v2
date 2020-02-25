from django_elasticsearch_dsl import Document
from django_elasticsearch_dsl.registries import registry
from minerals.models import Mineral


@registry.register_document
class MineralDocument(Document):
    class Index:
        name = 'minerals'
        settings = {
            'number_of_shards': 1,
            'number_of_replicas': 0,
        }
    class Django:
        model = Mineral
        fields = [
            'name',
            'image_filename',
            'image_caption',
            'category',
            'formula',
            'strunz_classification',
            'crystal_system',
            'unit_cell',
            'color',
            'crystal_symmetry',
            'cleavage',
            'mohs_scale_hardness',
            'luster',
            'streak',
            'diaphaneity',
            'optical_properties',
            'refractive_index',
            'group',
            'crystal_habit',
            'specific_gravity',
        ]
