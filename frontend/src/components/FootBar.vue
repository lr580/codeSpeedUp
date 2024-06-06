<template>
  <div class="footer-bar">
    <div class="footer-content">
      <a :href="this.config.icpHref">{{ this.config.icp }}</a>
      <span class="right-content">
        <a @click="toggleKeyboard"  class="mr"> {{keyboardOnShow ? '隐藏' : '显示'}}虚拟键盘</a>
        <a @click="ruleOnShow = true" class="mr">游戏规则</a>
        <a @click="aboutOnShow = true">关于</a>
      </span>
    </div>
  </div>
  <el-drawer v-model="aboutOnShow" direction="btt" title="关于" size="35%">
    <div class="drawerText">
      <div>当前版本：v1.0.1 (最后更新时间：2024/6/6)</div>
      <div>作者：lr580</div>
      <div>联系方式(QQ)：2277379149</div>
      <div>源码：<a href="https://github.com/lr580/codeSpeedUp" target="_blank">https://github.com/lr580/codeSpeedUp</a></div>
      <div>如果您对该游戏项目有任何改进建议或上传新关卡等灵感，欢迎提交 PR！</div>
    </div>
  </el-drawer>
  <el-drawer v-model="ruleOnShow" direction="btt" title="游戏规则">
    <div class="drawerText">
      <div>这是一个提高编程写代码速度的练习游戏。</div>
      <div>请选择主题与关卡，然后点击开始，在输入区依照参照代码编写内容。当输入完毕且与参考代码完全符合时，通过该关卡。</div>
      <div>可以将自己的练习成绩提交，与小伙伴比一比谁更快！用时越短排名越前。</div>
    </div>
  </el-drawer>
</template>

<script>
export default {
  inject: ["config"],
  data() {
    return {
      aboutOnShow: false,
      ruleOnShow: false,
      keyboardOnShow: true,
    };
  },
  methods: {
    toggleKeyboard() {
      this.keyboardOnShow = !this.keyboardOnShow;
      this.$emit("keyboardOnShow", this.keyboardOnShow);
    },
  }
};
</script>

<style scoped>
.footer-bar {
  position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  background-color: #f5f5f5;
  padding: 10px 0;
  box-shadow: 0 -2px 5px rgba(0, 0, 0, 0.1);
}

.footer-content {
  max-width: 1200px;
  margin: 0 auto;
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding-left: 10px;
}

.footer-content span {
  font-size: 14px;
  color: #666;
}

.right-content {
  margin-right: 20px;
}

a {
  color: black;
  text-decoration: none;
  cursor: pointer;
  font-size: 16px;
}
a:hover {
  text-decoration: underline;
}
.mr {
  margin-right: 10px;
}
.drawerText {
  font-size: 18px;
  text-align: left;
}
</style>
