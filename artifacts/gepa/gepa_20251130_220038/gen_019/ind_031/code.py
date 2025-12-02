
import pretty_midi

# Create a new MIDI file with the specified tempo
midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# Instruments for the quartet
sax = pretty_midi.Instrument(program=66)       # Tenor sax
bass = pretty_midi.Instrument(program=33)      # Double bass
piano = pretty_midi.Instrument(program=0)      # Piano
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Drums

# Drum notes: kick=36, snare=38, hihat=42
kick = 36
snare = 38
hihat = 42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
# Total bar length = 1.5 seconds = 600 milliseconds
# Each beat = 0.375 seconds (160 BPM, 4/4 time)

# Time grid in seconds: [0.0, 0.375, 0.75, 1.125, 1.5]
# Positions: 1, 2, 3, 4

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.0, end=0.375))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=0.75, end=1.125))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=0.375, end=0.75))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=1.125, end=1.5))

# Hihat on every eighth (0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125, 1.5)
for t in [0.0, 0.1875, 0.375, 0.5625, 0.75, 0.9375, 1.125, 1.3125]:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=t, end=t + 0.1875))

# Bar 2: Full quartet starts (1.5 - 3.0s)

# Bass: Walking line, chromatic approaches, no repeated notes
# F minor key (F, Gb, Ab, Bb, B, Db, Eb)
# Walking bass line in F minor: F, Gb, Ab, Bb, B, Db, Eb, F
# Time positions: [1.5, 1.875, 2.25, 2.625, 3.0]

bass_notes = [78, 77, 75, 73, 72, 70, 69, 78]
for i, note in enumerate(bass_notes):
    start = 1.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Chords: F7 (F, A, C, Eb), Bb7 (Bb, D, F, Ab), Eb7 (Eb, G, Bb, Db), Ab7 (Ab, C, Eb, Gb)
# Comp on 2 and 4 (1.875 and 3.0)

chords = [
    # F7 (1.5s)
    (78, 79, 80, 82),
    # Bb7 (1.875s)
    (77, 79, 80, 82),
    # Eb7 (2.25s)
    (69, 71, 77, 79),
    # Ab7 (3.0s)
    (75, 78, 79, 80)
]

for i, chord in enumerate(chords):
    start = 1.5 + i * 0.375
    end = start + 0.1875
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Sax: Motif — short, melodic, leaves it hanging
# Motif: F (78), Gb (77), Ab (75), Bb (73) — played on 1.5, 1.875, 2.25, 2.625

sax_notes = [78, 77, 75, 73]
for i, note in enumerate(sax_notes):
    start = 1.5 + i * 0.375
    end = start + 0.1875
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bar 3: Continue (3.0 - 4.5s)

# Bass: Continue walking line
# F, Gb, Ab, Bb, B, Db, Eb, F
# Time positions: [3.0, 3.375, 3.75, 4.125, 4.5]

bass_notes = [78, 77, 75, 73, 72, 70, 69, 78]
for i, note in enumerate(bass_notes):
    start = 3.0 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Chords: Bb7 (Bb, D, F, Ab), Eb7 (Eb, G, Bb, Db), Ab7 (Ab, C, Eb, Gb), F7 (F, A, C, Eb)
# Comp on 3.375 and 4.5

chords = [
    # Bb7 (3.375s)
    (77, 79, 80, 82),
    # Eb7 (3.75s)
    (69, 71, 77, 79),
    # Ab7 (4.125s)
    (75, 78, 79, 80),
    # F7 (4.5s)
    (78, 79, 80, 82)
]

for i, chord in enumerate(chords):
    start = 3.0 + i * 0.375
    end = start + 0.1875
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Sax: Motif again but with a twist — one note change (Ab to A)
# F (78), Gb (77), A (79), Bb (73) — played on 3.0, 3.375, 3.75, 4.125

sax_notes = [78, 77, 79, 73]
for i, note in enumerate(sax_notes):
    start = 3.0 + i * 0.375
    end = start + 0.1875
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Bar 4: Continue (4.5 - 6.0s)

# Bass: Continue walking line
# F, Gb, Ab, Bb, B, Db, Eb, F
# Time positions: [4.5, 4.875, 5.25, 5.625, 6.0]

bass_notes = [78, 77, 75, 73, 72, 70, 69, 78]
for i, note in enumerate(bass_notes):
    start = 4.5 + i * 0.375
    end = start + 0.375
    bass.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=start, end=end))

# Piano: 7th chords, comp on 2 and 4
# Chords: F7 (F, A, C, Eb), Bb7 (Bb, D, F, Ab), Eb7 (Eb, G, Bb, Db), Ab7 (Ab, C, Eb, Gb)
# Comp on 4.875 and 6.0

chords = [
    # F7 (4.875s)
    (78, 79, 80, 82),
    # Bb7 (5.25s)
    (77, 79, 80, 82),
    # Eb7 (5.625s)
    (69, 71, 77, 79),
    # Ab7 (6.0s)
    (75, 78, 79, 80)
]

for i, chord in enumerate(chords):
    start = 4.5 + i * 0.375
    end = start + 0.1875
    for note in chord:
        piano.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=start, end=end))

# Sax: Final motif — resolve the tension from before
# F (78), Gb (77), Ab (75), Bb (73) — played on 4.5, 4.875, 5.25, 5.625

sax_notes = [78, 77, 75, 73]
for i, note in enumerate(sax_notes):
    start = 4.5 + i * 0.375
    end = start + 0.1875
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=start, end=end))

# Drum pattern continues
# Kick on 1 and 3 (4.5, 5.25), snare on 2 and 4 (4.875, 5.625), hihat on every eighth

# Kick on 1 and 3
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=4.5, end=4.875))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=kick, start=5.25, end=5.625))

# Snare on 2 and 4
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=4.875, end=5.25))
drums.notes.append(pretty_midi.Note(velocity=100, pitch=snare, start=5.625, end=6.0))

# Hihat on every eighth
for t in [4.5, 4.6875, 4.875, 5.0625, 5.25, 5.4375, 5.625, 5.8125]:
    drums.notes.append(pretty_midi.Note(velocity=90, pitch=hihat, start=t, end=t + 0.1875))

# Add all instruments to MIDI
midi.instruments.extend([sax, bass, piano, drums])

# Save the MIDI file
midi.write("dante_intro.mid")
