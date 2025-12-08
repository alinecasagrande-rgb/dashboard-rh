# 🖼️ Como Adicionar o Logo da Empresa

## 📋 Passo a Passo

### **Opção 1: Adicionar Arquivo de Imagem (Recomendado)**

1. **Prepare o logo:**
   - Formato: PNG, JPG ou SVG (PNG é recomendado)
   - Tamanho recomendado: 200x200 pixels ou proporcional
   - Nome do arquivo: `logo.png`

2. **Coloque o arquivo na pasta do projeto:**
   - Copie o arquivo `logo.png` para a mesma pasta onde está o `index.html`
   - A pasta deve ficar assim:
     ```
     Dashboard Recursos Humanos/
     ├── index.html
     ├── dados.json
     ├── dashboard.js
     └── logo.png  ← Seu logo aqui
     ```

3. **Pronto!** O logo aparecerá automaticamente no dashboard.

### **Opção 2: Usar Logo Online (URL)**

Se o logo estiver hospedado online:

1. **Abra o arquivo `index.html`**
2. **Encontre a linha 229** (onde está `<img src="logo.png"...`)
3. **Substitua `logo.png` pela URL do logo:**
   ```html
   <img src="https://exemplo.com/logo.png" alt="Logo da Empresa" class="h-10 w-auto">
   ```

### **Opção 3: Converter Imagem para Base64 (Inline)**

Se quiser embutir o logo diretamente no HTML:

1. **Use um conversor online:** https://www.base64-image.de/
2. **Cole a imagem e copie o código Base64**
3. **Substitua no `index.html`** a linha 229:
   ```html
   <img src="data:image/png;base64;SEU_CODIGO_BASE64_AQUI" alt="Logo" class="h-10 w-auto">
   ```

---

## ✅ Verificação

Após adicionar o logo:

1. Abra o dashboard usando `ABRIR_DASHBOARD.bat`
2. Verifique se o logo aparece no canto superior esquerdo
3. Se não aparecer, verifique:
   - O arquivo está na mesma pasta que `index.html`?
   - O nome do arquivo está correto? (`logo.png`)
   - O formato da imagem é suportado? (PNG, JPG, SVG)

---

## 🎨 Dicas

- **Tamanho ideal:** 200x200 pixels (ou proporcional)
- **Formato recomendado:** PNG com fundo transparente
- **Cores:** O logo aparecerá em um fundo branco arredondado
- **Altura:** O logo será redimensionado automaticamente para altura de 40px

---

## 📝 Nota

Se o logo não for encontrado, aparecerá um placeholder com as iniciais "RH" em azul.


