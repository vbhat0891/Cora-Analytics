from django.http import HttpResponse
from .models import *
from django.shortcuts import render
from django.core.serializers import serialize
from django.db.models import *
from .serializers import BoneSerializer,SkeletalElementSerializer,SkeletalLinkSerializer, SkeletalNodeSerializer, SbArtSerializer, ArtSerializer
from django.dispatch import receiver
from import_export.signals import post_import, post_export
from tablib import Dataset
from django.views import generic
from django.http import JsonResponse
from django.db.models import Count
from django.db.models import Q

def index(request):
    return render(request, 'coraapp/index.html',
                         {'coraapp': index})


def about(request):
    return render(request, 'coraapp/about.html',
                  {'coraapp': about})

def datasource(request):
    return render(request, 'coraapp/datasource.html',
                  {'coraapp': datasource})

def analysis(request):
    return render(request, 'coraapp/analysis.html',
                  {'coraapp': analysis})

def dataStudio_viz(request):
    return render(request, 'coraapp/dataStudio_viz.html',
                  {'coraapp': dataStudio_viz})


def sbData(request):
        s_name = SkeletalBones.objects.all()
        s_boneType = SkeletalBones.objects.all()
        s_boneGroup = SkeletalBones.objects.all()
        serializer = BoneSerializer(s_name, many=True)
        return JsonResponse(serializer.data, safe=False)
        # return JsonResponse([{'s_name':"Name",'skeletal_name':s_name,
        #                      's_type':"Bone Type", 's_boneType':s_boneType,
        #                      's_group':"Bone Group", 's_boneGroup':s_boneGroup}],safe=False)

def seData(request):
    se_name = SkeletalElement.objects.all()
    serializer = SkeletalElementSerializer(se_name, many=True)
    return JsonResponse(serializer.data, safe=False)


# def forceNode(request):
#     skeletal_nodes = Nodes.objects.all()
#     serializer = SkeletalNode(skeletal_nodes, many=True)
#     new_node = {"node":serializer.data}
#     return JsonResponse(new_node, safe=False)


def forceLink(request):
    # node_link = {}
    skeletal_links = Links.objects.all()
    serialiser = SkeletalLinkSerializer(skeletal_links,many=True)
    new_link = {"links": serialiser.data}
    skeletal_nodes = Nodes.objects.all()
    serializer = SkeletalNodeSerializer(skeletal_nodes, many=True)
    new_node = {"nodes": serializer.data}
    node_link = {"nodes":serializer.data,"links":serialiser.data}
    return JsonResponse(node_link ,safe=False)


def vizData(request):
    sb_count = SkeletalElement.objects.filter(completeness__exact='Complete').count()
    sb_partial = SkeletalElement.objects.filter(completeness__exact='Partial').count()
    sb_mostly = SkeletalElement.objects.filter(completeness__exact='Mostly complete').count()
    sb_measured = SkeletalElement.objects.filter(measured='TRUE').count()
    return JsonResponse([{'sb_count':"Complete",'count':sb_count},
                         {'sb_partial': "Partial",'p_count':sb_partial},
                         {'sb_mostly':"Mostly", 'mostly_count': sb_mostly}],safe=False)

def visualization(request):
    elements = SkeletalElement.objects.distinct()
    # print(elements)
    sb_count = SkeletalElement.objects.filter(completeness__exact='Complete').count()
    sb_partial = SkeletalElement.objects.filter(completeness__exact='Partial').count()
    sb_mostly = SkeletalElement.objects.filter(completeness__exact='Mostly complete').count()
    # sb_value = SkeletalElement.objects.values('completeness', 'name', 'category')
    # print(sb_value)
    sb_measured = SkeletalElement.objects.filter(measured='TRUE').count()
    # print(sb_count)
    bona = SkeletalBones.objects.all()
    # bon_type = SkeletalBones.objects.filter(type__startswith="Flat")
    # bon_type_count = SkeletalBones.objects.annotate(cnt_bone=Count('type', filter=Q(type__exact='Flat')))
    # bon_type_count = SkeletalBones.objects.annotate(Count('type', distinct=True))

    bon_grp= SkeletalBones.objects.raw('Select * from coraapp_skeletalbones where "group" = "Axial"')
    # print(bon_type_count[1])
    # print(cnt_bone)
    # bon_type = SkeletalBones.objects.raw('SELECT COUNT(type) FROM coraapp_skeletalbones')
    # print(bon_type)
    # bon_group = SkeletalBones.objects.raw('SELECT DISTINCT id,group FROM coraapp_skeletalbones')
    # for bons in SkeletalBones.objects.raw('select DISTINCT bone_type from SkeletalBones'):
    #     print(bons)
    bons = bona.filter(created_date__lte=timezone.now())
    # print(bon_type)
    # print(bons)
    return render(request, 'coraapp/visualization.html',
                   {'bons': bona, 'elements': elements, 'sb_count':sb_count,
                    'sb_partial': sb_partial, 'sb_mostly':sb_mostly,
                    'sb_measured': sb_measured}
                )

# class VisualList(generic.ListView):
#     model = SkeletalBones
#     # context_object_name = 'skeletal_bone_list'
#     # queryset = SkeletalBones.filter(type__icontains="flat")
#     # template_name = 'coraapp/visualization.html'


@receiver(post_import, dispatch_uid='cora_import')
def _post_import(model, **kwargs):
    # model is the actual model instance which after import
    pass


@receiver(post_export, dispatch_uid='cora_export')
def _post_export(model, **kwargs):
    # model is the actual model instance which after export
    pass


def simple_upload(request):
    if request.method == 'POST':
        sb_resource = SbResource()
        dataset = Dataset()
        new_persons = request.FILES['myfile']

        imported_data = dataset.load(new_persons.read().decode('utf-8'),format='csv')
        result = sb_resource.import_data(dataset, dry_run=True)  # Test the data import

        if not result.has_errors():
            sb_resource.import_data(dataset, dry_run=False)  # Actually import now

    return render(request, 'coraapp/simple_upload.html')


def sbArt(request):
    sl_links = Art.objects.all()
    serialiser = ArtSerializer(sl_links, many=True)
    # new_link = {"links": serialiser.data}
    sl_nodes = Sb_art.objects.all()
    serializer = SbArtSerializer(sl_nodes, many=True)
    # new_node = {"nodes": serializer.data}
    node_link = {"nodes": serializer.data, "links": serialiser.data}
    return JsonResponse(node_link, safe=False)