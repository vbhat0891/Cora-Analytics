# from django.contrib import admin
# from .models import SkeletalBones, SkeletalElement
#
#
# class SkeletalBonesList(admin.ModelAdmin):
#     list_display = ('bone_id', 'bone_name', 'bone_category', 'bone_type', 'bone_group', 'bone_description', 'bone_paired', 'bone_articulated', 'bone_zones', 'bone_measurements', 'bone_dental')
#     list_filter = ('bone_id', 'bone_name' , 'bone_category','bone_type', 'bone_group')
#     search_fields = ('bone_name', 'bone_category', 'bone_type', 'bone_group')
#
#
# class SkeletalElementList(admin.ModelAdmin):
#     list_display = ('se_id', 'se_bone_id', 'se_key', 'se_accession_number', 'se_g_number', 'se_x_number', 'se_designator', 'se_side', 'se_completeness', 'se_measured', 'se_dna_sampled', 'se_ct_scanned', 'se_xray_scanned', 'se_clavicle_triage', 'se_inventoried', 'se_reviewed')
#     list_filter = ('se_key', 'se_accession_number','se_side', 'se_completeness')
#     search_fields = ('se_side','se_bone_id')
#
#
# admin.site.register(SkeletalBones, SkeletalBonesList)
# admin.site.register(SkeletalElement, SkeletalElementList)


from import_export.admin import ImportExportModelAdmin
from django.contrib import admin
from .models import SkeletalBones,SkeletalElement,Measurements,Pathology,Taphonomy,Trauma,Zones,SeAnomaly,SeArticulation,SeMeasurement,Nodes, Links, Sb_art, Art


@admin.register(SkeletalBones)
class Sb_admin(ImportExportModelAdmin):
    pass


@admin.register(SkeletalElement)
class SeAdmin(ImportExportModelAdmin):
    pass


@admin.register(Measurements)
class MeasurementAdmin(ImportExportModelAdmin):
    pass


@admin.register(Pathology)
class PathologyAdmin(ImportExportModelAdmin):
    pass


@admin.register(Taphonomy)
class TaphonomyAdmin(ImportExportModelAdmin):
    pass


@admin.register(Trauma)
class TraumaAdmin(ImportExportModelAdmin):
    pass


@admin.register(Zones)
class ZonesAdmin(ImportExportModelAdmin):
    pass


@admin.register(SeAnomaly)
class SeAnomalyAdmin(ImportExportModelAdmin):
    pass


@admin.register(SeArticulation)
class SeArticulationAdmin(ImportExportModelAdmin):
    pass


@admin.register(SeMeasurement)
class SeMeasurementAdmin(ImportExportModelAdmin):
    pass


@admin.register(Nodes)
class NodesAdmin(ImportExportModelAdmin):
    pass


@admin.register(Links)
class LinksAdmin(ImportExportModelAdmin):
    pass


@admin.register(Sb_art)
class SbArtAdmin(ImportExportModelAdmin):
    pass


@admin.register(Art)
class ArtAdmin(ImportExportModelAdmin):
    pass