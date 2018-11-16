from import_export import resources
from .models import SkeletalBones,SkeletalElement,Measurements,Pathology,Taphonomy,Trauma,Zones,SeAnomaly,SeArticulation,Nodes, Links, Sb_art, Art


class SbResource(resources.ModelResource):
    class Meta:
        model = SkeletalBones
        exclude = ('created_by','updated_by','created_at','updated_at','deleted_at')

class SeResource(resources.ModelResource):
    class Meta:
        model = SkeletalElement


class MeasurementResource(resources.ModelResource):
    class Meta:
        model = Measurements


class PathologyResource(resources.ModelResource):
    class Meta:
        model = Pathology


class TaphonomyResource(resources.ModelResource):
    class Meta:
        model = Taphonomy


class TraumaResource(resources.ModelResource):
    class Meta:
        model = Trauma


class ZonesResource(resources.ModelResource):
    class Meta:
        model = Zones

class SeAnomalyResource(resources.ModelResource):
    class Meta:
        model = SeAnomaly


class SeArticulationResource(resources.ModelResource):
    class Meta:
        model = SeArticulation


class NodesResource(resources.ModelResource):
    class Meta:
        model = Nodes
        import_id_fields = ['se_id']


class LinksResource(resources.ModelResource):
    class Meta:
        model = Links
        import_id_fields = ['source']


class SlLinkResource(resources.ModelResource):
    class Meta:
        model = Sb_art
        import_id_fields = ['source']


class SlNodeResource(resources.ModelResource):
    class Meta:
        model = Art
        import_id_fields = ['id']