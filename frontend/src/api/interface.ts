export interface GameStartPayload {
  player1_name: string
  player2_name: string
  player1_is_human: boolean
  player2_is_human: boolean
}

export interface GamePlayPayload {
  current_turn: string
  choice: string
}


export interface GameResponse {
  id: string,
  player1: string;
  player2: string;
  player1_is_human: boolean;
  player2_is_human: boolean;
  last_played: string | null;
  turn: string;
  winner: string | null;
}
