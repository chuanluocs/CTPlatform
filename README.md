# CTPlatform: 面向可配置软件的测试用例生成平台

欢迎使用 CTPlatform，一个用于生成可配置软件测试用例集合的平台。您可以访问我们的在线项目网站 http://www.ctplatform.top，并在网站首页找到详细的使用教程。

## 项目概述
CTPlatform 是一个针对可配置软件的测试用例生成工具。通过输入与系统相关的信息，您可以有效地生成具有较小的2-wise覆盖阵列，以进行软件测试。这对于需要确保全面测试覆盖并尽量减少测试用例数量的可配置软件非常有用。

本项目分为两个主要部分：

+ 前端：使用了 Vue.js 框架开发。
+ 后端：采用 Flask 框架开发。

## 主要特点

+ **高效的测试用例生成：**CTPlatform 使用 [SamplingCA](https://github.com/chuanluocs/SamplingCA) 算法生成覆盖阵列。本存储库包含 [SamplingCA](https://github.com/chuanluocs/SamplingCA) 的副本，它已集成到后端。在原始 [SamplingCA](https://github.com/chuanluocs/SamplingCA) 实现中，PCA 生成实例的输入需要采用 [Dimacs](http://www.satcompetition.org/2011/format-benchmarks2011.html) 格式的 CNF 布尔公式建模。这种输入格式对人类来说不够友好。因此，我们提供了一种更用户友好的输入方式，详细信息请参阅 http://www.ctplatform.top 的教程第2部分，并已集成到后端代码中，与 [Dimacs](http://www.satcompetition.org/2011/format-benchmarks2011.html) 格式的转换器兼容。

+ **Vue 前端界面：**存储库还包含了一个 Vue 前端界面，可视化地与平台进行交互。

## 项目部署与运行

有关项目的部署和运行说明，请参阅 backend 和 frontend 文件夹下的 `README.md` 文件。这些文件包含了详细的部署和运行步骤，帮助您开始使用 CTPlatform。