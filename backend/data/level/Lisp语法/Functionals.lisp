(defun partial (func &rest args1)
  (lambda (&rest args2)
    (apply func (append args1 args2))))

(defun auto-curry (fn num-args)
  (lambda (&rest args)
    (if (>= (length args) num-args)
        (apply fn args)
        (auto-curry (apply (partial #'partial fn) args)
                    (- num-args (length args))))))

(defmacro defun-auto-curry (fn-name (&rest args) &body body)
  (let ((currying-args (gensym)))
    `(defun ,fn-name (&rest ,currying-args)
       (apply (auto-curry (lambda (,@args) ,@body)
                          ,(length args))
           ,currying-args))))