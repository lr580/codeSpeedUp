<template>
    <h1>码上速成 Code Speed-Up</h1>
    <CodeInput :code="code"/>
    <!-- <KeyboardSample /> -->
    <div class="m5">
        <VirtualKeyboard/>
    </div>
</template>

<script>
import CodeInput from './CodeInput.vue';
import VirtualKeyboard from './VirtualKeyboard.vue';
import KeyboardSample from './KeyboardSample.vue';

export default {
  components: {
    CodeInput,
    VirtualKeyboard,
    KeyboardSample
  },
  data() {
    return {
        code: '#include <bits/stdc++.h>\nusing namespace std;'
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
</style>