<template>
  <div class="hello">

    <div style="margin-top: 15px;">
      <el-input placeholder="请输入内容" v-model="q" class="input-with-select">
        <el-button slot="append" icon="el-icon-search" @click="search"></el-button>
      </el-input>
    </div>

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
      <el-table-column
      fixed="right"
      label="操作"
      width="100">
        <template slot-scope="scope">
          <el-button @click="handleEdit(scope.row.pk, scope.row.fields.book_name)" type="text" size="small">编辑</el-button>
          <el-button @click="handleDel(scope.row.pk)" type="text" size="small">删除</el-button>
        </template>
      </el-table-column>
    </el-table>

    <el-form :inline="true" class="demo-form-inline">
      <el-form-item label="书名">
        <el-input v-model="bookName"></el-input>
      </el-form-item>
      <el-form-item>
        <el-button type="primary" @click="addBook">添加</el-button>
      </el-form-item>
    </el-form>

    <el-dialog title="编辑" :visible.sync="dialogFormVisible">
      <el-form>
        <el-form-item label="书名">
          <el-input v-model="newName"></el-input>
        </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button @click="dialogFormVisible = false">取 消</el-button>
        <el-button type="primary" @click="editSubmit">确 定</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
export default {
  name: 'HelloWorld',
  data () {
    return {
      data: [],
      bookName: '',
      q: '',
      newName: '',
      editId: null,
      dialogFormVisible: false
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
      this.$http.get('http://127.0.0.1:8000/api/add_book?book_name=' + this.bookName).then(res=>{
        this.$message(res.data.msg)
        this.getData()
      })
    },
    handleDel(e){
      console.log(e)
      this.$http.get('http://127.0.0.1:8000/api/del_book?id='+e).then(res=>{
        this.$message(res.data.msg)
        this.getData()
      })
    },
    handleEdit(id, e){
      this.dialogFormVisible = true
      this.editId = id
      this.newName = e
    },
    editSubmit(){
      if (this.newName == ''){
        this.$message('书名不能为空！')
        return
      }
      this.dialogFormVisible = false
      this.$http.get('http://127.0.0.1:8000/api/edit_book?id=' + this.editId + '&book_name=' + this.newName).then(res=>{
        this.$message(res.data.msg)
        this.getData()
      })
    },
    search(){
      console.log(this.q)
      this.$http.get('http://127.0.0.1:8000/api/search_books?q=' + this.q).then(res=>{
        this.data = res.data.list
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
.demo-form-inline {
  margin-top: 40px
}
</style>
