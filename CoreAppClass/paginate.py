from rest_framework.pagination import LimitOffsetPagination

class pagintes(LimitOffsetPagination):
    def __init__(self):
        pass
    
    def paginatefunc(self,model,request,serializer,filterType = "all",filter = None,fieldName= None):
        possibleFilters={"count",model.objects.order_by(key).count(),"filter":model.objects.filter(**key),"all":model.objects.all()}
        #TODO: add more abstract to the filters
        
        rawQuerySet = self.possibleFilters[filterType]

        rawQuerySetPaginate = self.paginate_queryset(rawQuerySet,request)
        serialiedData = serializer(rawQuerySetPaginate, many=True)
        return serialiedData
