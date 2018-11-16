from .models import *
from rest_framework import serializers


class BoneSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkeletalBones
        fields = ('id', 'name', 'category', 'type', 'group', 'description', 'paired', 'articulated', 'sb_zones', 'sb_measurements', 'dental')


class SkeletalElementSerializer(serializers.ModelSerializer):

    class Meta:
        model = SkeletalElement
        fields = ('id', 'sb_id_id', 'key', 'accession_number', 'g_number', 'x_number', 'designator', 'side', 'completeness', 'measured', 'dna_sampled', 'ct_scanned', 'xray_scanned', 'clavicle_triage', 'inventoried', 'reviewed')


class SkeletalNodeSerializer(serializers.ModelSerializer):

    class Meta:
        model = Nodes
        fields = ('id', 'sb_id', 'completeness', 'name', 'category', 'type', 'group', 'description', 'paired', 'articulated')
        # se_id = serializers.SkeletalNode(source='id')


class SkeletalLinkSerializer(serializers.ModelSerializer):

    class Meta:
        model = Links
        fields = ("source", "target", "value")


class SbArtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Sb_art
        fields = ("id", "group_name", "name", "category")


class ArtSerializer(serializers.ModelSerializer):

    class Meta:
        model = Art
        fields = ("source", "target", "value")
