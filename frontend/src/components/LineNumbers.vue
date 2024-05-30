<template>
  <div class="line-numbers">
    <div v-for="n in numRows" :key="n" class="line-number">{{n}}</div>
  </div>
  
</template>

<script>
export default {
  props: {
    numRows: {
      type: Number,
      required: true
    }
  }
}
</script>

<style scoped>
.line-numbers {
  float: left;
  text-align: right;
  padding-right: 8px;
  padding-left: 8px;
  user-select: none; /* Prevent user selection of line numbers */
  color: #888;
}

.line-number {
  height: var(--line-height, 1.5em); /* Adjust line height to match your text area */
}
</style>
