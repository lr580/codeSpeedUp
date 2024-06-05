<template>
  <codemirror
    v-model="code" ref="codemirror" 
    class="codemirror"
    placeholder="请输入代码..."
    :indent-with-tab="true"
    :tabSize="4"
    :extensions="extensions"
  />
</template>

<script>
import { Codemirror } from "vue-codemirror";
import { javascript } from "@codemirror/lang-javascript";
import { python } from "@codemirror/lang-python";
import { cpp } from "@codemirror/lang-cpp";
import { java } from "@codemirror/lang-java";
import { EditorView } from "@codemirror/view";
export default {
  props: ["language"],
  data() {
    return {
      code: "",
      baseExtensions: [EditorView.lineWrapping],
      extensions: [],
    };
  },
  created() {
    this.extensions = this.setupExtensions(this.language);
  },
  methods: {
    setupExtensions(language) {
      const extensions = [...this.baseExtensions];
      if(!language) {
        ;//pass
      } else if (language.endsWith(".js")) {
        extensions.push(javascript());
      } else if (language.endsWith(".py")) {
        extensions.push(python());
      } else if (language.endsWith(".cpp")) {
        extensions.push(cpp());
      } else if (language.endsWith(".java")) {
        extensions.push(java());
      } else {
        ;//pass
      }
      return extensions;
    },
    clear() { // 供父组件调用，下同
      this.code = '';
    },
    focus() {
      // TODO
      // console.log(this.$refs.codemirror.$el);
      // this.$refs.codemirror.$el.focus();
    }
  },
  watch: {
    language(newLang) {
      this.extensions = this.setupExtensions(newLang);
    },
    code(newCode) {
      this.$emit("code", newCode);
    },
  },
  components: {
    Codemirror,
  },
};
</script>
<style>
.codemirror {
  font-size: 18px;
  text-align: left;
}
</style>
