<template>
    <div class="main">
        <el-text>选择主题：</el-text>
        <el-select v-model="selectedLevelType" class="selector" placeholder='请选择主题'>
            <el-option v-for="(value, key) in levelTypeList" :key="key" :value="key">
                {{ value }}
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
        <span v-if="selectedLevelType && selectedLevel">
            <el-text class="ml"><b>关卡描述：</b>{{levelDesc[selectedLevelType][selectedLevel]}}&nbsp;</el-text>
            <el-button circle icon="Histogram" title="查看排行榜" @click="viewScoreboard"/>
        </span>
    </div>
</template>
<script>
import axios from 'axios';
import { ElMessage } from 'element-plus';
import { Histogram } from "@element-plus/icons-vue";
export default {
    data() {
        return {
            levelDesc: {},
            levelCodes: {},
            levelTypeList: {},
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
                console.error('获取关卡信息失败:', error);
            }
        },
        async getLevelTypeList() {
            try {
                const response = await axios.get(this.config.serverURL + '/getLevelTypeList');
                this.levelTypeList = response.data;
            } catch (error) {
                console.error('获取关卡信息失败:', error);
            }
        },
        async getLevelCodes() {
            try {
                const response = await axios.get(this.config.serverURL + '/getAllLevels');
                this.levelCodes = response.data;
            } catch (error) {
                console.error('获取关卡代码失败:', error);
                ElMessage({
                    message: '获取数据失败,请检查网络',
                    type: 'error',
                    duration: 3000,
                    showClose: true
                });
            }
        },
        viewScoreboard() {
            const url = `/scoreboard?level=${this.selectedLevel}&levelType=${this.selectedLevelType}`;
            window.open(url, "_blank");
        }
    },
    mounted() {
        this.getLevelDesc();
        this.getLevelTypeList();
        this.getLevelCodes();
    },
    watch:{
        selectedLevelType(newVal) {
            this.selectedLevel = '';
            this.$emit('levelType', newVal);
        },
        selectedLevel(newVal) {
            let code = '尚未选择关卡。';
            if(newVal) {
                code = this.levelCodes[this.selectedLevelType][newVal];
            }
            this.$emit('code', code);
            this.$emit('level', newVal);
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
    font-size: 11px; 
}
</style>