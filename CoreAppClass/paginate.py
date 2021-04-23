from rest_framework.pagination import LimitOffsetPagination

class pagintes(LimitOffsetPagination):
    def __init__(self):
        pass
    
    def paginatefunc(self,model,request,serializer,key = None):
        print(key)
    
        #TODO: add more abstract to the filters
        if key is not None:
            rawQuerySet = model.objects.filter(**key)
        else:
            rawQuerySet = model.objects.all()

        rawQuerySetPaginate = self.paginate_queryset(rawQuerySet,request)
        serialiedData = serializer(rawQuerySetPaginate, many=True)
        return serialiedData
