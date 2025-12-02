
import pretty_midi

# Initialize MIDI with tempo and instruments
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes
kick = 36
snare = 38
hihat = 42

# Time per bar (at 160 BPM, 4/4 time)
bar_duration = 1.5  # seconds
beat_duration = 0.375  # seconds

# ------------------------
# Bar 1: Drums only (0.0 - 1.5s)
# Little Ray plays a simple, tight kick/snare pattern with hihat
# A question in the air — setting up the mood

for bar in range(1):
    start_time = bar * bar_duration
    # Kick on 1 and 3
    kick_notes = [start_time, start_time + beat_duration * 2]
    for time in kick_notes:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    
    # Snare on 2 and 4
    snare_notes = [start_time + beat_duration, start_time + beat_duration * 3]
    for time in snare_notes:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    
    # Hihat on every eighth note
    for i in range(8):
        time = start_time + i * beat_duration / 2
        note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.05)
        drums.notes.append(note)

# ------------------------
# Bar 2: Full quartet (1.5 - 3.0s)
# You begin the melody — a simple, haunting motif

# Saxophone (Dante): Tenor Sax, D minor motif, phrased with space and tension
# Notes: D (D4), F (F4), G (G4), A (A4) → D minor scale, starting on D
# Play the first two notes, leave a rest, then come back

sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=1.5, end=1.6),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=1.6, end=1.7),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=1.8, end=1.9),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=2.0, end=2.1)   # A4
]
sax.notes.extend(sax_notes)

# Bass (Marcus): Walking line, chromatic under the sax
# Notes: D, C#, D, E → chromatic approach to the D, then to E

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=1.5, end=1.6),  # D3
    pretty_midi.Note(velocity=80, pitch=44, start=1.6, end=1.7),  # C#3
    pretty_midi.Note(velocity=80, pitch=45, start=1.7, end=1.8),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=1.8, end=1.9),  # E3
    pretty_midi.Note(velocity=80, pitch=47, start=1.9, end=2.0),  # E3
]
bass.notes.extend(bass_notes)

# Piano (Diane): 7th chords, comp on 2 and 4
# D7 in root position, then G7 (ii-V) leading to Cmaj7

# D7 (D, F#, A, C)
note_d7 = [
    pretty_midi.Note(velocity=90, pitch=62, start=1.5, end=1.6),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=1.5, end=1.6),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=1.5, end=1.6),  # C#5
    pretty_midi.Note(velocity=90, pitch=64, start=1.5, end=1.6),  # F#4
]
# G7 (G, B, D, F)
note_g7 = [
    pretty_midi.Note(velocity=90, pitch=67, start=2.0, end=2.1),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=2.0, end=2.1),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.1),  # D5
    pretty_midi.Note(velocity=90, pitch=69, start=2.0, end=2.1),  # F4
]
piano.notes.extend(note_d7 + note_g7)

# Drums continue
# Same pattern as before, but now with the rest of the band
for bar in range(1):
    start_time = 1.5 + bar * bar_duration
    kick_notes = [start_time, start_time + beat_duration * 2]
    for time in kick_notes:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    
    snare_notes = [start_time + beat_duration, start_time + beat_duration * 3]
    for time in snare_notes:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    
    for i in range(8):
        time = start_time + i * beat_duration / 2
        note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.05)
        drums.notes.append(note)

# ------------------------
# Bar 3: Full quartet (3.0 - 4.5s)
# You continue the motif — same notes, slightly delayed, more space

# Saxophone: same motif, but starting at 3.0s
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=3.0, end=3.1),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=3.1, end=3.2),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=3.3, end=3.4),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=3.5, end=3.6)   # A4
]
sax.notes.extend(sax_notes)

# Bass: chromatic line with more space
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=3.0, end=3.1),  # D3
    pretty_midi.Note(velocity=80, pitch=44, start=3.1, end=3.2),  # C#3
    pretty_midi.Note(velocity=80, pitch=45, start=3.2, end=3.3),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=3.4, end=3.5),  # E3
    pretty_midi.Note(velocity=80, pitch=47, start=3.5, end=3.6),  # E3
]
bass.notes.extend(bass_notes)

# Piano: D7 again, but with a space on beat 2
note_d7 = [
    pretty_midi.Note(velocity=90, pitch=62, start=3.0, end=3.1),  # D4
    pretty_midi.Note(velocity=90, pitch=67, start=3.0, end=3.1),  # A4
    pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.1),  # C#5
    pretty_midi.Note(velocity=90, pitch=64, start=3.0, end=3.1),  # F#4
]
piano.notes.extend(note_d7)

# Drums continue
for bar in range(1):
    start_time = 3.0 + bar * bar_duration
    kick_notes = [start_time, start_time + beat_duration * 2]
    for time in kick_notes:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    
    snare_notes = [start_time + beat_duration, start_time + beat_duration * 3]
    for time in snare_notes:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    
    for i in range(8):
        time = start_time + i * beat_duration / 2
        note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.05)
        drums.notes.append(note)

# ------------------------
# Bar 4: Full quartet (4.5 - 6.0s)
# You complete the motif — a resolution, a question answered

# Saxophone: finish the motif, hold the A a little longer
sax_notes = [
    pretty_midi.Note(velocity=110, pitch=62, start=4.5, end=4.6),  # D4
    pretty_midi.Note(velocity=110, pitch=65, start=4.6, end=4.7),  # F4
    pretty_midi.Note(velocity=110, pitch=67, start=4.8, end=4.9),  # G4
    pretty_midi.Note(velocity=110, pitch=69, start=4.9, end=5.3)   # A4 (sustained)
]
sax.notes.extend(sax_notes)

# Bass: chromatic line, ending on E
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=45, start=4.5, end=4.6),  # D3
    pretty_midi.Note(velocity=80, pitch=44, start=4.6, end=4.7),  # C#3
    pretty_midi.Note(velocity=80, pitch=45, start=4.7, end=4.8),  # D3
    pretty_midi.Note(velocity=80, pitch=47, start=4.8, end=5.0),  # E3
]
bass.notes.extend(bass_notes)

# Piano: G7 again, but now with a full comp
note_g7 = [
    pretty_midi.Note(velocity=90, pitch=67, start=4.5, end=4.6),  # G4
    pretty_midi.Note(velocity=90, pitch=71, start=4.5, end=4.6),  # B4
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.6),  # D5
    pretty_midi.Note(velocity=90, pitch=69, start=4.5, end=4.6),  # F4
]
piano.notes.extend(note_g7)

# Drums continue
for bar in range(1):
    start_time = 4.5 + bar * bar_duration
    kick_notes = [start_time, start_time + beat_duration * 2]
    for time in kick_notes:
        note = pretty_midi.Note(velocity=100, pitch=kick, start=time, end=time + 0.1)
        drums.notes.append(note)
    
    snare_notes = [start_time + beat_duration, start_time + beat_duration * 3]
    for time in snare_notes:
        note = pretty_midi.Note(velocity=100, pitch=snare, start=time, end=time + 0.1)
        drums.notes.append(note)
    
    for i in range(8):
        time = start_time + i * beat_duration / 2
        note = pretty_midi.Note(velocity=90, pitch=hihat, start=time, end=time + 0.05)
        drums.notes.append(note)

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
