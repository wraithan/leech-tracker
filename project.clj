(defproject leech-tracker "0.1.0-SNAPSHOT"
  :description "Tracks what sites LeechBlocked for you."
  :url "https://github.com/wraithan/leech-tracker"
  :dependencies [[org.clojure/clojure "1.4.0"]
                 [compojure "1.1.5"]
                 [org.clojure/java.jdbc "0.2.3"]
                 [postgresql "9.1-901.jdbc4"]]
  :plugins [[lein-ring "0.8.0"]]
  :ring {:handler leech-tracker.handler/app}
  :profiles
  {:dev {:dependencies [[ring-mock "0.1.3"]]}})
