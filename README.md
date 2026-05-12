# ⚡ SharpInput v3.0

<p align="center">
  <strong>AI Input Compiler — 把"烂问题"变成"好 Prompt"</strong>
</p>

<p align="center">
  <a href="https://github.com/gaoyechen/SharpInput/stargazers"><img src="https://img.shields.io/github/stars/gaoyechen/SharpInput?style=social" alt="Stars"></a>
  <a href="https://github.com/gaoyechen/SharpInput/network/members"><img src="https://img.shields.io/github/forks/gaoyechen/SharpInput?style=social" alt="Forks"></a>
  <a href="https://github.com/gaoyechen/SharpInput/issues"><img src="https://img.shields.io/github/issues/gaoyechen/SharpInput" alt="Issues"></a>
  <a href="https://github.com/gaoyechen/SharpInput/blob/main/LICENSE"><img src="https://img.shields.io/github/license/gaoyechen/SharpInput" alt="License: MIT"></a>
  <img src="https://img.shields.io/badge/platform-AI%20Agent%20Skill-blueviolet" alt="Platform">
  <img src="https://img.shields.io/badge/version-v3.0-brightgreen" alt="Version">
</p>

> **你花了几百块订阅 AI，却还在用搜索引擎级别的提问方式。**

<p align="center">
  <img src="assets/sharpinput-demo.svg" alt="SharpInput Demo" width="100%" />
</p>

---

## 🤦 这不是你吗？

| 你平时这么问 | AI 这么答 | 你什么感觉 |
|-------------|-----------|-----------|
| "帮我分析一下" | 泛泛列 5 点，每点就一行 | 这也叫分析？ |
| "XX和YY哪个好" | "各有优劣，建议根据实际需求选择" | 废话文学大师 |
| "这段代码有问题" | "建议优化代码结构，提高可维护性" | 说了跟没说一样 |
| "写个方案" | 教科书模板，换谁都能用 | 这方案值个屁钱 |

**每问一次，就浪费一次 API 调用费。**

你不是不会用 AI。你是**不会问**。

---

## ✅ SharpInput 治这个

```
你的烂输入
    ↓  ⚡ SharpInput —— AI 输入编译器
    ↓  意图识别 → 场景检测 → 上下文补全 → Prompt编译 → 压力测试
    ↓
复制即用的高质量 Prompt
```

**不是帮你回答问题，是帮你把问题本身升级。** 一条命令，让你的 AI 回答质量从"搜索引擎水平"变成"行业专家水平"。

---

## 🔥 看看区别

### 场景 1：历史分析

| 你原来的问法 | SharpInput 升级后 |
|-------------|-------------------|
| 为什么大统一的第一个王朝都很短命？ | 你是一位中国历史学者...请从"统一方式与合法性""制度设计与继承危机""中心-边缘整合成本""精英吸纳与排斥策略"四个维度，对秦、西晋、隋做结构性对比分析。输出要求：对比表格 + 2 个反共识观点 + 史料支撑 |

→ **AI 回答从"教科书摘要"变成「有观点的深度分析」**

### 场景 2：商业决策

| 你原来的问法 | SharpInput 升级后 |
|-------------|-------------------|
| 我们的转化率一直在下降，怎么办？ | 我们是 toB SaaS，注册→付费转化率 8%→3% 持续 3 个月，流量没变、产品没大改。**你必须选边站：问题出在产品、市场还是销售？** 给一个大多数人不会想的根因假设并辩护。如果按你的诊断做了，3 个月后最可能后悔什么？ |

→ **AI 不再给搜索引擎第一页的通用建议，而是给你有观点的决策支持**

### 场景 3：技术选型

| 你原来的问法 | SharpInput 升级后 |
|-------------|-------------------|
| 我觉得应该用微服务重构 | 三条路径任你选：**（A）风险优先**——假设重构让团队产出降 40% 半年，还坚持吗？**（B）反直觉**——说服我为什么不该用微服务，列出 3 个单体更优的理由。**（C）时间轴**——站在 3 年后回看，最大的技术债是什么？ |

→ **你选路径，AI 给你定向深度分析，而不是泛泛而谈的"微服务优缺点"**

---

## 🎯 凭什么 SharpInput 能做到？

| 能力 | 说明 |
|------|------|
| **意图识别** | 14 种意图双标签识别，不误判你到底是"想了解"还是"要决策" |
| **场景自动检测** | 电脑选购、AI 订阅、PRD 生成、UI 评审…识别场景后自动填入领域模板 |
| **四级施压系统** | Level 0-3 自动路由。查资料秒过，复杂决策走上完整对抗流程 |
| **强制上下文补全** | Level 2+ 强制补齐 audience/ goal/ constraints——你忘了说的，它替你想 |
| **认知压力测试** | 逼 AI 选边站、找反例、打掉幻觉、承认"放弃什么换什么" |
| **Judge 审查** | Level 3 高风险决策，独立审查路径质量，给出反转条件和反方攻击 |
| **自我学习** | 记住你的偏好，越用越懂你——"重置偏好"一键清零 |

**不是 demo，是真的能打的工具。**

---

## 🚀 怎么用？

### 安装

```bash
git clone https://github.com/gaoyechen/SharpInput.git
```

把 `SKILL.md` 和 `references/` 放进你的 AI Agent skills 目录。

### 触发

说其中一句话，SharpInput 自动接管：

```
帮我优化这个问题 / 这样问 AI 行不行 / 帮我润色一下这个 prompt
帮我理清思路 / 我这样说合适吗 / 帮我完善一下
```

### 控制等级

```
深度模式   → Level 3（完整对抗，复杂决策专用）
简单优化   → Level 1（轻度润色）
施压一下   → Level 0（快速输出好问题）
```

---

## 📦 项目结构

```
SharpInput/
├── SKILL.md            # 入口 + 运行时检查清单
├── AGENT.md            # Agent 编排流程 + 模块间数据传递规范
├── skills/             # 专项能力模块（按需加载）
│   ├── intent-detection/      # 意图识别
│   ├── scenario-detection/    # 场景模板匹配
│   ├── context-completion/    # 上下文强制补全
│   ├── prompt-compiler/       # Prompt 编译
│   ├── pressure-strategy/     # 认知施压策略
│   ├── judge-review/          # 独立质量审查
│   └── output-renderer/       # 用户界面输出
├── references/         # 13 个参考文件：意图分类法、场景模板、评分 Rubric
├── examples/           # 10 个各 Level/场景示例用例
└── tests/              # 回归测试 + 质量评分标准
```

> 设计理念：**Agent 管流程，Skill 管能力。** 不把所有逻辑塞进一个文件。

---

## 📌 更新日志

### v3.0
- 🔧 **修复**：`context-completion` 新增 Level-aware 强制门控，Level 2+ 不再能跳过上下文补全
- ✨ **新增**：14 种意图分类法 + 双标签识别（主意图/次意图）
- ✨ **新增**：7 个场景槽位模板（电脑选购/AI 订阅/PRD 生成/UI 评审…）
- ✨ **新增**：Level 3 Judge 独立审查模块（反方攻击 + 真实反例 + 翻转条件）
- ✨ **新增**：自我学习系统，滑动窗口追踪最近 10 次交互偏好
- ✨ **新增**：12 个回归测试用例 + 5 维质量评分 Rubric
- 📝 **架构重构**：从单体文件拆分为 Agent + 6 个独立 Skill 模块

---

## 📄 License

MIT —— 随便用，随便改。

---

**⭐ 如果你受够了 AI 给你灌水，给 SharpInput 一个 Star。**

**🌟 如果你想让每次 API 调用都值回票价，现在就去试试。**
