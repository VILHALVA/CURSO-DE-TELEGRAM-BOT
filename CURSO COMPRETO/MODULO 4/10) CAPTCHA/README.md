# CAPTCHA
## DESCRIÇÃO
Este bot é um moderador para grupos do Telegram que implementa um sistema de verificação com Captcha para novos membros. O objetivo principal é garantir que apenas humanos reais sejam capazes de ingressar e interagir no grupo, enquanto bots ou spammers são filtrados.

## RECURSOS
1. **Verificação de Captcha:** Quando um novo membro ingressa no grupo, o bot inicia o processo de verificação apresentando ao usuário um Captcha simples, que consiste em um número de quatro dígitos.

2. **Tempo Limite:** O novo membro tem até 3 minutos para inserir o Captcha corretamente e ser verificado como um usuário legítimo.

3. **Remoção Automática:** Se o novo membro não conseguir inserir o Captcha correto dentro do tempo limite de 3 minutos, o bot remove automaticamente o membro do grupo.

4. **Verificação Bem-Sucedida:** Se o novo membro inserir corretamente o Captcha, ele será considerado verificado e terá permissão para interagir livremente no grupo.

5. **Job Periódico:** O bot executa um trabalho periódico para verificar membros não verificados e removê-los após o tempo limite.

## OBSERVAÇÕES:
- Certifique-se de configurar o bot com seu próprio token e personalizar a mensagem e a lógica de verificação conforme suas necessidades específicas.
- Este bot é um exemplo simplificado de um sistema de verificação com Captcha e pode ser expandido e aprimorado de acordo com suas necessidades.

Lembre-se de que a implementação de um sistema de verificação com Captcha é uma medida de segurança para grupos e deve ser usada com responsabilidade, garantindo que os membros legítimos não sejam impedidos de ingressar no grupo.