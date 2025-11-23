# Brunn-Minkowski 不等式：理论与应用

本项目采用 [![CC BY-NC-SA Logo](https://i.creativecommons.org/l/by-nc-sa/4.0/80x15.png) CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/deed.en) 协议。内容同步发布在 ![loco](https://static.zhihu.com/heifetz/favicon.ico){ width=16; } [知乎](https://zhuanlan.zhihu.com/p/1973423321602348153) 平台。

这份笔记自笔者在山东大学数学学院 2025 暑期课程 [Brunn-Minkowski 不等式：理论与应用](https://www.math.sdu.edu.cn/info/1020/20825.htm) 》中的笔记；
课程主讲为[叶德平](https://www.math.mun.ca/~depingy/)老师, 整体纲举目张、深入浅出, 同时清晰易懂, 大概只需要读者有基本的实分析基础。
另外, 课中很多证明也是精华所在, 其结果、思想、工具都是凸几何领域的核心, 也都可以用于其它相关结论。

> ***摘要*** : 在数学理论与实际应用中, 对函数或集合施加凸性条件往往是关键前提, 因为凸函数与凸集合不仅具备丰富的优良性质, 还蕴含边界正则性、可微性等核心信息。Brunn-Minkowski 理论作为专注于凸体研究的数学领域, 系统整合了凸体的代数结构、几何特性与分析性质。其理论根基源于体积与凸体 Minkowski 加法的深度结合, 由此衍生的Brunn-Minkowski不等式及对应的变分公式, 推动了一系列里程碑式成果的诞生, 如Minkowski 不等式、Minkowski 问题等。本次课程将聚焦Brunn-Minkowski 理论的核心：Brunn-Minkowski 不等式, 将从不等式的严格证明出发, 深入探讨其在几何分析、泛函不等式等领域的经典应用, 并延伸至若干在实际问题中具有重要价值的关联不等式, 揭示凸体理论的跨学科应用潜力。

![poster](figures/poster.jpg)

笔记的六章内容安排如下：

+ [第一章](sections/section1.tex): 引入、 Brunn-Minkowski 不等式的等定义, 两种证明；
+ [第二章](sections/section2.tex): BM 不等式的泛函形式：Prékopa–Leindler 不等式和 Borell-Brascamp-Lieb 不等式, 以及最优传输的视角；
+ [第三章](sections/section3.tex): Steiner 对称化；
+ [第四章](sections/section4.tex): 混合体积、Minkowski 第一不等式、混合体积的变分公式；
+ [第五章](sections/section5.tex): Minkowski 问题的解决；
+ [第六章](sections/section6.tex): Blaschke–Santaló 不等式和仿射等周不等式。

![outline](figures/outline.png)



当然, Brunn-Minkowski 理论涉及的内容很多, 不仅有凸几何、微分几何、泛函、最优传输, 还可以推广到非常丰富的应用中 (如群论、环论、流形等等), 这门课程可以说是只介绍了最基础也最精华的一些部分。关于更多的内容, 读者可以去阅读相关教材, 笔者参考到的有

+ Schneider, R. (2013). *Convex bodies: the Brunn–Minkowski theory*(Vol. 151). Cambridge university press.
+ Gruber, P. M. (2007). *Convex and discrete geometry*. Berlin, Heidelberg: Springer Berlin Heidelberg.
+ Böröczky, K. J., Figalli, A., & Ramos, J. P. (2025).*Isoperimetric inequalities, Brunn-Minkowski theory and Minkowski type Monge-Ampère equations on the sphere*. <https://users.renyi.hu/~carlos/Brunn-Minkowski-Book-2026-06-06.pdf>

以及 Gruber 的一篇经典综述, Gardner, R. (2002).*The brunn-minkowski inequality*. Bulletin of the American mathematical society,39(3), 355-405。

本项目使用了 [ElegantBook](https://github.com/ElegantLaTeX/ElegantBook) 模板。