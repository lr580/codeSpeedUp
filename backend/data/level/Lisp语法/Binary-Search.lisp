(defun bin-search (lst key &optional (start 0) (end (length lst)))
    (if (>= start end)
      nil
      (let* ((mid (ash (+ start end) -1)))
        (cond ((= key (nth mid lst)) mid)
              ((< key (nth mid lst)) (bin-search lst key start mid))
              ((> key (nth mid lst)) (bin-search lst key (+ mid 1) end))))))