
import pretty_midi

# Initialize the MIDI file
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Drums: Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Calculate note durations (160 BPM => 0.375s per beat)
beat = 0.375

# Bar 1: Drums only
bar_start = 0.0
bar_end = 1.5

# Kick on 1 and 3
kick_notes = [bar_start, bar_start + 2 * beat]
for time in kick_notes:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + beat)
    drums.notes.append(note)

# Snare on 2 and 4
snare_notes = [bar_start + beat, bar_start + 3 * beat]
for time in snare_notes:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + beat)
    drums.notes.append(note)

# Hihat on every eighth note
hihat_notes = [bar_start + i * beat / 2 for i in range(8)]
for time in hihat_notes:
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + beat / 2)
    drums.notes.append(note)

# Bar 2-4: Full quartet (1.5 - 6.0s)
bar_start = 1.5
bar_end = 6.0

# sax motif: two short phrases. First in bar 2, second in bar 4
# motif: D - F# - B - D (F# is the 3rd, B is the 7th)
# First phrase: D, F#, B, D — 16th notes, starting on beat 1

sax_notes = [
    (bar_start + 0.0, 62),  # D5
    (bar_start + 0.375, 66),  # F#5
    (bar_start + 0.75, 67),  # G (Bb in D minor? Wait, D minor has Bb, but we're in D major. No, B is the 7th in D major. Let's keep it as D major with a minor 7th to give it that tension.)
    (bar_start + 1.125, 62),  # D5
    (bar_start + 2.0, 62),  # D5
    (bar_start + 2.375, 66),  # F#5
    (bar_start + 2.75, 67),  # G
    (bar_start + 3.125, 62)  # D5
]

for time, pitch in sax_notes:
    note = pretty_midi.Note(velocity=100, pitch=pitch, start=time, end=time + 0.1875)
    sax.notes.append(note)

# Marcus: walking bass line in D
# Chromatic approach to each chord, walking line

# Chords for the song (D7, F#m7, Bm7, D7) — the classic "D minor" sound with a dominant seventh on D
# Walking bass line in D minor: D, C, B, A, G, F#, E, D (chromatic approach to D)

bass_notes = [
    (bar_start, 62),  # D3
    (bar_start + beat, 60),  # C3
    (bar_start + 2 * beat, 59),  # B3
    (bar_start + 3 * beat, 57),  # A3
    (bar_start + 4 * beat, 65),  # G3
    (bar_start + 5 * beat, 64),  # F#3
    (bar_start + 6 * beat, 62),  # E3
    (bar_start + 7 * beat, 62)   # D3
]

for time, pitch in bass_notes:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=time, end=time + beat)
    bass.notes.append(note)

# Diane: Piano comping on 2 and 4 with 7th chords

# 7th chords for the first four bars: D7 (bar 1), F#m7 (bar 2), Bm7 (bar 3), D7 (bar 4)
# Play on 2 and 4 — bar 2: F#m7 on beat 2, bar 3: Bm7 on beat 2, bar 4: D7 on beat 2

# D7: D, F#, A, C
# F#m7: F#, A, C, E
# Bm7: B, D, F#, A
# D7 again on beat 4

piano_notes = []

# Bar 2: F#m7 on beat 2 (1.5 + beat = 2.0)
for pitch in [66, 69, 71, 74]:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=2.0, end=2.0 + beat / 2)
    piano_notes.append(note)

# Bar 3: Bm7 on beat 2 (1.5 + 2 * beat = 3.0)
for pitch in [71, 62, 66, 69]:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=3.0, end=3.0 + beat / 2)
    piano_notes.append(note)

# Bar 4: D7 on beat 2 (1.5 + 3 * beat = 4.0)
for pitch in [62, 66, 69, 71]:
    note = pretty_midi.Note(velocity=80, pitch=pitch, start=4.0, end=4.0 + beat / 2)
    piano_notes.append(note)

for note in piano_notes:
    piano.notes.append(note)

# Drums for bars 2-4: Same pattern as bar 1
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 2
bar_start = 1.5
kick_notes = [bar_start, bar_start + 2 * beat]
for time in kick_notes:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + beat)
    drums.notes.append(note)

snare_notes = [bar_start + beat, bar_start + 3 * beat]
for time in snare_notes:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + beat)
    drums.notes.append(note)

hihat_notes = [bar_start + i * beat / 2 for i in range(8)]
for time in hihat_notes:
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + beat / 2)
    drums.notes.append(note)

# Bar 3
bar_start = 1.5 + 2 * beat
kick_notes = [bar_start, bar_start + 2 * beat]
for time in kick_notes:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + beat)
    drums.notes.append(note)

snare_notes = [bar_start + beat, bar_start + 3 * beat]
for time in snare_notes:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + beat)
    drums.notes.append(note)

hihat_notes = [bar_start + i * beat / 2 for i in range(8)]
for time in hihat_notes:
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + beat / 2)
    drums.notes.append(note)

# Bar 4
bar_start = 1.5 + 4 * beat
kick_notes = [bar_start, bar_start + 2 * beat]
for time in kick_notes:
    note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + beat)
    drums.notes.append(note)

snare_notes = [bar_start + beat, bar_start + 3 * beat]
for time in snare_notes:
    note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + beat)
    drums.notes.append(note)

hihat_notes = [bar_start + i * beat / 2 for i in range(8)]
for time in hihat_notes:
    note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + beat / 2)
    drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
