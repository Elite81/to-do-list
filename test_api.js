import http from 'k6/http';
import { check, sleep } from 'k6';

// 1. Configuration: Proactive Performance Monitoring
export const options = {
  stages: [
    { duration: '30s', target: 5 },  // Ramp up to 5 users (safe for Render Free)
    { duration: '1m', target: 10 }, // Push to 10 users to test limits
    { duration: '30s', target: 0 },  // Ramp down
  ],
  thresholds: {
    // If more than 10% of requests fail, the test is marked as failed
    http_req_failed: ['rate<0.10'], 
    // 95% of requests should ideally be under 1.5s on free-tier hosting
    http_req_duration: ['p(95)<1500'], 
  },
};

const BASE_URL = 'https://tasks-7ugz.onrender.com';

export default function () {
  // --- STEP 1: Homepage Visit ---
  // This populates the CookieJar with the 'csrftoken'
  let homeRes = http.get(`${BASE_URL}/`);
  
  check(homeRes, {
    'home status is 200': (r) => r.status === 200,
    'home carries cookies': (r) => r.cookies.csrftoken !== undefined,
  });

  // Simulated "Think Time" - mimics a real human user
  sleep(2);

  // --- STEP 2: Search Functionality ---
  let searchRes = http.get(`${BASE_URL}/search/?q=task`);
  
  check(searchRes, {
    'search status is 200': (r) => r.status === 200,
  });

  sleep(1);

  // --- STEP 3: Create Task Form (GET) ---
  // Testing the "New Task" page load performance
  let newTaskPage = http.get(`${BASE_URL}/new_task/`);
  
  check(newTaskPage, {
    'new_task page loaded': (r) => r.status === 200,
  });

  // Final sleep before the next iteration
  sleep(2);
}