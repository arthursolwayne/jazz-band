
import pretty_midi
from pretty_midi import Note, Instrument

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI(initial_tempo=160)

# Set time signature (4/4)
pm.time_signature_changes = [pretty_midi.TimeSignature(numerator=4, denominator=4, time=0)]

# Define instruments
# Bass
bass_program = pretty_midi.instrument_name_to_program('Acoustic Bass')
bass = Instrument(program=bass_program, is_drum=False)

# Piano
piano_program = pretty_midi.instrument_name_to_program('Acoustic Grand Piano')
piano = Instrument(program=piano_program, is_drum=False)

# Drums
drum_program = pretty_midi.instrument_name_to_program('Acoustic Drum Kit')
drums = Instrument(program=drum_program, is_drum=True)

# Tenor Sax
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
sax = Instrument(program=sax_program, is_drum=False)

# Add instruments to the PrettyMIDI object
pm.instruments = [bass, piano, drums, sax]

# Define note durations in seconds
beat = 0.375  # 160 BPM => 60 / 160 = 0.375s per beat
half_beat = beat / 2
quarter_beat = beat / 4

# BAR 1: Drums only — build tension
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    # Bar 1
    (0, 36, 100, 0),  # Kick on beat 1
    (0, 38, 90, 0),   # Snare on beat 2
    (0, 42, 80, 0),   # Hihat on 1
    (0, 42, 80, half_beat),  # Hihat on 1.5
    (0, 36, 100, beat),  # Kick on beat 3
    (0, 38, 90, beat + half_beat),  # Snare on beat 4
    (0, 42, 80, beat + quarter_beat),  # Hihat on 3.25
    (0, 42, 80, beat + half_beat + quarter_beat),  # Hihat on 3.75
    (0, 42, 80, beat + beat),  # Hihat on 4
]

for note in drum_notes:
    dr = Note(
        pitch=note[0],
        start=note[2],
        end=note[2] + 0.1,
        velocity=note[3]
    )
    drums.notes.append(dr)

# BAR 2: Sax enters with the melody — sparse, emotional, unresolved
# D major scale: D E F# G A B C#
# We'll use a motif: D (beat 1), F# (beat 2), A (beat 3), rest (beat 4)
sax_notes = [
    (62, 0, 100),  # D on beat 1
    (65, beat, 100),  # F# on beat 2
    (67, beat * 2, 100),  # A on beat 3
    (62, beat * 3, 90),  # D on beat 4 — but slightly softer, hinting at something
]

for note in sax_notes:
    n = Note(
        pitch=note[0],
        start=note[1],
        end=note[1] + 0.15,
        velocity=note[2]
    )
    sax.notes.append(n)

# BAR 2: Bass — walking line with chromatic twists
# D - Eb - F# - G - A - Bb - B - C - D
# D (beat 1), Eb (beat 2), F# (beat 3), G (beat 4)
bass_notes = [
    (62, 0, 80),   # D on beat 1
    (63, beat, 80),  # Eb on beat 2
    (65, beat * 2, 80),  # F# on beat 3
    (67, beat * 3, 80),  # G on beat 4
]

for note in bass_notes:
    n = Note(
        pitch=note[0],
        start=note[1],
        end=note[1] + 0.25,
        velocity=note[2]
    )
    bass.notes.append(n)

# BAR 2: Piano — 7th chords, comp on 2 and 4
# D7: D, F#, A, C
# Comp on beat 2 and 4
piano_notes = [
    (62, beat, 80),   # D on beat 2
    (65, beat, 80),   # F#
    (67, beat, 80),   # A
    (60, beat, 80),   # C
    (62, beat * 3, 80),  # D on beat 4
    (65, beat * 3, 80),  # F#
    (67, beat * 3, 80),  # A
    (60, beat * 3, 80),  # C
]

for note in piano_notes:
    n = Note(
        pitch=note[0],
        start=note[1],
        end=note[1] + 0.25,
        velocity=note[2]
    )
    piano.notes.append(n)

# BAR 3: Drums continue, same pattern
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0, 36, 100, beat * 2),  # Kick on beat 1
    (0, 38, 90, beat * 2 + half_beat),  # Snare on beat 2
    (0, 42, 80, beat * 2),  # Hihat on 1
    (0, 42, 80, beat * 2 + half_beat),  # Hihat on 1.5
    (0, 36, 100, beat * 3),  # Kick on beat 3
    (0, 38, 90, beat * 3 + half_beat),  # Snare on beat 4
    (0, 42, 80, beat * 3 + quarter_beat),  # Hihat on 3.25
    (0, 42, 80, beat * 3 + half_beat + quarter_beat),  # Hihat on 3.75
    (0, 42, 80, beat * 3 + beat),  # Hihat on 4
]

for note in drum_notes:
    dr = Note(
        pitch=note[0],
        start=note[2],
        end=note[2] + 0.1,
        velocity=note[3]
    )
    drums.notes.append(dr)

# BAR 3: Sax continues with variation — same motif, but more dynamic
# D (beat 1), F# (beat 2), rest (beat 3), A (beat 4)
sax_notes = [
    (62, beat * 2, 100),  # D on beat 1
    (65, beat * 3, 100),  # F# on beat 2
    (67, beat * 4, 100),  # A on beat 4
]

for note in sax_notes:
    n = Note(
        pitch=note[0],
        start=note[1],
        end=note[1] + 0.15,
        velocity=note[2]
    )
    sax.notes.append(n)

# BAR 3: Bass continues walking with chromatic twist
# G - A - Bb - B - C - D - Eb - F# - G
# G (beat 1), A (beat 2), Bb (beat 3), B (beat 4)
bass_notes = [
    (67, beat * 2, 80),   # G on beat 1
    (69, beat * 3, 80),   # A on beat 2
    (70, beat * 4, 80),   # Bb on beat 3
    (71, beat * 5, 80),   # B on beat 4
]

for note in bass_notes:
    n = Note(
        pitch=note[0],
        start=note[1],
        end=note[1] + 0.25,
        velocity=note[2]
    )
    bass.notes.append(n)

# BAR 3: Piano — 7th chords, comp on 2 and 4
# G7: G, Bb, D, F
# Comp on beat 2 and 4
piano_notes = [
    (67, beat * 3, 80),  # G on beat 2
    (70, beat * 3, 80),  # Bb
    (69, beat * 3, 80),  # D
    (65, beat * 3, 80),  # F
    (67, beat * 5, 80),  # G on beat 4
    (70, beat * 5, 80),  # Bb
    (69, beat * 5, 80),  # D
    (65, beat * 5, 80),  # F
]

for note in piano_notes:
    n = Note(
        pitch=note[0],
        start=note[1],
        end=note[1] + 0.25,
        velocity=note[2]
    )
    piano.notes.append(n)

# BAR 4: Drums continue, same pattern
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
drum_notes = [
    (0, 36, 100, beat * 4),  # Kick on beat 1
    (0, 38, 90, beat * 4 + half_beat),  # Snare on beat 2
    (0, 42, 80, beat * 4),  # Hihat on 1
    (0, 42, 80, beat * 4 + half_beat),  # Hihat on 1.5
    (0, 36, 100, beat * 5),  # Kick on beat 3
    (0, 38, 90, beat * 5 + half_beat),  # Snare on beat 4
    (0, 42, 80, beat * 5 + quarter_beat),  # Hihat on 3.25
    (0, 42, 80, beat * 5 + half_beat + quarter_beat),  # Hihat on 3.75
    (0, 42, 80, beat * 5 + beat),  # Hihat on 4
]

for note in drum_notes:
    dr = Note(
        pitch=note[0],
        start=note[2],
        end=note[2] + 0.1,
        velocity=note[3]
    )
    drums.notes.append(dr)

# BAR 4: Sax concludes with a lingering note — A, held through the bar
sax_notes = [
    (67, beat * 4, 70),  # A on beat 1
    (67, beat * 4 + beat, 70),  # A on beat 4
]

for note in sax_notes:
    n = Note(
        pitch=note[0],
        start=note[1],
        end=note[1] + beat,
        velocity=note[2]
    )
    sax.notes.append(n)

# BAR 4: Bass continues walking
# B - C - D - Eb - F# - G - A - Bb - B
# B (beat 1), C (beat 2), D (beat 3), Eb (beat 4)
bass_notes = [
    (71, beat * 4, 80),   # B on beat 1
    (69, beat * 5, 80),   # C on beat 2
    (67, beat * 6, 80),   # D on beat 3
    (63, beat * 7, 80),   # Eb on beat 4
]

for note in bass_notes:
    n = Note(
        pitch=note[0],
        start=note[1],
        end=note[1] + 0.25,
        velocity=note[2]
    )
    bass.notes.append(n)

# BAR 4: Piano — 7th chords, comp on 2 and 4
# B7: B, D, F#, A
# Comp on beat 2 and 4
piano_notes = [
    (71, beat * 5, 80),  # B on beat 2
    (67, beat * 5, 80),  # D
    (65, beat * 5, 80),  # F#
    (62, beat * 5, 80),  # A
    (71, beat * 7, 80),  # B on beat 4
    (67, beat * 7, 80),  # D
    (65, beat * 7, 80),  # F#
    (62, beat * 7, 80),  # A
]

for note in piano_notes:
    n = Note(
        pitch=note[0],
        start=note[1],
        end=note[1] + 0.25,
        velocity=note[2]
    )
    piano.notes.append(n)

# Write MIDI to a file
pm.write('dante_introduction.mid')
