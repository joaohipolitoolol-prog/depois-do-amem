# 7 Dias Depois do Amém

Landing page estática em português.

## Publicação

Importe este repositório no Vercel com Framework Preset **Other**, diretório raiz `./`, sem comando de build. A página inicial é `index.html`.

## Checkout

Defina a URL HTTPS da oferta em `config.js`, na propriedade `checkoutUrl`. Enquanto ela estiver nula, o botão informa que as vendas ainda não abriram.

Configure também `upsellCheckoutUrl` para a continuação e `whatsappNumber` para suporte opcional. O telefone deve conter código do país e número, apenas dígitos. Sem telefone configurado, o botão de WhatsApp fica oculto.

## Páginas e entrega

- `/`: página de vendas, R$27.
- `/obrigado`: guia, diário e áudio do produto principal.
- `/obrigadocomoracoes`: principal mais o adicional de R$17.
- `/obrigadooracoes`: entrega apenas da coleção de orações.
- `/continuar`: convite opcional para a continuação de R$97.
- `/obrigadocontinuacao`: entrega da continuação.

Os arquivos completos estão em `materiais/`. As páginas de entrega e arquivos têm instruções para não indexar. Este fluxo é de acesso por link: não autentica compradores nem confirma pagamentos, e qualquer pessoa com o endereço pode acessar os arquivos. Não tratar o `noindex` como proteção de acesso.

Na plataforma de pagamento, disponibilize o endereço correspondente somente após pagamento aprovado. Se a plataforma não permitir distinguir principal e principal com bump no redirecionamento, entregue o adicional pela área de membros ou mensagem transacional da própria plataforma. Não encaminhe todos os compradores ao pacote com orações.

Para restringir efetivamente o acesso, será necessária uma área de membros ou integração de servidor que valide o pagamento e gere acessos individuais. Isso não está implementado nesta versão estática.

## Antes de anunciar

Cadastre os produtos e o adicional na plataforma escolhida, conecte os links reais de checkout, configure os endereços de entrega e os dados reais de suporte/vendedor. Faça uma compra de teste com cada combinação. Vendas continuam indisponíveis enquanto os links de checkout forem nulos.

O áudio tem aproximadamente 6 minutos e 59 segundos, com voz sintetizada e pausas de reflexão. PDFs e áudio são hospedados neste próprio projeto; a entrega não depende de login em um gerador de voz.

## Arquivos

`assets/amostra-depois-do-amem.pdf` contém apenas capa e primeiro encontro. Imagens WebP, favicon SVG/ICO e metadados estão incluídos. O projeto pode ser editado diretamente e publicado sem instalar dependências. `builddelivery.py` registra a montagem dos materiais a partir dos arquivos originais do projeto; não é necessário executá-lo para publicar o site pronto.

## Estado desta entrega

Esta pasta contém a versão completa pronta para publicação, incluindo os arquivos pagos. A versão pública aprovada nesta etapa contém apenas a landing page e prévias das páginas de entrega, com downloads desativados. A publicação dos arquivos completos aguarda autorização explícita para disponibilizá-los publicamente no domínio depoisdoamem.vercel.app. O checkout ainda não está configurado.
