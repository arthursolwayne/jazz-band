
import pretty_midi

midi = pretty_midi.PrettyMIDI(initial_tempo=160)

# The quartet
sax = pretty_midi.Instrument(program=66)       # Dante
bass = pretty_midi.Instrument(program=33)      # Marcus
piano = pretty_midi.Instrument(program=0)      # Diane
drums = pretty_midi.Instrument(program=0, is_drum=True)  # Little Ray

# Drums: kick=36, snare=38, hihat=42

# Bar 1: Little Ray alone (0.0 - 1.5s)
# Kick on 1 and 3, snare on 2 and 4, hihat on every eighth
bar_length = 1.5
for beat in range(4):
    time = beat * bar_length / 4
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 8)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 8)
        drums.notes.append(note)

# Bar 2: Full quartet
# Start with sax, bass, piano

# Sax: motif in F minor with chromatic passing tones
sax_notes = [
    (pretty_midi.Note(velocity=110, pitch=65, start=1.5, end=1.5 + 0.375), 1.5),
    (pretty_midi.Note(velocity=110, pitch=67, start=1.5 + 0.375, end=1.5 + 0.75), 1.5 + 0.375),
    (pretty_midi.Note(velocity=110, pitch=64, start=1.5 + 0.75, end=1.5 + 1.125), 1.5 + 0.75),
    (pretty_midi.Note(velocity=110, pitch=66, start=1.5 + 1.125, end=1.5 + 1.5), 1.5 + 1.125)
]
for note in sax_notes:
    sax.notes.append(note[0])

# Bass: walking line in F minor (F, Gb, G, Ab)
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=64, start=1.5, end=1.5 + 0.375), 1.5),
    (pretty_midi.Note(velocity=80, pitch=65, start=1.5 + 0.375, end=1.5 + 0.75), 1.5 + 0.375),
    (pretty_midi.Note(velocity=80, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125), 1.5 + 0.75),
    (pretty_midi.Note(velocity=80, pitch=68, start=1.5 + 1.125, end=1.5 + 1.5), 1.5 + 1.125)
]
for note in bass_notes:
    bass.notes.append(note[0])

# Piano: 7th chords on 2 and 4, F7 and C7
piano_notes = [
    # F7 (F, A, C, Eb)
    (pretty_midi.Note(velocity=100, pitch=64, start=1.5 + 0.75, end=1.5 + 1.125), 1.5 + 0.75),
    (pretty_midi.Note(velocity=100, pitch=69, start=1.5 + 0.75, end=1.5 + 1.125), 1.5 + 0.75),
    (pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 0.75, end=1.5 + 1.125), 1.5 + 0.75),
    (pretty_midi.Note(velocity=100, pitch=65, start=1.5 + 0.75, end=1.5 + 1.125), 1.5 + 0.75),
    # C7 (C, E, G, Bb)
    (pretty_midi.Note(velocity=100, pitch=67, start=1.5 + 1.5, end=1.5 + 1.875), 1.5 + 1.5),
    (pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.875), 1.5 + 1.5),
    (pretty_midi.Note(velocity=100, pitch=74, start=1.5 + 1.5, end=1.5 + 1.875), 1.5 + 1.5),
    (pretty_midi.Note(velocity=100, pitch=71, start=1.5 + 1.5, end=1.5 + 1.875), 1.5 + 1.5)
]
for note in piano_notes:
    piano.notes.append(note[0])

# Bar 3: Full quartet (1.5 - 3.0s)
# Sax continues the motif, slightly varied
sax_notes = [
    (pretty_midi.Note(velocity=110, pitch=69, start=3.0, end=3.0 + 0.375), 3.0),
    (pretty_midi.Note(velocity=110, pitch=71, start=3.0 + 0.375, end=3.0 + 0.75), 3.0 + 0.375),
    (pretty_midi.Note(velocity=110, pitch=68, start=3.0 + 0.75, end=3.0 + 1.125), 3.0 + 0.75),
    (pretty_midi.Note(velocity=110, pitch=70, start=3.0 + 1.125, end=3.0 + 1.5), 3.0 + 1.125)
]
for note in sax_notes:
    sax.notes.append(note[0])

# Bass: walking line in F minor (F, Gb, G, Ab)
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=64, start=3.0, end=3.0 + 0.375), 3.0),
    (pretty_midi.Note(velocity=80, pitch=65, start=3.0 + 0.375, end=3.0 + 0.75), 3.0 + 0.375),
    (pretty_midi.Note(velocity=80, pitch=67, start=3.0 + 0.75, end=3.0 + 1.125), 3.0 + 0.75),
    (pretty_midi.Note(velocity=80, pitch=68, start=3.0 + 1.125, end=3.0 + 1.5), 3.0 + 1.125)
]
for note in bass_notes:
    bass.notes.append(note[0])

# Piano: 7th chords on 2 and 4, F7 and C7
piano_notes = [
    # F7 (F, A, C, Eb)
    (pretty_midi.Note(velocity=100, pitch=64, start=3.0 + 0.75, end=3.0 + 1.125), 3.0 + 0.75),
    (pretty_midi.Note(velocity=100, pitch=69, start=3.0 + 0.75, end=3.0 + 1.125), 3.0 + 0.75),
    (pretty_midi.Note(velocity=100, pitch=67, start=3.0 + 0.75, end=3.0 + 1.125), 3.0 + 0.75),
    (pretty_midi.Note(velocity=100, pitch=65, start=3.0 + 0.75, end=3.0 + 1.125), 3.0 + 0.75),
    # C7 (C, E, G, Bb)
    (pretty_midi.Note(velocity=100, pitch=67, start=3.0 + 1.5, end=3.0 + 1.875), 3.0 + 1.5),
    (pretty_midi.Note(velocity=100, pitch=71, start=3.0 + 1.5, end=3.0 + 1.875), 3.0 + 1.5),
    (pretty_midi.Note(velocity=100, pitch=74, start=3.0 + 1.5, end=3.0 + 1.875), 3.0 + 1.5),
    (pretty_midi.Note(velocity=100, pitch=71, start=3.0 + 1.5, end=3.0 + 1.875), 3.0 + 1.5)
]
for note in piano_notes:
    piano.notes.append(note[0])

# Bar 4: Full quartet (3.0 - 6.0s)
# Sax completes the motif and ends on a high note
sax_notes = [
    (pretty_midi.Note(velocity=110, pitch=72, start=4.5, end=4.5 + 0.375), 4.5),
    (pretty_midi.Note(velocity=110, pitch=73, start=4.5 + 0.375, end=4.5 + 0.75), 4.5 + 0.375),
    (pretty_midi.Note(velocity=110, pitch=72, start=4.5 + 0.75, end=4.5 + 1.125), 4.5 + 0.75),
    (pretty_midi.Note(velocity=110, pitch=70, start=4.5 + 1.125, end=4.5 + 1.5), 4.5 + 1.125)
]
for note in sax_notes:
    sax.notes.append(note[0])

# Bass: walking line in F minor (F, Gb, G, Ab)
bass_notes = [
    (pretty_midi.Note(velocity=80, pitch=64, start=4.5, end=4.5 + 0.375), 4.5),
    (pretty_midi.Note(velocity=80, pitch=65, start=4.5 + 0.375, end=4.5 + 0.75), 4.5 + 0.375),
    (pretty_midi.Note(velocity=80, pitch=67, start=4.5 + 0.75, end=4.5 + 1.125), 4.5 + 0.75),
    (pretty_midi.Note(velocity=80, pitch=68, start=4.5 + 1.125, end=4.5 + 1.5), 4.5 + 1.125)
]
for note in bass_notes:
    bass.notes.append(note[0])

# Piano: 7th chords on 2 and 4, F7 and C7
piano_notes = [
    # F7 (F, A, C, Eb)
    (pretty_midi.Note(velocity=100, pitch=64, start=4.5 + 0.75, end=4.5 + 1.125), 4.5 + 0.75),
    (pretty_midi.Note(velocity=100, pitch=69, start=4.5 + 0.75, end=4.5 + 1.125), 4.5 + 0.75),
    (pretty_midi.Note(velocity=100, pitch=67, start=4.5 + 0.75, end=4.5 + 1.125), 4.5 + 0.75),
    (pretty_midi.Note(velocity=100, pitch=65, start=4.5 + 0.75, end=4.5 + 1.125), 4.5 + 0.75),
    # C7 (C, E, G, Bb)
    (pretty_midi.Note(velocity=100, pitch=67, start=4.5 + 1.5, end=4.5 + 1.875), 4.5 + 1.5),
    (pretty_midi.Note(velocity=100, pitch=71, start=4.5 + 1.5, end=4.5 + 1.875), 4.5 + 1.5),
    (pretty_midi.Note(velocity=100, pitch=74, start=4.5 + 1.5, end=4.5 + 1.875), 4.5 + 1.5),
    (pretty_midi.Note(velocity=100, pitch=71, start=4.5 + 1.5, end=4.5 + 1.875), 4.5 + 1.5)
]
for note in piano_notes:
    piano.notes.append(note[0])

# Drums continue in bar 3 and 4
for beat in range(4):
    time = (beat + 2) * bar_length / 4
    if beat % 2 == 0:
        note = pretty_midi.Note(velocity=100, pitch=36, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 8)
        drums.notes.append(note)
    else:
        note = pretty_midi.Note(velocity=100, pitch=38, start=time, end=time + bar_length / 4)
        drums.notes.append(note)
        note = pretty_midi.Note(velocity=100, pitch=42, start=time, end=time + bar_length / 8)
        drums.notes.append(note)

midi.instruments.extend([sax, bass, piano, drums])
midi.write('dante_intro.mid')
