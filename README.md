# 知识摘要

##debug express:
node-inspector
node --debug bin/www
或者 DEBUG=signupexpress:* —debug-brk ./bin/www 
mongoldb:
sudo su用最高权限打开
##CSS
1.  inline元素的margin和padding属性，水平方向的padding-left, padding-right, margin-left, margin-right都产生边距效果；但竖直方向的padding-top, padding-bottom, margin-top, margin-bottom不会产生边距效果。
2. text-align：center 让容器中的元素居中                        margin：0 auto； 让容器自己居中
3. overflow: hidden;
	vertical-align: top; 
4. display:block
    - block元素会独占一行，多个block元素会各自新起一行。默认情况下，block元素宽度自动填满其父元素宽度。
    - block元素可以设置width,height属性。块级元素即使设置了宽度,仍然是独占一行。
    - block元素可以设置margin和padding属性。# knowledge