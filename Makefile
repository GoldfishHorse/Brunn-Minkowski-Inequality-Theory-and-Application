PROJECT_NAME := Brunn-Minkowski不等式理论与应用
OUTPUT_DIR := output
LATEXMK := latexmk
LATEXMK_FLAGS := -pdf -output-directory=$(OUTPUT_DIR) -f -xelatex -interaction=nonstopmode -shell-escape

.PHONY: all clean
all:
	@echo "Building $(PROJECT_NAME).pdf"
	@mkdir -p $(OUTPUT_DIR)
	$(LATEXMK) $(LATEXMK_FLAGS) main.tex
	@mv "$(OUTPUT_DIR)/main.pdf" "$(OUTPUT_DIR)/$(PROJECT_NAME).pdf" 2>/dev/null || true
	@echo "Build completed: $(OUTPUT_DIR)/$(PROJECT_NAME).pdf"

clean:
	@echo "Cleaning temporary files..."
	cd $(OUTPUT_DIR) && rm -f *.aux *.log *.idx *.ind *.ilg *.thm *.toc *.blg *.bbl *.bcf *.out *.fls *.fdb_latexmk *.run.xml *.synctex.gz *.xdv *.lof *.lot *.nav *.snm *.vrb && cd ..

