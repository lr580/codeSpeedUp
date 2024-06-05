<template>
  <codemirror
    v-model="code"
    class="codemirror"
    placeholder="请输入代码..."
    :indent-with-tab="true"
    :extensions="extensions"
  />
</template>

<script>
import { Codemirror } from "vue-codemirror";
import { javascript } from "@codemirror/lang-javascript";
import { python } from "@codemirror/lang-python";
import { cpp } from "@codemirror/lang-cpp";
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
        extensions.push(cpp());
      } else if (language.endsWith(".js")) {
        extensions.push(javascript());
      } else if (language.endsWith(".py")) {
        extensions.push(python());
      } else if (language.endsWith(".cpp")) {
        extensions.push(cpp());
      } else {
        extensions.push(python());
      }
      return extensions;
    },
  },
  watch: {
    language(newLang) {
      this.extensions = this.setupExtensions(newLang);
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
