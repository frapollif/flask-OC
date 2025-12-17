
// const bottone_carica=document.getElementById('bottone-carica');
// bottone_carica.addEventListener('click', caricaStudenti);
const bottone_aggiungi=document.getElementById('bottone-aggiungi');
bottone_aggiungi.addEventListener('click', aggiungiStudente);


async function aggiungiStudente() {
    const nome = document.getElementById("nome_studente").value;
    const classe = document.getElementById("classe_studente").value;
    
    if (!nome || !classe){
        alert("Inserisci nome e classe!")
        return "";
    }

    const nuovoStudente ={
        nome : nome,
        classe: classe
    };

    const response = await fetch('/api/studenti' , 
        {
        method : 'POST',
        headers: {
            'Content-Type' : 'application/json',
        },
        body: JSON.stringify(nuovoStudente)
        }
    );

    const studenteCreato = await response.json();
    console.log(studenteCreato);

    caricaStudenti();
}


async function caricaStudenti(){

    const lista = document.getElementById("lista-studenti");
    lista.textContent ="Caricamento lista";


    const response = await fetch('/api/studenti');
    const studenti = await response.json();

    lista.textContent ="";
    studenti.forEach(studente =>{
        const item = document.createElement('li');
        item.textContent = `${studente.nome} - Classe ${studente.classe}`;
        lista.appendChild(item);

    })

}

document.addEventListener('DOMContentLoaded', function() {
    caricaStudenti();

})