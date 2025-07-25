#!/bin/bash
node {
    stage 'build'
    echo 'build'

    stage 'tests'
    echo 'tests'

    stage 'end-to-end-tests'
    def e2e = build job:'end-to-end-tests', propagate: false
    result = e2e.result
    if (result.equals("SUCCESS")) {
        stage 'deploy'
        build 'deploy'
    } else {
        currentBuild.result = 'FAILURE'
    }
}