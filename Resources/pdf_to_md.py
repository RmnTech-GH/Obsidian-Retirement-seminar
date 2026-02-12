"""
PDF → Markdown 변환 스크립트
사용법:
    python pdf_to_md.py input.pdf                    # 같은 폴더에 .md 저장
    python pdf_to_md.py input.pdf -o output_dir      # 지정 폴더에 저장
    python pdf_to_md.py folder_path                  # 폴더 내 모든 PDF 일괄 변환
"""

import sys
import os
import re
import argparse
from pathlib import Path

import pymupdf4llm


def convert_pdf_to_md(pdf_path: str, output_dir: str | None = None) -> str:
    """단일 PDF 파일을 Markdown으로 변환"""
    pdf_path = Path(pdf_path)
    if not pdf_path.exists():
        print(f"[오류] 파일을 찾을 수 없습니다: {pdf_path}")
        return ""

    print(f"[변환 중] {pdf_path.name} ...")

    # 출력 경로 결정
    if output_dir:
        out_dir = Path(output_dir)
    else:
        out_dir = pdf_path.parent
    out_dir.mkdir(parents=True, exist_ok=True)

    # 이미지 저장 폴더: {출력폴더}/{PDF이름}_images/
    image_dir = out_dir / f"{pdf_path.stem}_images"
    image_dir.mkdir(parents=True, exist_ok=True)

    md_text = pymupdf4llm.to_markdown(
        str(pdf_path),
        write_images=True,
        image_path=str(image_dir),
        image_format="png",
        image_size_limit=0.05,  # 페이지 면적의 5% 미만 이미지는 무시
    )

    # 이미지 경로를 Obsidian 형식 ![[파일명]]으로 변환
    def to_obsidian_embed(match):
        img_path = match.group(1)
        filename = Path(img_path).name
        return f"![[{filename}]]"

    md_text = re.sub(r'!\[[^\]]*\]\(([^)]+)\)', to_obsidian_embed, md_text)

    out_path = out_dir / f"{pdf_path.stem}.md"
    out_path.write_text(md_text, encoding="utf-8")
    print(f"[완료] {out_path}")
    return str(out_path)


def convert_folder(folder_path: str, output_dir: str | None = None) -> list[str]:
    """폴더 내 모든 PDF를 일괄 변환"""
    folder = Path(folder_path)
    pdf_files = sorted(folder.glob("*.pdf"))

    if not pdf_files:
        print(f"[알림] PDF 파일이 없습니다: {folder}")
        return []

    print(f"[일괄 변환] {len(pdf_files)}개 PDF 발견\n")
    results = []
    for pdf in pdf_files:
        result = convert_pdf_to_md(str(pdf), output_dir)
        if result:
            results.append(result)

    print(f"\n[요약] {len(results)}/{len(pdf_files)}개 변환 완료")
    return results


def main():
    parser = argparse.ArgumentParser(description="PDF → Markdown 변환")
    parser.add_argument("input", help="PDF 파일 또는 폴더 경로")
    parser.add_argument("-o", "--output", help="출력 폴더 경로 (미지정 시 원본과 같은 폴더)")
    args = parser.parse_args()

    input_path = Path(args.input)

    if input_path.is_dir():
        convert_folder(str(input_path), args.output)
    elif input_path.is_file() and input_path.suffix.lower() == ".pdf":
        convert_pdf_to_md(str(input_path), args.output)
    else:
        print(f"[오류] 유효한 PDF 파일 또는 폴더가 아닙니다: {input_path}")
        sys.exit(1)


if __name__ == "__main__":
    main()
