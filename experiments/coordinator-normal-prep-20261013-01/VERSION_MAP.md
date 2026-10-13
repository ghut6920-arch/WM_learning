# 实际中间版本与最终版本对应

此表为本次冻结事实，不是后续采用指针。当前仍须查协调数据库。没有生成专业成品v2，不补造返工。

| 对象 | 实际中间版本/变化 | 最终交付 |
|---|---|---|
| 原请求 | sessions/2026-10-13-normal-prep-01/raw/request-001.txt revision1，完整保存读回；original-request.txt为隔离复制 | 同一revision1，不改原话 |
| 研究/来源/机制 | research-v1、source-fragments-v1、mechanism-notes-v1，研究提交与专业确认后采用；无研究回修 | 同一v1；研究主稿SHA256 3e22127185fc543df797fc22a32c52014cf64bd895cddcf2085e2861f689aefe |
| 设计/目标/计划 | design-v1、goal-v1、plan-v1，先提交候选并确认；未覆盖 | 同一v1；设计主稿SHA256 9382ea8bccdb395f1a45ae0c64cc6c868667036839eb42b728b116edf1bd4df5 |
| 材料规格反馈 | AG2实际回问扰动对象/轴；AG1 material-clarification-001-v1，判为材料合法实例化，未改目标/判据或design正文 | 固定澄清SHA256 6ab66a133658cefa4a285832f125e28a51d8c401279fec6d9f6c387de8472793，进入B/C与参考/MaterialUse |
| 材料主稿草稿001 | observations/AG2/drafts/material-use-draft-001.md，SHA256 163f3f11dece21c679c2cd2c62620dc7702a75c2cfcccce64ef27596adf729df；核验状态字段随后修正 | 真实原正文保留，不登记为Candidate |
| 材料主稿草稿002 | observations/AG2/drafts/material-use-draft-002.md，SHA256 af87d2720fc6a0d551d1361018326a6b17a0eeb3b06c1a7f8e0084b3e18752e8；表中竖线随后改为文字 | 真实原正文保留，不登记为Candidate |
| 材料候选/最终 | material-use-v1在两次提交前修正后提交，暂定设计输入明确保留；AG3通过后与design一事务采用 | 同一v1，SHA256 4e0ba1f114c1fee6d238c65c83c950343ff10e0762832475333b08acbec72457；两段完整diff在version-diffs/ |
| 14项实际材料 | manifest-v1逐项固定；3讲解、A/B/C、3参考、备用支持、代码、教师输入/输出及澄清，均直接形成v1 | manifest-v1 SHA256 42cf94a0c586119eb23758fad9c47869be79b404b58e99ba7afdfd6182b00b1f；逐项路径/hash见原manifest及file-snapshot-manifest |
| 审查 | 先定review-questions-v1，收到成品后review-v1；两个supported回执绑定两个确切目标 | review-v1 SHA256 9430635c709226a3ee940d3f110d4c192d11199822b382b1def7e0f329c956b8；review-return-v1保留回传时未采用状态；无返修/补审/v2 |
| 正式采用 | 研究先采用；设计与材料在审查回执后normal-prep-final-adopt-v1整组采用；事前expected_pointers均null | 最终查询三目标均v1，材料回执适用且输入问题为空；原始程序响应在observations/AG0/ |

补充观测：AG2手抄草稿001哈希曾误插空格，原material-version-map-v1.json保留，material-version-map-correction-001.json追加正确值；执行层从实际草稿独立核对见material-draft-byte-verification.json。AG0派发前任务文本01文件与实际spawn正文02文件分开保存；输入边界的真实澄清单独记录，不冒称专业返工。每个实际被读取文件的所有可观察字节版本、归档时间和原记录定位见observed-file-version-history.json；未观察到的草稿不补造。
