from rest_framework.pagination import LimitOffsetPagination

class pagintes(LimitOffsetPagination):
    def __init__(self):
        pass
    
    def paginatefunc(self,model,request,serializer,key = None):
    
        #TODO: add more abstract to the filters
        filter_kwargs={}
        if key is not None:
            filter_kwargs = {key : request.user.steamID}

        rawQuerySet = model.objects.all()

        rawQuerySetPaginate = self.paginate_queryset(rawQuerySet,request)
        serialiedData = serializer(rawQuerySetPaginate, many=True)
        return serialiedData
