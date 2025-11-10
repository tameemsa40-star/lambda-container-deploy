FROM public.ecr.aws/lambda/python:3.11

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}

# (Optional) install dependencies
COPY requirements.txt  .
RUN pip install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

# Command to run Lambda
CMD ["app.handler"]