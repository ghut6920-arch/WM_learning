# 机械臂BC闭环第一阶段备课

本次仅备课，未授课。正常AG3审查支持两个确切v1目标，无必要返修；AG0已通过协调程序执行normal-prep-final-adopt-v1（bundle normal-prep-final-adoption-v1，state50）。采用后current查询返回的字节哈希与交付一致，材料审查回执当前适用且input_issues为空。本页只是本次结果的固定导航；后续当前采用仍须查询协调数据库，不根据文件名或本文更新指针。

## 教学成品

| 位置 | 成果 |
|---|---|
| [材料与用途主稿](material/material-use-v1.md) | 14项成品清单、精确哈希、来源与核验范围、主线和帮助边界 |
| [第一份讲解](../../materials/bc-normal-20261013-01/01-loop-and-feedback-v1.md) | 执行链、离线与闭环、完整反馈示范及静态轨迹表 |
| [第二份讲解](../../materials/bc-normal-20261013-01/02-evidence-and-diagnosis-v1.md) | 竞争解释、预测与反证、合法实验比较 |
| [第三份讲解](../../materials/bc-normal-20261013-01/03-data-information-and-modes-v1.md) | 恢复标签、条件均值、信息与模式、条件更新 |
| [A题面](../../questions/visible/bc-normal-20261013-01/A-v1.md)、[B题面](../../questions/visible/bc-normal-20261013-01/B-v1.md)、[C题面](../../questions/visible/bc-normal-20261013-01/C-v1.md) | 同一连续作品；B初始判断保存后才呈现C新增证据 |
| [A参考](../../questions/teacher-reference/bc-normal-20261013-01/A-reference-v1.md)、[B参考](../../questions/teacher-reference/bc-normal-20261013-01/B-reference-v1.md)、[C参考](../../questions/teacher-reference/bc-normal-20261013-01/C-reference-v1.md) | 多解、条件不足、证据和实际帮助的解释范围 |
| [备用支持](../../questions/backup/bc-normal-20261013-01/supports-v1.md) | 触发条件、代做范围及返回同一作品的位置 |

## 正常专业依据

- [研究交接](disciplinary/research-v1.md)及其固定来源/机制附件。
- [认知设计](design/design-v1.md)、[目标](../../goals/bc-normal-20261013-01/goal-v1.md)、[计划](../../plan/bc-normal-20261013-01/plan-v1.md)。
- [实际扰动澄清](design/material-clarification-001-v1.md)：物体世界y方向+1cm及合法/保持条件；成品已经落实，原design v1未覆盖。
- [AG3原始审查](../../assessment/bc-normal-20261013-01/review-v1.md)及read-boundary-v1.json、review-return-v1.md。
- [教师数值代码](../../code/bc-normal-20261013-01/scalar_check_v1.py)及experiments/bc-normal-20261013-01/teacher-checks/的真实输入输出；只支持教师有限数值核验。

## 本次固定交付与恢复

科研依据、设计、材料最终交付均为v1；材料主稿另有两份真实提交前草稿，参见[版本对应](../../experiments/coordinator-normal-prep-20261013-01/VERSION_MAP.md)。正文中的prepared、尚待审查或无回问是生成时快照，不作为当前协调状态。

当前采用查询：用现有code/coordination/normal-prep-20261013-01/observe.py query AG0 current，分别指定稳定id EMB-BC-NORMAL-RESEARCH-20261013-01、EMB-BC-NORMAL-DESIGN-20261013-01、EMB-BC-NORMAL-MATERIAL-20261013-01，intended_use teaching、scope BC-first-stage。独立过程档案只作事实性复核，不作为教学额外输入。

停止原因：本次备课请求已完成。未授课、未取得学习者原答或能力/效果证据；未执行BC训练、仿真闭环改进或真实机器人实验。后续教学须依实际新控制与原协议开始，不自动发送A/B/C。原学习状态与计划未据此记为完成或改排期。
