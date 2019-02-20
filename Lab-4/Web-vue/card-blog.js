Vue.component('card-blog', {
    props: ["blog"],
    methods:{
        changeBGColor(blog){
          if (blog.bgColor === 'bg-light'){
            blog.bgColor = 'bg-dark'
            blog.textColor = 'text-light'
          } 
          else{
            blog.bgColor = 'bg-light'
            blog.textColor = 'text.dark'
          }
          
          console.log('change bg color')
        },
        showComment(blog){
          blog.showComment = !blog.showComment
          console.log('show comment')
        }
    },
    template: 
    `<div class="col-md-4">
    <div class="card my-3">
      <img :src="blog.image" class="card-img-top img-fluid" alt="..." />
      <div class="card-body">
        <h5 class="card-title">
          {{ blog.title }}
          <span class="badge badge-success ml-5">Likes: {{blog.likes}}</span>
        </h5>
        <p class="card-text">
          {{ blog.content }}<br />
          <small class="text-muted">Create By: {{blog.createBy}}</small>
          <small class="text-muted ml-5">Create Date: {{blog.createDate}}</small>
        </p>
        <button class="btn btn-success" @click="$emit('add-like')">I like this!</button>
        <button class="btn btn-info" @click.stop="showComment(blog)">Show comment...</button>
        <div class="card mt-2 text-dark" v-show="blog.showComment" v-for="comment in blog.comments">
          <div class="card-body" >
            <h6 class="card-title">Comment</h6>
            <p class="card-text">
                {{comment.text}}<br />
              <small class="text-muted">Create By: {{comment.createBy}}</small>
              <small class="text-muted ml-5">Create Date: {{blog.createDate}}</small>
            </p>
          </div>
        </div>
      </div>
    </div>
</div>
    `
});