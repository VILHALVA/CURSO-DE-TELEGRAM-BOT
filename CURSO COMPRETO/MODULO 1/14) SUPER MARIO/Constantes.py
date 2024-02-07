from Enderecos import *
TOKEN_ID= 'EAAN5cPHx5hoBAANnJdLkvqSX6lEOZCEqHPDBW9gM6yKcNKdd0Suj18XPUq1ZCfeHwbGrLpIvIrjfBN6X6IgpiFJ7cv6fbvoJ3PjaeZCWYr2kCTlzGWdZCdWTzVzWOCVtOldZAn1bPSHxmL5XeMR0YuVsf9HE5gXYseHckAOwOuRTbpOZC0ecFGfpZBKHBM8VM0lkv0hPBofewZDZD'
#pegar o token de acordo com o link deste site: https://medium.com/vertice/como-criar-um-page-access-token-de-facebook-que-n%C3%A3o-expira-ff8026020963
VIDEO_ID = ''   #video da live do facebook
URL = "https://streaming-graph.facebook.com/" + VIDEO_ID + "/live_comments" #pega a url da live e os comentarios
PARAMETROS = {'access_token': TOKEN_ID, 'comment_rate':'ten_per_second'} #passa os parametros em um dicionario

dicionarioComandos = dict([
    ('pena',MARIO_PENINHA),
    ('pequeno',MARIO_PEQUENO),
    ('cogumelo',MARIO_GRANDE),
    ('flor',MARIO_FLOR_DE_FOGO),
    ('peninha',MARIO_PENINHA),
    ('fogo',MARIO_FLOR_DE_FOGO)
])
listaComandos = [
    ('pena'),
    ('pequeno'),
    ('cogumelo'),
    ('flor'),
    ('peninha'),
    ('fogo')
]