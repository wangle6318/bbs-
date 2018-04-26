$(function(){
	var E = window.wangEditor
    var editor = new E('#editor')
    var $text1 = $('#text1')
    //配置菜单    
    editor.customConfig.menus = [
	 	'bold', // 粗体
	 	'fontSize', // 字号
	 	'fontName', // 字体
	 	'italic', // 斜体
	 	'foreColor', // 文字颜色
	 	'backColor', // 背景颜色
	 	'justify', // 对齐方式
	 	'quote', // 引用
	 	'emoticon', // 表情
	 	'image', // 插入图片
	 	'table', // 表格
	 	'undo', // 撤销
	 	'redo' // 重复
 	]
    
    // 关闭粘贴样式的过滤
    editor.customConfig.pasteFilterStyle = false
    
    editor.customConfig.colors = [
        '#000000',
        '#ffffff',
        '#eeece0',
        '#1c487f',
        '#c24f4a',
        '#99ff00',
        '#ffff00',
        '#9933cc',
        '#ff9900',
        '#ff0000',
        '#6699ff',
        '#660000',
        '#990000',
        '#11ccff',
        '#cc55bb',
        '#00ffff'
    ]
    
    //配置表情
    editor.customConfig.emotions = [
        {
            // tab 的标题
            title: '默认',
            // type -> 'emoji' / 'image'
            type: 'image',
            // content -> 数组
            content: [
                {
                    alt: '[坏笑]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/50/pcmoren_huaixiao_org.png'
                },
                {
                    alt: '[舔屏]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/40/pcmoren_tian_org.png'
                },
                {
                    alt: '[污]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/3c/pcmoren_wu_org.png'
                },
                {
                    alt: '[允悲]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/2c/moren_yunbei_org.png'
                },
                {
                    alt: '[笑而不语]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/3a/moren_xiaoerbuyu_org.png'
                },
                {
                    alt: '[费解]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/3c/moren_feijie_org.png'
                },
                {
                    alt: '[憧憬]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/37/moren_chongjing_org.png'
                },
                {
                    alt: '[并不简单]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/fc/moren_bbjdnew_org.png'
                },
                {
                    alt: '[微笑]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/5c/huanglianwx_org.gif'
                },
                {
                    alt: '[酷]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/8a/pcmoren_cool2017_org.png'
                },
                {
                    alt: '[嘻嘻]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/0b/tootha_org.gif'
                },
                {
                    alt: '[哈哈]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/6a/laugh.gif'
                },
                {
                    alt: '[可爱]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/14/tza_org.gif'
                },
                {
                    alt: '[可怜]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/af/kl_org.gif'
                },
                {
                    alt: '[挖鼻]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/0b/wabi_org.gif'
                },
                {
                    alt: '[吃惊]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/f4/cj_org.gif'
                },
                {
                    alt: '[害羞]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/6e/shamea_org.gif'
                },
                {
                    alt: '[闭嘴]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/29/bz_org.gif'
                },
                {
                    alt: '[鄙视]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/71/bs2_org.gif'
                },
                {
                    alt: '[爱你]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/6d/lovea_org.gif'
                },
                {
                    alt: '[流泪]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/9d/sada_org.gif'
                },
                {
                    alt: '[偷笑]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/19/heia_org.gif'
                },
                {
                    alt: '[亲亲]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/8f/qq_org.gif'
                },
                {
                    alt: '[生病]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/b6/sb_org.gif'
                },
                {
                    alt: '[白眼]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/d9/landeln_org.gif'
                },
                {
                    alt: '[嘘]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/a6/x_org.gif'
                },
                {
                    alt: '[委屈]',
                    src: 'http://img.t.sinajs.cn/t4/appstyle/expression/ext/normal/73/wq_org.gif'
                }
            ]
        },
        {
            // tab 的标题
            title: 'emoji',
            // type -> 'emoji' / 'image'
            type: 'emoji',
            // content -> 数组
            content: ['😀','😁','😂','😄','😊','😋','😍','😘','😥',
            		'😜','😝','🙃','😭','😱','😡','👌','👍','🐷','❤',
            		'😋','🙄','😐','😣','😥','😖','🤑','😤','😩','😢']
        }
    ]
    
	//配置字体

	editor.customConfig.fontNames = [
		'楷体',
		'黑体',
        '宋体',
        '仿宋',
        '微软雅黑',
        'Arial',
        'Tahoma',
        'Verdana',
        'times new roman'
    ]
    
    // 下面两个配置，使用其中一个即可显示“上传图片”的tab。但是两者不要同时使用！！！
    editor.customConfig.uploadImgShowBase64 = true   // 使用 base64 保存图片
    //editor.customConfig.uploadImgServer = '/upload'  // 上传图片到服务器
    //editor.customConfig.uploadFileName = 'yourFileName'
    
    editor.customConfig.onchange = function (html) {
        // 监控变化，同步更新到 textarea
        $text1.val(html);
    }
    editor.create()
        // 初始化 textarea 的值
    $text1.val(editor.txt.html())
  
       	
})