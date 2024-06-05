<template>
    <CodeLoader @code="code = $event"
    @level="level = $event"
    @levelType="levelType = $event" />
    <CodeInput :code="code"
    @score="score = $event"
    @finish="finish = $event" />
    <ScoreSubmit :finish="finish" :score="score" 
    :level="level" :levelType="levelType" />
    <div class="m5 mt"><VirtualKeyboard/></div>
    <FootBar />
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