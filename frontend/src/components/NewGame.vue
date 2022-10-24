<template>
  <div>
    <h1>New Game</h1>

    <NewPlayer v-model="state.player1.name" id="player-1" :is-human="state.player1.isHuman" :always-human="true">
    </NewPlayer>
    <NewPlayer v-model="state.player2.name" id="player-2" :is-human="state.player2.isHuman"
      @update:is-human="updateIsHumanForPlayer2"></NewPlayer>

    <div class="buttons">
      <button :disabled="!canStart" @click="startGame">Start game</button>
    </div>
  </div>
</template>

<script setup lang="ts">
import { computed, reactive } from "vue";
import NewPlayer from "./NewPlayer.vue";
import { useRouter } from 'vue-router'
import api from '../api';

const router = useRouter();

const state = reactive({
  player1: {
    name: '',
    isHuman: true,
  },
  player2: {
    name: '',
    isHuman: false
  }
});


function updateIsHumanForPlayer2(value: boolean) {
  state.player2.isHuman = value
}

async function startGame() {
  try {
    const game = await api.startNewGame({
      player1_name: state.player1.name,
      player2_name: state.player2.name,
      player1_is_human: state.player1.isHuman,
      player2_is_human: state.player2.isHuman,
    })

    router.push({
      name: 'game',
      params: {
        id: game.id,
      }
    })

  } catch (error) {
    console.error('Sorry, could not start a game!')
  }
}

const canStart = computed(() => {
  return state.player1.name !== state.player2.name
})

</script>

<style>
.buttons {
  margin-top: 5px;
}
</style>
