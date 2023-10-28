from chalice import Response

class HttpCustomErrors():

    #Tratamento customizado para quando o não é localizada a task
    def not_found_error(self, message):
        return Response(body={"message": message}, 
                        status_code= 404,
                        headers={'Content-Type': 'application/json'})
    
    #Tratamento customizado para quando o corpo de envio em Json contém informações incorretas
    def json_error(self, message):
        return Response(body={"message": message}, 
                        status_code= 400,
                        headers={'Content-Type': 'application/json'})
    
    #Tratamento customizado para quando a ação solicitada é bem sucedida 
    def action_successfully(self, message):
        return Response(body= message, 
                        status_code= 200,
                        headers={'Content-Type': 'application/json'})
    
    #Tratamento customizado para retorno de erro vindo do servidor
    def server_error(self, e):
        return Response(body={"error": str(e)}, 
                        status_code= 500,
                        headers={'Content-Type': 'application/json'})
