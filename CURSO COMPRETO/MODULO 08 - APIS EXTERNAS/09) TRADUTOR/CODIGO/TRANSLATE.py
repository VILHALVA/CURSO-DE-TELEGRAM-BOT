from google.cloud import translate_v2 as translate

translate_client = translate.Client.from_service_account_json('caminho/para/seu/arquivo-de-credenciais.json')