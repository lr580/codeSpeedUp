<template>
    <div class="line">
        <el-text class="levelname"><b>关卡：</b>[{{levelType}}] {{level}} <b>玩家战绩排行榜</b> <a href="/">回到主页</a> </el-text>
    </div>
    <div v-if="data">
        <el-table :data="data" height="520px" table-layout="auto">
            <el-table-column prop="name" sortable label="姓名" min-width="200" align="center"/>
            <el-table-column prop="timePretty" label="用时" min-width="80" align="center"/>
            <el-table-column prop="speed" sortable label="速度(字符/分钟)" min-width="150" align="center"/>
            <el-table-column prop="date" sortable label="提交时间" min-width="260" align="center"/>
        </el-table>
    </div>
    <div v-else> 暂无数据。</div>
</template>
<script>
import axios from 'axios';
export default {
  data() {
    return {
        level : '',
        levelType : '',
        data: '',
    };
  },
  inject: ['config'],
  async mounted() {
    this.level = this.$route.query.level;
    this.levelType = this.$route.query.levelType;
    try {
        const response = await axios.get(this.config.serverURL + `/getRank/${this.levelType}/${this.level}`);
        this.data = response.data;
    } catch(error) {
        console.error('获取关卡代码失败:', error);
        this.$message({message:'获取失败',type:'error'});
    }
  }
}
</script>
<style scoped>
.levelname {
    font-size: 18px;
}
a {
    text-decoration: none;
}
.line {
    margin-bottom: 12px;
}
</style>