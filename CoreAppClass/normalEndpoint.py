from .paginate import pagintes
from rest_framework.pagination import LimitOffsetPagination

#TODO Incesao de dependencias

class endpoints(LimitOffsetPagination):
    def __init__(self):
        pass

    def NormalEndPoint(self,model,request,serializer,key = None,**kwargs):
        serialiedData = pagintes.paginatefunc(self,model,request,serializer,key)

        #TODO Ver como mandar a func com parametors para os kwargs   
        responseData ={
            'Pagination':{
                'next':self.get_next_link(),
                'previous':self.get_previous_link(),
            },
            'Data': serialiedData.data,
            'ExtraData': kwargs,
        }
        print(responseData)
        return responseData

   