<template>
  <div class="new-player">
    <h2>Player: {{ modelValue }}</h2>

    <div>

      <label for="name">Name</label>
      <input id="name" :modelValue="modelValue" @input="(event: Event) => updateName((event.target as any).value)"
        type="text" placeholder="e.g Julio" />

      <template v-if="!alwaysHuman">
        <label for="isHuman">Is Human</label>
        <input type="checkbox" @change="(event: any) => updateIsHuman((event.target as any).checked)" />
      </template>

    </div>

  </div>
</template>

<script setup lang="ts">
export interface Props {
  modelValue: string
  isHuman?: boolean
  alwaysHuman?: boolean
}

const props = withDefaults(defineProps<Props>(), {
  modelValue: '',
  isHuman: true,
  alwaysHuman: false,
})

const emit = defineEmits(['update:modelValue', 'update:isHuman'])
const updateName = (value: string) => emit('update:modelValue', value);
const updateIsHuman = (value: boolean) => emit('update:isHuman', value);

</script>

<style>
input {
  margin-left: 5px;
  margin-right: 5px;
}

.new-player {
  margin-top: 5px;
}
</style>
