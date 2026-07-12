---
name: adaptive-english-teaching-studio
description: Turn English textbooks, passages, questions, answer keys, and learner profiles into a coherent Chinese-taught one-to-one lesson package. Use whenever a teacher is preparing primary or KET/A2 Key, junior-high, senior-high, CET-4/6, New Concept English, IELTS, or TOEFL reading lessons and needs a teacher verbatim script, a real PPTX deck, in-class practice, or homework—even if the user only uploads a passage or worksheet sample and says “帮我备课”, “做教案”, “做逐字稿”, “做PPT”, “出课堂练习”, or “照这个样例出作业”.
compatibility: Requires file-reading tools, DOCX generation for scripts and worksheets, and PPTX generation for slides.
---

# Adaptive English Teaching Studio

Build an integrated lesson package from one shared teaching blueprint. The files should feel like parts of the same lesson, not unrelated AI outputs.

## Default teaching context

Use these defaults unless the user supplies different information:

- online, one-to-one lesson
- 120 minutes including a short break
- Chinese as the teaching language; preserve English source text and examples
- systematic explanation with frequent comprehension checks
- homework assigned after every lesson

Do not ask again for facts already present in the conversation or source files.

## Ask the user to choose

Inspect the supplied materials first. Infer the course track, material type, available answer key, and likely difficulty when the evidence is clear.

Before generating the lesson, ask only for choices that are still missing. Use the environment's choice-question controls so the user can click options. If clickable choices are unavailable, present the same options as a compact numbered list.

Ask one direct question: **请选择具体学段或课程（单选）**

- 小学
- 初中
- 高中
- 四级
- 六级
- 雅思
- 托福
- 新概念

Do not ask for a higher-level course category first. If the user selects 新概念, then ask for the book and lesson number only when they are not clear from the uploaded material; infer the student's real school stage or ask only if it changes the teaching depth.

Next ask **需要哪些成品？** as a multi-select choice with four independent options:

- 教师逐字稿
- PPT
- 课堂练习
- 课后作业

Create only the selected deliverables. If the user selects nothing, recommend the complete package of teacher script, PPT, in-class practice, and homework, but do not silently add an unselected file.

If the interface only supports single-select buttons, ask the user to select several option numbers in one reply instead of forcing multiple rounds of yes/no questions.

Ask for student level/current score, target, or weakness only when it is not already available and the missing information would materially change the lesson. Do not turn the intake into a long form.

Accept natural-language choices such as “雅思阅读，逐字稿＋PPT＋练习” or “小学KET阅读，做逐字稿、PPT和课堂练习”. Treat them exactly like button selections and do not ask the same questions again.

After the choices, display one confirmation line, for example: “小学KET｜120分钟线上一对一｜已选：教师逐字稿、PPT、课堂练习。” Continue without a separate confirmation question unless the material scope is ambiguous.

For TOEFL, determine whether the material targets the legacy format or the test used from 21 January 2026. Ask for the test date only when the material itself does not reveal the format. Read [references/track-profiles.md](references/track-profiles.md) before planning the lesson.

## Source and rights rules

Work from user-provided materials whenever possible. For missing examples, use official public samples, public-domain/government material, or an original passage clearly labeled as such.

Do not search for or reproduce pirated textbook scans. New Concept English and commercial school textbooks require a user-provided excerpt or licensed copy. A short identifying title is not enough to reconstruct the full lesson text.

Cite external sources in the teaching blueprint and in any artifact that reproduces or closely adapts them. Keep source credits away from student answer areas. Read [references/source-guide.md](references/source-guide.md) when sourcing material rather than using an upload.

## Build the shared teaching blueprint

Before producing any artifact, create `teaching-blueprint.md` with:

- student profile, track, source, lesson goal, and measurable end-of-class outcome
- material map: topic, genre, paragraph functions, key logic, and question types
- language map: essential vocabulary, chunks, grammar, long sentences, and paraphrase pairs
- difficulty diagnosis: what the student can probably do, likely sticking points, and misconceptions
- answer-and-evidence map: each source question, answer, textual evidence, and reasoning
- 120-minute lesson flow with a realistic break and time total
- one content map linking each teaching point to the script, slide, practice item, and homework item

Distinguish source facts from optional background knowledge. Background knowledge should make the English easier to understand; it must not replace textual evidence when answering reading questions.

If an answer key is absent, solve the questions independently. Mark uncertain or ambiguous items for teacher review instead of inventing certainty.

## Plan the 120-minute lesson

Adapt the sequence to the learner, but use this as the default skeleton:

| Time | Purpose |
|---|---|
| 0–10 min | goal, warm-up, and quick diagnostic |
| 10–30 min | essential vocabulary and just-enough background |
| 30–60 min | guided reading, grammar, and long-sentence work |
| 60–65 min | short break |
| 65–95 min | question strategy and evidence-based guided practice |
| 95–110 min | independent check, correction, and transfer task |
| 110–120 min | recap, retrieval check, and homework briefing |

Use shorter activity cycles for younger learners. Do not pad a short source to fill two hours; add purposeful retrieval, retelling, transfer, or related practice instead.

## Generate selected deliverables

Read [references/deliverable-specs.md](references/deliverable-specs.md) and create only the selected deliverables. When several are selected, generate them from `teaching-blueprint.md` and preserve identical terminology, question numbering, answers, and difficulty.

Recommended filenames:

- `teaching-blueprint.md`
- `teacher-script.docx`
- `lesson-slides.pptx`
- `class-practice.docx` and `class-practice-answer-key.docx`
- `homework.docx` and `homework-answer-key.docx`

Place student-facing materials and answer keys in separate files. Never expose later answers on an earlier PPT slide or exercise page.

## Quality review

Before delivery, verify:

- The lesson timing adds up to 120 minutes and includes interaction rather than two hours of monologue.
- Every source-question answer is supported by the passage, a supplied key, or a clearly explained inference.
- The Chinese explanation is natural and teacher-like; English examples are accurate.
- The PPT shows what the student needs to see, while private reminders stay in the teacher script.
- Practice checks the lesson objective; homework includes retrieval plus a small transfer task.
- All artifacts use the same terms, examples, question IDs, and answers.
- Copyrighted source text is not reproduced beyond what the user supplied or what the source permits.
- Factual background claims and current exam-format claims are sourced.

For PPTX, render the slides, inspect every page for overflow, clipping, weak contrast, answer leakage, and excessive text, then complete at least one fix-and-verify cycle. For DOCX scripts and worksheets, render every page to images and inspect response space, table wrapping, page breaks, checkbox size, and answer separation before delivery.

Finish with a short `teacher-review-notes.md` listing decisions, uncertainties, and the few items the teacher should verify before class. Do not claim the lesson is classroom-ready when unresolved answer or source issues remain.
