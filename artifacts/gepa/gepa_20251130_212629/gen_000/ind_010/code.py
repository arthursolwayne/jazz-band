
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
    (36, 0.0), (38, 0.375), (42, 0.375),
    (36, 0.75), (38, 1.125), (42, 1.125),
    (36, 1.5), (38, 1.875), (42, 1.875)
]
for note, time in drum_notes:
    drums.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.125))

# Bars 2-4: Full quartet (1.5 - 6.0s)

# Bass line: walking in Fm, chromatic approaches
bass_notes = [
    (39, 1.5), (40, 1.875), (38, 2.25), (37, 2.625), # Fm root motion
    (39, 3.0), (40, 3.375), (38, 3.75), (37, 4.125),
    (39, 4.5), (40, 4.875), (38, 5.25), (37, 5.625)
]
for note, time in bass_notes:
    bass.notes.append(pretty_midi.Note(velocity=80, pitch=note, start=time, end=time + 0.25))

# Piano: 7th chords on 2 and 4
piano_notes = [
    # Bar 2: F7 (F A C Eb)
    (53, 3.0), (58, 3.0), (57, 3.0), (55, 3.0),
    # Bar 3: Bb7 (Bb D F Ab)
    (50, 4.5), (55, 4.5), (53, 4.5), (51, 4.5),
    # Bar 4: Eb7 (Eb G Bb Db)
    (52, 6.0), (59, 6.0), (57, 6.0), (54, 6.0)
]
for note, time in piano_notes:
    piano.notes.append(pretty_midi.Note(velocity=90, pitch=note, start=time, end=time + 0.25))

# Sax: motif in Fm, one short phrase with tension
sax_notes = [
    # Bar 2: F - Eb - F - Gb (sax starts on beat 2)
    (53, 1.875), (51, 2.25), (53, 2.625), (52, 3.0),
    # Bar 3: rest, then resolution
    (57, 4.125), (55, 4.5),
    # Bar 4: repeat motif with variation
    (53, 5.625), (51, 6.0), (53, 6.375), (54, 6.75)
]
for note, time in sax_notes:
    sax.notes.append(pretty_midi.Note(velocity=100, pitch=note, start=time, end=time + 0.25))

midi.instruments.extend([sax, bass, piano, drums])
midi.write("dante_intro.mid")
