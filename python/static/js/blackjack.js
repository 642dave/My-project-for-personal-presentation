var dealerSum = 0;
var playerSum = 0;

var dealerAceCount = 0;
var yourAceCount = 0;

var hidden;
var deck;

var canHit = true; // allows the player (you) to draw while yourSum <= 21

window.onload = function() {
    buildDeck();
    shuffleDeck();
    startGame();
}

function buildDeck() {
    let values = ['A','2','3','4','5','6','7','8','9','10','J','Q','K'];
    let types = ['H','D','C','S'];
    deck = [];

    for (let i = 0; i < values.length; i++) {
        for (let j = 0; j < values.length; j++) {
            deck.push(values[j] + "-" + types[i]); // A-C -> K-C, A-D, K-D 
        }
    }
    console.log(deck);
} 

function shuffleDeck() {
    for (let i = 0; i < deck.lenght; i++) {
        let j = Math.floor(Math.random() * deck.length); // (0-1) * 52 -> (0-51.9999)
        let temp = deck[i];
        deck[i] = deck[j];
        deck[j] = temp;
    }
    console.log(deck);
}    

function startGame() {
    hidden = deck.pop();
    dealerSum += getValue(hidden);
}

function getValue(card) {
    let data = card.split("-"); // 4-C -> ['4','C'] 
    let value = data[0];

    //continue 19:20
}
