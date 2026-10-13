# BC第一阶段实际材料与用途核验 / revision1

type MaterialUse；id EMB-BC-NORMAL-MATERIAL-20261013-01；revision1；owner AG2；schema_version pl-contracts/0.1.0。正常人工文件视图，不声称完整JSON schema校验。生成时为待提交备课候选；协调器才维护登记状态、审查回执与当前采用指针。全部成品prepared、未displayed；本次未授课、无学习者原答或能力结论。

## 固定输入与绑定

basis_refs：已采用的EMB-BC-NORMAL-RESEARCH-20261013-01 v1，teaching/BC-first-stage，SHA256 `3e22127185fc543df797fc22a32c52014cf64bd895cddcf2085e2861f689aefe`；exact EMB-BC-NORMAL-DESIGN-20261013-01 v1，SHA256 `9382ea8bccdb395f1a45ae0c64cc6c868667036839eb42b728b116edf1bd4df5`。任务normal-prep-ag2-material-v1实际start，取得boundary和snapshot，解码字节位于coordination/runs/normal-prep-20261013-01/snapshots/AG2/，哈希与固定输入相符。研究同一字节正文沿前阶段已读内容复用；设计实际读清，不按最高文件名替换。

设计是明确暂定输入：只据确切v1生产候选材料，不属于正式采用；最终使用需适用AG1设计确认、AG2材料确认、AG3审查及AG0对相容版本整组采用。当前专业核验支持这些条件下的候选用途，不隐藏input_not_adopted。

goal_refs：EMB-G-BC-NORMAL-20261013-01 v1，goals/bc-normal-20261013-01/goal-v1.md，SHA256 `eab5f2f7d750dd52bd25710a8b23009090f0ff3c486ca6b214d5f36480e115df`。criterion_refs R1–R4各revision1。Activity EMB-A-BC-NORMAL-DOSSIER-20261013-01 v1、MethodConfig EMB-MC-BC-NORMAL-20261013-01 v1均在固定design v1；AG2依据该完整配置实例化R06/O05及三个Post的操作和帮助边界，不宣称自己重新读取全部策略原包。

预算/计划：EMB-P-BC-NORMAL-20261013-01 v1，plan/bc-normal-20261013-01/plan-v1.md，SHA256 `5e8ce32945700f6e8e13b428d25883ff7eef8916175efb89200c2f014a0b1ac7`。本次自报Python/ML/仿真/BC经历，仅作起点；熟练度、预算和设备unknown。只备课，不安装/收费/真实机器人执行/外部消息/共享框架修改。未改旧学习事实或plan/current。

fragment_refs：materials/bc-normal-20261013-01/source-fragments-v1.json，EMB-BC-NORMAL-SOURCE-FRAGMENTS-20261013-01 v1，SHA256 `9af535b40e7c5a8b16b596f0205a71451ec515dd2b9be1ac3f73fdb8d6252770`，含原始论文R1/R2/R3实际读范围；disciplinary/mechanism-notes-v1.md SHA256 `7046cf8d5a5f7d5c3a2b71230e058ebac44c83e8b06d324d65abb3653300d91d`提供完整有限推导。来源原图不可获得，不引用图高度或精确论文效果量。

## 一个实际回问的落实

AG2制作时发现design B的“已定义1cm横向位移扰动”未定位移动对象/轴，实际回问AG1。AG1接受其v1允许的材料实例化并保存artifacts/bc-normal-20261013-01/design/material-clarification-001-v1.md revision1，SHA256 `6ab66a133658cefa4a285832f125e28a51d8c401279fec6d9f6c387de8472793`；AG2已实际读取和核哈希。它是固定专业附件，没有冒称被协调器另登记，也没有替换固定design输入。

必要完整决定已进入成品：B中t=2秒无接触时把待抓取物体世界y平移+0.01m，其他位置分量/朝向/速度、机械臂及其他物理状态保持；新位置无碰撞且仍可抓取。控制器内部状态沿同次执行保留而不重置，但其影响与时间链在B仍未核。C使用同样扰动，并单独给其新增的相同物理/必要内部状态、扰动和剩余物理时长匹配条件。B-v1、B-reference-v1、C-v1及C-reference-v1实际承接；备用支持解释匹配必要内部状态，调用时不得换成末端/相机扰动。此澄清没有改变R1–R4、主要任务、A模型或计划；设计原稿生成时“未发生回问”保留其历史位置。

## 实际文件、版本与哈希

完整14项本地文件清单在artifacts/bc-normal-20261013-01/material/manifest-v1.json revision1，SHA256 `42cf94a0c586119eb23758fad9c47869be79b404b58e99ba7afdfd6182b00b1f`。其中每项保存path/revision/SHA256/origin，已经写后读回；清单只固定字节，不维护第二套采用指针。实际成品如下，所有文件均revision1：

| 文件（工作区相对位置） | 实际功能与使用边界 |
|---|---|
| materials/bc-normal-20261013-01/01-loop-and-feedback-v1.md | 首份学习者讲解：x/o/a/u执行链、两个评估对象、完整b=0.02示范、实际轨迹表、b/ρ/容差及机器人边界 |
| materials/bc-normal-20261013-01/02-evidence-and-diagnosis-v1.md | A反馈后输入：候选关系、预测/反证和合法比较；用不同的(x,v)欠观测情境完整示范实验，不代选目标病例唯一原因 |
| materials/bc-normal-20261013-01/03-data-information-and-modes-v1.md | B初答保存后的输入：恢复标签定位、DAgger聚合机制、完整条件均值推导、信息/模式/覆盖区别及合法集变化 |
| questions/visible/bc-normal-20261013-01/A-v1.md | 已讲模型下推演新b、e_0、容差及工程边界；数值、说明接同一作品 |
| questions/visible/bc-normal-20261013-01/B-v1.md | 初始病例、完整扰动/未知/资源与实验选择工作；不含C新增核验或恢复统计 |
| questions/visible/bc-normal-20261013-01/C-v1.md | 新事实后修订B，保留/更新、恢复数据作用点、I/II及合法集变化、对照与边界 |
| questions/teacher-reference/bc-normal-20261013-01/A-reference-v1.md | A准确轨迹/容差、多种合法推法、机制映射、帮助与有限结论 |
| questions/teacher-reference/bc-normal-20261013-01/B-reference-v1.md | B事实限度、四种可靠下一步候选/信息不足、预测/结果分支/保持条件及多因联动 |
| questions/teacher-reference/bc-normal-20261013-01/C-reference-v1.md | C新证据更新、数据比较、多解与信息/模式的完整参考、作用点和整体收束 |
| questions/backup/bc-normal-20261013-01/supports-v1.md | 真实卡点才调用：对象、一步/整表、机制桥接、对照、恢复标签、均值合法集；每项含代做范围和父作品返回 |
| code/bc-normal-20261013-01/scalar_check_v1.py | AG2 AI编写的教师有限数值核验原件；未给学习者作为自主实现任务，不是机器人仿真 |
| experiments/bc-normal-20261013-01/teacher-checks/scalar-input-v1.json / scalar-output-v1.json | 明确模型输入与实际教师执行输出、环境和代码/输入哈希；不是真实PerformanceEvent |
| artifacts/bc-normal-20261013-01/design/material-clarification-001-v1.md | AG1实际专业回问返回的固定附件，限定B/C扰动释义 |

## visible_input、backup_help与teacher_reference

未来当前控制允许教学且上述版本通过审查/采用后，AG0可沿同一EMB-A-BC-NORMAL-DOSSIER主线执行：01讲解与A；保存A实际原答/帮助后给必要反馈，直接接02讲解与B；保存B初始判断后给03讲解与C新增信息/修订任务。真正需要原答处等待，其余必要讲解直接推进，不设置逐题“继续”开关。这里是备课呈现次序，不是已经展示的事件。

B/C分文件隔离：初始B不泄露相关接口已核一致、专家18/20/P6/20、偏离覆盖少见或专家可标注的新增事实。03可以在B初答保存后随C准备材料展示；它教清机制，但不提供C目标病例的一份完整建议。02的不同情境示范留下目标B的解释、顺序和具体预测。A示范没有给新b/e_0的答案；A-reference和教师执行输出不默认展示。

备用与完整教参后台保留。需要时可以直接给足可靠帮助，记录代做范围，再回同一作品；不要求先答错、固定提示等级或额外小测。各可见题面预备的等待动作只检查自己的已交说明，没有加必做负担。用户请求完整答案可转教学，不再用已给结论宣称其此前自主完成。

leakage_risk：术语、模型、方程、MSE恒等式及不同情境示范都是教师提供的真实输入；A是有支持推演，B是已教原理下的方案选择，C是已教关系的应用和证据更新，不能扩为无提示发现/陌生广泛迁移。03明确教信息与模式区别，所以C相关解释的证据条件保留这些支持；未给的是其病例建议、比较设计和连续修订。代码/输出或整表一旦给学习者，数值核算被代做；参考一旦展开，相应选择/理由也被代做。文件是否可访问不等于本轮已displayed或用户从未看过。

## verification：内容正确性与教学功能

content.status=supported_for_declared_scope，reviewer=AG2；用途为teaching/BC-first-stage候选成品。实际原件/定义对照、有限代数推导、逐项数值核算及题面—参考—帮助检查分别成立；全部正文已读回。校验字节不证明学科正确，教师自查不冒称盲评；最终正常AG3审查尚待执行。

| 目标/whole_obligations | 实际成品怎样承担联系、学习者还做什么 | 核验锚点与限制 |
|---|---|---|
| R1：执行链、两个对象/条件、重放、失败/失稳区别 | 01的同一对象表和返回链接到损失/轨迹；B要求将现有证据定位到链上，不靠“都好/都差”归因 | research固定v1、01与A/B参考；a/u分开、重放绕过接口、未知内部状态保留，未声称真实机制发生 |
| R2：合法递推、两策略、偏差/恢复/容差、机器人映射 | 01先给环境+策略的中间代入和每步表；A对新条件推演并解释保持项，回机械臂删去结构 | mechanism-notes及实际数值输出；A e6=0.01140625，B e6=0.21573415；收缩有偏、边界|ρ|=1及有限成功/一般保证分开 |
| R3：预测与竞争解释、合法比较、分支及边界 | 02有可追踪示范；B选择相容原因、下一证据、预测/反证与条件改进，参考支持不同顺序及信息不足 | B完整物体扰动/病例未知、AG1澄清、B参考四路线；匹配必要内部状态、物理时长、版本/初态与指标，不凭成功数唯一归因 |
| R4：证据更新、作用点/条件、信息与多解、保持有效旧域、效果检验 | 03提供条件均值完整推导与恢复标签机制；C修B建议、处理I/II/合法集变化并拟定比较 | mechanism-notes、03/C及C参考；±1均值0，MSE最小1，端点MSE2；非凸集/凸区间区别、路径一致、更多标签不自动补信息/修接口 |

verification.content.whole_coverage.status=supported，target_operations为解释、推演、证据限定、竞争预测/实验设计、条件选用和修订；obligations为以上R1–R4完整连接。anchor_refs为01/02/03、A/B/C及三份教参v1、固定研究/机制附件、AG1澄清和教师数值输出；确切哈希由本稿及manifest绑定。该声明支持材料承担整体工作，不等于学习者已完成整体作品。局部数字/每份题数不能替代最终连续原件评审。

实际数值执行：Python3.12.3，stdlib，无安装；四个示范/任务实例递推与闭式一致，并核ρ=1、负收缩、b=0的公式分支。实际输入/输出及code字节已保存读回；表格中所有示范和A值据输出核对。有限算例只校数字/分支，一般关系沿代数推导；未运行仿真/机器人、未验证BC训练或改进效果。

静态对象表、因果返回链和轨迹表是当前必要可视化：变量身份、每行变成下一输入、相同名义损失后的恢复差异在实际正文可读，表数值与方程逐项一致。未制作动画/交互或复用未读原图；不以媒体数量替代功能。平方可积条件、合法集边界、不同任务的MSE尺度及真实系统未核项均保留。

task_qualification在此范围supported：题面必要模型/事实/允许资源已给，参考可核合法多解，关键解释/预测/方案/更新仍有学习者工作，没有新增Python前置或固定术语测验。源示范/帮助的支持条件限定证据用途；实际个体适配要等原答，不把备用信号写成用户缺陷。

## 交接、实际完成与未完成

交AG0/AG1：主线实际成品及参考已有可靠依据，当前仍是设计暂定输入下的候选；AG1可核它们承接认知配置，AG0依程序安排确认/审查/最终采用。交AG3：从原用途回查本稿、所有实际成品、固定研究/来源与扰动澄清，核必要学科联系、多解/未知分支与剩余学习者操作。只备课，不向用户发A/B/C教学提示。

本阶段实际新增读取：固定设计快照及Goal/Plan附件、SK02材料实例、SK03 design-whole、实际AG1回问返回、所有新成品与教师输入/输出。稳定研究/规则复用；没读旧专题审计或隔离过程档案，不为记录额外研究。前阶段“不读旧BC材料”派发边界已由AG0澄清为起始隔离而非新增系统规则；当前充分故未发生旧专业材料复用。

已完成讲解/示范、必要静态表、A/B/C题面、备用支持、多解教师参考、有限数值核验、出处/条件/哈希与用途核验，发生一次具体专业回问并落实。未完成AG3最终审查/AG0整组采用；本次没有授课、原答、用户运行、真实项目诊断或学习效果。原始PDF图像内容和远端字节哈希仍不可获得，未读证明/附录不进入当前用途保证；完整DAgger实现、架构横评、全局稳定与硬件试验未安排。无新学习需要或复习债务。
