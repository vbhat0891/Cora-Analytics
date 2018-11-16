from django.db import models
from django.utils import timezone
# Create your models here.


class SkeletalBones(models.Model):
    id = models.IntegerField(default=0,primary_key=True)
    name = models.CharField(max_length=50)
    category = models.CharField(max_length=30)
    bone_type = (
        ('FLAT', 'flat'),
        ('IRREGULAR', 'irregular'),
        ('LONG', 'long bone'),
        ('SHORT', 'short bone'),
        ('TOOTH', 'tooth'),
        ('N/A', 'not available'),
    )
    type = models.CharField(max_length=12,default='', choices=bone_type)
    bone_group = (
        ('AP', 'Appendicular'),
        ('AX', 'Axial'),
        ('N/A', 'Not available'),
        ('Toot', 'Tooth'),
    )
    group = models.CharField(max_length=30, default='',choices=bone_group)
    description = models.CharField(max_length=30)
    sb_paired = (
        ('TRUE', True),
        ('FALSE', False),
    )
    paired = models.CharField(max_length=6,choices=sb_paired)
    sb_articulated = (
        ('TRUE', True),
        ('FALSE', False),
    )
    articulated = models.BooleanField(max_length=6,choices=sb_articulated)
    sbb_zones = (
        ('TRUE', True),
        ('FALSE', False),
    )
    sb_zones = models.BooleanField(max_length=6,choices=sbb_zones,default=False)
    sbb_measure = (
        ('TRUE', True),
        ('FALSE', False),
    )
    sb_measurements = models.BooleanField(max_length=6,choices=sbb_measure,default=False)
    sbb_dental = (
        ('TRUE', True),
        ('FALSE', False),
    )
    dental = models.BooleanField(max_length=6,choices=sbb_dental,default=False)
    created_date = models.DateTimeField(default=timezone.now)



# class SkeletalBonesDelete(resources.ModelResource):
#     delete = fields.Field(widget=widgets.BooleanWidget())
#
#     def for_delete(self, row, instance):
#         return self.fields['delete'].clean(row)
#
#     class Meta:
#         model = SkeletalBones



class SkeletalElement(models.Model):
    id = models.IntegerField(default=0, primary_key=True)
    sb_id = models.ForeignKey(SkeletalBones, on_delete=models.CASCADE)
    key = models.CharField(max_length=150)
    accession_number = models.CharField(max_length=100)
    g_number =  models.CharField(max_length=100)
    x_number = models.CharField(max_length=50)
    designator = models.IntegerField(default=0)
    side = (
        ('LEFT', 'Left'),
        ('RIGHT', 'Right'),
        ('MIDDLE', 'Middle'),
        ('UNSIDED', 'Unsided'),
    )
    se_side = models.CharField(max_length=10, default='',choices=side)
    complete = (
        ('COMPLETE', 'Complete'),
        ('MC', 'Mostly complete'),
        ('PARTIAL', 'Partial'),
    )
    completeness = models.CharField(max_length=20, default='',choices=complete)
    se_measured = (
        ('TRUE', True),
        ('FALSE', False),
    )
    measured = models.CharField(max_length=10, choices=se_measured)
    se_dna = (
        ('TRUE', True),
        ('FALSE', False),
    )
    dna_sampled = models.CharField(max_length=10, choices=se_dna)
    se_ct = (
        ('TRUE', True),
        ('FALSE', False),
    )
    ct_scanned = models.CharField(max_length=10, choices=se_ct)
    se_xray = (
        ('TRUE', True),
        ('FALSE', False),
    )
    xray_scanned = models.CharField(max_length=10, choices=se_xray)
    se_triage = (
        ('TRUE', True),
        ('FALSE', False),
    )
    clavicle_triage = models.CharField(max_length=10, choices=se_triage)
    se_inven= (
        ('TRUE', True),
        ('FALSE', False),
    )
    inventoried = models.CharField(max_length=10, choices=se_inven)
    se_review = (
        ('TRUE', True),
        ('FALSE', False),
    )
    reviewed = models.CharField(max_length=10, choices=se_review)

    def __int__(self):
        return self.id


class Anomalys(models.Model):
    anomaly_id = models.IntegerField(default=0)
    anomaly_bone_id = models.ForeignKey(SkeletalBones, on_delete=models.CASCADE)
    individuating_trait = models.CharField(max_length=50)
    created_date = models.DateTimeField(default=timezone.now)


class Measurements(models.Model):
    measurement_id = models.IntegerField(default=0)
    measurement_bone_id = models.ForeignKey(SkeletalBones, on_delete=models.CASCADE)
    measurement_name = models.CharField(max_length=100)
    measurement_display_name = models.CharField(max_length=300)
    measurement_desc = models.CharField(max_length=600)
    measurement_stature = models.BooleanField(default=False)
    measurement_sex = models.BooleanField(default=False)
    created_date = models.DateTimeField(default=timezone.now)


class Pathology(models.Model):
    pathology_id = models.IntegerField(default=0)
    abnormality_category = models.CharField(max_length=30)
    pathology_characteristics = models.CharField(max_length=30)
    created_date = models.DateTimeField(default=timezone.now)


class Taphonomy(models.Model):
    taphonomy_id = models.IntegerField(default=0)
    taphonomy_branch = models.CharField(max_length=20)
    taphonomy_name = models.CharField(max_length=100)
    taphonomy_category = models.CharField(max_length=100)
    taphonomy_type = models.CharField(max_length=50)
    taphonomy_subtype = models.CharField(max_length=50)


class Trauma(models.Model):
    trauma_id = models.IntegerField(default=0)
    timing = (
        ('ANTE','Antemortem'),
        ('PERI', 'Perimortem'),
    )
    trauma_timing = models.CharField(max_length=40,default='',choices=timing)
    trauma_type = models.CharField(max_length=50, default='')


class Zones(models.Model):
    zone_id = models.IntegerField(default=0)
    zone_sb_id = models.ForeignKey(SkeletalBones, on_delete=models.CASCADE)
    zone_name = models.IntegerField(default='')
    zone_description = models.CharField(max_length=120)


class SeAnomaly(models.Model):
    anomaly_se_id = models.ForeignKey(SkeletalElement, on_delete=models.CASCADE)
    anomaly_id = models.IntegerField()


class SeArticulation(models.Model):
    articulation_se_id = models.ForeignKey(SkeletalElement, on_delete=models.CASCADE)
    articulation_id = models.IntegerField(default='')


class SeMeasurement(models.Model):
    measure_se_id = models.ForeignKey(SkeletalElement, on_delete=models.CASCADE)
    measurement_id = models.IntegerField()
    measure = models.FloatField(max_length=10)


class Nodes(models.Model):
    # id = models.IntegerField(primary_key=True, null=False, default=0)
    id = models.IntegerField(primary_key=True)
    sb_id = models.IntegerField()
    side = (
        ('LEFT', 'Left'),
        ('RIGHT', 'Right'),
        ('MIDDLE', 'Middle'),
        ('UNSIDED', 'Unsided'),
    )
    se_side = models.CharField(max_length=20, default='', choices=side)
    complete = (
        ('COMPLETE', 'Complete'),
        ('MC', 'Mostly complete'),
        ('PARTIAL', 'Partial'),
    )
    completeness = models.CharField(max_length=20, default='', choices=complete)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    bone_type = (
        ('FLAT', 'flat'),
        ('IRREGULAR', 'irregular'),
        ('LONG', 'long bone'),
        ('SHORT', 'short bone'),
        ('TOOTH', 'tooth'),
        ('N/A', 'not available'),
    )
    type = models.CharField(max_length=20, default='', choices=bone_type)
    bone_group = (
        ('AP', 'Appendicular'),
        ('AX', 'Axial'),
        ('N/A', 'Not available'),
        ('Toot', 'Tooth'),
    )
    group = models.CharField(max_length=30, default='', choices=bone_group)
    description = models.CharField(max_length=30)
    sb_paired = (
        ('TRUE', True),
        ('FALSE', False),
    )
    paired = models.CharField(max_length=10, choices=sb_paired)
    sb_articulated = (
        ('TRUE', True),
        ('FALSE', False),
    )
    articulated = models.CharField(max_length=10, choices=sb_articulated)


class Links(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    source = models.IntegerField()
    target = models.IntegerField()
    value = models.IntegerField()


class Sb_art(models.Model):
    # id = models.IntegerField(primary_key=True, default=0)
    id = models.IntegerField(primary_key=True,default=0)
    group_name = models.CharField(max_length=40)
    name = models.CharField(max_length=50, default='')
    category = models.CharField(max_length=40, default='')


class Art(models.Model):
    id = models.IntegerField(primary_key=True, default=0)
    source = models.IntegerField()
    target = models.IntegerField()
    value = models.IntegerField()

