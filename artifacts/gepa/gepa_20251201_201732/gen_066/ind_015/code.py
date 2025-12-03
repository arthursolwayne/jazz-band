
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Create instruments
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')

bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)
sax = pretty_midi.Instrument(program=sax_program)

# Add instruments to the PrettyMIDI object
pm.instruments.append(bass)
pm.instruments.append(piano)
pm.instruments.append(drums)
pm.instruments.append(sax)

# Define note durations in seconds
beat = 0.375  # 160 BPM = 60 / 160 = 0.375 seconds per beat
bar = 1.5  # 4 beats per bar

# --------------------------
# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# --------------------------

# Kick on 1 and 3
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=0.0, end=0.15),
              pretty_midi.Note(velocity=100, pitch=36, start=beat * 2, end=beat * 2 + 0.15)]
drums.notes.extend(kick_notes)

# Snare on 2 and 4
snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=beat * 1, end=beat * 1 + 0.1),
               pretty_midi.Note(velocity=100, pitch=38, start=beat * 3, end=beat * 3 + 0.1)]
drums.notes.extend(snare_notes)

# Hihat on every eighth note (8 notes per bar)
hihat_notes = []
for i in range(8):
    start = i * beat * 0.5
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.05))
drums.notes.extend(hihat_notes)

# --------------------------
# Bar 2: All instruments in
# --------------------------

# --------------------------
# Bass: Walking line (D2-G2, D-F-G), roots and fifths with chromatic approaches
# D2 (MIDI 38), F (MIDI 41), G (MIDI 43), G# (MIDI 44), D3 (MIDI 46)
# Time: bar 2 start
# --------------------------

bass_notes = [
    pretty_midi.Note(velocity=80, pitch=38, start=bar, end=bar + 0.25),  # D2
    pretty_midi.Note(velocity=80, pitch=41, start=bar + beat, end=bar + beat + 0.25),  # F
    pretty_midi.Note(velocity=80, pitch=43, start=bar + beat * 2, end=bar + beat * 2 + 0.25),  # G
    pretty_midi.Note(velocity=80, pitch=44, start=bar + beat * 3, end=bar + beat * 3 + 0.25),  # G#
]

bass.notes.extend(bass_notes)

# --------------------------
# Piano: Open voicings, different chord each bar, resolve on the last
# Bar 2: Dm7 (D F A C)
# Bar 3: Gm7 (G Bb D F)
# Bar 4: Cm7 (C Eb G Bb)
# --------------------------

# Bar 2: Dm7 (D, F, A, C) - open voicing
note_times = np.array([0.0, 0.25, 0.5, 0.75])
for t, pitch in zip(note_times, [62, 65, 69, 67]):  # D4, F4, A4, C4
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar + t, end=bar + t + 0.1))

# Bar 3: Gm7 (G, Bb, D, F)
note_times = np.array([0.0, 0.25, 0.5, 0.75])
for t, pitch in zip(note_times, [67, 69, 62, 65]):  # G4, Bb4, D4, F4
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar + beat + t, end=bar + beat + t + 0.1))

# Bar 4: Cm7 (C, Eb, G, Bb)
note_times = np.array([0.0, 0.25, 0.5, 0.75])
for t, pitch in zip(note_times, [60, 63, 67, 69]):  # C4, Eb4, G4, Bb4
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=pitch, start=bar + beat * 2 + t, end=bar + beat * 2 + t + 0.1))

# --------------------------
# Drums: Bar 2-4
# Continue with the same pattern: kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# --------------------------

# Bar 2
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar, end=bar + 0.15),
              pretty_midi.Note(velocity=100, pitch=36, start=bar + beat * 2, end=bar + beat * 2 + 0.15)]
drums.notes.extend(kick_notes)

snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar + beat, end=bar + beat + 0.1),
               pretty_midi.Note(velocity=100, pitch=38, start=bar + beat * 3, end=bar + beat * 3 + 0.1)]
drums.notes.extend(snare_notes)

hihat_notes = []
for i in range(8):
    start = bar + i * beat * 0.5
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.05))
drums.notes.extend(hihat_notes)

# Bar 3
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar + beat, end=bar + beat + 0.15),
              pretty_midi.Note(velocity=100, pitch=36, start=bar + beat * 3, end=bar + beat * 3 + 0.15)]
drums.notes.extend(kick_notes)

snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar + beat * 2, end=bar + beat * 2 + 0.1),
               pretty_midi.Note(velocity=100, pitch=38, start=bar + beat * 4, end=bar + beat * 4 + 0.1)]
drums.notes.extend(snare_notes)

hihat_notes = []
for i in range(8):
    start = bar + beat + i * beat * 0.5
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.05))
drums.notes.extend(hihat_notes)

# Bar 4
kick_notes = [pretty_midi.Note(velocity=100, pitch=36, start=bar + beat * 2, end=bar + beat * 2 + 0.15),
              pretty_midi.Note(velocity=100, pitch=36, start=bar + beat * 4, end=bar + beat * 4 + 0.15)]
drums.notes.extend(kick_notes)

snare_notes = [pretty_midi.Note(velocity=100, pitch=38, start=bar + beat * 3, end=bar + beat * 3 + 0.1),
               pretty_midi.Note(velocity=100, pitch=38, start=bar + beat * 5, end=bar + beat * 5 + 0.1)]
drums.notes.extend(snare_notes)

hihat_notes = []
for i in range(8):
    start = bar + beat * 2 + i * beat * 0.5
    hihat_notes.append(pretty_midi.Note(velocity=90, pitch=42, start=start, end=start + 0.05))
drums.notes.extend(hihat_notes)

# --------------------------
# Sax: One short motif, start it, leave it hanging, come back and finish it
# Dm: D, F, A, C
# Motif: D F A | G Bb D | C F D
# --------------------------

# Bar 2: D F A
notes = [
    pretty_midi.Note(velocity=100, pitch=62, start=bar, end=bar + 0.25),  # D4
    pretty_midi.Note(velocity=100, pitch=65, start=bar + 0.25, end=bar + 0.5),  # F4
    pretty_midi.Note(velocity=100, pitch=69, start=bar + 0.5, end=bar + 0.75),  # A4
]

sax.notes.extend(notes)

# Bar 3: G Bb D
notes = [
    pretty_midi.Note(velocity=100, pitch=67, start=bar + beat, end=bar + beat + 0.25),  # G4
    pretty_midi.Note(velocity=100, pitch=69, start=bar + beat + 0.25, end=bar + beat + 0.5),  # Bb4
    pretty_midi.Note(velocity=100, pitch=62, start=bar + beat + 0.5, end=bar + beat + 0.75),  # D4
]

sax.notes.extend(notes)

# Bar 4: C F D
notes = [
    pretty_midi.Note(velocity=100, pitch=60, start=bar + beat * 2, end=bar + beat * 2 + 0.25),  # C4
    pretty_midi.Note(velocity=100, pitch=65, start=bar + beat * 2 + 0.25, end=bar + beat * 2 + 0.5),  # F4
    pretty_midi.Note(velocity=100, pitch=62, start=bar + beat * 2 + 0.5, end=bar + beat * 2 + 0.75),  # D4
]

sax.notes.extend(notes)

# Write the MIDI file
pm.write("dante_intro.mid")
