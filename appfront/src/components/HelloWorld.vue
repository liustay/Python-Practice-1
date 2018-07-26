<template>
  <div class="hello">
    <el-form :inline="true" class="demo-form-inline">
      <el-form-item label="书名">
        <el-input v-model="bookName"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="addBook">添加</el-button>
      </el-form-item>
    </el-form>
    <el-table
      :data="data"
      style="width: 100%">
      <el-table-column
        prop="pk"
        label="编号"
        width="180">
      </el-table-column>
      <el-table-column
        prop="fields.book_name"
        label="书名"
        width="180">
      </el-table-column>
      <el-table-column
        prop="fields.add_time"
        label="添加时间">
      </el-table-column>
    </el-table>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      data: [],
      bookName: ''
    }
  },
  mounted(){
    this.getData()
  },
  methods: {
    getData(){
      this.$http.get('http://127.0.0.1:8000/api/show_books').then(res=>{
        this.data = res.data.list
      })
    },
    addBook(){
      this.$http.get('http://127.0.0.1:8000/api/add_book?book_name='+this.bookName).then(res=>{
        this.$message(res.data.msg)
        this.getData()
      })
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.hello {
  max-width: 700px
}
</style>
