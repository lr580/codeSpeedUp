<template>
  <div ref="editorContainer" class="codemirror"></div>
</template>

<script>
import { EditorState } from "@codemirror/state";
import { EditorView } from "@codemirror/view";
import { javascript } from "@codemirror/lang-javascript";
import { python } from "@codemirror/lang-python";
import { cpp } from "@codemirror/lang-cpp";

export default {
  props: ["language"],
  data() {
    return {
      code: "",
      editorView: null,
    };
  },
  mounted() {
    console.log("Component mounted, initializing editor...");
    this.initEditor();
  },
  beforeDestroy() {
    if (this.editorView) {
      console.log("Destroying editor instance...");
      this.editorView.destroy();
    }
  },
  methods: {
    initEditor() {
      console.log("Initializing editor...");
      const extensions = [
        EditorView.lineWrapping,
      ];
      if (!this.language) {
        extensions.push(cpp());
      } else if (this.language.endsWith(".js")) {
        extensions.push(javascript());
      } else if (this.language.endsWith(".py")) {
        extensions.push(python());
      } else if (this.language.endsWith(".cpp")) {
        extensions.push(cpp());
      } else {
        extensions.push(python());
      }

      this.editorView = new EditorView({
        state: EditorState.create({
          doc: this.code,
          extensions: extensions,
        }),
        parent: this.$refs.editorContainer,
      });
      console.log("Editor should now be initialized.", this.editorView);
    },
    focus() {
      if (this.editorView) {
        console.log("Focusing editor...");
        this.editorView.focus();
      }
    },
  },
  watch: {
    code(newCode) {
      console.log("Code changed:", newCode);
      this.code = newCode;
      this.updateEditorContent();
    },
    language(newLang) {
      console.log("Language changed:", newLang);
      if (this.editorView) {
        this.editorView.destroy();
        this.initEditor(); // Reinitialize editor with new language
      }
    },
  },
};
</script>


<style>
.codemirror {
  font-size: 16px;
  height: 400px;
  color: #333;
  background-color: #f5f5f5;
  border: 1px solid #ccc;
}

.cm-editor {
  font-family: monospace;
  height: 100%;
}

.cm-scroller {
  overflow: auto;
}

/* 调整光标颜色 */
.cm-cursor {
  border-left: 2px solid #000;
}

/* 调整选中文本的背景颜色 */
.cm-selectionBackground, .cm-content ::selection {
  background: #b0d0f0;
}
</style>

