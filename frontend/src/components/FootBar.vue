<template>
  <div class="footer-bar">
    <div class="footer-content">
      <a :href="this.config.icpHref">{{ this.config.icp }}</a>
      <span class="right-content">
        <a @click="gameRule" class="mr">游戏规则</a>
        <a @click="about">关于</a>
      </span>
    </div>
  </div>
</template>

<script>
export default {
  inject: ["config"],
  methods: {
    gameRule() {
        alert("TODO");
    },
    about() {
        alert("欢迎查看源码 https://github.com/lr580/codeSpeedUp")
    }
  },
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
</style>
