# ASSINATURA VIA PIX
## DESCRIÇÃO:
- Este bot oferece um serviço de assinatura mensal para permitir que os usuários acessem recursos adicionais do bot.
- Quando um usuário inicia o bot ou sua assinatura expira, o bot envia um botão inline oferecendo a opção de pagar a assinatura mensal via PIX para desbloquear recursos premium.
- Após o usuário clicar no botão "Pagar Assinatura Mensal", o bot processa o pagamento e, se bem-sucedido, registra a assinatura do usuário no sistema, permitindo o acesso aos recursos premium por 30 dias.
- O bot também verifica se o usuário já está assinado e permite o uso normalmente se já estiver.

## CARACTERISTICAS:
- Assinatura Mensal: O bot oferece uma opção de assinatura mensal, fornecendo aos usuários acesso contínuo aos recursos premium por 30 dias após o pagamento.
- Pagamento via PIX: O bot integra um sistema de pagamento PIX para processar transações financeiras de forma rápida e segura.
- Registro de Assinatura: O bot mantém um banco de dados MySQL para registrar as assinaturas dos usuários e controlar a validade das assinaturas.
