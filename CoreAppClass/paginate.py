from rest_framework.pagination import LimitOffsetPagination

class pagintes(LimitOffsetPagination):
    def __init__(self):
        pass



    def paginatefunc(self,model,request,serializer,key):
    
        #TODO: add more abstract to the filters
        filter_kwargs = { key : request.user.steamID,'mission':request.data["mission"]}

        rawQuerySet = model.objects.all().filter(**filter_kwargs)

        rawQuerySetPaginate = self.paginate_queryset(rawQuerySet,request)
        serialiedData = serializer(rawQuerySetPaginate, many=True)
        return serialiedData
