import http from 'k6/http';
import { check, sleep } from 'k6';

// Test Configuratio
export const options = {
  stages: [
    { duration: '1m', target: 20 },   // Ramp up users
    { duration: '2m', target: 100 },  // Peak load
    { duration: '1m', target: 0 },    // Ramp down
  ],

  thresholds: {
    http_req_failed: ['rate<0.10'],     // Allow small failure rate
    http_req_duration: ['p(95)<5000'],  // 95% of requests < 5s
  },
};

const BASE_URL = 'https://tasks-7ugz.onrender.com';


// Main Test Scenario

export default function () {

  // STEP 1: Load form page
  // Capture session + CSRF token
  
  const formRes = http.get(`${BASE_URL}/new_task/`, {
    tags: { name: "load_task_form" }
  });

  check(formRes, {
    'form page loaded (200)': (r) => r.status === 200,
  });

  const jar = http.cookieJar();
  const cookies = jar.cookiesForURL(BASE_URL);

  let csrfToken = cookies.csrftoken ? cookies.csrftoken[0] : null;

  sleep(1);

  // Stop if CSRF token missing
  if (!csrfToken) {
    return;
  }

  // Unique task name per user
  const taskName = `task-VU${__VU}-ITER${__ITER}`;

  // STEP 2: Create Task
  const payload = {
    task: taskName,
    status: 'pending',
    priority: 'medium',
    description: 'Load testing task lifecycle',
    csrfmiddlewaretoken: csrfToken,
  };

  const params = {
    headers: {
      'Referer': `${BASE_URL}/new_task/`,
      'X-CSRFToken': csrfToken,
    },
    redirects: 1,
    tags: { name: "create_task" },
  };

  const createRes = http.post(
    `${BASE_URL}/new_task/`,
    payload,
    params
  );

  check(createRes, {
    'task creation not forbidden': (r) => r.status !== 403,
    'task creation success': (r) => r.status === 200 || r.status === 302,
  });

  sleep(1);

  // STEP 3: Search Task
  const searchRes = http.get(`${BASE_URL}/search/?q=${taskName}`, {
    tags: { name: "search_task" }
  });

  check(searchRes, {
    'search returned result': (r) => r.status === 200,
  });

  // Simulated User Think Time
  sleep(Math.random() * 4 + 2);
}