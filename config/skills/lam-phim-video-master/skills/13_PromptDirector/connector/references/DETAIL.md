# connector — Chi Tiết Đầy Đủ

> File này chứa bảng tra cứu, checklist và ví dụ mở rộng của skill `connector`.
> Được tách từ SKILL.md để tuân thủ giới hạn 24KB của Antigravity.
> Xem hướng dẫn chính tại [SKILL.md](../SKILL.md)

---

查找方法用 list_skills，read_skill 的 body 读正文，references 读完整原词引用，files 读文件清单，versions 读保留历史。按 nextOffset 和 revision/expectedRevision 读全再解析；versionId 可固定保留版本。文件清单中 current 是所读版本正文生成的文件，package 是原样保存的包，包内 SKILL.md 可能早于人工文字编辑。packageFileScope=unrecorded 表示该旧版本未记录包文件，不能以当前脚本替代。read_skill_file 按路径和来源读文字，续页还需 expectedHash。download_skill_file 完整取回已列文件，按 relativePath 组织宿主目录；二进制原件核对 SHA-256。插件不执行脚本，宿主根据用户任务与权限决定是否运行，下载成功不能称脚本已验证。

用户委托保存方法或完整文件包时用 save_skill，新建不传 skillId，更新须 skillId 与已读 expectedRevision。正文保存提供 callName/skillMarkdown，省略 references 保留引用，显式 [] 才清空。整包提供明确的本机绝对 path 与包内 packagePath，必须含 SKILL.md；不要同时传另一份正文、引用、说明或 portableId。包内 name 必须匹配目标 Skill 的 portableId；不匹配应核对目标，不自动改为新建。连接器在上传前查 status 的能力和 skillPackageLimits，核对当前声明的传输边界；单次分块长度不能解释为文件或包总量限制。保存原始 frontmatter、脚本、空文件及二进制字节，但不执行内容。

完整正文或引用已有文件时直接用files，不把全文重抄进调用参数。内联受含JSON信封的单次本机消息上限约束，过大时改用文件分块；MAX_SAFE_INTEGER是数值表达边界，不是无限传输/解析承诺，maxTextBytes是本次正文和引用解析预算。不要自行缩短、压缩或丢弃原文来通过限制。references的runtime=true会进入插件应用Skill时的模型上下文，false仍完整保存可读，按实际常驻需要选择；不能把默认常驻理解为必需，也不因长资料自动改写该值。示例和两种互斥保存方式见README。

恢复用 restore_skill，默认 complete 恢复已记录的正文、引用和文件；旧版本文件未知时明确失败，仅在用户明确要求只恢复文字时用 mode=text，保留当前文件。版本沿用插件保留规则。save_skill/restore_skill 直接返回最终回执，不用 get_task；相同请求重试沿用 requestId 和参数，版本冲突重读核对。replayed 不代表对象当前仍存在，必要时重新读取。内部草稿仍可在插件查看保存。

用户委托批量分析时，插件只接收结果，不替宿主调用模型。read_case_details固定案例版本；实际看过原件后才登记视觉assets的assetId/sha256/coverage，文字分析用空assets。manage_analysis_batch用create创建，add分批登记，seal结束登记；一个案例每批一次。read_analysis_batch取得每项attemptId与批次epoch，submit_analysis_result逐项提交result或error。result支持AI标签tags、逐媒体mediaPrompts、新增视频timeNotes，以及imageAnalyses、videoAnalyses、visualSetAnalyses。逐图提交assetId/reconstructionPrompt/tags（1–6条）；视频提交assetId/reconstructionPrompt/tags（4–8条视觉标签）/uncertainties/analysisScope（visual只看画面，video包含音画），coverage仍须如实写具体已观察范围。整组提交assetIds、逐图imageRoles、sharedVisualSystem、differences、continuity、compositionRules、reusablePrompt，必须有与当前原件一致的逐图有效分析，可在同项先提交逐图再总结。不要对同一素材同时交mediaPrompts和完整逆推。自由格式完整报告用save_material关联来源。tags的g从part=taxonomy读取，不猜分类编号；过长、重复、未知标签整项拒绝。不得把AI词写成原词，不覆盖人工正文、旧笔记或已有不同AI提示词。用read_case_details(media/annotations)核对完整保存；analysis_coverage读取已存范围、摘要和未知项，verified_at_save只说明保存时核验，不能据此宣称刚刚重验字节或已看完整视频。status的analysisResultVersion/analysisResultFields声明实际后台能力，旧Chrome后台需重载才有新字段。

断线或忘记编号时，先list_analysis_batches按query/status找到当前库的外部批次，再read_analysis_batch核对；列表摘要截断不等于完整要求，后续页固定revision为expectedRevision。多个已完成结果用submit_analysis_results合并一页保存（最多24项，与读取一页一致），每项带caseId/attemptId及result或error，批次epoch和requestId放顶层；不能重复caseId，不能把过期结果换新身份。逐项核对items[].state/error；冲突项失败不妨碍同页其他有效结果。取消在已开始提交的页完成后生效，不要为了凑满一页等待模型。

submit返回ok不代表写回成功，必须查item.state及error；全批查看saved/failed/pending与status，partial要说明失败范围。相同请求重试沿用requestId和参数；失去回执先续查，不重新分析收费内容。取消传当前epoch，成功项保留，宿主也要停止自己正在运行的模型/脚本；resume仅恢复接收，不自动重跑。retry仅针对失败项并携带重新读取的输入，使用新attemptId，不能给旧分析重新贴新版本或新epoch来绕过冲突。read_analysis_batch读取分页和完整result，后续携带expectedRevision；taxonomy续页还需expectedContentRevision。批次运行记录未纳入备份，长期报告另存案例。内部/外部共用写入服务不等于任意模型都有视频理解能力。

采集完整性：summary.platform给出实际适配能力，candidates[].supplements列出评论来源与partial；用read_capture(part=supplement,candidateId,supplementId)调用插件评论展开采集器，按返回selector用textSources保存冻结全文。partial仍未完整，保存后的originalVerification是实际入库读回结果；duplicate不能证明新增全文已保存。

采集模块定位：read_capture(part=page)返回当前选区及可见代码/对话框的context事实；需要完整源码或长正文，read_capture(part=source,selector)取得实际区域并冻结完整原文，再update_capture(candidates[].textSources=[{selector,target:"text"或"prompt"}])直接保存原文，不让模型重写源码。分页只表示Agent读到的范围，不用前半页声称全文已读。status.captureReadParts用于确认当前后台读取能力，缺少source声明时不假定可用。批量执行用update_capture.task记录实际目标、candidateIds、outcome和active/waiting；有缺项不假报完成。新建项目用create_project的即时项目回执，不把它当get_task的异步任务。已准备好的本机文件可在媒体中用localTransferId沿同一采集管线选择保存；聊天附件不默认入库。外部宿主独立保存文件仍可save_material(files)，两者不需要再次调用插件内部模型。

当前页面的弹窗/源码页签变化不以URL变化判断。read_capture(part=context,tabId)直接读可见代码及弹窗；query按目标模块标题查实际selector，再source读取并通过textSources保留完整原文。单模块创建独立候选，不重命名整页候选而混入其他正文。context是完整的小快照，较大范围用query聚焦或增加length，不拼接不同时间的现场分页。

正文与评论可用context的textModules定位，query也匹配正文片段，使用返回的selector而非猜DOM序号。保存后的缺失核对用read_case_details按需读取真实source/media/document，区分案例完整原词与图片附带短词。save_capture.contentTypeId可指定库内真实内容类型，人工预览中的类型选择优先。用户要保留代码交互效果时，原CSS/React/Prompt用textSources完整保留，可另附candidates[].codePreview.html自包含HTML复现；与源代码分开，不能冒称原站原件或已验证运行。预览隔离且不联网，不依赖远程CDN/在线编译；缺依赖时说明源码已保留、预览未完成，不将没有视频URL等同无法保存代码效果。只按用户要求制作复现，不在普通采集中自动生成代码。

同一模块多个源码区域可用read_capture(part=source,selectors=[真实selector列表])一次冻结完整原文，返回共同revision及sources。length在区域间分摊，sources[].nextOffset不是全文已读；理解时用对应单个selector续读，保存用已冻结textSources，不重写源码。不要按同一旧revision并行发多个单区域读取。
