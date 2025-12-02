
import pretty_midi

# Create a new MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# MIDI note numbers
# D = 62, scale: D, E, F#, G, A, B, C#
# Drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Add instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Bar 1: Little Ray on drums (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in range(1):
    for beat in range(4):
        time = bar * 1.5 + beat * 0.375
        # Hihat on every eighth note
        piano.notes.append(pretty_midi.Note(velocity=64, pitch=HIHAT, start=time, end=time + 0.1875))
        if beat == 0 or beat == 2:
            # Kick on 1 and 3
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1875))
        if beat == 1 or beat == 3:
            # Snare on 2 and 4
            drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time, end=time + 0.1875))

# Bar 2: Full band in (1.5 - 3.0s)
# Sax: D (62), F# (66), B (71), D (62)
# Bass: Walking line in D minor
# Piano: 7th chords on 2 and 4
# Drums: Same pattern

# Saxophone (Dante)
# Motif: D F# B D
# Start at 1.5s
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=1.5, end=1.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=1.75, end=2.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=2.0, end=2.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=2.25, end=2.5))

# Bass (Marcus)
# Walking line: D (62), E (64), F# (66), G (67), A (69), B (71), C# (72), D (62)
# Loop over bar 2
bass_notes = [62, 64, 66, 67, 69, 71, 72, 62]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=end))

# Piano (Diane)
# 7th chords on 2 and 4 (i.e., at 1.75 and 2.25)
# D7 = D, F#, A, C#
# Bm7 = B, D, F#, A
# D7 at 1.75 s
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=1.75, end=2.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=1.75, end=2.0))
# Bm7 at 2.25 s
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=2.25, end=2.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=2.25, end=2.5))

# Drums (Little Ray)
# Same pattern from before
for bar in range(1):
    for beat in range(4):
        time = 1.5 + bar * 1.5 + beat * 0.375
        piano.notes.append(pretty_midi.Note(velocity=64, pitch=HIHAT, start=time, end=time + 0.1875))
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1875))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time, end=time + 0.1875))

# Bar 3: Full band (3.0 - 4.5s)
# Sax: D (62), F# (66), B (71), D (62) again
# Bass: Same walking line
# Piano: 7th chords on 2 and 4 (3.25 and 3.75)
# Drums: Same pattern

# Saxophone (Dante)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.0, end=3.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=3.25, end=3.5))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=3.5, end=3.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=3.75, end=4.0))

# Bass (Marcus)
for i, note in enumerate(bass_notes):
    start = 3.0 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=end))

# Piano (Diane)
# D7 at 3.25
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.25, end=3.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=3.25, end=3.5))
# Bm7 at 3.75
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=3.75, end=4.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=3.75, end=4.0))

# Drums (Little Ray)
for bar in range(1):
    for beat in range(4):
        time = 3.0 + bar * 1.5 + beat * 0.375
        piano.notes.append(pretty_midi.Note(velocity=64, pitch=HIHAT, start=time, end=time + 0.1875))
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1875))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time, end=time + 0.1875))

# Bar 4: Full band (4.5 - 6.0s)
# Sax: D (62), F# (66), B (71), D (62) again (leaving it hanging)
# Bass: Same walking line
# Piano: 7th chords on 2 and 4 (4.75 and 5.25)
# Drums: Same pattern

# Saxophone (Dante)
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=4.5, end=4.75))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=66, start=4.75, end=5.0))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=71, start=5.0, end=5.25))
sax.notes.append(pretty_midi.Note(velocity=100, pitch=62, start=5.25, end=5.5))

# Bass (Marcus)
for i, note in enumerate(bass_notes):
    start = 4.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=70, pitch=note, start=start, end=end))

# Piano (Diane)
# D7 at 4.75
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=4.75, end=5.0))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=72, start=4.75, end=5.0))
# Bm7 at 5.25
piano.notes.append(pretty_midi.Note(velocity=80, pitch=71, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=62, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=66, start=5.25, end=5.5))
piano.notes.append(pretty_midi.Note(velocity=80, pitch=69, start=5.25, end=5.5))

# Drums (Little Ray)
for bar in range(1):
    for beat in range(4):
        time = 4.5 + bar * 1.5 + beat * 0.375
        piano.notes.append(pretty_midi.Note(velocity=64, pitch=HIHAT, start=time, end=time + 0.1875))
        if beat == 0 or beat == 2:
            drums.notes.append(pretty_midi.Note(velocity=100, pitch=KICK, start=time, end=time + 0.1875))
        if beat == 1 or beat == 3:
            drums.notes.append(pretty_midi.Note(velocity=90, pitch=SNARE, start=time, end=time + 0.1875))

# Write the MIDI file to disk
midi.write("dante_intro.mid")
