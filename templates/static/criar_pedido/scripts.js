
(() => {
  let cliente = null;
  let enderecoId = null;
  const carrinho = [];
  const NOVO_PEDIDO_URL = "{% url 'novo_pedido' %}";
  const clientesEl = document.getElementById('clientes');
  const enderecosEl = document.getElementById('enderecos');
  const produtosEl = document.getElementById('produtos');
  const carrinhoEl = document.getElementById('carrinho');
  const totalEl = document.getElementById('total');
  const enviarBtn = document.getElementById('enviar');
  const msgEl = document.getElementById('msg');

  function atualizaCarrinho() {
    carrinhoEl.innerHTML = '';
    let total = 0;
    carrinho.forEach((p, i) => {
      const li = document.createElement('li');
      li.textContent = `${p.codigo} x${p.q} — R$ ${p.valor.toFixed(2).replace('.', ',')}`;
      const rm = document.createElement('button');
      rm.textContent = 'Remover';
      rm.type = 'button';
      rm.onclick = () => {
        carrinho.splice(i, 1);
        atualizaCarrinho();
      };
      li.appendChild(document.createTextNode(' '));
      li.appendChild(rm);
      carrinhoEl.appendChild(li);
      total += p.q * p.valor;
    });
    totalEl.textContent = total.toFixed(2).replace('.', ',');
  }

  clientesEl.addEventListener('click', e => {
    const el = e.target.closest('.cliente_item');
    if (!el) return;
    Array.from(clientesEl.querySelectorAll('.cliente_item')).forEach(c => c.classList.remove('selected'));
    el.classList.add('selected');
    cliente = { id: el.dataset.clienteId, cpf: el.dataset.clienteCpf };

    const labels = Array.from(enderecosEl.querySelectorAll('.endereco'));
    labels.forEach(label => {
      if (label.dataset.cliente === cliente.cpf) {
        label.classList.add('visible');
        label.querySelector('input').disabled = false;
      } else {
        label.classList.remove('visible');
        const inp = label.querySelector('input');
        inp.checked = false;
        inp.disabled = true;
      }
    });

    const firstVisible = enderecosEl.querySelector('.endereco.visible input');
    if (firstVisible) {
      firstVisible.checked = true;
      enderecoId = firstVisible.value;
    } else {
      enderecoId = null;
    }
    msgEl.textContent = '';
  });

  enderecosEl.addEventListener('change', e => {
    if (e.target.name === 'endereco_radio') enderecoId = e.target.value;
  });

  produtosEl.addEventListener('click', e => {
    if (!e.target.classList.contains('btn-add')) return;
    const li = e.target.closest('li.produto-item');
    const id = li.dataset.id;

    // pega o valor bruto de forma segura e converte para número
    const valorRaw = li.dataset.valor ?? li.getAttribute('data-valor') ?? '';
    const valor = parseFloat(String(valorRaw).replace(',', '.')) || 0;

    const codigo = li.dataset.codigo || li.textContent.split(' - ')[0].trim();
    const existente = carrinho.find(p => p.id === id);
    if (existente) existente.q++;
    else carrinho.push({ id, codigo, valor, q: 1 });
    atualizaCarrinho();
  });

  enviarBtn.addEventListener('click', () => {
    msgEl.style.color = 'red';
    if (!cliente) { msgEl.textContent = 'Selecione um cliente.'; return; }
    if (!enderecoId) { msgEl.textContent = 'Selecione um endereço.'; return; }
    if (carrinho.length === 0) { msgEl.textContent = 'Adicione pelo menos um produto.'; return; }

    const payload = {
      cliente_id: cliente.id,
      cliente_cpf: cliente.cpf,
      endereco_id: enderecoId,
      produtos: carrinho.map(p => ({ produto_id: p.id, codigo: p.codigo, quantidade: p.q, valor_unitario: p.valor }))
    };

    const url = NOVO_PEDIDO_URL;
    const csrf = document.querySelector('meta[name="csrf-token"]').content;
    fetch(url, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-CSRFToken': csrf },
      body: JSON.stringify(payload)
    })
    .then(r => r.ok ? r.json() : r.json().then(err => Promise.reject(err)))
    .then(data => {
      msgEl.style.color = 'green';
      msgEl.textContent = 'Pedido criado. ID: ' + (data.pedido_id || '—');
      cliente = null;
      enderecoId = null;
      carrinho.length = 0;
      Array.from(clientesEl.querySelectorAll('.cliente_item')).forEach(c => c.classList.remove('selected'));
      Array.from(enderecosEl.querySelectorAll('.endereco')).forEach(l => {
        l.classList.remove('visible');
        const inp = l.querySelector('input');
        inp.checked = false;
        inp.disabled = false;
      });
      atualizaCarrinho();
    })
    .catch(err => { msgEl.textContent = (err && err.detail) ? err.detail : String(err); });
  });
})();
