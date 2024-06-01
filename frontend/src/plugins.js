// 全局函数
import { ElMessage } from 'element-plus'

export default {
  install(app, options) {
    app.config.globalProperties.$message = (params) => {
      ElMessage({
        message: params.message || '获取数据失败,请检查网络',
        type: params.type || 'error',
        duration: params.duration || 3000,
        showClose: params.showClose || true,
      })
    }
  }
}