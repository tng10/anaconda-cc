<template>
  <h1>Game View page | {{ game.player1 }} vs {{ game.player2 }}</h1>

  <div v-if="hasScore">
    <h3>
      {{ game.player1 }}: {{ player1Score }}
    </h3>
    <h3>
      {{ game.player2 }}: {{ player2Score }}
    </h3>
  </div>

  <div v-if="!game.winner">

    <div>
      <h2>Current turn: {{ game.turn }}</h2>
      <h3 v-if="game.last_played">
        Last played: {{ game.last_played }}
      </h3>
    </div>

    <div>Chosen: {{ chosen }}</div>

    <input type="radio" id="rock" value="rock" v-model="chosen" />
    <label for="rock">rock</label>

    <input type="radio" id="paper" value="paper" v-model="chosen" />
    <label for="paper">paper</label>

    <input type="radio" id="scissor" value="scissor" v-model="chosen" />
    <label for="scissor">scissor</label>

    <div>
      <button :disabled="!chosen" @click="play">Play</button>
    </div>
  </div>
  <div v-else>

    <div>
      <h2>Winner: {{ game.winner }}</h2>
      <h3>Last played: {{ game.last_played }}</h3>
    </div>

    <div>
      <button @click="startNewGame">Start a new game?</button>
    </div>
  </div>

</template>

<script lang="ts">
import type { GamePlayPayload, GameResponse } from '@/api/interface';
import { computed, defineComponent, reactive, ref, toRefs } from 'vue';
import { useRoute } from 'vue-router'
import { useRouter } from 'vue-router'
import api from '../api';

export default defineComponent({
  props: {
    id: String,
  },
  async setup() {
    const route = useRoute();
    const router = useRouter();

    let state = reactive<{ game: GameResponse }>({
      game: {
        id: '',
        player1: '',
        player2: '',
        player1_is_human: true,
        player2_is_human: true,
        last_played: null,
        turn: '',
        winner: null,
      },
    })

    try {
      state.game = await api.resumeGame(route.params.id as string)
    } catch (error) {
      console.error(`Could not load the game ${route.params.id}`)
    }

    const player1Score = ref<number>(0);
    const player2Score = ref<number>(0);
    const chosen = ref<null | string>();

    const hasScore = computed(() => {
      return (player1Score.value + player2Score.value) > 0
    })

    const play = async function () {

      if (!chosen.value) {
        console.error(`An element must be chosen`)
        return
      }

      if (!state.game) {
        console.error(`This is not a valid game`)
        return
      }

      const payload: GamePlayPayload = {
        current_turn: state.game.turn,
        choice: chosen.value as string,
      }
      state.game = await api.playGame(state.game.id, payload)

      chosen.value = null;

      if (state.game.winner) {
        if (state.game.winner === state.game.player1) {
          player1Score.value += 1
        } else if (state.game.winner === state.game.player2) {
          player2Score.value += 1
        }
      }

    }

    const startNewGame = async function () {
      if (!state.game) {
        console.error(`This is not a valid game`)
        return
      }

      try {
        const game: GameResponse = await api.startNewGame({
          player1_name: state.game.player1,
          player2_name: state.game.player2,
          player1_is_human: state.game.player1_is_human,
          player2_is_human: state.game.player2_is_human,
        })

        state.game = game;

        router.push({
          name: 'game',
          params: {
            id: game.id,
          }
        })

      } catch (error) {
        console.error('Sorry, could not start a new game!')
      }
    }

    return {
      ...toRefs(state),
      chosen,
      play,
      startNewGame,
      player1Score,
      player2Score,
      hasScore,
    }

  }
})

</script>

<style>
input[type="radio"] {
  margin-left: 5px;
  margin-right: 5px;
}
</style>