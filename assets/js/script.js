const $ = document.querySelector.bind(document);

const app = $("#app");

// SELECT ONE TABLE
// es: http://127.0.0.1:8000/select/nome_tabela
const url = "http://127.0.0.1:8000/select/persone";

// INSERT INTO TABLE VALUES
// format: http://127.0.0.1:8000/insert/nome_tabela/colonne es: (nome,cognome,eta) solo con le virgole /valori es: (Luca,Rossi,25);
// es: http://127.0.0.1:8000/insert/nome_tabela/nome,cognome,eta/Luca,Rossi,25;

async function start() {
  const f = await (await fetch(url)).json();
  f.forEach((e, i) => {
    const div = document.createElement("div");
    div.innerHTML = `${e.id} | ${e.nome} ${e.cognome} | ${e.eta}`;
    div.classList.add("p-1");
    if (i % 2 == 0) div.classList.add("bg-gray-1");
    else div.classList.add("bg-gray-2");
    app?.append(div);
  });
}

start();

// fetch( url ).then( r => r.json() ).then( r => console.log( r ) );

// fetch( url, {
//     method: 'GET',
//     headers: { 'Content-Type': 'application/json' }
// } ).then( r => r.json() ).then( r => console.log( r ) );
