(defproject leech-tracker "0.1.0-SNAPSHOT"
  :description "FIXME: write description"
  :url "http://example.com/FIXME"
  :dependencies [[org.clojure/clojure "1.4.0"]
                 [compojure "1.1.5"]]
  :plugins [[lein-ring "0.8.0"]]
  :ring {:handler leech-tracker.handler/app}
  :profiles
  {:dev {:dependencies [[ring-mock "0.1.3"]]}})
