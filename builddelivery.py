from pathlib import Path
from PIL import Image,ImageDraw,ImageFont
from pypdf import PdfReader,PdfWriter
import shutil,json

ROOT=Path(__file__).parent
SOURCE=Path('/workspace/scratch/b234ec73924a')
PDF=SOURCE/'output/pdf'
ASSETS=ROOT/'assets'
FILES=ROOT/'materiais';FILES.mkdir(exist_ok=True)
products={
 'principal':'exec-fe677cd7-2b2c-4bb5-845c-3985e04d55b6.png',
 'oracoes':'exec-5827bbcf-d495-4d92-a65b-e7e1dce450b5.png',
 'continuacao':'exec-b4db287a-c047-4c9f-8d37-59d4c5614497.png'
}
for key,file in products.items():
 im=Image.open(SOURCE/'generated_images'/file).convert('RGB');im.thumbnail((960,960));im.save(ASSETS/f'{key}.webp','WEBP',quality=86)

# Optimize embedded cover image without changing the guide content.
writer=PdfWriter();writer.clone_document_from_reader(PdfReader(PDF/'7_Dias_Depois_do_Amem_Guia.pdf'))
for page in writer.pages:
 for img in page.images:img.replace(img.image,quality=82)
writer.write(FILES/'guia.pdf')
for src,dst in [('Diario_Depois_do_Amem.pdf','diario.pdf'),('21_Oracoes_Para_Dias_Dificeis.pdf','oracoes.pdf'),('Depois_do_Amem_na_Vida_Real.pdf','continuacao.pdf'),('Audio_Depois_do_Amem.mp3','audio.mp3'),('Narracao_Depois_do_Amem.txt','transcricao.txt')]:
 shutil.copy2(PDF/src,FILES/dst)

favicon='<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 64 64"><rect width="64" height="64" rx="16" fill="#203e35"/><text x="32" y="48" text-anchor="middle" font-family="Georgia,serif" font-size="48" fill="#faf7f0">A</text></svg>'
(ROOT/'favicon.svg').write_text(favicon)
icon=Image.new('RGB',(180,180),'#203e35');draw=ImageDraw.Draw(icon)
font=ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSerif.ttf',137)
draw.text((90,78),'A',font=font,anchor='mm',fill='#faf7f0');icon.save(ROOT/'appleicon.png');icon.save(ROOT/'favicon.ico',sizes=[(16,16),(32,32),(48,48)])

def head(title,description):
 return f'''<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="theme-color" content="#203e35"><meta name="robots" content="noindex,nofollow"><meta name="description" content="{description}"><title>{title} | Depois do Amém</title><link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="apple-touch-icon" href="/appleicon.png"><link rel="stylesheet" href="/styles.css"><link rel="stylesheet" href="/entrega.css"><script src="/config.js" defer></script><script src="/entrega.js" defer></script></head><body><a class="skip" href="#conteudo">Pular para o conteúdo</a><header class="delivery-nav"><a class="delivery-brand" href="/">Depois do Amém<span>UMA ORAÇÃO. UM PRÓXIMO PASSO.</span></a></header>'''
def foot():
 return '''<footer class="delivery-footer"><p>Depois do Amém · Material devocional digital</p><p>Uma prática para acompanhar sua oração, no seu ritmo.</p></footer></body></html>'''
def card(number,title,desc,href,button,format):
 return f'''<article class="download-card"><span class="download-number">{number}</span><h2>{title}</h2><p>{desc}</p><a class="button" href="{href}" download>{button} <span aria-hidden="true">↓</span></a><a class="open-file" href="{href}" target="_blank" rel="noopener">Abrir em uma nova aba ↗</a><small>{format}</small></article>'''
def support(product):
 return f'''<section class="support-panel" data-support hidden><h2>Precisa de ajuda com o acesso?</h2><p>Abra o WhatsApp com uma mensagem pronta e conte o que aconteceu.</p><a class="button" data-whatsapp data-product="{product}" href="#">Falar sobre meu material ↗</a></section>'''
def thanks(kind,main=False,bump=False):
 names={'principal':'7 Dias Depois do Amém','oracoes':'21 Orações Para Dias Difíceis','continuacao':'Depois do Amém na Vida Real'}
 name=names[kind]
 html=head('Seu material está aqui',f'Acesse o material digital {name}.')
 html+=f'''<main id="conteudo" class="delivery-shell"><section class="delivery-hero"><div><p class="eyebrow">BEM-VINDA AO SEU MOMENTO DE PRÁTICA</p><h1>Obrigada por escolher<br><em>caminhar com a gente.</em></h1><p class="delivery-lead">Seu material está aqui. Abra no celular ou baixe os arquivos para guardar e acessar quando quiser.</p><p class="delivery-product">{name}</p><a class="text-link" href="#materiais">Ir para meus materiais ↓</a></div><img src="/assets/{kind}.webp" alt="Apresentação ilustrativa do produto digital {name}" width="960" height="960" fetchpriority="high"></section><section id="materiais" class="download-section"><p class="eyebrow">SEU ACESSO</p><h2>Comece com <em>um pequeno passo.</em></h2><div class="download-grid">'''
 if main:
  html+=card('01','Guia de 7 dias','12 páginas com os sete encontros. Comece pelas boas-vindas e siga para o primeiro dia.','/materiais/guia.pdf','Baixar meu guia','PDF · 12 páginas')
  html+=card('02','Diário Depois do Amém','Quatro perguntas em uma folha. Imprima novamente sempre que quiser ou use um caderno.','/materiais/diario.pdf','Baixar meu diário','PDF · 1 folha reutilizável')
  html+='''<article class="download-card audio-card"><span class="download-number">03</span><h2>Seu momento de oração</h2><p>Uma faixa guiada de cerca de 7 minutos, com pausas para responder no seu ritmo. Você pode repetir quando quiser.</p><audio controls preload="none" aria-label="Áudio guiado Depois do Amém"><source src="/materiais/audio.mp3" type="audio/mpeg">Seu navegador não reproduz áudio. Use o botão de download abaixo.</audio><a class="button" href="/materiais/audio.mp3" download="AudioDepoisDoAmem.mp3">Baixar meu áudio <span aria-hidden="true">↓</span></a><a class="open-file" href="/materiais/transcricao.txt" target="_blank" rel="noopener">Ler a transcrição ↗</a><small>MP3 · Voz sintetizada · Sem música de fundo</small></article>'''
 if bump or kind=='oracoes':
  html+=card('04' if main else '01','21 Orações Para Dias Difíceis','Escolha o tema pelo índice. Cada oração acompanha uma pergunta e um pequeno gesto possível.','/materiais/oracoes.pdf','Baixar minhas orações','PDF · 24 páginas · 21 orações')
 if kind=='continuacao':
  html+=card('01','Depois do Amém na Vida Real','21 encontros para praticar nas relações e na rotina. Inclui três revisões e plano de continuidade.','/materiais/continuacao.pdf','Baixar minha continuação','PDF · 28 páginas · Jornada autoguiada')
 html+='</div></section>'
 html+='''<section class="first-steps"><div><p class="eyebrow">PARA GUARDAR COM VOCÊ</p><h2>Como usar<br><em>seu material.</em></h2></div><ol><li><strong>Baixe e guarde.</strong><p>Os arquivos normalmente ficam na pasta Downloads do celular ou computador. Você também pode salvar esta página nos favoritos.</p></li><li><strong>Comece no seu ritmo.</strong><p>Leia as orientações iniciais. Escolha um momento possível e adapte as palavras à sua maneira de orar.</p></li><li><strong>Retome quando precisar.</strong><p>Não é preciso compensar dias nem fazer tudo de uma vez. Um encontro pode ser suficiente para hoje.</p></li></ol></section>'''
 if main:
  html+='''<aside class="continuation-invite"><img src="/assets/continuacao.webp" alt="Produto digital Depois do Amém na Vida Real" width="960" height="960" loading="lazy"><div><p class="eyebrow">UM CONVITE OPCIONAL PARA DEPOIS</p><h2>Quer continuar<br><em>além dos sete dias?</em></h2><p>Sua jornada já é completa. Se quiser ampliar a prática, conheça mais 21 encontros para as conversas, decisões e cuidados do dia a dia.</p><a class="text-link" href="/continuar">Conhecer a continuação ↗</a></div></aside>'''
 html+=support(name)+'</main>'+foot()
 return html
(ROOT/'obrigado.html').write_text(thanks('principal',main=True))
(ROOT/'obrigadocomoracoes.html').write_text(thanks('principal',main=True,bump=True))
(ROOT/'obrigadooracoes.html').write_text(thanks('oracoes'))
(ROOT/'obrigadocontinuacao.html').write_text(thanks('continuacao'))

upsell=head('Continue a prática','Conheça mais 21 encontros para aplicar os quatro passos em conversas, decisões e rotina.')+'''<main id="conteudo" class="delivery-shell"><a class="back-to-material" href="/obrigado">← Acessar meus 7 dias</a><section class="delivery-hero"><div><p class="eyebrow">UMA CONTINUAÇÃO OPCIONAL</p><h1>A prática pode seguir<br><em>para a vida real.</em></h1><p class="delivery-lead">Mais 21 encontros para levar os quatro passos às conversas, decisões e cuidados da rotina.</p><p>Sua jornada de sete dias já é completa. Esta continuação amplia o tempo e as situações de prática, com novos exercícios escritos.</p><a class="button" href="#continuar">Conhecer a continuação ↓</a></div><img src="/assets/continuacao.webp" alt="Mockup ilustrativo da jornada digital Depois do Amém na Vida Real" width="960" height="960" fetchpriority="high"></section><section class="download-section"><p class="eyebrow">TRÊS SEMANAS, NO SEU RITMO</p><h2>Uma prática que cabe<br><em>nas situações de verdade.</em></h2><div class="download-grid"><article class="download-card"><span class="download-number">01</span><h2>Reconhecer o que pesa</h2><p>Separar fatos de suposições, formular pedidos claros, reconhecer limites e escolher uma atitude que caiba no dia.</p></article><article class="download-card"><span class="download-number">02</span><h2>Cuidar das relações</h2><p>Escutar antes de aconselhar, preparar conversas, comunicar limites, reparar o possível e receber apoio.</p></article><article class="download-card"><span class="download-number">03</span><h2>Construir uma rotina possível</h2><p>Encontrar espaço para a prática, criar uma versão curta, retomar depois de uma pausa e escolher como continuar.</p></article></div></section><section class="continuation-offer" id="continuar"><div><p class="eyebrow">DEPOIS DO AMÉM NA VIDA REAL</p><h2>Novos encontros.<br><em>O mesmo espaço para respirar.</em></h2><p>Em cada encontro: reflexão, oração, exercício prático e espaço para registrar. Ao final de cada semana, uma revisão para observar o que foi útil.</p><p>Você escolhe o ritmo. Os 21 encontros podem durar mais de 21 dias corridos.</p><p class="quiet">Material autoguiado em PDF. Não inclui aulas em vídeo, áudios adicionais, grupo ou atendimento individual.</p></div><div class="price-card"><p class="eyebrow">COMPRA OPCIONAL · PAGAMENTO ÚNICO</p><h3>Depois do Amém<br><em>na Vida Real</em></h3><ul><li>21 encontros com novos exercícios</li><li>3 revisões semanais</li><li>1 plano de continuidade</li><li>28 páginas em PDF</li></ul><div class="price"><span>R$</span>97<span class="cents">,00</span></div><p class="payment">Sem assinatura. 100% digital.</p><button class="button" type="button" data-upsell>Quero continuar por R$97 ↗</button><a class="decline" href="/obrigado">Agora não. Quero acessar meus 7 dias.</a><p class="card-foot">7 dias para solicitar reembolso pela plataforma de compra.</p></div></section><section class="delivery-faq"><h2>Antes de escolher.</h2><details><summary>Preciso comprar para usar os sete dias?</summary><p>Não. Seu produto principal já inclui tudo o que foi apresentado. Esta é uma compra separada e opcional.</p></details><details><summary>É um curso com acompanhamento?</summary><p>Não. É uma jornada autoguiada em PDF, com exercícios escritos e revisões. Não há comunidade, mentoria ou atendimento individual incluídos.</p></details><details><summary>As preocupações vão acabar em 21 dias?</summary><p>Essa não é a promessa. O material oferece uma sequência para praticar, observar situações e escolher atitudes possíveis.</p></details></section></main><dialog id="upsell-dialog" aria-labelledby="upsell-dialog-title"><button class="dialog-close" type="button" aria-label="Fechar">×</button><p class="eyebrow">CONTINUAÇÃO DA JORNADA</p><h2 id="upsell-dialog-title">A compra ainda<br><em>não está disponível.</em></h2><p>Você pode continuar usando seu material de sete dias normalmente.</p><a class="button" href="/obrigado">Acessar meus 7 dias</a></dialog>'''+foot()
(ROOT/'continuar.html').write_text(upsell)

index=ROOT/'index.html';html=index.read_text()
if 'favicon.svg' not in html:
 html=html.replace('<link rel="stylesheet" href="/styles.css">','<link rel="icon" href="/favicon.svg" type="image/svg+xml">\n  <link rel="apple-touch-icon" href="/appleicon.png">\n  <meta property="og:image" content="https://depoisdoamem.vercel.app/assets/principal.webp">\n  <meta property="og:image:alt" content="7 Dias Depois do Amém, guia digital, áudio e diário">\n  <meta name="twitter:card" content="summary_large_image">\n  <link rel="stylesheet" href="/styles.css">')
if 'offer-product-image' not in html:
 html=html.replace('<p class="eyebrow">SUA JORNADA COMPLETA</p>','<img class="offer-product-image" src="/assets/principal.webp" alt="Mockup ilustrativo do produto digital 7 Dias Depois do Amém: guia, áudio e diário" width="960" height="960" loading="lazy"><p class="eyebrow">SUA JORNADA COMPLETA</p>')
if 'Como recebo o material?' not in html:
 html=html.replace('<details><summary>Vou receber um livro em casa?', '<details><summary>Como recebo o material?<span class="toggle" aria-hidden="true"></span></summary><p>Após a aprovação do pagamento, o acesso será disponibilizado pela plataforma de compra. A página de entrega reúne os botões para baixar o guia e o diário, além do áudio para ouvir e baixar.</p></details>\n      <details><summary>Vou receber um livro em casa?')
index.write_text(html)
with (ROOT/'styles.css').open('a') as f:f.write('\n.offer-product-image{width:100%;height:auto;max-height:350px;object-fit:contain;border-radius:4px;margin:0 0 28px}\n')

config={'version':2,'cleanUrls':True,'trailingSlash':False,'headers':[{'source':'/materiais/:path*','headers':[{'key':'X-Robots-Tag','value':'noindex, nofollow, nosnippet'},{'key':'X-Content-Type-Options','value':'nosniff'}]}]}
(ROOT/'vercel.json').write_text(json.dumps(config,indent=2))
(ROOT/'robots.txt').write_text('User-agent: *\nAllow: /\nDisallow: /obrigado\nDisallow: /continuar\nDisallow: /materiais/\nSitemap: https://depoisdoamem.vercel.app/sitemap.xml\n')
(ROOT/'sitemap.xml').write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://depoisdoamem.vercel.app/</loc></url></urlset>')
print('Delivery pages, assets, favicon and metadata created.')
