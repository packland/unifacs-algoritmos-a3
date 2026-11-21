# Apresentação — Módulo 5

Deck de slides (16:9) sobre o sistema de gestão de estoque. Cada tela é
estática: quem apresenta decide quando passar para a próxima.

## Dois jeitos de abrir

**1. Direto no navegador (o normal).** Dê dois cliques em `index.html` — ou
arraste o arquivo para uma aba. A tela se ajusta à janela e aparece o passador
no rodapé:

- `→`, `Espaço`, `Enter`, `PageDown` ou clique em qualquer lugar: próxima tela
- `←`, `PageUp`, `Backspace`: tela anterior
- `Home` / `End`: primeira / última
- `‹ 03 / 08 ›` no rodapé também funciona com o mouse

Não tem play, não tem barra de tempo, não roda sozinho.

**2. Com o apresentador do HyperFrames** (notas do apresentador e aba de
audiência separada):

```bash
npm run dev
```

Aperte `P` para abrir a tela da audiência — é essa aba que você compartilha no
Meet/Zoom. Aqui as setas também avançam, mas quem manda é o player.

## Arquivos

- `index.html` — os 9 slides, estilos, animações e o passador do modo direto.
- `assets/fonts/` — EB Garamond, Inter e JetBrains Mono (com as licenças OFL).
- `vendor/` — GSAP e o runtime do HyperFrames, para funcionar offline.
