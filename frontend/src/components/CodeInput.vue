<template>
  <div class="topper">
    <el-button-group>
      <el-button round type="success" @click="startTiming" :disabled="timerId !== null">开始</el-button>
      <el-button round type="warning" @click="pauseTiming" :disabled="timerId === null">暂停</el-button>
      <el-button round type="danger" @click="resetInput">重置</el-button>
    </el-button-group>
    <span class="statinfo">
      总用时：<span v-if="totalMilliseconds>=600">{{Math.floor(totalMilliseconds/600)}}分</span>{{Math.floor(totalMilliseconds/10%60)}}.{{totalMilliseconds%10}}秒 &nbsp;
      进度：{{correctCount}} / {{code.length}} &nbsp;
      <!-- 正确率：{{Math.floor(correctCount/Math.max(1,totalCount)*100)}}% &nbsp; -->
      速度：{{(totalCount/(Math.max(1,totalMilliseconds)/600)).toFixed(2)}} 字/分钟
    </span>
  </div>
  <el-row class="title">
    <el-col :span="12">输入区</el-col>
    <el-col :span="12">参考代码</el-col>
  </el-row>
  <el-scrollbar height="290px">
    <el-row class="code-editor">
      <el-col :span="1">
        <LineNumbers :numRows="numRows" />
      </el-col>
      <el-col :span="11">
        <textarea
          v-model="input"
          @input="handleInput"
          :rows="numRows"
          placeholder="请输入代码..."
          :disabled="inputDisabled"
          @paste.prevent=""
          class="codeinput">
        </textarea>
      </el-col>
      <el-col :span="1">
        <LineNumbers :numRows="numRows" />
      </el-col>
      <el-col :span="11">
        <pre v-html="formattedCode" class="code-display"></pre>
      </el-col>
    </el-row>
  </el-scrollbar>
  <div v-if="finishCoding" class="finishText">
    <span>你过关！</span>
  </div>
</template>

<script>
import { ElInput, ElRow, ElCol } from 'element-plus';
import LineNumbers from './LineNumbers.vue';

export default {
  components: {
    ElInput,
    ElRow,
    ElCol,
    LineNumbers
  },
  props: ['code'],
  data() {
    return {
      input: '',
      inputDisabled: true,
      hasStarted: false,
      correctCount: 0,
      totalCount: 0,
      timerId: null,
      totalMilliseconds: 0
    };
  },
  computed: {
    formattedCode() {
      let result = '';
      for (let i = 0; i < this.code.length; i++) {
        const inputChar = this.input[i];
        const codeChar = this.code[i];
        if (inputChar === codeChar) {
          result += `<span class="correct">${this.escapeHtml(codeChar)}</span>`;
        } else if (typeof inputChar === 'undefined') {
          result += `<span class="untyped">${this.escapeHtml(codeChar)}</span>`;
        } else {
          result += `<span class="incorrect">${this.escapeHtml(codeChar)}</span>`;
        }
      }
      return result;
    },
    numRows() {
      return 1+((this.formattedCode.match(/\n/g) || []).length);
    },
    finishCoding() {
      return this.correctCount == this.code.length;
    }
  },
  watch: {
    code(newCode) {
      this.resetInput();
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
      this.correctCount = this.input.split('').filter((char, index) => char === this.code[index]).length;
      this.totalCount = this.input.length; // 输入总数
      if(this.correctCount == this.code.length) {
        this.pauseTiming();
      }
    },
    startTiming() {
      if(this.code == '尚未选择关卡。') {
        alert("您尚未选择关卡，无法开始。");
        return;
      }
      if (this.timerId === null) {
        this.timerId = setInterval(() => {
          this.totalMilliseconds += 1;
        }, 100);
        this.inputDisabled = false;
      }
    },
    pauseTiming() {
      if (this.timerId !== null) {
        clearInterval(this.timerId);
        this.timerId = null;
        this.inputDisabled = true;
      }
    },
    resetInput() {
      if (this.timerId !== null) {
        clearInterval(this.timerId);
        this.timerId = null;
      }
      this.input = '';
      this.totalCount = 0;
      this.correctCount = 0;
      this.totalMilliseconds = 0;
      this.inputDisabled = true;
    }
  }
};
</script>

<style scoped>
.code-editor {
  font-family: 'Fira Code', monospace; 
  font-size: 16px; 
  line-height: 1.5em;
  padding-left: 5%;
  padding-right: 5%;
}
textarea.codeinput {
  font-family: 'Fira Code', monospace; 
  font-size: 16px; 
  line-height: 1.5em;
  width: 100%;                /* 确保填满容器 */
  height: 100%;               /* 高度自适应 */
  outline: none;              /* 点击时无轮廓线 */
  resize: none;               /* 禁止用户调整大小 */
  box-sizing: border-box;     /* 盒模型调整，包含内边距和边框 */
  overflow: auto;             /* 超出滚动 */
}
.code-display {
  background-color: #f4f4f4;
  margin-top: 0;
  text-align: left;
  white-space: pre-wrap;
  word-wrap: break-word;
}
.topper {
  margin-bottom: 10px;
}
.statinfo {
  margin-left: 3%;
  font-size: 16px; 
}
.title {
  margin-bottom: 10px;
  font-size: 20px;
  font-weight: 800;
}
.finishText span {
  font-size: 18px;
}
</style>

<style>
.code-display .correct {
  color: #333300;
  background-color: #ccff99;
}
.code-display .incorrect {
  color: red;
  background-color: #ffcccc;
}
.code-display .untyped {
  color: black;
}
</style>