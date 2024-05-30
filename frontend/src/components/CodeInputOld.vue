<template>
  <div class="code-editor">
    <textarea v-model="input" @input="handleInput" rows="10" placeholder="请输入代码..."></textarea>
    <pre v-html="formattedCode"></pre>
  </div>
</template>

<script>
export default {
  data() {
    return {
      input: '',
      code: '<div>Hello  World</div>\n<div>Hell Word</div>', // 示例代码
      correctCount: 0,
      totalCount: 0,
      startTime: null,
      endTime: null
    };
  },
  computed: {
    formattedCode() {
      let result = '';
      for (let i = 0; i < this.code.length; i++) {
        const inputChar = this.input[i];
        const codeChar = this.code[i];
        if (inputChar === codeChar) {
          result += `<span style="color: green;">${this.escapeHtml(codeChar)}</span>`;
        } else if (typeof inputChar === 'undefined') {
          result += `<span style="color: black;">${this.escapeHtml(codeChar)}</span>`;
        } else {
          result += `<span style="color: red;">${this.escapeHtml(codeChar)}</span>`;
        }
      }
      return result;
    }
  },
  methods: {
    escapeHtml(unsafe) {
      return unsafe
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;")
        .replace(/"/g, "&quot;")
        .replace(/'/g, "&#039;");
    },
    handleInput() {
      if (!this.startTime) {
        this.startTime = new Date();
      }
      this.endTime = new Date();
      this.correctCount = this.input.split('').filter((char, index) => char === this.code[index]).length;
      this.totalCount = this.input.length;
    }
  }
};
</script>

<style>
  .code-editor {
    display: flex;
  }
  textarea {
    width: 50%;
    margin-right: 20px;
  }
  pre {
    width: 50%;
    background-color: #f4f4f4;
    padding: 10px;
    overflow-x: auto;
  }
</style>
