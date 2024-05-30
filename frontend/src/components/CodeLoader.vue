<template>
    <div class="main">
        <el-text>选择主题：</el-text>
        <el-select v-model="selectedLevelType" class="selector" placeholder='请选择主题'>
            <el-option v-for="(value, key) in levelDesc" :key="key" :value="key">
                {{ key }}
            </el-option>
        </el-select>
        <el-text class='ml'>选择关卡：</el-text>
        <el-text v-if="!selectedLevelType">
            请先选择主题。
        </el-text>
        <el-select v-else v-model="selectedLevel" class="selector2" placeholder='请选择关卡'>
            <el-option v-for="(value, key) in levelDesc[selectedLevelType]" :key="key" :value="key">
                <span class="level-key">{{ key }}</span>
                <span class="level-description">{{ value }}</span> <!--这里的value是for那个不是:value-->
            </el-option>
        </el-select>
        <el-text v-if="selectedLevelType && selectedLevel" class="ml"><b>关卡描述：</b>{{levelDesc[selectedLevelType][selectedLevel]}}</el-text>
    </div>
</template>
<script>
import axios from 'axios';
export default {
    data() {
        return {
            levelDesc: {},
            levelCodes: {},
            selectedLevelType: '',
            selectedLevel: ''
        }
    },
    inject: ['config'],
    methods: {
        async getLevelDesc() {
            try {
                const response = await axios.get(this.config.serverURL + '/getLevelDesc');
                this.levelDesc = response.data;
            } catch (error) {
                console.error('获取关卡信息失败:', error)
            }
        },
        async getLevelCodes() {
            try {
                const response = await axios.get(this.config.serverURL + '/getAllLevels');
                this.levelCodes = response.data;
            } catch (error) {
                console.error('获取关卡代码失败:', error)
            }
        }
    },
    mounted() {
        this.getLevelDesc();
        this.getLevelCodes();
    },
    watch:{
        selectedLevel(newVal) {
            let code = this.levelCodes[this.selectedLevelType][newVal];
            this.$emit('code', code);
        }
    }
}
</script>
<style scoped>
.main {
    margin-bottom: 15px;
}
.selector {
    width: 140px;
    padding: 0 5px;
}
.selector2 {
    width: 220px;
    padding: 0 5px;
}
.ml {
    margin-left: 5px;
}
.level-key {
    float: left;
}
.level-description {
    float: right;
    font-size: 11px; /* 小字 */
}
.levelDesc { /* abandoned */
    font-size: 16px;
}
</style>