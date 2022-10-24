<template>

  <Suspense>
    <template #default>
      <CurrentGame :id="($route.params.id as string)" />
    </template>
    <template #fallback>
      <span>Loading...</span>
    </template>
  </Suspense>


</template>

<script setup lang="ts">
import CurrentGame from '../components/CurrentGame.vue';

</script>