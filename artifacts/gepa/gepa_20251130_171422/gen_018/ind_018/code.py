
import pretty_midi

# Create a new MIDI file with a tempo of 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Sax
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum note numbers
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray on drums (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth

# Bar 1 (0.0 - 1.5s)
# 1.0s = beat, 0.375s = 160 BPM = 60/160 = 0.375
bar_start = 0.0
bar_duration = 1.5

# Kick on 1 and 3 (beats 0 and 2)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start, end=bar_start + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=bar_start + 0.75, end=bar_start + 0.75 + 0.375))

# Snare on 2 and 4 (beats 1 and 3)
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 0.375, end=bar_start + 0.375 + 0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=SNARE, start=bar_start + 0.75 * 3, end=bar_start + 0.75 * 3 + 0.375))

# Hi-hat on every eighth note
for i in range(8):
    start = bar_start + (i * 0.375)
    end = start + 0.375
    drums.notes.append(pretty_midi.Note(velocity=80, pitch=HIHAT, start=start, end=end))

# Bar 2-4: Full band (1.5s - 6.0s)
bar_start = 1.5

# Bass: Walking line with chromatic approaches (F7 chord: F A C E)
# F, Gb, G, A, Bb, B, C, Db, D, Eb, E, F#, G, Ab, A, Bb, B, C
bass_line = [
    71,  # F (C4)
    70,  # E (Bb4)
    69,  # D (Ab4)
    68,  # C (G4)
    67,  # B (F4)
    66,  # Bb (E4)
    65,  # A (D4)
    64,  # G (C4)
    63,  # F# (Bb3)
    62,  # F (A3)
    61,  # E (G3)
    60,  # D (F3)
    59,  # C (Eb3)
    58,  # B (D3)
    57,  # Bb (C3)
    56,  # A (Bb2)
    55,  # G (A2)
    54,  # F# (G2)
    53,  # F (F2)
]

# Time between notes (1/16 note at 160 BPM)
note_duration = 0.375 / 2  # 1/16 = 0.375, 1/8 = 0.75, 1/4 = 1.5s
note_start = bar_start

for note in bass_line:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=note_start, end=note_start + note_duration))
    note_start += note_duration

# Piano: 7th chords on 2 and 4, comping
# F7 chord: F, A, C, E
# Root (F) on beat 1, 3, 5, 7
# 7th (E) on beat 2, 4, 6, 8

# F7 chord notes (F, A, C, E)
F = 71
A = 74
C = 72
E = 76

# Bars 2-4: 3 bars (1.5s - 6.0s)
# 8 beats per bar, 3 bars = 24 beats
for bar in range(2, 5):  # Bars 2, 3, 4
    bar_time = (bar - 1) * bar_duration
    for beat in range(8):  # 8 beats per bar
        if beat % 2 == 0:  # On 1, 3, 5, 7
            piano.notes.append(pretty_midi.Note(velocity=80, pitch=F, start=bar_time + beat * 0.375, end=bar_time + beat * 0.375 + 0.15))
            piano.notes.append(pretty_midi.Note(velocity=80, pitch=C, start=bar_time + beat * 0.375, end=bar_time + beat * 0.375 + 0.15))
            piano.notes.append(pretty_midi.Note(velocity=80, pitch=A, start=bar_time + beat * 0.375, end=bar_time + beat * 0.375 + 0.15))
        else:  # On 2, 4, 6, 8
            piano.notes.append(pretty_midi.Note(velocity=80, pitch=E, start=bar_time + beat * 0.375, end=bar_time + beat * 0.375 + 0.15))
            piano.notes.append(pretty_midi.Note(velocity=80, pitch=C, start=bar_time + beat * 0.375, end=bar_time + beat * 0.375 + 0.15))
            piano.notes.append(pretty_midi.Note(velocity=80, pitch=A, start=bar_time + beat * 0.375, end=bar_time + beat * 0.375 + 0.15))

# Sax: Your moment. One short motif, start it, leave it hanging, come back and finish it.
# Let's use a simple F7 motif: F - A - C - E, with a suspension and release
# 1st bar: F - A - C - E (beat 1, 2, 3, 4)
# 2nd bar: F - (rest) - C - E

# Bar 2: Start the motif
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=bar_start + 0.0, end=bar_start + 0.375))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=bar_start + 0.375, end=bar_start + 0.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=bar_start + 0.75, end=bar_start + 1.125))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=bar_start + 1.125, end=bar_start + 1.5))

# Bar 3: Let it hang (rest on A, then resolve)
# Rest on A (beat 1), then resolve to C and E on beat 3 and 4
sax.notes.append(pretty_midi.Note(velocity=100, pitch=74, start=bar_start + 1.5, end=bar_start + 1.875))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=72, start=bar_start + 2.25, end=bar_start + 2.625))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=76, start=bar_start + 2.625, end=bar_start + 3.0))

# Add the instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
