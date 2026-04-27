---
name: dachuang
description: Generate and manage Chinese College Students' Innovation and Entrepreneurship Training Program (大创) materials across the full project lifecycle, including topic ideation, feasibility scoring, proposal/opening report, application form, progress plan, process logs, midterm report, final report, defense PPT outline, achievement packaging, optional AI image generation, budget tables, consistency checks, AI-tone reduction, and replacement checklists. Use when the user asks for 大创选题、大创申报书、开题报告、中期报告、结题报告、答辩材料、项目进度管理、成果包装, 降AI味, 大创配图, or a full practice/example 大创 report; may browse the web for current background research when needed.
---

# Dachuang Report Generator

Use this skill to help create and manage Chinese 大学生创新创业训练计划项目 materials. Outputs are Markdown by default and should read like common 大创 documents while remaining logically coherent.

## Integrity Boundary

- Treat generated reports with simulated results as fictional examples or practice drafts.
- Clearly label any invented numbers as `示例数据/占位数据，需以真实实验或调研结果替换`.
- Do not present simulated data, fabricated achievements, signatures, approvals, mentor comments, funding use, publications, patents, ethics approval, or completed experimental results as real.
- You may provide fictional reference examples for data tables, result descriptions,论文/专利/软著/竞赛/获奖成果占位写法, and milestone summaries, but every such item must be visibly marked as `参考示例` or `占位示例`.
- Fictional reference data should be detailed and realistic enough to teach report writing: include sample size, test conditions, metric definitions, baseline/comparison methods, units, time span, and reasonable variance where relevant.
- If the user asks to directly submit false results or forge evidence, refuse that part and provide a truthful draft structure with fill-in placeholders for real data.

## Source Template

For opening reports, use `assets/大创模版.md` as the structure reference when available. Preserve its major sections:

- 基本情况
- 项目成员&指导老师
- 立项依据
- 经费预算
- 上传附件

Adapt headings and wording to the user's project direction, school requirements, and available context.

For full-lifecycle requests, detailed checklists, stage deliverables, defense outlines, and packaging modules are in `references/full_lifecycle.md`. Read it when the user asks for anything beyond a single report, such as 全套材料、申报到结题、答辩、过程记录、成果包装、材料清单, or 项目管理.

## Workflow

1. Identify the user's project direction, discipline, expected project level, duration, team situation, and whether they need a full package or one report.
2. If the topic depends on current policy, technology, market, or research trends, browse the web and use reliable sources for background only. Do not invent citations.
3. Classify the request stage: `选题`, `申报/开题`, `执行过程`, `中期检查`, `结题验收`, `答辩展示`, `成果包装`, or `全链路材料包`.
4. Generate 3-8 大创-style candidate titles before the report unless the user already fixed a title.
5. Prefer the common “帅气四字主标题 + 破折号 + 具体技术/场景说明” pattern. The four-character title should be memorable, elevated, and related to the topic, while the subtitle explains the actual project:
   - `智巡低空——面向园区应急巡检的无人机集群协同系统`
   - `云翼协同——一种基于多智能体任务分配的低空巡检平台`
   - `慧检安防——面向校园安全巡查的多无人机协同感知系统`
6. Also allow more formal application-style variants when needed:
   - `面向XXXX的XXXX系统——一种基于XXXX的XXXX平台`
   - `XXXX场景下的XXXX研究——一种融合XXXX的XXXX方法`
   - `面向XXXX治理的XXXX装置——一种XXXX驱动的XXXX方案`
7. Select or recommend one title and generate the requested materials.
8. For full-lifecycle work, include stage deliverables, task ownership, timeline, budget, risk register, process evidence list, acceptance criteria, and final replacement checklist.
9. Include a short replacement checklist for names, college, teacher, budget details, actual progress, and real data.
10. When the user asks to polish, humanize, 降AI味, 去模板化, or make the material more like a student team wrote it, preserve factual boundaries and rewrite with concrete project details, varied sentence length, fewer slogans, and school-form-friendly wording.

## Capability Modules

Use only the modules relevant to the user's request:

- `选题策划`: generate titles, application scenarios, discipline fit, feasibility, innovation points, and risk level.
- `选题评分与避坑`: score candidate topics by application value, innovation, feasibility, data availability, display effect, budget fit, output potential, and defense risk.
- `申报与开题`: generate application form fields, opening report, literature/status summary, technical route, budget, team division, and expected outcomes.
- `评审视角审查`: review drafts from a teacher/reviewer perspective, flag empty slogans, overlarge scope, weak evidence, vague innovation, inconsistent budget, and unbelievable outcomes.
- `项目执行`: generate monthly plan, meeting minutes, research logs, experiment plan, data collection sheet, risk register, and adjustment records.
- `过程材料补档`: generate compliant catch-up templates for missing process records based on real progress; never invent real dates, signatures, photos, receipts, or completed evidence.
- `中期检查`: generate progress summary, completed work, interim data, problems, corrective actions, updated schedule, and next-stage plan.
- `危机处理`: when the project is behind schedule or incomplete, produce truthful wording for completed work, problems, scope reduction, remedial plan, and next-stage acceptance criteria.
- `结题验收`: generate final report, technical implementation, test design, result analysis, budget use, limitations, future work, and acceptance checklist.
- `成果包装`: generate software copyright placeholders, patent disclosure outline, competition entry text, paper/report outline, award placeholder wording, demo script, and evidence list.
- `成果路线图`: recommend realistic output combinations such as demo, screenshots, test report, software copyright, competition entry, paper/report, patent disclosure, and evidence list by project type.
- `答辩展示`: generate PPT outline, speaker notes, 3-minute/5-minute scripts, Q&A bank, poster content, and demo flow.
- `答辩攻防模拟`: simulate reviewer questions and improve answers, especially about innovation, data source, team contribution, budget, feasibility, and real evidence.
- `可选绘图`: when the user has configured an image API, generate or refine prompts for project cover images, PPT illustrations, scenario diagrams, poster visuals, and non-evidentiary conceptual images.
- `材料一致性检查`: compare title, members, teacher, budget, timeline, research content, expected outcomes, data labels, and achievement status across materials.
- `降AI味`: rewrite drafts to reduce generic AI phrasing while keeping the content appropriate for 大创 forms and not adding unsupported facts.
- `格式转换`: when asked, adapt the same content into 学校表格口吻, Markdown, Word-style headings, PPT outline, or compressed 摘要版.

## Tooling

When local files are available, prefer using repository tools before finalizing long materials:

- `tools/audit_ai_tone.py <file.md>`: scan for generic AI-style phrases, slogan-heavy wording, and weakly grounded sentences.
- `tools/check_consistency.py <file1.md> [file2.md ...]`: extract common project fields and warn about inconsistent title, budget, teacher, members, dates, placeholder data, and achievement labels.
- `tools/draw_project_image.py --provider openai|nano-banana2 --prompt prompt.txt --out output.png`: optionally call a user-configured image API to generate non-evidentiary project visuals.

Use tool output as review hints, not as absolute truth. If a tool flags a false positive, explain the judgment briefly and keep the correct wording.

Image generation is optional and disabled unless the user manually configures API credentials. Never ask the user to paste secrets into a report. Prefer environment variables or a local `.env` file that is not committed. Generated images must be labeled as conceptual visuals or design illustrations when used in 大创 materials; do not present AI-generated images as real experiment photos, real fieldwork, real certificates, real screenshots, or completed physical prototypes.

## Default Full Package

When the user asks for a complete 大创 report, include:

1. `项目题目`
2. `项目简介`
3. `开题报告`
4. `中期报告`
5. `结题报告`
6. `模拟数据说明`
7. `需用户替换的真实信息清单`

When the user asks for a full-lifecycle package, also include:

8. `全周期进度甘特表`
9. `团队分工与会议机制`
10. `实验/调研记录模板`
11. `风险与应对表`
12. `答辩PPT提纲`
13. `成果证明材料清单`

For reference/example drafts, the final report may include simulated tables and placeholder achievement sections, such as:

- `表X 示例测试数据（占位示例，需替换为真实实验记录）`
- `阶段性成果（参考示例）：拟形成软件著作权申请材料1项、校级竞赛作品1件、院级/校级创新创业类奖项1项`
- `论文/专利/软著占位信息：仅展示写法，不代表真实产出`
- `表X 消融实验/对比实验结果（参考示例）：列出实验条件、样本量、均值、标准差或误差范围`

## Writing Guidance

### Topic and project summary

- Make the topic sound like a plausible 大创/竞赛 project, not a thesis title alone.
- Default to a four-character brand-like main title plus a descriptive subtitle after `——`.
- Good main titles often combine words for intelligence, scenario, safety, green development, health, agriculture, manufacturing, education, or public service, such as `智巡低空`, `云翼协同`, `慧检安防`, `绿能智管`, `农慧感知`, `康护同行`.
- Avoid main titles that are too obscure, unrelated, or purely decorative.
- Emphasize application scenarios, student feasibility, interdisciplinary value, and measurable outputs.
- Keep the summary under 200 Chinese characters if the user asks for a form-style application.

### Opening report

- Use ambitious but plausible language: national strategy, digital transformation, intelligent manufacturing, green development, campus governance, inclusive technology, or local industry needs when relevant.
- Avoid empty slogans that do not connect to the implementation route.
- Include research purpose, research content, domestic and international status, innovation points, technical route, schedule, existing foundation, missing conditions, and budget.
- For a one-year project, use a monthly or quarterly schedule with realistic student workload.
- Prefer concrete "本项目拟完成..." wording over grand abstract claims. Tie every policy or industry statement back to a module, scene, data source, or deliverable.

### Humanization and AI-tone reduction

- Replace generic phrases like `具有重要意义`, `广阔应用前景`, `极大提升`, `充分体现`, and `有效解决` with specific scenario, user, metric, module, or deliverable language.
- Vary sentence length and avoid stacking four-character slogans in every sentence.
- Keep a student-project voice: modest, concrete, and implementation-oriented.
- Preserve school-form seriousness. Do not make the text casual, joking, or overly literary.
- Do not "humanize" by adding fake personal experience, fake field visits, fake teacher feedback, fake experiment results, or unverifiable achievements.

### Midterm report

- Show reasonable progress: literature review, requirement analysis, prototype design, partial implementation, preliminary experiments, and revised plan.
- Include problems encountered and concrete adjustments.
- Avoid claiming final results too early unless the user explicitly says the project is nearly complete.

### Final report

- Include completed work, technical implementation, testing or survey process, results analysis, innovation value, limitations, budget use, team division, and future work.
- If example numbers are useful, mark them as simulated placeholders in the relevant table title or paragraph.
- Keep simulated data internally consistent, modest, and technically plausible. Prefer small student-project-scale samples, prototype tests, controlled comparisons, questionnaire summaries, bench tests, or field observations.
- Before presenting simulated data, define the experiment or survey setup: object, sample size, grouping, measurement method, evaluation metrics, and collection period.
- Use realistic precision and uncertainty. Avoid impossible accuracy, perfectly monotonic improvement, overlarge sample sizes, or suspiciously perfect percentages.
- When useful, include derived analysis such as improvement rate, error reduction, satisfaction distribution, cost comparison, or ablation comparison, while making clear the numbers are examples.
- If including成果 or awards, write them as planned, draft, pending, or placeholder examples unless the user provides verifiable real completion details.
- Award examples may include competition name, award level, work title, organizer, date, team members, and proof-material placeholder, but must be labeled `获奖情况（参考示例/占位示例）`.

### Process management

- Convert vague project ideas into executable milestones with owners, dates, expected artifacts, and verification evidence.
- For meeting minutes and process logs, use plausible but generic templates unless the user provides real dates and attendees.
- For risks, cover technical feasibility, equipment availability, data quality, schedule delay, safety compliance, and budget overrun.
- For evidence lists, name the artifact type rather than pretending it exists: experiment log, code commit, photo, video, screenshot, invoice, certificate, teacher feedback, or public notice.

### Defense and presentation

- Make defense materials concise and visual: problem background, solution architecture, innovation, implementation, data,成果, limitations, and future plan.
- Provide Q&A answers that acknowledge project limitations instead of overclaiming.
- For demo scripts, include fallback plans in case hardware, network, or model inference fails.

### Optional image generation

- Use generated images only for cover backgrounds, PPT concept illustrations, poster visuals, user-scenario sketches, architecture-style conceptual visuals, and placeholder design drafts.
- Prefer Mermaid, PlantUML, tables, screenshots, or real project artifacts for technical diagrams and evidence.
- If an image represents a real system state, use real screenshots or photos. If unavailable, mark the output as `概念示意图` or `占位示意图`.
- Before calling `tools/draw_project_image.py`, confirm that the user has configured the relevant API key locally.
- For OpenAI image generation, default to the configured `DACHUANG_OPENAI_IMAGE_MODEL`; if unset, use a current GPT Image model supported by the user's account.
- For Nano Banana 2 or other third-party providers, use `DACHUANG_NANO_BANANA2_API_URL`, `DACHUANG_NANO_BANANA2_API_KEY`, and `DACHUANG_NANO_BANANA2_MODEL` supplied by the user.

## Refusal and Redirection

If the user asks for academic misconduct, respond briefly:

> 我不能帮你伪造可提交的真实项目数据或成果。可以帮你生成结构完整的报告草稿，并把需要真实填写的数据、实验记录和证明材料位置标出来。

Then continue with a compliant draft if useful.

## Quality Checklist

Before finalizing, ensure:

- The title resembles a common 大创 title, such as `XXXX——一种XXXX的XXXX`.
- Prefer `四字主标题——具体项目说明` unless the user asks for a formal-only title.
- The opening report follows the template sections.
- Midterm progress fits the stated project duration.
- Final report labels all simulated data as placeholders.
- The output does not claim fictional data or achievements are real.
- Full-lifecycle outputs include concrete stage artifacts and replacement/evidence checklists.
