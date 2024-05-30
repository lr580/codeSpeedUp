<template>
    <h1>码上速成 Code Speed-Up</h1>
    <CodeLoader @code="code = $event"/>
    <CodeInput :code="code"/>
    <div class="m5 mt">
        <VirtualKeyboard/>
    </div>
</template>

<script>
import CodeInput from './CodeInput.vue';
import VirtualKeyboard from './VirtualKeyboard.vue';
import CodeLoader from './CodeLoader.vue';

export default {
  components: {
    CodeInput,
    VirtualKeyboard,
    CodeLoader
  },
  data() {
    return {
        code: '尚未选择关卡。'
    }
  }
}
</script>

<style scoped>
h1 {
  margin-top: -30px;
}
.m5 {
  margin: 0 5%;
}
.mt {
  margin-top: 5px;
}
</style>