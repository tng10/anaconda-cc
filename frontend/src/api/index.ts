import axios from "axios";
// import dotenv from "dotenv";
import { HttpClient } from "./client";
import type { GamePlayPayload, GameStartPayload } from "./interface";
// import {
//   AllIngredientsResponse,
//   AvailableIngredientsResponse,
//   CocktailRecipesResponse,
// } from "./interface";
import { AxiosHttpClientProvider } from "./provider";

// dotenv.config();

enum EndpointEnum {
  START = "start",
  RESUME = "resume",
  PLAY = "play",
}

class RockPaperScissorAPI {
  private httpClient: HttpClient;

  constructor(httpClient: HttpClient) {
    this.httpClient = httpClient;
  }

  private buildEndpointUrl(endpoint: EndpointEnum) {
    return `${this.httpClient.baseUrl}/game/${endpoint}`;
  }

  async startNewGame(payload: GameStartPayload): Promise<any> {
    /**
     * Endpoint: https://0.0.0.0:8000/game/start
     */
    let data = [];
    try {
      const response = await axios.post(
        this.buildEndpointUrl(EndpointEnum.START),
        payload,
      );
      data = response.data;
    } catch (err) {
      console.error(err);
    }
    return data;
  }

  async resumeGame(id: string): Promise<any> {
    /**
     * Endpoint: https://0.0.0.0:8000/game/resume/:id
     */
    let data = [];
    try {
      const response = await axios.get(
        `${this.buildEndpointUrl(EndpointEnum.RESUME)}/${id}`,
      );
      data = response.data;
    } catch (err) {
      console.error(err);
    }
    return data;
  }

  async playGame(id: string, payload: GamePlayPayload): Promise<any> {
    /**
     * Endpoint: https://0.0.0.0:8000/game/play/:id
     */
    let data = [];
    try {
      const response = await axios.put(
        `${this.buildEndpointUrl(EndpointEnum.PLAY)}/${id}`,
        payload,
      );
      data = response.data;
    } catch (err) {
      console.error(err);
    }
    return data;
  }
}

const API_BASE_URL = import.meta.env.VITE_API_BASE_URL || "not-defined";
const axiosHttpClientProvider = new AxiosHttpClientProvider(API_BASE_URL);
const httpClient = new HttpClient(axiosHttpClientProvider);
const api = new RockPaperScissorAPI(httpClient);

export default api;
