
import pretty_midi

midi = pretty_midi.PrettyMIDI()

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# 160 BPM, 4/4
# Beat = 0.375s, Bar = 1.5s
# Bar 1: 0.0 - 1.5s
# Bar 2: 1.5 - 3.0s
# Bar 3: 3.0 - 4.5s
# Bar 4: 4.5 - 6.0s

KICK = 36
SNARE = 38
HIHAT = 42

# Key: D minor. The sound of Newark at 2am.

# ═══════════════════════════════════════════════════════════════
# BAR 1: Little Ray alone. Make them wait.
# ═══════════════════════════════════════════════════════════════

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=0.0, end=0.15))
drums.notes.append(pretty_midi.Note(velocity=90, pitch=KICK, start=0.75, end=0.9))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=95, pitch=SNARE, start=0.375, end=0.45))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=1.125, end=1.2))

# Hihat on every eighth
for i in range(8):
    t = i * 0.1875
    vel = 70 if i % 2 == 0 else 55
    drums.notes.append(pretty_midi.Note(velocity=vel, pitch=HIHAT, start=t, end=t + 0.1))

# ═══════════════════════════════════════════════════════════════
# BARS 2-4: Full quartet. This is the moment.
# ═══════════════════════════════════════════════════════════════

# Little Ray continues - bars 2, 3, 4
for bar in range(3):
    bar_start = 1.5 + bar * 1.5
    
    # Kick on 1 and 3
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start, end=bar_start + 0.15))
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=KICK, start=bar_start + 0.75, end=bar_start + 0.9))
    
    # Snare on 2 and 4
    drums.notes.append(pretty_midi.Note(velocity=95, pitch=SNARE, start=bar_start + 0.375, end=bar_start + 0.45))
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 1.125, end=bar_start + 1.2))
    
    # Hihat eighths
    for i in range(8):
        t = bar_start + i * 0.1875
        vel = 70 if i % 2 == 0 else 55
        drums.notes.append(pretty_midi.Note(velocity=vel, pitch=HIHAT, start=t, end=t + 0.1))

# ═══════════════════════════════════════════════════════════════
# Marcus: Walking bass in D minor. Never the same note twice.
# Chromatic approaches, root movement. The anchor.
# ═══════════════════════════════════════════════════════════════

# D2=38, E2=40, F2=41, G2=43, A2=45, Bb2=46, C3=48, Db3=49, D3=50

marcus_line = [
    # Bar 2: D minor established
    (1.5, 38, 0.35),      # D2 - root, strong
    (1.875, 40, 0.32),    # E2 - climbing
    (2.25, 41, 0.32),     # F2 - the minor third's friend  
    (2.625, 40, 0.32),    # E2 - chromatic approach back
    
    # Bar 3: Move to the A, the dominant pull
    (3.0, 45, 0.35),      # A2 - dominant
    (3.375, 44, 0.32),    # Ab2 - chromatic below
    (3.75, 43, 0.32),     # G2 - stepping down
    (4.125, 42, 0.32),    # Gb2 - chromatic tension
    
    # Bar 4: Resolve back home
    (4.5, 41, 0.35),      # F2 - relative major color
    (4.875, 43, 0.32),    # G2 - climbing
    (5.25, 45, 0.32),     # A2 - dominant again
    (5.625, 37, 0.35),    # Db2 - chromatic approach to D
]

for start, pitch, dur in marcus_line:
    bass.notes.append(pretty_midi.Note(velocity=85, pitch=pitch, start=start, end=start + dur))

# ═══════════════════════════════════════════════════════════════
# Diane: Comping on 2 and 4. 7th chords. Angry but controlled.
# ═══════════════════════════════════════════════════════════════

# Dm7: D F A C (62 65 69 72)
# Am7: A C E G (57 60 64 67)  
# Gm7: G Bb D F (55 58 62 65)
# A7b9: A C# E G Bb (57 61 64 67 70) - the tension

diane_chords = [
    # Bar 2: Dm7 on 2 and 4
    (1.875, [62, 65, 69, 72], 0.28),   # Dm7 on 2
    (2.625, [62, 65, 69, 72], 0.28),   # Dm7 on 4
    
    # Bar 3: Am7 to A7b9 - she's building something
    (3.375, [57, 60, 64, 67], 0.28),   # Am7 on 2
    (4.125, [57, 61, 64, 70], 0.28),   # A7b9 on 4 - the anger shows
    
    # Bar 4: Gm7 to Dm7 - bring it home
    (4.875, [55, 58, 62, 65], 0.28),   # Gm7 on 2
    (5.625, [62, 65, 69, 72], 0.28),   # Dm7 on 4 - resolution
]

for start, pitches, dur in diane_chords:
    for p in pitches:
        piano.notes.append(pretty_midi.Note(velocity=72, pitch=p, start=start, end=start + dur))

# ═══════════════════════════════════════════════════════════════
# Dante: The motif. One phrase. Leave it hanging. Come back.
# This is what Wayne needs to hear.
# ═══════════════════════════════════════════════════════════════

# The motif: D up to A, bend to Bb, fall to F. A question.
# Then silence. Let it breathe.
# Come back: F up to A, land on D. The answer.

# Tenor sax range: D3 (50) to D6 (86)
# Playing in the middle: D4=62, F4=65, A4=69, Bb4=70, D5=74

dante_phrase = [
    # Bar 2: The question - start on beat 2, syncopated
    (1.95, 62, 0.25, 90),     # D4 - pickup, soft
    (2.25, 69, 0.5, 100),     # A4 - reach up, hold it
    (2.8, 70, 0.35, 95),      # Bb4 - the bend, the blue note
    (3.2, 65, 0.4, 85),       # F4 - fall, leave it hanging
    
    # Bar 3: Silence. Let them wonder. Just breath.
    # (Nothing. The space IS the music.)
    
    # Bar 4: The answer - beat 2, come back strong
    (4.9, 65, 0.22, 88),      # F4 - pickup
    (5.15, 69, 0.3, 100),     # A4 - reach again
    (5.5, 74, 0.45, 105),     # D5 - land high, resolution with authority
]

for start, pitch, dur, vel in dante_phrase:
    sax.notes.append(pretty_midi.Note(velocity=vel, pitch=pitch, start=start, end=start + dur))

# ═══════════════════════════════════════════════════════════════

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
