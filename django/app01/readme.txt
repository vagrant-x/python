python3 manage.py runserver 0.0.0.0:8000

======== 单表实例 =================================================================================

    添加：
        方式一：实例化对象模型，调用 对象.save()
                book = models.Book(title="菜鸟教程", price="30", publish="菜鸟出版社", pub_date="2021-8-8")
                book.save()
        方式二：通过ORM提供的objects 提供的create方法
                book = models.Book.objects.create(title="菜鸟教程2", price="40", publish="菜鸟出版社", pub_date="2021-9-9")

    查找
        all(): 查询所有内容：models.Book.objects.all()
        filter(): 查询符合条件的数据，id用pk
        exclude(): 查询不符合条件的数据
        get(): 返回一个模型类对象，如果对象超过一个或没有都会抛出异常
        order_by: 用于对查询结果的排序
            a.参数字段需要加引号
            b.降序为在字段前面加符号 -
        reverse(): 查询结果进行反转
        count(): 查询数据的数量，返回整数
        first(): 返回第一条数据，类型为模型类的对象
        last(): 返回最后一条数据， 类型为模型类的对象
        exists(): 判断查询结果 QuerySet 列表是否有数据，True/False
            注意：判断的数据类型只能是 QuerySet 类型数据，不能为整型或是模型类的对象
        values(): 查询部分字段数据，返回 QuerySet 类型，里面是可迭代字段对象，key是字段，value是数据
        values_list(): 查询部分字段数据，返回 QuerySet 类型, 里面是一个个元组，元组里面放的是查询字段对应的数据
        distinct(): 对数据去重，返回 QuerySet 数据。对模型类对象去重没意义，每一个对象都不同；一般联合 values 或 values_list 使用

        filter() 方法基于双下划线的模糊查询（exclude 方法同理）：filter 中运算符号只能使用等于号 = ，不能使用大于号 > ，小于号 < ，等等其他符号。
            print("=====> __in 用于读取区间，= 号后面为列表")
            books = models.Book.objects.filter(price__in=[30, 40])
            print(books)
            print("=====> __gt 大于号 ，= 号后面为数字")
            books = models.Book.objects.filter(price__gt=49)
            print(books)
            print("=====> __gte 大于等于，= 号后面为数字")
            books = models.Book.objects.filter(price__gte=50)
            print(books)
            print("=====> __lt 小于，=号后面为数字")
            books = models.Book.objects.filter(price__lt=31)
            print(books)
            print("=====> __lte 小于等于，= 号后面为数字")
            books = models.Book.objects.filter(price__lte=30)
            print(books)
            print("=====> __range 在 ... 之间，左闭右闭区间，= 号后面为两个元素的列表")
            books = models.Book.objects.filter(price__range=[30, 40])
            print(books)
            print("=====> __contains 包含，= 号后面为字符串")
            books = models.Book.objects.filter(publish__contains='3')
            print(books)
            print("=====> __icontains 不区分大小写的包含，= 号后面为字符串")
            books = models.Book.objects.filter(publish__icontains='a')
            print(books)
            print("=====> __startswith 以指定字符开头，= 号后面为字符串")
            books = models.Book.objects.filter(publish__startswith='a')
            print(books)
            print("=====> __endswith 以指定字符结尾，= 号后面为字符串")
            books = models.Book.objects.filter(publish__endswith='3A')
            print(books)
            print("=====> __year 是 DateField 数据类型的年份，= 号后面为数字")
            books = models.Book.objects.filter(pub_date__year=2021)
            print(books)
            print("=====> __month 是DateField 数据类型的月份，= 号后面为数字")
            books = models.Book.objects.filter(pub_date__month=10)
            print(books)
            print("=====> __day 是DateField 数据类型的天数，= 号后面为数字")
            books = models.Book.objects.filter(pub_date__day=9)
            print(books)

    删除
        方式一：使用模型类对象  对象.delete(), 返回值：元组，第一个元素为受影响的行数， 如 (2, {'app01.Book': 2})
                models.Book.objects.filter(pk=5).first().delete()
        方式二：使用 QuerySet 数据类型.delete() （推荐）, 返回值：元组，第一个元素为受影响的行数， 如 (2, {'app01.Book': 2})
                models.Book.objects.filter(pk__in=[3, 4]).delete()
            注意：
                a. Django 删除数据时，会模仿 SQL约束 ON DELETE CASCADE 的行为，也就是删除一个对象时也会删除与它相关联的外键对象。
                b. delete() 方法是 QuerySet 数据类型的方法，但并不适用于 Manager 本身。也就是想要删除所有数据，不能不写 all。

    更新
        方式一：模型类对象.属性 = 更改属性值
                模型类对象.save()
                返回值：编辑的模型类对象
        方式二：QuerySet 类型数据.update(字段名=更新的数据) （推荐）
                返回值：整数，受影响的行数


======== 多表实例 =================================================================================
添加
    一对多（外键 ForeignKye）
        方式一：传对象的形式，返回值的数据类型是对象，如书籍对象
                book = app02_models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2020-10-10", publish=pub_obj)

        方式二：传对象id的形式；一对多中，设置外键属性的类（多的表）中，mysql中显示的字段是：外键属性名_id; 返回值是数据类型对象
                book = app02_models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2020-10-10", publish_id=pub_obj_id)

    多对多（ManyToManyField）
        方式一：传递对象形式，无返回值
                 book.authors.add(author1, author2)
        方式二：传对象id形式，无返回值
                book.authors.add(author.pk)


    关联管理器（对象调用）
        前提：
            多对多（双向均有关联管理器）
            一对多（只有多的那个类的对象有关联管理器，即反向才有）
        语法格式：
            正向：属性名
            反向：小写类名加_set
        注意：一对多只能反向
        常用方法：
            add(): 对于多对多，把指定的模型对象添加到关联对象集（关系表）中
                注意：add() 在一对多(即外键)中，只能传对象（ *QuerySet数据类型），不能传 id（*[id表]）。
                正向: 属性名
                    方式一：传对象
                        book_obj.authors.add(*author_list)
                     方式二：传对象 id
                        book_obj.authors.add(*[1, 2, 3])
                反向: 小写表名_set
                    author.book_set.add(book_obj)

            create(): 创建一个新的对象，并同时将它添加到关联对象集中
                    返回值：新创建的对象
                    book = author.book_set.create(title="吸星大法", price=300, pub_date="1999-9-9", publish=pub_obj)

            remove()：从关联对象集中移除执行的模型对象
                    对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在，无返回值。
                    author.book_set.remove(book)

            clear(): 从关联对象集中移除一切对象，删除关联，不会删除对象
                    对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在；无返回值。
                    book.authors.clear()


查询
    基于对象的跨表查询
        正向：属性名称
        反向：小写类名_set

    一对多
        正向：
            注意：多.一.属性
            city = book.publish.city  # 多.一.属性
        反向：
            对象.小写类名_set  : 可以跳转到关联的表
            q_set = pub.book_set.all()  # 对象.小写类名_set.all()

    一对一
        正向：
            对象.属性: 可以跳转到关联的表
            tel = author.au_detail.tel
        反向：
            对象.小写类名 （不用加 _set）可以跳转到关联的表
            name = authorDetail.author.name

    多对多
        正向：
            对象.属性 ： 可以跳转到关联的表
            authors = book.authors.all()
        反向：
            books = author.book_set.all()


基于双下划线的跨表查询
    正向：
        属性名称__跨表的属性名称
    反向：
        小写类名__跨表的属性名称

    一对多
        正向：
            # publish__name  属性名称__跨表的属性名称
            res = app02_models.Book.objects.filter(publish__name="华山出版社").values_list("title", "price")
        反向
            # book_name  小写类名__跨表的属性名称
            res = app02_models.Publish.objects.filter(name="华山出版社").values_list("book__title", "book__price")

    多对多
        查询任我行出过的所有书籍的名字。
        正向：
            通过 属性名称__跨表的属性名称(authors__name) 跨表获取数据：
            res = models.Book.objects.filter(authors__name="任我行").values_list("title")
        反向：
            通过 小写类名__跨表的属性名称（book__title） 跨表获取数据：
            res = models.Author.objects.filter(name="任我行").values_list("book__title")

    一对一
        查询任我行的手机号。
        正向：
            通过 属性名称__跨表的属性名称 跨表获取数据
            res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")
        反向：
            通过 小写类名__跨表的属性名称 跨表获取数据
            res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")


----------------------------- 详细版本 ----------------------------------
添加
    一对多（外键 ForeignKye）
        方式一：传对象的形式，返回值的数据类型是对象，如书籍对象
                def add_book(request):
                    print("=======================>")
                    # 获取出版社对象
                    pub_obj = app02_models.Publish.objects.filter(pk=1).first()
                    # 给书籍的 publish属性传传 出版社对象
                    book = app02_models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2020-10-10", publish=pub_obj)
                    print(book, type(book))
                    return HttpResponse("app02_test 添加")

        方式二：传对象id的形式；一对多中，设置外键属性的类（多的表）中，mysql中显示的字段是：外键属性名_id; 返回值是数据类型对象
                def add_book(request):
                    print("=======================>")
                    # 获取出版社对象
                    pub_obj = app02_models.Publish.objects.filter(pk=1).first()
                    # 获取出版社对象的 id
                    pk = pub_obj.pk
                    # 给书籍的 publish属性传传 出版社对象的 id
                    book = app02_models.Book.objects.create(title="菜鸟教程", price=200, pub_date="2020-10-10", publish_id=pk)
                    print(book, type(book))
                    return HttpResponse("app02_test 添加")

    多对多（ManyToManyField）
        方式一：传递对象形式，无返回值
                def add_book(request):
                    print("=======================>")
                    # 获取作者对象
                    chong =  app02_models.Author.objects.filter(name="令狐冲").first()
                    ying = app02_models.Author.objects.filter(name="任盈盈").first()
                    # 获取书籍对象
                    book = app02_models.Book.objects.filter(title="菜鸟教程").first()
                    # 给书籍对象的 author 属性用 add 方法传作者对象
                    book.authors.add(chong, ying)
                    return HttpResponse(book)
        方式二：传对象id形式，无返回值
                def add_book(request):
                    print("=======================>")
                    # 获取作者对象
                    chong =  app02_models.Author.objects.filter(name="令狐冲").first()
                    # 获取书籍对象
                    book = app02_models.Book.objects.filter(title="菜鸟教程2").first()
                    # 给书籍对象的 author 属性用 add 方法传作者对象的 id
                    book.authors.add(chong.pk)
                    return HttpResponse(book)


    关联管理器（对象调用）
        前提：
            多对多（双向均有关联管理器）
            一对多（只有多的那个类的对象有关联管理器，即反向才有）
        语法格式：
            正向：属性名
            反向：小写类名加_set
        注意：一对多只能反向
        常用方法：
            add(): 对于多对多，把指定的模型对象添加到关联对象集（关系表）中
                注意：add() 在一对多(即外键)中，只能传对象（ *QuerySet数据类型），不能传 id（*[id表]）。
                正向: 属性名
                    方式一：传对象
                    方式二：传对象 id
                    def add_book(reuqest):
                        book_obj = app02_models.Book.objects.get(id=1)
                        author_list = app02_models.Author.objects.filter(id__gte=2)
                        # 方法一： 传递对象
                        book_obj.authors.add(*author_list)
                        # 方法二：传递对象id
                        book_obj.authors.add(*[1, 2, 3])
                反向: 小写表名_set
                    def add_book(reuqest):
                        author = app02_models.Author.objects.filter(pk=2).first()
                        book_obj = app02_models.Book.objects.get(pk=1)
                        # 小写表名_set
                        author.book_set.add(book_obj)
                        return HttpResponse("OK")

            create(): 创建一个新的对象，并同时将它添加到关联对象集中
                    返回值：新创建的对象
                    def add_book(reuqest):
                        pub = app02_models.Publish.objects.filter(name="明教出版社").first()
                        author = app02_models.Author.objects.filter(name="任我行").first()
                        # 使用 create方法： 插件书，关联出版社和作者
                        book = author.book_set.create(title="吸星大法", price=300, pub_date="1999-9-9", publish=pub)
                        return HttpResponse(book)

            remove()：从关联对象集中移除执行的模型对象
                    对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在，无返回值。
                    def add_book(reuqest):
                        book = app02_models.Book.objects.get(pk=1)
                        author = app02_models.Author.objects.get(pk=2)
                        author.book_set.remove(book)
                        return HttpResponse("ok")
            clear(): 从关联对象集中移除一切对象，删除关联，不会删除对象
                    对于 ForeignKey 对象，这个方法仅在 null=True（可以为空）时存在；无返回值。
                    def add_book(reuqest):
                        book = app02_models.Book.objects.get(pk=3)
                        book.authors.clear()
                        return HttpResponse("ok")


查询
    基于对象的跨表查询
        正向：属性名称
        反向：小写类名_set

    一对多
        正向：
            注意：多.一.属性
            def add_book(reuqest):
                book = app02_models.Book.objects.filter(pk=1).first()
                city = book.publish.city  # 多.一.属性
                return HttpResponse(city)
        反向：
            对象.小写类名_set  : 可以跳转到关联的表
            def add_book(reuqest):
                pub = app02_models.Publish.objects.filter(name="华山出版社").first()
                q_set = pub.book_set.all()  # 对象.小写类名_set.all()
                for b in q_set:
                    print(b.title)
                return HttpResponse("ok")

    一对一
        正向：
            对象.属性: 可以跳转到关联的表
            def add_book(reuqest):
                author = app02_models.Author.objects.get(pk=1)
                tel = author.au_detail.tel
                return HttpResponse(tel)
        反向：
            对象.小写类名 （不用加 _set）可以跳转到关联的表
            def add_book(reuqest):
                ad = app02_models.AuthorDetail.objects.get(pk=1)
                name = ad.author.name
                return HttpResponse(name)

    多对多
        正向：
            对象.属性 ： 可以跳转到关联的表
            def add_book(request):
                book = app02_models.Book.objects.filter(title="菜鸟教程1").first()
                authors = book.authors.all()
                # 作者表里没有作者电话，因此再次通过对象.属性(i.au_detail)跳转到关联的表（作者详情表）。
                for a in authors:
                    print(a.name, a.au_detail.tel)
                return HttpResponse("ok")
        反向：
            def add_book(request):
                author = app02_models.Author.objects.filter(pk=2).first()
                books = author.book_set.all()
                for b in books:
                    print(b.title)
                return HttpResponse("ok")


基于双下划线的跨表查询
    正向：
        属性名称__跨表的属性名称
    反向：
        小写类名__跨表的属性名称

    一对多
        正向：
            def add_book(request):
                # publish__name  属性名称__跨表的属性名称
                res = app02_models.Book.objects.filter(publish__name="华山出版社").values_list("title", "price")
                return HttpResponse(res)
        反向
            def add_book(request):
                # book_name  小写类名__跨表的属性名称
                res = app02_models.Publish.objects.filter(name="华山出版社").values_list("book__title", "book__price")
                return HttpResponse(res)

    多对多
        查询任我行出过的所有书籍的名字。
        正向：
            通过 属性名称__跨表的属性名称(authors__name) 跨表获取数据：
            res = models.Book.objects.filter(authors__name="任我行").values_list("title")
        反向：
            通过 小写类名__跨表的属性名称（book__title） 跨表获取数据：
            res = models.Author.objects.filter(name="任我行").values_list("book__title")

    一对一
        查询任我行的手机号。
        正向：
            通过 属性名称__跨表的属性名称 跨表获取数据
            res = models.Author.objects.filter(name="任我行").values_list("au_detail__tel")
        反向：
            通过 小写类名__跨表的属性名称 跨表获取数据
            res = models.AuthorDetail.objects.filter(author__name="任我行").values_list("tel")








