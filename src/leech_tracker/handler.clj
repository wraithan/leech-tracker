(ns leech-tracker.handler
  (:use compojure.core)
  (:require [cheshire.core :as json]
            [clabango.parser :refer [render-file]]
            [clojure.java.jdbc :as sql]
            [compojure.route :as route]
            [compojure.handler :as handler]
            [ring.middleware.session :as session]))

(defn get-context [request]
  {:session (get request :session)})

(defn render-with-context [request file extra-context]
  (render-file file (merge (get-context request) extra-context)))

(defroutes app-routes
  (GET "/" [request]
       (render-with-context request "leech_tracker/templates/index.html" {}))
  (GET "/blocked/" [request]
       (render-with-context request "leech_tracker/templates/blocked.html" {}))
  (POST "/blocked/" [request body]
        (sql/with-connection (System/getenv "DATABASE_URL")
          (sql/insert-record
           :blocked {:url (get (json/parse-string (slurp body) true) :url)})))
  (GET "/list/" [request]
       (sql/with-connection (System/getenv "DATABASE_URL")
         (json/generate-string (sql/with-query-results results
                                 ["SELECT * FROM blocked"]
                                 (into [] results)))))
  (route/resources "/")
  (route/not-found
   (render-file "leech_tracker/templates/404.html" {})))

(def app
  (session/wrap-session (handler/site app-routes)))
