
import pretty_midi

# Initialize the MIDI file with 160 BPM
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Define instruments
sax = pretty_midi.Instrument(program=66)       # Tenor Saxophone
bass = pretty_midi.Instrument(program=33)      # Double Bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Define drum notes
KICK = 36
SNARE = 38
HIHAT = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
for bar in [0]:  # Bar 0 is the first bar
    for beat in [0, 2]:  # Kick on 1 and 3
        note = pretty_midi.Note(
            velocity=80,
            pitch=KICK,
            start=bar * 1.5 + beat * 0.375,
            end=bar * 1.5 + beat * 0.375 + 0.125
        )
        drums.notes.append(note)
    for beat in [1, 3]:  # Snare on 2 and 4
        note = pretty_midi.Note(
            velocity=100,
            pitch=SNARE,
            start=bar * 1.5 + beat * 0.375,
            end=bar * 1.5 + beat * 0.375 + 0.125
        )
        drums.notes.append(note)
    for eighth in range(8):  # Hihat on every eighth
        note = pretty_midi.Note(
            velocity=80,
            pitch=HIHAT,
            start=bar * 1.5 + eighth * 0.125,
            end=bar * 1.5 + eighth * 0.125 + 0.025
        )
        drums.notes.append(note)

# Bar 2: Full quartet (1.5 - 3.0s)
# Bass: Walking line in D minor (D, C, Bb, A), chromatic approaches
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=2, start=1.5, end=1.625),  # D
    pretty_midi.Note(velocity=80, pitch=1, start=1.625, end=1.75), # C
    pretty_midi.Note(velocity=80, pitch=10, start=1.75, end=1.875),# Bb
    pretty_midi.Note(velocity=80, pitch=9, start=1.875, end=2.0),  # A
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4, comp on the off-beats
# D7 (D, F#, A, C) on beat 2, G7 (G, B, D, F) on beat 4
piano_notes = []
# Beat 2: D7
piano_notes.append(pretty_midi.Note(velocity=80, pitch=2, start=1.625, end=2.0))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=6, start=1.625, end=2.0))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=9, start=1.625, end=2.0))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=11, start=1.625, end=2.0))

# Beat 4: G7
piano_notes.append(pretty_midi.Note(velocity=80, pitch=7, start=2.25, end=2.625))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=11, start=2.25, end=2.625))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=9, start=2.25, end=2.625))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=10, start=2.25, end=2.625))

piano.notes.extend(piano_notes)

# Sax: Motif in D minor. Start with a short phrase, leave it hanging.
# D - Eb - C - D - Eb (hanging on Eb)
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=2, start=1.5, end=1.625), # D
    pretty_midi.Note(velocity=100, pitch=3, start=1.625, end=1.75), # Eb
    pretty_midi.Note(velocity=100, pitch=0, start=1.75, end=1.875), # C
    pretty_midi.Note(velocity=100, pitch=2, start=1.875, end=2.0),  # D
    pretty_midi.Note(velocity=100, pitch=3, start=2.0, end=2.125),  # Eb (hanging)
]
sax.notes.extend(sax_notes)

# Bar 3: Full quartet (3.0 - 4.5s)
# Bass: Walking line (D, C, Bb, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=2, start=3.0, end=3.125),
    pretty_midi.Note(velocity=80, pitch=1, start=3.125, end=3.25),
    pretty_midi.Note(velocity=80, pitch=10, start=3.25, end=3.375),
    pretty_midi.Note(velocity=80, pitch=9, start=3.375, end=3.5),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = []
# Beat 2: Bm7 (B, D, F#, A)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=10, start=3.625, end=4.0))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=2, start=3.625, end=4.0))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=6, start=3.625, end=4.0))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=9, start=3.625, end=4.0))

# Beat 4: A7 (A, C#, E, G)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=9, start=4.25, end=4.625))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=4, start=4.25, end=4.625))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=7, start=4.25, end=4.625))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=10, start=4.25, end=4.625))

piano.notes.extend(piano_notes)

# Sax: Motif variation, resolve it this time
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=3, start=3.0, end=3.125), # Eb
    pretty_midi.Note(velocity=100, pitch=0, start=3.125, end=3.25), # C
    pretty_midi.Note(velocity=100, pitch=2, start=3.25, end=3.375), # D
    pretty_midi.Note(velocity=100, pitch=3, start=3.375, end=3.5),  # Eb
    pretty_midi.Note(velocity=100, pitch=2, start=3.5, end=3.625),  # D
    pretty_midi.Note(velocity=100, pitch=1, start=3.625, end=3.75), # C
    pretty_midi.Note(velocity=100, pitch=2, start=3.75, end=4.0),  # D
]
sax.notes.extend(sax_notes)

# Drums: Same pattern as bar 1
for bar in [2]:  # Bar 2 is the third bar
    for beat in [0, 2]:  # Kick on 1 and 3
        note = pretty_midi.Note(
            velocity=80,
            pitch=KICK,
            start=bar * 1.5 + beat * 0.375,
            end=bar * 1.5 + beat * 0.375 + 0.125
        )
        drums.notes.append(note)
    for beat in [1, 3]:  # Snare on 2 and 4
        note = pretty_midi.Note(
            velocity=100,
            pitch=SNARE,
            start=bar * 1.5 + beat * 0.375,
            end=bar * 1.5 + beat * 0.375 + 0.125
        )
        drums.notes.append(note)
    for eighth in range(8):  # Hihat on every eighth
        note = pretty_midi.Note(
            velocity=80,
            pitch=HIHAT,
            start=bar * 1.5 + eighth * 0.125,
            end=bar * 1.5 + eighth * 0.125 + 0.025
        )
        drums.notes.append(note)

# Bar 4: Full quartet (4.5 - 6.0s)
# Bass: Walking line (D, C, Bb, A)
bass_notes = [
    pretty_midi.Note(velocity=80, pitch=2, start=4.5, end=4.625),
    pretty_midi.Note(velocity=80, pitch=1, start=4.625, end=4.75),
    pretty_midi.Note(velocity=80, pitch=10, start=4.75, end=4.875),
    pretty_midi.Note(velocity=80, pitch=9, start=4.875, end=5.0),
]
bass.notes.extend(bass_notes)

# Piano: 7th chords on 2 and 4
piano_notes = []
# Beat 2: Cm7 (C, Eb, G, Bb)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=1, start=5.125, end=5.5))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=3, start=5.125, end=5.5))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=7, start=5.125, end=5.5))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=10, start=5.125, end=5.5))

# Beat 4: D7 (D, F#, A, C)
piano_notes.append(pretty_midi.Note(velocity=80, pitch=2, start=5.75, end=6.0))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=6, start=5.75, end=6.0))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=9, start=5.75, end=6.0))
piano_notes.append(pretty_midi.Note(velocity=80, pitch=11, start=5.75, end=6.0))

piano.notes.extend(piano_notes)

# Sax: Resolve the motif, end on C
sax_notes = [
    pretty_midi.Note(velocity=100, pitch=2, start=4.5, end=4.625), # D
    pretty_midi.Note(velocity=100, pitch=3, start=4.625, end=4.75), # Eb
    pretty_midi.Note(velocity=100, pitch=0, start=4.75, end=4.875), # C
    pretty_midi.Note(velocity=100, pitch=2, start=4.875, end=5.0),  # D
    pretty_midi.Note(velocity=100, pitch=3, start=5.0, end=5.125),  # Eb
    pretty_midi.Note(velocity=100, pitch=0, start=5.125, end=5.25), # C
    pretty_midi.Note(velocity=100, pitch=0, start=5.25, end=5.5),  # C
]
sax.notes.extend(sax_notes)

# Drums: Same pattern as bar 1
for bar in [3]:  # Bar 3 is the fourth bar
    for beat in [0, 2]:  # Kick on 1 and 3
        note = pretty_midi.Note(
            velocity=80,
            pitch=KICK,
            start=bar * 1.5 + beat * 0.375,
            end=bar * 1.5 + beat * 0.375 + 0.125
        )
        drums.notes.append(note)
    for beat in [1, 3]:  # Snare on 2 and 4
        note = pretty_midi.Note(
            velocity=100,
            pitch=SNARE,
            start=bar * 1.5 + beat * 0.375,
            end=bar * 1.5 + beat * 0.375 + 0.125
        )
        drums.notes.append(note)
    for eighth in range(8):  # Hihat on every eighth
        note = pretty_midi.Note(
            velocity=80,
            pitch=HIHAT,
            start=bar * 1.5 + eighth * 0.125,
            end=bar * 1.5 + eighth * 0.125 + 0.025
        )
        drums.notes.append(note)

# Add instruments to the MIDI file
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_russo_intro.mid")
