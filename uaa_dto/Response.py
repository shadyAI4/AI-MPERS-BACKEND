import json
import graphene
from graphene_federation import key, external, extend


@key(fields='id')
class ResponseObject(graphene.ObjectType):
    id = graphene.String()
    status = graphene.Boolean()
    code = graphene.Int()
    message = graphene.String()

    def __resolve_reference(self, info, **kwargs):
        try:
            if self.id == None:
                return ResponseObject()

            response_code = ResponseObject.__read_code_file(str(self.id))
            
            return ResponseObject(
                response_code['id'],
                response_code['status'],
                response_code['code'],
                response_code['message'],
            )
        except:
            return ResponseObject()

    def __read_code_file(code_id):
        file = open('ai_mpers_response_codes.json', 'r')
        file_codes = file.read()
        response_codes = json.loads(file_codes)
        response_code = next(code for code in response_codes if code["id"] == code_id)
        return response_code

    def get_response(id):
        try:

            response_code = ResponseObject.__read_code_file(id)
            return ResponseObject(
                response_code['id'],
                response_code['status'],
                response_code['code'],
                response_code['message'],
            )
        except:
            return ResponseObject()
        


