# 知识摘要

##debug express:

>node-inspector  
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
    - block元素可以设置margin和padding属性。

5. inline与inlineblock的区别

- display:inline

    > - inline元素不会独占一行，多个相邻的行内元素会排列在同一行里，直到一行排列不下，才会新换一行，其宽度随元素的内容而变化。
    > - inline元素设置width,height属性无效。
    > - inline元素的margin和padding属性，水平方向的padding-left, padding-right, margin-left, margin-right都产生边距效果；但竖直方向的padding-top, padding-bottom, margin-top, margin-bottom不会产生边距效果。

- display:inline-block

    > - 简单来说就是将对象呈现为inline对象，但是对象的内容作为block对象呈现。之后的内联对象会被排列在同一行内。比如我们可以给一个link（a元素）inline-block属性值，使其既具有block的宽度高度特性又具有inline的同行特性。

##git的使用
git clone 下来，然后更改文件  
git init   
git add .  
git commit . -m "first commit"  
git remote add origin https://github.com/huige555551/crawler.git(或者用ssh：git@github.com:huige555551/knowledge.git)    如果出现fatal: remote origin already exists. 就先 git remote remove origin
git push -f origin master   (-f强推)
