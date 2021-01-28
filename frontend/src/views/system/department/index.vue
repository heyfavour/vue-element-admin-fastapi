<template>
  <div class="app-container">
    <el-form :inline="true">
      <!--      <el-form-item label="部门名称">-->
      <!--        <el-input-->
      <!--          v-model="queryParams.deptName"-->
      <!--          placeholder="请输入部门名称"-->
      <!--          clearable-->
      <!--          size="small"-->
      <!--          @keyup.enter.native="handleQuery"-->
      <!--        />-->
      <!--      </el-form-item>-->
      <!--      <el-form-item label="状态">-->
      <!--        <el-select v-model="queryParams.status" placeholder="部门状态" clearable size="small">-->
      <!--          <el-option v-for="dict in statusOptions" :key="dict.dictValue" :label="dict.dictLabel" :value="dict.dictValue" />-->
      <!--        </el-select>-->
      <!--      </el-form-item>-->
      <el-form-item>
        <el-button class="filter-item" type="primary" icon="el-icon-search" size="mini" @click="handleQuery">搜索
        </el-button>
        <el-button class="filter-item" type="primary" icon="el-icon-plus" size="mini" @click="handleAdd">新增</el-button>
      </el-form-item>
    </el-form>

    <el-table
      v-loading="loading"
      :data="deptList"
      row-key="id"
      default-expand-all
      :tree-props="{children: 'children', hasChildren: 'hasChildren'}"
    >
      <el-table-column prop="name" label="部门名称" width="260" />
      <el-table-column prop="code" label="部门代码" width="260" />
      <el-table-column prop="order" label="排序" width="200" />
      <el-table-column label="操作" align="center" class-name="small-padding fixed-width">
        <template slot-scope="scope">
          <el-button size="mini" type="text" icon="el-icon-edit" @click="handleUpdate(scope.row)">修改</el-button>
          <el-button size="mini" type="text" icon="el-icon-plus" @click="handleAdd(scope.row)">新增</el-button>
          <el-button
            v-if="scope.row.parent_id !== -1"
            size="mini"
            type="text"
            icon="el-icon-delete"
            @click="handleDelete(scope.row)"
          >删除
          </el-button>
        </template>
      </el-table-column>
    </el-table>

    <!-- 添加或修改部门对话框 -->
    <el-dialog :title="title" :visible.sync="open" width="600px" append-to-body>
      <el-form ref="form" :model="form" :rules="rules" label-width="80px">
        <el-row>
          <el-col v-if="form.parent_id !== null" :span="24">
            <el-form-item label="上级部门" prop="parent_id">
              <treeselect
                v-model="form.parent_id"
                :options="deptOptions"
                :normalizer="normalizer"
                placeholder="选择上级部门"
              />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="部门代码" prop="code">
              <el-input v-model="form.code" placeholder="请输入部门代码" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="部门名称" prop="name">
              <el-input v-model="form.name" placeholder="请输入部门名称" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="显示排序" prop="order">
              <el-input-number v-model="form.order" controls-position="right" :min="0" />
            </el-form-item>
          </el-col>
          <el-col :span="12">
            <el-form-item label="部门状态">
              <el-radio-group v-model="form.status">
                <el-radio :label="true">正常</el-radio>
                <el-radio :label="false">停用</el-radio>
              </el-radio-group>
            </el-form-item>
          </el-col>
        </el-row>
      </el-form>
      <div slot="footer" class="dialog-footer">
        <el-button type="primary" @click="submitForm">确 定</el-button>
        <el-button @click="cancel">取 消</el-button>
      </div>
    </el-dialog>
  </div>
</template>

<script>
import { listDept, getDept, delDept, addDept, updateDept, listDeptExcludeChild } from '@/api/system/dept'
import Treeselect from '@riophae/vue-treeselect'
import '@riophae/vue-treeselect/dist/vue-treeselect.css'

export default {
  name: 'Department',
  components: { Treeselect },
  data() {
    return {
      // 遮罩层
      loading: true,
      // 表格树数据
      deptList: [],
      // 部门树选项
      deptOptions: [],
      // 弹出层标题
      title: '',
      // 是否显示弹出层
      open: false,
      // 状态数据字典
      statusOptions: [],
      // 查询参数
      queryParams: {
        name: undefined,
        status: undefined
      },
      // 表单参数
      form: {},
      // 表单校验
      rules: {
        parent_id: [
          { required: true, message: '上级部门不能为空', trigger: 'blur' }
        ],
        code: [
          { required: true, message: '部门名称不能为空', trigger: 'blur' }
        ],
        order: [
          { required: true, message: '部门顺序不能为空', trigger: 'blur' }
        ]
      }
    }
  },
  created() {
    this.getList()
  },
  methods: {
    /** 查询部门列表 */
    getList() {
      this.loading = true
      listDept(this.queryParams).then(response => {
        this.deptList = response.data
        this.loading = false
      })
    },
    /** 转换部门数据结构 */
    normalizer(node) {
      if (node.children && !node.children.length) {
        delete node.children
      }
      return {
        id: node.id,
        label: node.name,
        children: node.children
      }
    },
    // 取消按钮
    cancel() {
      this.open = false
      this.reset()
    },
    // 表单重置
    reset() {
      this.form = {
        id: undefined,
        parent_id: undefined,
        name: undefined,
        order: undefined,
        status: '0'
      }
      this.resetForm('form')
    },
    /** 搜索按钮操作 */
    handleQuery() {
      this.getList()
    },
    /** 新增按钮操作 */
    handleAdd(row) {
      this.reset()
      if (row !== undefined) {
        this.form.parent_id = row.id
      }
      this.open = true
      this.title = '添加部门'
      listDept().then(response => {
        this.deptOptions = response.data
      })
    },
    /** 修改按钮操作 */
    handleUpdate(row) {
      this.reset()
      getDept(row.id).then(response => {
        this.form = response.data
        this.open = true
        this.title = '修改部门'
      })
      listDeptExcludeChild(row.id).then(response => {
        this.deptOptions = response.data
      })
    },
    /** 提交按钮 */
    submitForm: function() {
      this.$refs['form'].validate(valid => {
        if (valid) {
          if (this.form.id !== undefined) {
            updateDept(this.form).then(response => {
              if (response.code === 20000) {
                this.msgSuccess(response.message)
                this.open = false
                this.getList()
              }
            })
          } else {
            addDept(this.form).then(response => {
              if (response.code === 20000) {
                this.msgSuccess(response.message)
                this.open = false
                this.getList()
              }
            })
          }
        }
      })
    },
    /** 删除按钮操作 */
    handleDelete(row) {
      this.$confirm('是否确认删除名称为"' + row.name + '"的数据项?', '警告', {
        confirmButtonText: '确定',
        cancelButtonText: '取消',
        type: 'warning'
      }).then(function() {
        return delDept(row.id)
      }).then(() => {
        this.getList()
        this.msgSuccess('删除成功')
      }).catch(function() {
      })
    }
  }
}
</script>
