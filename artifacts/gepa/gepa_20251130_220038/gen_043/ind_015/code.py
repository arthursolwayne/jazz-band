
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
drum_notes = [
    # Bar 1
    (0.0, 36), (0.375, 42), (0.75, 38), (1.125, 42),
    (1.5, 36), (1.875, 42), (2.25, 38), (2.625, 42)
]

for time, note in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking line in Fm, chromatic approaches
bass_notes = [
    # Bar 2
    (1.5, 53), (1.75, 51), (2.0, 50), (2.25, 48),
    # Bar 3
    (2.5, 47), (2.75, 45), (3.0, 44), (3.25, 43),
    # Bar 4
    (3.5, 42), (3.75, 40), (4.0, 39), (4.25, 38),
    # Resolution
    (4.5, 37), (4.75, 39), (5.0, 40), (5.25, 42)
]

for time, note in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2
    (2.0, 60), (2.0, 64), (2.5, 60), (2.5, 64),
    # Bar 3
    (3.0, 59), (3.0, 63), (3.5, 59), (3.5, 63),
    # Bar 4
    (4.0, 60), (4.0, 64), (4.5, 60), (4.5, 64)
]

for time, note in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.5))

# Sax: Whisper at first, then cry
# Bar 2: 4 notes, motif
sax_notes = [
    # Bar 2
    (1.5, 62), (1.75, 64), (2.0, 60), (2.25, 62),
    # Bar 3: spaces and tension
    (2.5, 63), (2.75, 61), (3.0, 63), (3.25, 65),
    # Bar 4: resolution and cry
    (3.5, 62), (3.75, 64), (4.0, 60), (4.25, 62),
    (4.5, 63), (4.75, 64), (5.0, 60), (5.25, 62)
]

for time, note in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("fm_intro.mid")
