
import pretty_midi
import numpy as np

# Create a new PrettyMIDI object
pm = pretty_midi.PrettyMIDI()
pm.time_signature_changes = [pretty_midi.TimeSignature(4, 4, 0.0)]
pm.beat_tracker = pretty_midi.BeatTracking()

# Set tempo to 160 BPM
pm.tempo_changes = [pretty_midi.TempoChange(160.0, 0.0)]

# Create instruments
sax_program = pretty_midi.instrument_name_to_program('Tenor Saxophone')
bass_program = pretty_midi.instrument_name_to_program('Double Bass')
piano_program = pretty_midi.instrument_name_to_program('Acoustic Piano')
drums_program = pretty_midi.instrument_name_to_program('Drums')

sax = pretty_midi.Instrument(program=sax_program)
bass = pretty_midi.Instrument(program=bass_program)
piano = pretty_midi.Instrument(program=piano_program)
drums = pretty_midi.Instrument(program=drums_program)

pm.instruments = [sax, bass, piano, drums]

# BPM: 160, 4/4 time
# Tempo in MIDI is in microseconds per beat
# 60,000,000 microseconds per minute
# 60,000,000 / 160 = 375,000 microseconds per beat
# 1 beat = 0.375 seconds
# 1 bar = 1.5 seconds (4 beats)
# 4 bars = 6 seconds

# Bar 1: Drums only (Little Ray)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Time per beat: 0.375s
# 1 bar = 4 beats = 1.5s

# MIDI note numbers
# Kick: C1 (36), Snare: D2 (62), Hihat: C8 (104)

# Bar 1: Drums only
# Bar is 1.5 seconds, so beat spacing is 0.375

for i in range(4):
    beat_time = i * 0.375
    if i % 2 == 0:
        # Kick on 1 and 3
        note = pretty_midi.Note(velocity=80, pitch=36, start=beat_time, end=beat_time + 0.1)
        drums.notes.append(note)
    else:
        # Snare on 2 and 4
        note = pretty_midi.Note(velocity=80, pitch=62, start=beat_time, end=beat_time + 0.1)
        drums.notes.append(note)
    # Hihat on every eighth
    note = pretty_midi.Note(velocity=50, pitch=104, start=beat_time, end=beat_time + 0.1)
    drums.notes.append(note)

# Bar 2: Tenor sax starts motif
# Fm key: F, Ab, Bb, Db, Eb, Gb
# Motif: F, Ab, Bb, rest — 4 notes, 4 beats, spaced out

# Start on beat 0.0 (start of bar)
# F (65), Ab (68), Bb (71), rest on beat 3.0

# F (65) on beat 0.0
note = pretty_midi.Note(velocity=100, pitch=65, start=0.0, end=0.25)
sax.notes.append(note)

# Ab (68) on beat 1.0
note = pretty_midi.Note(velocity=100, pitch=68, start=1.0, end=1.25)
sax.notes.append(note)

# Bb (71) on beat 2.0
note = pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25)
sax.notes.append(note)

# Bar 2: Bass (Marcus) walking line
# Start on beat 0.0
# Fm key: F, Ab, Bb, Db, Eb, Gb

# Walking line: F, Gb, Ab, Bb — chromatic approach

# F (65) on beat 0.0
note = pretty_midi.Note(velocity=80, pitch=65, start=0.0, end=0.25)
bass.notes.append(note)

# Gb (66) on beat 0.375
note = pretty_midi.Note(velocity=80, pitch=66, start=0.375, end=0.625)
bass.notes.append(note)

# Ab (68) on beat 0.75
note = pretty_midi.Note(velocity=80, pitch=68, start=0.75, end=1.0)
bass.notes.append(note)

# Bb (71) on beat 1.125
note = pretty_midi.Note(velocity=80, pitch=71, start=1.125, end=1.375)
bass.notes.append(note)

# Bar 2: Piano (Diane) — 7th chords, comp on 2 and 4

# F7: F, A, C, Eb
# Comp on beat 1.0 and 3.0

# F7 (beat 1.0)
note = pretty_midi.Note(velocity=90, pitch=65, start=1.0, end=1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=1.0, end=1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=72, start=1.0, end=1.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=1.0, end=1.125)
piano.notes.append(note)

# F7 (beat 3.0)
note = pretty_midi.Note(velocity=90, pitch=65, start=3.0, end=3.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=3.0, end=3.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=72, start=3.0, end=3.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=3.0, end=3.125)
piano.notes.append(note)

# Bar 3: Sax continues with motif, but now lower
# Motif: F, Ab, Bb, rest — repeat but shifted down an octave

# F (48) on beat 0.0
note = pretty_midi.Note(velocity=100, pitch=48, start=1.5, end=1.75)
sax.notes.append(note)

# Ab (51) on beat 1.0 (bar 3)
note = pretty_midi.Note(velocity=100, pitch=51, start=2.5, end=2.75)
sax.notes.append(note)

# Bb (54) on beat 2.0 (bar 3)
note = pretty_midi.Note(velocity=100, pitch=54, start=3.5, end=3.75)
sax.notes.append(note)

# Bar 3: Bass (Marcus) continues walking line
# Next chromatic: C (60), Db (61), Eb (62), F (65)

# C on beat 1.5
note = pretty_midi.Note(velocity=80, pitch=60, start=1.5, end=1.75)
bass.notes.append(note)

# Db on beat 1.875
note = pretty_midi.Note(velocity=80, pitch=61, start=1.875, end=2.125)
bass.notes.append(note)

# Eb on beat 2.25
note = pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5)
bass.notes.append(note)

# F on beat 2.625
note = pretty_midi.Note(velocity=80, pitch=65, start=2.625, end=2.875)
bass.notes.append(note)

# Bar 3: Piano (Diane) — 7th chords, comp on 2 and 4

# F7 on beat 2.5
note = pretty_midi.Note(velocity=90, pitch=65, start=2.5, end=2.625)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=2.5, end=2.625)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=72, start=2.5, end=2.625)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=2.5, end=2.625)
piano.notes.append(note)

# F7 on beat 3.5
note = pretty_midi.Note(velocity=90, pitch=65, start=3.5, end=3.625)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=68, start=3.5, end=3.625)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=72, start=3.5, end=3.625)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=69, start=3.5, end=3.625)
piano.notes.append(note)

# Bar 4: Sax motif returns, this time with a resolution

# F (65) on beat 0.0
note = pretty_midi.Note(velocity=100, pitch=65, start=3.0, end=3.25)
sax.notes.append(note)

# Ab (68) on beat 1.0
note = pretty_midi.Note(velocity=100, pitch=68, start=4.0, end=4.25)
sax.notes.append(note)

# Bb (71) on beat 2.0
note = pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25)
sax.notes.append(note)

# Bar 4: Bass (Marcus) resolves the walking line
# Next chromatic: F (65), Gb (66), Ab (68), Bb (71)
# Resolving to Bb7 (Bb, D, F, Ab)

note = pretty_midi.Note(velocity=80, pitch=65, start=3.0, end=3.25)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=66, start=3.375, end=3.625)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=68, start=3.75, end=4.0)
bass.notes.append(note)
note = pretty_midi.Note(velocity=80, pitch=71, start=4.125, end=4.375)
bass.notes.append(note)

# Bar 4: Piano (Diane) — 7th chords, comp on 2 and 4

# Bb7 (beat 4.0)
note = pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=74, start=4.0, end=4.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=76, start=4.0, end=4.125)
piano.notes.append(note)
note = pretty_midi.Note(velocity=90, pitch=71, start=4.0, end=4.125)
piano.notes.append(note)

# Save the MIDI file
pm.write("jazz_intro.mid")
