<template>
  <CodeLoader @code="code = $event"
  @level="level = $event"
  @levelType="levelType = $event" />
  <CodeInput :code="code" :level="level"  
  @score="score = $event"
  @finish="finish = $event" 
  :wider="!keyboardVisible" />
  <ScoreSubmit :finish="finish" :score="score" 
  :level="level" :levelType="levelType" />
  <div v-if="keyboardVisible" class="m5 mt">
    <VirtualKeyboard />
  </div>
  <FootBar @keyboardOnShow="keyboardVisible=$event"/>
</template>

<script>
import CodeInput from './CodeInput.vue';
import VirtualKeyboard from './VirtualKeyboard.vue';
import CodeLoader from './CodeLoader.vue';
import ScoreSubmit from './ScoreSubmit.vue';
import FootBar from './FootBar.vue';

export default {
  components: {
    CodeInput,
    VirtualKeyboard,
    CodeLoader,
    ScoreSubmit,
    FootBar
  },
  data() {
    return {
      code: '尚未选择关卡。',
      level: '',
      levelType: '',
      score: 0,
      finish: false,
      keyboardVisible: true,
    }
  },
  methods: {
    toggleKeyboard() {
      this.keyboardVisible = !this.keyboardVisible;
    }
  }
}
</script>

<style scoped>
.m5 {
  margin: 0 5%;
}
.mt {
  margin-top: 4px;
}
</style>
``
