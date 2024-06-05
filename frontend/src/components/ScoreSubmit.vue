<template>
  <div v-if="finish" class="finishText">
    <span>你过关！</span>
    <span v-if="!submitted">
        <el-button v-if="!showedSubmit" type='primary' plain @click="showSubmit">提交成绩</el-button>
        <span v-else>
            <el-text class="ml">输入名称：</el-text>
            <el-input v-model="name" placeholder="请输入名称" clearable 
            minlength=1 maxlength=20 v-no-whitespace show-word-limit
            :style="{ width: '260px' }" />
            <el-button type='primary' plain @click="submit" class="ml">提交</el-button>
        </span>
    </span>
    <span v-else>
    提交成功！
    <el-button type='info' plain @click="showRank">查看排行榜</el-button>
    </span>
  </div>
</template>
<script>
import { ElMessage } from 'element-plus';
import axios from 'axios';
export default {
    props: ['score', 'finish', 'level', 'levelType'], //score用时(单位100ms)
    inject: ['config'],
    data() {
        return {
            showedSubmit: false,
            submitted: false,
            name: '',
        }
    },
    directives: {
        noWhitespace: {
            beforeMount(el, binding, vnode) {
                el.addEventListener('input', function(e) {
                    e.target.value = e.target.value.replace(/\s/g, ''); // 移除所有类型的空格
                    vnode.component?.emit('update:modelValue', e.target.value); // 强制更新v-model
                });
            }
        }
    },
    watch:{
        finish(newVal) {
            this.submitted = false;
        }
    },
    methods: {
        getCurrentDateTime() {
            const currentDate = new Date();
            const year = currentDate.getFullYear();
            const month = String(currentDate.getMonth() + 1).padStart(2, '0');
            const day = String(currentDate.getDate()).padStart(2, '0');
            const hours = String(currentDate.getHours()).padStart(2, '0');
            const minutes = String(currentDate.getMinutes()).padStart(2, '0');
            const seconds = String(currentDate.getSeconds()).padStart(2, '0');
            return `${year}-${month}-${day}-${hours}-${minutes}-${seconds}`;
        },
        showSubmit() {
            this.showedSubmit = true;
        },
        async submit() {
            if(!this.name) {
                alert("名字不能为空！");
                return;
            }
            let time = this.getCurrentDateTime(); // str
            let data = {
                name: this.name,
                time: time,
                score: this.score,
                level: this.level,
                levelType: this.levelType
            };
            try {
                await axios.post(this.config.serverURL + '/submitScore', data);
            } catch(error) {
                console.error('提交错误：', error);
                ElMessage({
                    message: '提交失败',
                    type: 'error',
                    showClose: true
                });
                return;
            }
            this.submitted = true;
            ElMessage({
                message: '提交成功',
                type: 'success',
                showClose: true
            });
        },
        showRank() {
            const url = `/scoreboard?level=${this.level}&levelType=${this.levelType}`;
            window.open(url, "_blank");
        }
    }
}
</script>
<style scoped>
.finishText span {
  font-size: 18px;
}
.ml {
    margin-left: 10px;
}
</style>