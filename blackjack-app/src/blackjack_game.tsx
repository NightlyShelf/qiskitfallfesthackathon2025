import React, { useState, useEffect } from "react";
import seedrandom from "seedrandom";

type Card = { suit: string; rank: string };
type GameState = {
  deck: Card[];
  playerHand: Card[];
  dealerHand: Card[];
  bet: number;
  status: "idle" | "playing" | "finished";
  message?: string;
};

const suits = ["♠️", "♥️", "♦️", "♣️"];
const ranks = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"];

const getCardValue = (card: Card) => {
  if (["J", "Q", "K"].includes(card.rank)) return 10;
  if (card.rank === "A") return 11;
  return parseInt(card.rank);
};

const calculateHandValue = (hand: Card[]) => {
  let total = hand.reduce((sum, card) => sum + getCardValue(card), 0);
  let aces = hand.filter((c) => c.rank === "A").length;
  while (total > 21 && aces > 0) {
    total -= 10;
    aces--;
  }
  return total;
};

export default function QuantumBlackjack() {
  const [game, setGame] = useState<GameState>({
    deck: [],
    playerHand: [],
    dealerHand: [],
    bet: 10,
    status: "idle",
  });
  const [rng, setRng] = useState<() => number>(() => Math.random);
  const [balance, setBalance] = useState(100);
  const [message, setMessage] = useState<string>("Loading seed...");

  // Fetch Python seed and init RNG
  useEffect(() => {
    fetch("http://localhost:5000/seed")
      .then((res) => res.json())
      .then((data) => {
        const rngFunc = seedrandom(data.seed.toString());
        setRng(() => rngFunc);
        console.log("No error");
        setMessage("Ready to play!");
      })
      .catch(() => {
        console.log("Error");
        setMessage("Failed to connect to seed server. Using default random.");
      });
  }, []);

  const createDeck = () => {
    const deck: Card[] = [];
    suits.forEach((suit) =>
      ranks.forEach((rank) => deck.push({ suit, rank }))
    );
    // Shuffle with seeded RNG
    for (let i = deck.length - 1; i > 0; i--) {
      const j = Math.floor(rng() * (i + 1));
      [deck[i], deck[j]] = [deck[j], deck[i]];
    }
    return deck;
  };

  const startGame = () => {
    const deck = createDeck();
    const playerHand = [deck.pop()!, deck.pop()!];
    const dealerHand = [deck.pop()!, deck.pop()!];
    setGame({
      deck,
      playerHand,
      dealerHand,
      bet: 10,
      status: "playing",
    });
    setMessage("Game started! Hit or Stand?");
  };

  const hit = () => {
    if (game.status !== "playing") return;
    const deck = [...game.deck];
    const newCard = deck.pop()!;
    const newPlayerHand = [...game.playerHand, newCard];
    const value = calculateHandValue(newPlayerHand);

    if (value > 21) {
      setGame({ ...game, playerHand: newPlayerHand, status: "finished" });
      setBalance(balance - game.bet);
      setMessage("Bust! You lose.");
    } else {
      setGame({ ...game, deck, playerHand: newPlayerHand });
    }
  };

  const stand = () => {
    if (game.status !== "playing") return;

    const deck = [...game.deck];
    let dealerHand = [...game.dealerHand];
    while (calculateHandValue(dealerHand) < 17) {
      dealerHand.push(deck.pop()!);
    }

    const playerValue = calculateHandValue(game.playerHand);
    const dealerValue = calculateHandValue(dealerHand);
    let resultMsg = "";

    if (dealerValue > 21 || playerValue > dealerValue) {
      resultMsg = "You win!";
      setBalance(balance + game.bet);
    } else if (dealerValue === playerValue) {
      resultMsg = "Push (tie).";
    } else {
      resultMsg = "Dealer wins.";
      setBalance(balance - game.bet);
    }

    setGame({ ...game, dealerHand, deck, status: "finished" });
    setMessage(resultMsg);
  };

  return (
    <div className="p-6 text-center">
      <h1 className="text-2xl font-bold mb-4">Quantum Blackjack 🃏</h1>
      <p className="mb-2">Balance: ${balance}</p>
      <p className="mb-4">{message}</p>

      {game.status === "idle" && (
        <button onClick={startGame} className="bg-green-600 text-white px-4 py-2 rounded">
          Start Game
        </button>
      )}{game.status === "playing" && (
        <div>
          <div className="mb-4">
            <p>Player: {game.playerHand.map((c) => c.suit + c.rank).join(" ")}</p>
            <p>Dealer: {game.dealerHand[0].suit + game.dealerHand[0].rank} ??</p>
          </div>
          <button onClick={hit} className="bg-blue-600 text-white px-4 py-2 rounded m-2">Hit</button>
          <button onClick={stand} className="bg-yellow-500 text-white px-4 py-2 rounded m-2">Stand</button>
        </div>
      )}

      {game.status === "finished" && (
        <div>
          <p>Player: {game.playerHand.map((c) => c.suit + c.rank).join(" ")}</p>
          <p>Dealer: {game.dealerHand.map((c) => c.suit + c.rank).join(" ")}</p>
          <button onClick={startGame} className="bg-green-600 text-white px-4 py-2 rounded mt-4">
            Play Again
          </button>
        </div>
      )}
    </div>
  );
}
    