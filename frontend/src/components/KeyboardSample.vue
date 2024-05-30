<template>
  <div>
    <el-input v-model='password' style="width:300px;" @focus="showDialog"></el-input>
    <el-input v-model='password2' style="width:300px;" @focus="showDialog2"></el-input>
    <VirtualKeyboard v-show="isShowFirst" 
    :layout="layout" 
    @onChange="onChange" 
    @onKeyPress="onKeyPress" 
    keyboardClass="myBaseClass" />
    <VirtualKeyboard 
    v-show="!isShowFirst" 
    @onChange="onChange2" 
    @onKeyPress="onKeyPress2" 
    keyboardClass="myBaseClass2" />
  </div>
</template>
<script>
import VirtualKeyboard from './VirtualKeyboard.vue'
export default {
  components: {
    VirtualKeyboard
  },
  data() {
    return {
      password:undefined,
      password2:undefined,
      isShowFirst:true,
      layout:{
        'default': [
          "1 2 3 4",
          "5 6 7 8",
          '{bksp} 9 0 {enter}',
        ],
      },
    }
  },
 methods: {
    showDialog(){
      this.isShowFirst = true;
    },
    showDialog2(){
      this.isShowFirst = false;
    },
    onChange2(input) {
      // input 是当前点击按钮的值
        console.log(input)
        this.password2 = input
     },

    onKeyPress2(button) {
      if (button == "{enter}") {
      	// 如果按确认键的相应操作
        console.log(111)
      }
      if (button == "{bksp}") {
       // 删除键的相应操作
        console.log(222)
      }
    },
    onChange(input) {
      // input 是当前点击按钮的值
        console.log(input)
        this.password = input
     },

    onKeyPress(button) {
      if (button == "{enter}") {
      	// 如果按确认键的相应操作
        console.log(111)
      }
      if (button == "{bksp}") {
       // 删除键的相应操作
        console.log(222)
      }
    },
  }
}
</script>